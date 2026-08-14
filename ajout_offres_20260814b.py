"""Relance exhaustive du 14/08/2026 - les 8 axes.

Postes verifies ouverts par API Ashby / Lever quand le board l'exposait.
Ecartes car fermes malgre leur presence dans les moteurs : Deel (Solutions
Engineer EMEA, Customer Onboarding Manager EMEA), Flagright Implementation
Manager EMEA, Keyrock, WeTravel Client Onboarding EMEA, GitLab TAM.
"""

import add_offre

add_offre.COLS = add_offre.COLS + ['Date trouvée', 'Date publiée']

D = '14/08/2026'
FW = 'https://www.free-work.com'
MF = 'https://app.mission-freelances.fr'
CV_SIRH_FR = 'Resume_GaetanFRANCOIS_SIRH.pdf'
CV_SIRH_EN = 'Resume_GaetanFRANCOIS_SIRH_EN.pdf'
CV_CSM_EN = 'CV_GaetanFRANCOIS_CSM_EN.pdf'
CV_IA = 'Resume_GaetanFRANCOIS_IA.pdf'

OFFRES = [

    # ================= GXO Logistics : rollout SuccessFactors Europe continentale =================
    {
        'Priorité': '⭐⭐⭐⭐⭐', 'Poste': 'HR Product Specialist - Continental Europe',
        'Entreprise': 'GXO Logistics', 'Source': 'jobs.gxo.com',
        'Contrat': 'CDI', 'Localisation': 'Neuilly-sur-Seine', 'Remote': None,
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Publie le 14/08/2026, ref 387747. GXO mene un rollout SAP SuccessFactors pluriannuel sur toute l'Europe continentale. Poste produit RH sur perimetre multi-pays : croise le parcours SIRH, la dimension internationale et la nouvelle cible produit. Le meilleur fit trouve dans cette relance.",
        'Lien': 'https://jobs.gxo.com/job/NEUILLY-SUR-SEINE-HR-Product-Specialist-Continental-Europe-92200/1419472400/',
        'CV à envoyer': CV_SIRH_EN, 'Prétention': '80-100 K€',
        'Date trouvée': D, 'Date publiée': '14/08/2026',
    },
    {
        'Priorité': '⭐⭐⭐⭐', 'Poste': 'Manager Implementations & Turnarounds - System Support, Continental Europe',
        'Entreprise': 'GXO Logistics', 'Source': 'jobs.gxo.com',
        'Contrat': 'CDI', 'Localisation': 'Neuilly-sur-Seine', 'Remote': None,
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Pilotage de deploiements sur l'Europe continentale : correspond a l'axe Implementation ajoute le 14/08 et au parcours de deploiement multi-pays.",
        'Lien': 'https://jobs.gxo.com/job/NEUILLY-SUR-SEINE-Manager-Implementations-&-Turnarounds-System-Support-Continental-Europe-92200/1381623000/',
        'CV à envoyer': CV_SIRH_EN, 'Prétention': '80-95 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Senior HR Systems Analyst (SuccessFactors, Employee Central)',
        'Entreprise': 'GXO Logistics', 'Source': 'jobs.gxo.com',
        'Contrat': 'CDI', 'Localisation': 'Northampton (UK)', 'Remote': None,
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Employee Central, module central du parcours L'Oreal. Poste britannique : question visa a clarifier.",
        'Lien': 'https://jobs.gxo.com/job/Northampton-Senior-HRIT-Analyst-(Success-Factors,-Employee-Central)-ENG-NN1-5GE/1407108400/',
        'CV à envoyer': CV_SIRH_EN, 'Prétention': '70-85 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Senior HR Systems Analyst (SuccessFactors, Onboarding)',
        'Entreprise': 'GXO Logistics', 'Source': 'jobs.gxo.com',
        'Contrat': 'CDI', 'Localisation': 'Northampton (UK)', 'Remote': None,
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Module Onboarding de SuccessFactors ; croise SIRH et onboarding, deux axes du profil. Poste britannique.",
        'Lien': 'https://jobs.gxo.com/job/Northampton-Senior-HR-Systems-Analyst-(SuccessFactors,-Onboarding)-ENG-NN1-5GE/1407109100/',
        'CV à envoyer': CV_SIRH_EN, 'Prétention': '70-85 K€',
        'Date trouvée': D, 'Date publiée': None,
    },

    # ================= Implementation / Solutions (nouveaux axes) =================
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Implementation Consultant - French Market',
        'Entreprise': 'Agicap', 'Source': 'jobs.lever.co',
        'Contrat': 'CDI', 'Localisation': 'Lyon', 'Remote': 'Hybride',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Scale-up francaise (gestion de tresorerie), deploiement client sur le marche francais. Verifie ouvert par API Lever. Hybride Lyon, donc en retrait sur le critere remote.",
        'Lien': 'https://jobs.lever.co/agicap/ab6e4fda-90c1-4529-8f90-55652f54f3a8',
        'CV à envoyer': CV_SIRH_FR, 'Prétention': '70-85 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Customer Solutions Consultant - French Market',
        'Entreprise': 'Agicap', 'Source': 'jobs.lever.co',
        'Contrat': 'CDI', 'Localisation': 'Lyon', 'Remote': 'Hybride',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Avant-vente et conseil solution sur le marche francais. Verifie ouvert par API Lever.",
        'Lien': 'https://jobs.lever.co/agicap/9f696d60-b9fe-4170-bbb4-2a3fd8ab27bf',
        'CV à envoyer': CV_CSM_EN, 'Prétention': '70-85 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Implementation Consultant I',
        'Entreprise': 'Cority', 'Source': 'jobs.lever.co',
        'Contrat': 'CDI', 'Localisation': 'Royaume-Uni', 'Remote': 'Full remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Deploiement client en full remote depuis le Royaume-Uni ; verifier l'eligibilite depuis la France. Verifie ouvert par API Lever.",
        'Lien': 'https://jobs.lever.co/cority/54893de6-a997-495c-badf-4140d032e836',
        'CV à envoyer': CV_SIRH_EN, 'Prétention': '70-85 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Remote Implementation Consultant',
        'Entreprise': 'n.c. (via Jobgether)', 'Source': 'jobs.lever.co',
        'Contrat': 'CDI', 'Localisation': 'Remote', 'Remote': 'Full remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Accompagnement client sur l'integration des workflows, pilotage multi-chantiers et onboarding des donnees : proche du parcours d'integration mene chez L'Oreal.",
        'Lien': 'https://jobs.lever.co/jobgether/7e21bf19-ac58-4a10-9de6-0066923794cf',
        'CV à envoyer': CV_SIRH_EN, 'Prétention': '70-85 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Solutions Consultant',
        'Entreprise': 'Caseware', 'Source': 'jobs.lever.co',
        'Contrat': 'CDI', 'Localisation': 'Maidstone (UK)', 'Remote': 'Full remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Avant-vente sur grands comptes strategiques, de l'evaluation jusqu'au deploiement. Full remote UK, verifie ouvert par API Lever.",
        'Lien': 'https://jobs.lever.co/caseware/9df37a92-2245-4005-bcb2-ff94d1ab1c59',
        'CV à envoyer': CV_CSM_EN, 'Prétention': '80-95 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐', 'Poste': 'Solutions Consultant',
        'Entreprise': 'Caseware', 'Source': 'jobs.lever.co',
        'Contrat': 'CDI', 'Localisation': 'Apeldoorn (Pays-Bas)', 'Remote': 'Hybride',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Meme poste, antenne neerlandaise, en hybride donc moins aligne sur le remote.",
        'Lien': 'https://jobs.lever.co/caseware/78f4de69-d89e-4c40-a633-1d313c7cebe9',
        'CV à envoyer': CV_CSM_EN, 'Prétention': '80-95 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Solutions Engineering Manager',
        'Entreprise': 'WeTravel', 'Source': 'jobs.ashbyhq.com',
        'Contrat': 'CDI', 'Localisation': 'Amsterdam', 'Remote': None,
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Encadrement d'une equipe d'avant-vente technique, en Europe. Verifie ouvert par API Ashby.",
        'Lien': 'https://jobs.ashbyhq.com/wetravel/cac3fb0c-2dfa-403a-bf7b-99f993a32f7b',
        'CV à envoyer': CV_CSM_EN, 'Prétention': '85-100 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Customer Success Manager - EMEA',
        'Entreprise': 'Flagright', 'Source': 'jobs.ashbyhq.com',
        'Contrat': 'CDI', 'Localisation': 'Royaume-Uni', 'Remote': None,
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "CSM EMEA chez un editeur conformite financiere. Verifie ouvert par API Ashby ; le poste Implementation Manager EMEA du meme employeur est deja ferme.",
        'Lien': 'https://jobs.ashbyhq.com/flagright.com/e06aef39-fdaf-44d5-8283-dbe3d8fb5c69',
        'CV à envoyer': CV_CSM_EN, 'Prétention': '80-95 K€',
        'Date trouvée': D, 'Date publiée': None,
    },

    # ================= IA =================
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Business Analyst IA Générative',
        'Entreprise': 'Comet', 'Source': 'free-work',
        'Contrat': 'Mission freelance', 'Localisation': 'Île-de-France', 'Remote': None,
        'Salaire / TJM': None, 'Durée mission': '1 an',
        'Fit / Notes': "Business Analyst sur des sujets IA generative, publie le 14/08. La posture BA est deja une cible du profil ; Comet est une plateforme freelance identifiee dans CLAUDE.md.",
        'Lien': FW + '/fr/tech-it/job-mission/business-analyst/misison-freelance-business-analyst-ia-generative',
        'CV à envoyer': CV_IA, 'Prétention': '650-750 €/j',
        'Date trouvée': D, 'Date publiée': '14/08/2026',
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Expert IA générative et Plateforme IA (H/F)',
        'Entreprise': 'Freelance.com', 'Source': 'free-work',
        'Contrat': 'Mission freelance', 'Localisation': 'Île-de-France', 'Remote': None,
        'Salaire / TJM': '510-590 €/j', 'Durée mission': '1 an',
        'Fit / Notes': "Mission longue sur plateforme IA, publiee le 14/08. Niveau de technicite a qualifier.",
        'Lien': FW + '/fr/tech-it/job-mission/expert-seo-consultant-referencement/expert-ia-generative-et-plateforme-ia-h-f',
        'CV à envoyer': CV_IA, 'Prétention': '590 €/j',
        'Date trouvée': D, 'Date publiée': '14/08/2026',
    },
    {
        'Priorité': '⭐⭐⭐⭐', 'Poste': 'Formateur(trice) freelance en intelligence artificielle',
        'Entreprise': 'n.c. (via LinkedIn / mission-freelances.fr)', 'Source': 'mission-freelances.fr',
        'Contrat': 'Mission freelance', 'Localisation': 'Chambéry et Bourg-en-Bresse', 'Remote': None,
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Formation IA, cible principale de l'onglet IA.",
        'Lien': MF + '/missions/formateur-trice-freelance-en-intelligence-artificielle-chambery-et-bourg-en-bresse-27cdb82e/',
        'CV à envoyer': CV_IA, 'Prétention': '650-750 €/j',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Consultant IA',
        'Entreprise': 'n.c. (via Free-Work / mission-freelances.fr)', 'Source': 'mission-freelances.fr',
        'Contrat': 'Mission freelance', 'Localisation': 'Cergy et/ou Malakoff', 'Remote': None,
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Conseil IA en entreprise ; contour a qualifier sur le niveau technique attendu.",
        'Lien': MF + '/missions/consultant-ia-cergy-et-ou-malakoff-a7867ef0/',
        'CV à envoyer': CV_IA, 'Prétention': '650-750 €/j',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Directeur IA & Innovation',
        'Entreprise': 'n.c. (via Free-Work / mission-freelances.fr)', 'Source': 'mission-freelances.fr',
        'Contrat': 'Mission freelance', 'Localisation': 'Paris', 'Remote': None,
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Poste de direction sur le perimetre IA et innovation ; seniorite coherente avec 15 ans d'experience.",
        'Lien': MF + '/missions/directeur-ia-innovation-paris-75f914af/',
        'CV à envoyer': CV_IA, 'Prétention': '750 €/j',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Product Manager IA',
        'Entreprise': 'n.c. (via HelloWork / mission-freelances.fr)', 'Source': 'mission-freelances.fr',
        'Contrat': 'Mission freelance', 'Localisation': 'Paris', 'Remote': None,
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Croisement produit et IA : correspond a la fois au nouvel axe Product Manager et a l'onglet IA.",
        'Lien': MF + '/missions/product-manager-ia-paris-a80209f9/',
        'CV à envoyer': 'Resume_GaetanFRANCOIS_Constructor_PM_EN.pdf', 'Prétention': '650-750 €/j',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐', 'Poste': 'Expert(e) IA',
        'Entreprise': 'n.c. (via Free-Work / mission-freelances.fr)', 'Source': 'mission-freelances.fr',
        'Contrat': 'Mission freelance', 'Localisation': 'Niort', 'Remote': None,
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Intitule large, a qualifier ; localisation excentree.",
        'Lien': MF + '/missions/expert-ia-niort-f278cd3b/',
        'CV à envoyer': CV_IA, 'Prétention': '650-750 €/j',
        'Date trouvée': D, 'Date publiée': None,
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
