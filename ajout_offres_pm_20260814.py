"""Premiere recherche Product Manager - 14/08/2026. Onglet "Offres PM", priorite au remote.

Sources verifiees par API quand c'etait possible :
  - API Ashby  : api.ashbyhq.com/posting-api/job-board/<entreprise>
  - API Lever  : api.lever.co/v0/postings/<entreprise>?mode=json
Les postes Deel, Dash0, EverAI, SignalWire et Workwize remontes par WebSearch
etaient deja fermes ; ils ne figurent pas ici.
"""

import add_offre

add_offre.COLS = add_offre.COLS + ['Date trouvée', 'Date publiée']

D = '14/08/2026'
CV_PM = 'Resume_GaetanFRANCOIS_Constructor_PM_EN.pdf'
FW = 'https://www.free-work.com'

OFFRES = [

    # ---------- Camunda : verifie live par API Ashby, tous en Remote ----------
    {
        'Priorité': '⭐⭐⭐⭐', 'Poste': 'Senior Product Manager - Core Platform (Remote)',
        'Entreprise': 'Camunda', 'Source': 'jobs.ashbyhq.com',
        'Contrat': 'CDI', 'Localisation': 'Remote', 'Remote': 'Full remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Editeur d'orchestration de processus, entreprise remote-first. Gaetan avait deja cible Camunda (CV_GaetanFRANCOIS_Camunda_EN existe), donc le contexte est connu. Poste verifie ouvert par l'API Ashby le 14/08.",
        'Lien': 'https://jobs.ashbyhq.com/camunda/b771e145-a5cf-4867-ad13-b54830e3b744',
        'CV à envoyer': CV_PM, 'Prétention': '85-100 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐⭐⭐', 'Poste': 'Senior Product Builder - Connectors Experience - EMEA',
        'Entreprise': 'Camunda', 'Source': 'jobs.ashbyhq.com',
        'Contrat': 'CDI', 'Localisation': 'EMEA', 'Remote': 'Full remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Produit centre sur l'experience des connecteurs, donc sur l'integration : c'est l'angle le plus proche du parcours (parcours d'integration L'Oreal, charniere metier/developpeurs). Verifie ouvert par API.",
        'Lien': 'https://jobs.ashbyhq.com/camunda/05cb2825-dcd9-40e6-bf92-bda409d99374',
        'CV à envoyer': CV_PM, 'Prétention': '85-100 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Product Manager, Self Managed Service',
        'Entreprise': 'Camunda', 'Source': 'jobs.ashbyhq.com',
        'Contrat': 'CDI', 'Localisation': 'Remote', 'Remote': 'Full remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Troisieme poste produit ouvert chez Camunda ; perimetre self-managed, plus technique. Verifie ouvert par API.",
        'Lien': 'https://jobs.ashbyhq.com/camunda/5652a3f3-e418-4e91-b58b-4be13f36853b',
        'CV à envoyer': CV_PM, 'Prétention': '80-95 K€',
        'Date trouvée': D, 'Date publiée': None,
    },

    # ---------- Welcome to the Jungle : teletravail total affiche ----------
    {
        'Priorité': '⭐⭐⭐⭐', 'Poste': 'Product Manager',
        'Entreprise': '360Learning', 'Source': 'welcometothejungle.com',
        'Contrat': 'CDI', 'Localisation': 'Paris', 'Remote': 'Télétravail total',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Plateforme de learning : le domaine recoupe directement l'experience de formation utilisateurs-cles et de transfert de connaissances. Teletravail total, editeur francais bien etabli. Un des meilleurs croisements produit/parcours du lot.",
        'Lien': 'https://www.welcometothejungle.com/en/companies/360learning/jobs/product-manager_paris_360LE_lGeWWq1',
        'CV à envoyer': CV_PM, 'Prétention': '75-90 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐⭐⭐', 'Poste': 'Product Manager',
        'Entreprise': 'Side', 'Source': 'welcometothejungle.com',
        'Contrat': 'CDI', 'Localisation': 'Paris', 'Remote': 'Télétravail total',
        'Salaire / TJM': '55-59 K€', 'Durée mission': None,
        'Fit / Notes': "Teletravail total, plus de 4 ans d'experience demandes, demarrage 31/08/2026. Remuneration sous la cible ; le salaire ne sert pas de filtre.",
        'Lien': 'https://www.welcometothejungle.com/fr/companies/side/jobs/product-manager_paris_SIDE_jRLO2Ar',
        'CV à envoyer': CV_PM, 'Prétention': '75-90 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐⭐⭐', 'Poste': 'Product Manager',
        'Entreprise': 'Inqom', 'Source': 'welcometothejungle.com',
        'Contrat': 'CDI', 'Localisation': 'Paris / Tours', 'Remote': 'Télétravail total',
        'Salaire / TJM': '50-55 K€', 'Durée mission': None,
        'Fit / Notes': "Teletravail total sur un SaaS comptable. Fourchette sous la cible, a negocier.",
        'Lien': 'https://www.welcometothejungle.com/fr/companies/inqom/jobs/product-manager',
        'CV à envoyer': CV_PM, 'Prétention': '75-90 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Product Manager (senior level)',
        'Entreprise': 'Joko', 'Source': 'welcometothejungle.com',
        'Contrat': 'CDI', 'Localisation': 'Paris', 'Remote': 'Télétravail total',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Niveau senior explicite, teletravail total. Produit B2C, ce qui recoupe l'experience WallOfTraders.com.",
        'Lien': 'https://www.welcometothejungle.com/en/companies/joko/jobs/product-manager-senior-level',
        'CV à envoyer': CV_PM, 'Prétention': '75-90 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Product Manager (full remote avec déplacements)',
        'Entreprise': 'RISE', 'Source': 'welcometothejungle.com',
        'Contrat': 'CDI', 'Localisation': 'France', 'Remote': 'Télétravail total',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Full remote avec deplacements ponctuels, compatible avec une base a Anglet.",
        'Lien': 'https://www.welcometothejungle.com/fr/companies/rise/jobs/28b1f52c-1924-40ec-b7e0-18bbdcda6c56',
        'CV à envoyer': CV_PM, 'Prétention': '75-90 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Product Manager',
        'Entreprise': 'Follow', 'Source': 'welcometothejungle.com',
        'Contrat': 'CDI', 'Localisation': 'France', 'Remote': 'Télétravail total',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Teletravail total, secteur sante. A qualifier sur la seniorite attendue.",
        'Lien': 'https://www.welcometothejungle.com/fr/companies/follow-health/jobs/product-manager',
        'CV à envoyer': CV_PM, 'Prétention': '75-90 K€',
        'Date trouvée': D, 'Date publiée': None,
    },

    # ---------- Jobgether via API Lever : variantes France uniquement ----------
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Product Manager, Data Activation',
        'Entreprise': 'n.c. (via Jobgether)', 'Source': 'jobs.lever.co',
        'Contrat': 'CDI', 'Localisation': 'France', 'Remote': 'Full remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Remote depuis la France, verifie ouvert par l'API Lever. Jobgether publie la meme offre par pays ; seule la variante France est retenue ici.",
        'Lien': 'https://jobs.lever.co/jobgether/dad5d8dc-4e02-4536-b7f6-8680e1df16ce',
        'CV à envoyer': CV_PM, 'Prétention': '75-90 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Product Manager, Data Orchestration',
        'Entreprise': 'n.c. (via Jobgether)', 'Source': 'jobs.lever.co',
        'Contrat': 'CDI', 'Localisation': 'France', 'Remote': 'Full remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Remote depuis la France, verifie ouvert par l'API Lever.",
        'Lien': 'https://jobs.lever.co/jobgether/5245a149-8431-4452-ab44-50cbb9bafbcf',
        'CV à envoyer': CV_PM, 'Prétention': '75-90 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Product Owner',
        'Entreprise': 'n.c. (via Jobgether)', 'Source': 'jobs.lever.co',
        'Contrat': 'CDI', 'Localisation': 'France', 'Remote': 'Full remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Product Owner en full remote depuis la France, verifie ouvert par l'API Lever.",
        'Lien': 'https://jobs.lever.co/jobgether/5405e9ec-8ab3-4075-8f5e-96425e4f11a6',
        'CV à envoyer': CV_PM, 'Prétention': '75-90 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'B2C Growth Product Manager',
        'Entreprise': 'n.c. (via Jobgether)', 'Source': 'jobs.lever.co',
        'Contrat': 'CDI', 'Localisation': 'France', 'Remote': 'Full remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Produit B2C oriente growth : recoupe directement WallOfTraders.com (acquisition SEO, paid social, boucle de retour utilisateurs).",
        'Lien': 'https://jobs.lever.co/jobgether/bae287fc-687d-48a6-a860-100430cbe25e',
        'CV à envoyer': CV_PM, 'Prétention': '75-90 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Sr. Product Manager, Core Platform',
        'Entreprise': 'n.c. (via Jobgether)', 'Source': 'jobs.lever.co',
        'Contrat': 'CDI', 'Localisation': 'France / Pays-Bas', 'Remote': 'Full remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Poste senior sur plateforme coeur, full remote.",
        'Lien': 'https://jobs.lever.co/jobgether/3efb5da5-0c07-4209-a4b6-037ead7571c2',
        'CV à envoyer': CV_PM, 'Prétention': '80-95 K€',
        'Date trouvée': D, 'Date publiée': None,
    },

    # ---------- Pennylane : URLs issues de WebSearch, non verifiees par API ----------
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Senior Product Manager',
        'Entreprise': 'Pennylane', 'Source': 'jobs.lever.co',
        'Contrat': 'CDI', 'Localisation': 'Europe', 'Remote': 'Remote Europe',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Scale-up francaise, remote depuis n'importe ou en Europe. URL issue de WebSearch : l'API Lever n'a pas repondu sur ce slug, verifier que l'annonce est encore ouverte avant de candidater.",
        'Lien': 'https://jobs.lever.co/pennylane/e821e150-f513-4297-86a7-6d2ee25ac50c',
        'CV à envoyer': CV_PM, 'Prétention': '80-95 K€',
        'Date trouvée': D, 'Date publiée': None,
    },

    # ---------- free-work : missions PO France, majoritairement sur site ----------
    {
        'Priorité': '⭐⭐', 'Poste': 'ITSM Platform Architect / Technical Product Owner',
        'Entreprise': 'LeHibou', 'Source': 'free-work',
        'Contrat': 'Mission freelance', 'Localisation': 'Paris', 'Remote': None,
        'Salaire / TJM': '650 €/j', 'Durée mission': '6 mois',
        'Fit / Notes': "Product Owner technique sur plateforme ITSM. Sur site Paris, donc en retrait sur le critere remote.",
        'Lien': FW + '/fr/tech-it/job-mission/product-owner/itsm-platform-architect-technical-product-owner',
        'CV à envoyer': CV_PM, 'Prétention': '650 €/j',
        'Date trouvée': D, 'Date publiée': '12/08/2026',
    },
    {
        'Priorité': '⭐⭐', 'Poste': 'Product Owner (H/F) 69',
        'Entreprise': 'Mindquest', 'Source': 'free-work',
        'Contrat': 'Mission freelance', 'Localisation': 'Lyon', 'Remote': None,
        'Salaire / TJM': '400-550 €/j', 'Durée mission': '3 mois',
        'Fit / Notes': "Mission PO courte a Lyon, sur site.",
        'Lien': FW + '/fr/tech-it/job-mission/product-owner/product-owner-h-f-69-1',
        'CV à envoyer': CV_PM, 'Prétention': '550 €/j',
        'Date trouvée': D, 'Date publiée': '12/08/2026',
    },
    {
        'Priorité': '⭐⭐', 'Poste': 'Product Owner',
        'Entreprise': 'WIKEYS', 'Source': 'free-work',
        'Contrat': 'Mission freelance', 'Localisation': 'Bruxelles', 'Remote': None,
        'Salaire / TJM': '600-610 €/j', 'Durée mission': '6 mois',
        'Fit / Notes': "Mission PO a Bruxelles ; contexte international, mais sur site.",
        'Lien': FW + '/fr/tech-it/job-mission/product-owner/product-owner-1365',
        'CV à envoyer': CV_PM, 'Prétention': '610 €/j',
        'Date trouvée': D, 'Date publiée': '03/08/2026',
    },
]


def _liens_existants():
    import openpyxl
    wb = openpyxl.load_workbook(add_offre.FICHIER)
    lien_idx = add_offre._col_index(wb['Offres SIRH'], 'Lien')
    liens = set()
    for name in ('Offres SIRH', 'Offres CSM', 'Offres IA', 'Offres PM', 'Fait'):
        for row in wb[name].iter_rows(min_row=2):
            v = row[lien_idx].value
            if v:
                liens.add(str(v).strip())
    return liens


if __name__ == '__main__':
    connus = _liens_existants()
    nouvelles = [o for o in OFFRES if o['Lien'] not in connus]
    print(f"{len(OFFRES)} offres collectees, {len(OFFRES) - len(nouvelles)} deja presentes, "
          f"{len(nouvelles)} a ajouter\n")
    add_offre.ajouter_offres(nouvelles)
