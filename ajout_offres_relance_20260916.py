"""
Intégration de la relance de recherche du 16/09/2026 (4 clusters en parallèle).
Fusionne les 4 fichiers finaux produits par les agents, normalise vers le
schéma attendu par add_offre.ajouter_offres(), déduplique en interne (Lien +
paire entreprise/poste normalisée) avant insertion, puis délègue tout le
routage/filtre remote/tri à ajouter_offres (qui déduplique aussi contre les
liens déjà en base).
"""
import json
import re
import unicodedata

from add_offre import ajouter_offres

SCRATCH = "/private/tmp/claude-501/-Users-gaetan-Documents-IA-recherche-taf/f0716b1d-0a44-4f5a-8e45-9c6a65e05f99/scratchpad"

STRONG_FIT_RE = re.compile(
    r'excellent|meilleur match|meilleure trouvaille|parfait|correspond exactement|'
    r'c[oœ]ur de cible|match exact|le plus juste', re.I)
STRONG_REMOTE_RE = re.compile(
    r'full remote|100\s*%|worldwide|anywhere|explicite|confirm[ée]', re.I)


def normalise(s):
    s = str(s or '').lower().strip()
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    s = re.sub(r'\b(h/f|f/h|h\s*/\s*f)\b', '', s)
    s = re.sub(r'\(.*?\)', '', s)
    s = re.sub(r'[^a-z0-9]+', ' ', s).strip()
    return s


def priorite_defaut(fit_text, remote_text, plancher=3):
    stars = plancher
    blob = f"{fit_text} {remote_text}"
    if STRONG_REMOTE_RE.search(blob):
        stars += 1
    if STRONG_FIT_RE.search(blob):
        stars = 5
    return '⭐' * min(stars, 5)


def load(path):
    with open(path) as f:
        return json.load(f)


def from_offres_finales():
    rows = load(f"{SCRATCH}/offres_finales.json")
    out = []
    for r in rows:
        onglet = r.get('Onglet_cible')
        out.append({
            'Poste': r.get('Poste'), 'Entreprise': r.get('Entreprise'),
            'Source': r.get('Source'), 'Lien': r.get('Lien'),
            'Contrat': r.get('Contrat'), 'Localisation': r.get('Localisation'),
            'Remote': r.get('Remote'), 'Salaire / TJM': r.get('Salaire_TJM'),
            'Fit / Notes': r.get('Fit_note'), 'Date publiée': r.get('Date_publiee'),
            'Priorité': priorite_defaut(r.get('Fit_note'), r.get('Remote')),
            'Onglet': onglet if onglet in ('Offres USA', 'Pays Basque') else None,
        })
    return out


def from_pb_cluster():
    rows = load(f"{SCRATCH}/pb_cluster_final.json")
    out = []
    for r in rows:
        fit = r.get('Fit', '')
        m = re.match(r'\s*(⭐+)\s*-?\s*(.*)', fit)
        stars, fit_clean = (m.group(1), m.group(2)) if m else ('⭐⭐⭐', fit)
        out.append({
            'Poste': r.get('Poste'), 'Entreprise': r.get('Entreprise'),
            'Source': 'Relance 16/09/2026 - cluster Pays Basque', 'Lien': r.get('Lien'),
            'Contrat': r.get('Contrat'), 'Localisation': r.get('Localisation'),
            'Remote': r.get('Remote'), 'Salaire / TJM': r.get('Salaire'),
            'Fit / Notes': fit_clean, 'Priorité': stars,
            'Onglet': 'Pays Basque',
        })
    return out


def from_remote_vc():
    rows = load(f"{SCRATCH}/cluster_remote_vc/final_offres.json")
    out = []
    for r in rows:
        onglet = r.get('Onglet')
        out.append({
            'Poste': r.get('Poste'), 'Entreprise': r.get('Entreprise'),
            'Source': r.get('Source'), 'Lien': r.get('Lien'),
            'Contrat': r.get('Contrat'), 'Localisation': r.get('Localisation'),
            'Remote': r.get('Remote'), 'Salaire / TJM': r.get('Salaire'),
            'Fit / Notes': f"Relance 16/09/2026, cluster remote/VC/niches ({r.get('Source')})",
            'Priorité': priorite_defaut('', r.get('Remote')),
            'Onglet': onglet if onglet in ('Offres USA', 'Pays Basque') else None,
        })
    return out


def from_ats():
    rows = load(f"{SCRATCH}/ats_relance/resultats_finaux.json")
    out = []
    for r in rows:
        onglet = r.get('Onglet')
        note = r.get('Note') or ''
        out.append({
            'Poste': r.get('Poste'), 'Entreprise': r.get('Entreprise'),
            'Source': r.get('Source'), 'Lien': r.get('Lien'),
            'Contrat': r.get('Contrat'), 'Localisation': r.get('Localisation'),
            'Remote': r.get('Remote'), 'Salaire / TJM': r.get('Salaire'),
            'Fit / Notes': note or f"Relance 16/09/2026, cluster ATS/HRIS/USA ({r.get('Source')})",
            'Priorité': priorite_defaut(note, r.get('Remote')),
            'Onglet': onglet if onglet in ('Offres USA', 'Pays Basque') else None,
        })
    return out


def main():
    all_offers = from_offres_finales() + from_pb_cluster() + from_remote_vc() + from_ats()
    print(f"Total brut fusionné : {len(all_offers)}")

    # Dédoublonnage interne par Lien
    seen_liens = set()
    seen_pairs = set()
    deduped = []
    dup_lien = dup_pair = 0
    for o in all_offers:
        lien = str(o.get('Lien') or '').strip()
        pair = (normalise(o.get('Entreprise')), normalise(o.get('Poste')))
        if lien and lien in seen_liens:
            dup_lien += 1
            continue
        if pair != ('', '') and pair in seen_pairs:
            dup_pair += 1
            continue
        if lien:
            seen_liens.add(lien)
        seen_pairs.add(pair)
        deduped.append(o)

    print(f"Doublons internes retirés : {dup_lien} (lien) + {dup_pair} (paire entreprise/poste)")
    print(f"Restant à soumettre à ajouter_offres : {len(deduped)}")

    # Nettoyage des clés auxiliaires non attendues par add_offre (Onglet=None -> retiré)
    for o in deduped:
        if o.get('Onglet') is None:
            o.pop('Onglet', None)

    ajouter_offres(deduped, verbose=True)


if __name__ == '__main__':
    main()
