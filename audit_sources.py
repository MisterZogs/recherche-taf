"""Détecte les sources productives absentes des fichiers lus par les agents de relance.

Usage : python3 audit_sources.py [seuil]   (seuil = nb mini d'offres, défaut 5)

Compte les offres par source dans offres_emploi.xlsx (tous onglets, colonne Source),
en extrait le domaine ou le slug ATS (« Greenhouse API - Datadog », « Ashby (camunda) »),
et signale toute source qui a produit au moins `seuil` offres mais dont le nom
n'apparaît dans aucun relance_sources_*.md / relance_regles_communes.md.
À lancer après chaque fusion de relance (créé le 06/10/2026 : l'allègement du 25/09
avait fait disparaître Station F, LinkedIn et six slugs Greenhouse sans que personne
ne le remarque).
"""
import collections
import glob
import re
import sys

import openpyxl

SEUIL = int(sys.argv[1]) if len(sys.argv) > 1 else 5

# Mots qui décrivent la méthode ou la plateforme, pas la source elle-même
BRUIT = {
    'api', 'ashby', 'ashbyhq', 'lever', 'greenhouse', 'board', 'boards', 'via', 'jobs',
    'job', 'www', 'com', 'fr', 'io', 'co', 'recherche', 'page', 'websearch', 'relance',
    'cluster', 'radar', 'remote', 'emploi', 'careers', 'career', 'the', 'and', 'de', 'des',
    'ats', 'who',
}

# Sources volontairement hors des fichiers de relance (intermédiaires de republication,
# canaux non interrogeables). Ajouter ici une source écartée en connaissance de cause.
IGNOREES = {'whatjobs.com', 'carriere-info.fr', 'réseau'}


def cles(source):
    """Renvoie les identifiants candidats d'une source (domaines, slugs ATS)."""
    s = source.lower()
    domaines = re.findall(r'[a-z0-9-]+(?:\.[a-z0-9-]+)*\.(?:com|fr|io|co|ch|nl|eu|app|ai|org|net|work|pro|me|de)\b', s)
    if domaines:
        # garder le nom de domaine sans sous-domaine générique (jobs., careers., www.)
        return [re.sub(r'^(www|jobs|careers|career|api|boards-api|job-boards|fr|open\.app)\.', '', d) for d in domaines]
    mots = [m for m in re.findall(r'[^\W_][\w.&-]{2,}', s) if m not in BRUIT]
    return mots[:1]


def reference(cle, texte):
    """Vrai si la source apparaît dans le texte, sous son domaine ou son nom nu."""
    nom = cle.split('.')[0]
    variantes = {nom, nom.replace('-', ' '), nom.replace('-', ''), re.split(r'[-.]', cle)[0]}
    return cle in IGNOREES or cle in texte or any(len(v) >= 3 and v in texte for v in variantes)


def main():
    texte = ''.join(open(f).read().lower()
                    for f in glob.glob('relance_sources_*.md') + ['relance_regles_communes.md'])
    wb = openpyxl.load_workbook('offres_emploi.xlsx', read_only=True)
    compte = collections.Counter()
    exemples = {}
    for ws in wb:
        lignes = ws.iter_rows(values_only=True)
        entete = next(lignes, None)
        if not entete or 'Source' not in entete:
            continue
        i = list(entete).index('Source')
        for r in lignes:
            if not r[i]:
                continue
            for k in cles(str(r[i])):
                compte[k] += 1
                exemples.setdefault(k, str(r[i])[:60])
    manquantes = [(k, n) for k, n in compte.most_common()
                  if n >= SEUIL and not reference(k, texte)]
    if not manquantes:
        print(f'OK : toutes les sources à {SEUIL}+ offres sont référencées dans relance_sources_*.md')
        return
    print(f'{len(manquantes)} source(s) à {SEUIL}+ offres absentes des fichiers de relance :')
    for k, n in manquantes:
        print(f'  {n:4d}  {k:30s}  ex. « {exemples[k]} »')
    print('\nPour chacune : la réintégrer dans le bon relance_sources_<cluster>.md, ou noter '
          'dans SOURCES_COMPLETES.md pourquoi elle est volontairement écartée (morte, à sec).')


if __name__ == '__main__':
    main()
