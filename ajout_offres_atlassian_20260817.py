"""Atlassian - complement de la relance du 17/08/2026.

Trouve apres coup : Gaetan a transmis une annonce LinkedIn (Enterprise CSM
Royaume-Uni) que la relance avait manquee. Cause : Atlassian n'etait dans
aucune source de CLAUDE.md, ne publie ni sur Ashby, ni sur Lever, ni sur
Greenhouse (ATS iCIMS), et les pages categories LinkedIn utilisees etaient
geo-filtrees sur la France.

Atlassian expose une API carrieres publique qui rend les 271 postes ouverts
en JSON avec titre, localisations, date de mise a jour et URL iCIMS :
    curl -s "https://www.atlassian.com/endpoint/careers/listings"

Les cinq liens ci-dessous ont ete verifies en HTTP 200 le 17/08/2026.
"""

import openpyxl

import add_offre

add_offre.COLS = add_offre.COLS + ['Date trouvée', 'Date publiée']

D = '17/08/2026'
CV_CSM_EN = 'CV_GaetanFRANCOIS_CSM_EN.pdf'
ATL = 'https://globalcareers-atlassian.icims.com/jobs/'

OFFRES = [
    {
        'Priorité': '⭐⭐⭐⭐⭐', 'Poste': 'Senior Principal Customer Success Manager, Strategic - France',
        'Entreprise': 'Atlassian', 'Source': 'atlassian.com (API carrières)',
        'Contrat': 'CDI', 'Localisation': 'Paris / France', 'Remote': 'Full remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Le poste le plus haut de la famille CSM chez Atlassian sur la France : relation C-suite, plans de succes, QBR et sessions de planification strategique sur des equipes mondiales. C'est mot pour mot le travail mene dix ans sur le compte L'Oreal monde. Atlassian se declare distributed-first et recrute dans tout pays ou le groupe a une entite ; la France en fait partie.",
        'Lien': ATL + '26241/senior-principal-customer-success-manager%2c-strategic---france/job',
        'CV à envoyer': CV_CSM_EN, 'Prétention': '95-115 K€',
        'Date trouvée': D, 'Date publiée': '11/08/2026',
    },
    {
        'Priorité': '⭐⭐⭐⭐⭐', 'Poste': 'Principal Customer Success Manager, Strategic, France',
        'Entreprise': 'Atlassian', 'Source': 'atlassian.com (API carrières)',
        'Contrat': 'CDI', 'Localisation': 'Remote France / Paris', 'Remote': 'Full remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Segment strategique, clients complexes, adoption produit et realisation de valeur. Remote France explicitement liste, avec le Royaume-Uni, la Pologne, les Pays-Bas et l'Allemagne en repli. Un cran sous le poste Senior Principal ; candidater aux deux se defend, le processus est le meme.",
        'Lien': ATL + '26057/principal-customer-success-manager%2c-strategic%2c-france/job',
        'CV à envoyer': CV_CSM_EN, 'Prétention': '90-110 K€',
        'Date trouvée': D, 'Date publiée': '10/08/2026',
    },
    {
        'Priorité': '⭐⭐⭐⭐', 'Poste': 'Customer Success Architect (AI)',
        'Entreprise': 'Atlassian', 'Source': 'atlassian.com (API carrières)',
        'Contrat': 'CDI', 'Localisation': 'Londres / Remote', 'Remote': 'Full remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Croisement direct entre le succes client et l'adoption de l'IA en entreprise : les deux axes de recherche a la fois. Poste rattache a Londres avec remote ouvert ; verifier l'eligibilite depuis la France avant de postuler.",
        'Lien': ATL + '26380/customer-success-architect-%28ai%29/job',
        'CV à envoyer': CV_CSM_EN, 'Prétention': '95-115 K€',
        'Date trouvée': D, 'Date publiée': '12/08/2026',
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Enterprise Customer Success Manager (Amsterdam / Remote UK)',
        'Entreprise': 'Atlassian', 'Source': 'atlassian.com (API carrières)',
        'Contrat': 'CDI', 'Localisation': 'Amsterdam / Royaume-Uni', 'Remote': 'Remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "L'annonce reperee par Gaetan sur LinkedIn (offre 4454883666). Adoption produit, expansion de solution et croissance sur un portefeuille enterprise. Zone remote limitee au Royaume-Uni et aux Pays-Bas : le poste France est nettement plus accessible, celui-ci reste un repli.",
        'Lien': ATL + '26045/customer-success-manager/job',
        'CV à envoyer': CV_CSM_EN, 'Prétention': '85-100 K€',
        'Date trouvée': D, 'Date publiée': '14/08/2026',
    },
    {
        'Priorité': '⭐⭐', 'Poste': 'Principal Customer Success Manager, Strategic DACH',
        'Entreprise': 'Atlassian', 'Source': 'atlassian.com (API carrières)',
        'Contrat': 'CDI', 'Localisation': 'Remote France éligible / Munich / Amsterdam', 'Remote': 'Full remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "La France figure dans les zones remote autorisees, mais le marche couvert est le DACH ; l'allemand sera vraisemblablement attendu. A garder en repli derriere les deux postes France.",
        'Lien': ATL + '26063/principal-customer-success-manager%2c-strategic-dach/job',
        'CV à envoyer': CV_CSM_EN, 'Prétention': '90-110 K€',
        'Date trouvée': D, 'Date publiée': '10/08/2026',
    },
]


def _cles_existantes():
    wb = openpyxl.load_workbook(add_offre.FICHIER)
    cles = set()
    for ws in wb.worksheets:
        for row in ws.iter_rows(min_row=2, values_only=True):
            if row[3]:
                cles.add((str(row[3]).strip().lower(),
                          str(row[4] or '').strip().lower()))
    return cles


if __name__ == '__main__':
    existantes = _cles_existantes()
    nouvelles = [o for o in OFFRES
                 if (o['Poste'].strip().lower(), o['Entreprise'].strip().lower())
                 not in existantes]
    add_offre.ajouter_offres(nouvelles)
    print(f"\n{len(nouvelles)} offres ajoutées, {len(OFFRES) - len(nouvelles)} doublons ignorés.")
