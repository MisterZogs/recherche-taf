"""Fusionne les fichiers JSON de sortie des clusters d'une relance en un seul
fichier dédoublonné, prêt pour add_offre.ajouter_offres().

Usage : python3 merge_relance.py <date YYYYMMDD>
Cherche automatiquement tous les fichiers relance_<date>_cluster_*.json
présents dans le dossier courant, fusionne, dédoublonne (lien exact + paire
Entreprise/Poste normalisée), retire les stage/alternance/entry-level en
filet de sécurité, et écrit relance_<date>_merged.json.
"""
import glob
import json
import re
import sys
import unicodedata


def norm(s):
    if not s:
        return ""
    s = str(s).lower().strip()
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def norm_link(l):
    if not l:
        return ""
    l = str(l).strip()
    l = re.sub(r"[?#].*$", "", l)
    l = l.rstrip("/")
    l = re.sub(r"^https?://(www\.)?", "", l)
    return l.lower()


JUNIOR_RE = re.compile(
    r"alternance|alternant|stage(?!ment)|stagiaire|apprenti|\bpfe\b|entry.level|"
    r"jeune dipl[oô]m[ée]",
    re.I,
)


def main():
    if len(sys.argv) != 2:
        print("Usage : python3 merge_relance.py <date YYYYMMDD>")
        sys.exit(1)
    date = sys.argv[1]

    files = sorted(glob.glob(f"relance_{date}_cluster_*.json"))
    if not files:
        print(f"Aucun fichier relance_{date}_cluster_*.json trouvé dans le dossier courant.")
        sys.exit(1)

    all_offres = []
    for f in files:
        with open(f, encoding="utf-8") as fh:
            data = json.load(fh)
        print(f"{f}: {len(data)} offres")
        all_offres.append((f, data))

    merged = []
    seen_links = set()
    seen_pairs = set()
    dropped_link = 0
    dropped_pair = 0
    dropped_junior = 0

    for fname, data in all_offres:
        for offre in data:
            for k, v in list(offre.items()):
                if isinstance(v, list):
                    offre[k] = ", ".join(str(x) for x in v)

            titre = str(offre.get("Poste") or "")
            if JUNIOR_RE.search(titre):
                dropped_junior += 1
                continue

            lien = norm_link(offre.get("Lien"))
            pair = (norm(offre.get("Entreprise")), norm(offre.get("Poste")))

            if lien and lien in seen_links:
                dropped_link += 1
                continue
            if pair[0] and pair[1] and pair in seen_pairs:
                dropped_pair += 1
                continue

            if lien:
                seen_links.add(lien)
            if pair[0] and pair[1]:
                seen_pairs.add(pair)
            merged.append(offre)

    print(f"\nTotal brut : {sum(len(d) for _, d in all_offres)}")
    print(f"Doublons lien retirés : {dropped_link}")
    print(f"Doublons paire Entreprise+Poste retirés : {dropped_pair}")
    print(f"Stage/alternance/entry-level retirés : {dropped_junior}")
    print(f"Total fusionné : {len(merged)}")

    out = f"relance_{date}_merged.json"
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(merged, fh, ensure_ascii=False, indent=1)

    print(f"\nÉcrit dans {out}")


if __name__ == "__main__":
    main()
