"""
Ajout des offres trouvées lors de la recherche du 2026-07-29.
Sources couvertes : LinkedIn (SAP HCM, SIRH, SuccessFactors, CSM, Formateur IA),
free-work.com (IA/IA générative fetch direct + WebSearch SIRH), ACT-ON HRIS (SmartRecruiters),
Arago (SmartRecruiters), Lucca, Harvey AI, Riot Security, Okta, Najar (Senior CSM),
Salesforce, Cegos, INGELINE TECHNOLOGIES, Michael Page (formateur IA),
Editions ENI (formateur IA collectivité), mission-freelances.fr (consultant IA conduite changement),
Sia Partners (HR Digital IA), SD Worx (implementation consultant),
EY (transformation RH, paie), Eramet (Lead SIRH).
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from add_offre import ajouter_offres

offres = [

    # ── ONGLET OFFRES SIRH ─────────────────────────────────────────────────────

    # ACT-ON HRIS - Consultant AMOA SIRH (nouveau poste, différent de celui du 27/07)
    {
        'Priorité': '⭐⭐⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Consultant(e) AMOA SIRH (F/H)',
        'Entreprise': 'ACT-ON HRIS',
        'Source': 'SmartRecruiters / LinkedIn',
        'Contrat': 'CDI',
        'Localisation': 'Neuilly-sur-Seine',
        'Remote': 'Partiel',
        'Salaire / TJM': '',
        'Durée mission': '',
        'Fit / Notes': 'ACT-ON HRIS 600+ consultants, 65M€ CA, 1 500+ missions. AMOA SIRH multi-outils (HR Access, Meta4, SAP SF). Posté juillet 2026. Postes actifs en juillet 2026, différent du poste AMOA déjà dans tableur.',
        'Lien': 'https://jobs.smartrecruiters.com/ACT-ON/744000045913473-consultant-e-amoa-sirh-f-h-',
        'CV à envoyer': 'CV_GaetanFRANCOIS_CSM.html',
        'Prétention': '70-85K€',
    },

    # ACT-ON - Consultant Chef de projet AMOA/SIRH (poste expiré - à vérifier sur site)
    # Skipped - offre expirée

    # Arago - SAP HCM Technical Consultant
    {
        'Priorité': '⭐⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'SAP HCM Technical Consultant (BIB & Infoporter)',
        'Entreprise': 'Arago',
        'Source': 'SmartRecruiters / LinkedIn',
        'Contrat': 'CDI',
        'Localisation': 'Paris',
        'Remote': 'Partiel',
        'Salaire / TJM': '',
        'Durée mission': '',
        'Fit / Notes': 'Arago cabinet conseil HR/Paie/T&E, présence FR/BE/CH/ES/PT/MA/CA/CO. SAP HCM+SF, intégrations BIB & Infoporter, projets internationaux. Posté il y a 3 semaines. Profil technique - moins centré management mais fort fit SAP HR.',
        'Lien': 'https://jobs.smartrecruiters.com/Arago/744000136242689-sap-hcm-technical-consultant-bib-infoporter-',
        'CV à envoyer': 'CV_GaetanFRANCOIS_CSM.html',
        'Prétention': '70-85K€',
    },

    # Eramet - Spécialiste SIRH Groupe
    {
        'Priorité': '⭐⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Spécialiste SIRH Groupe (F/H)',
        'Entreprise': 'Eramet',
        'Source': 'LinkedIn / fr.trabajo.org',
        'Contrat': 'CDI',
        'Localisation': 'Paris',
        'Remote': 'Partiel',
        'Salaire / TJM': '',
        'Durée mission': '',
        'Fit / Notes': 'Eramet groupe minier, déploiement SAP SF global (20 pays, 12 000 employés). Spécialiste SIRH modules Performance & Compensation. Profil internationalisation = fit fort L\'Oréal. International travel occasionnel.',
        'Lien': 'https://fr.linkedin.com/jobs/successfactors-emplois',
        'CV à envoyer': 'CV_GaetanFRANCOIS_CSM.html',
        'Prétention': '70-85K€',
    },

    # EY - Consultant Transformation RH/Change/SIRH (secteur financier)
    {
        'Priorité': '⭐⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Consultant expérimenté Transformation RH/Change Management/SIRH - secteur financier (H/F)',
        'Entreprise': 'EY',
        'Source': 'careers.ey.com',
        'Contrat': 'CDI',
        'Localisation': 'Paris La Défense',
        'Remote': 'Partiel',
        'Salaire / TJM': '',
        'Durée mission': '',
        'Fit / Notes': 'EY Technology & Transformation, transformation RH + change management + SIRH, secteur financier. Différent du poste "Manager SR Transformation RH" déjà dans tableur - niveau Consultant expérimenté. 39 postes actifs.',
        'Lien': 'https://careers.ey.com/ey/search/?q=SIRH+SAP&locationsearch=France',
        'CV à envoyer': 'CV_GaetanFRANCOIS_CSM.html',
        'Prétention': '70-85K€',
    },

    # EY - Consultants Expérimentés Paie
    {
        'Priorité': '⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Consultant expérimenté - Gestion de projets Paie (H/F)',
        'Entreprise': 'EY',
        'Source': 'careers.ey.com',
        'Contrat': 'CDI',
        'Localisation': 'Paris La Défense',
        'Remote': 'Partiel',
        'Salaire / TJM': '',
        'Durée mission': '',
        'Fit / Notes': 'EY Paie / Centre Opérationnel d\'Excellence. Nouveau poste identifié en juillet 2026 sur le site EY, différent des postes déjà ajoutés. Expertise paie FR + gestion de projet.',
        'Lien': 'https://careers.ey.com/ey/search/?q=SIRH+SAP&locationsearch=France',
        'CV à envoyer': 'CV_GaetanFRANCOIS_CSM.html',
        'Prétention': '70-85K€',
    },

    # SD Worx - Implementation Consultant French Speaking (nouveau - Time & Planning)
    {
        'Priorité': '⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Implementation Consultant (French Speaking) - Time & Planning',
        'Entreprise': 'SD Worx',
        'Source': 'careers.sdworx.com',
        'Contrat': 'CDI',
        'Localisation': 'France',
        'Remote': 'Partiel',
        'Salaire / TJM': '',
        'Durée mission': '',
        'Fit / Notes': 'SD Worx, nouveau poste (time & planning) différent des deux postes payroll déjà ajoutés. Posté mai 2026. Implémentation HRIS modules time/planning FR.',
        'Lien': 'https://careers.sdworx.com/jobs/7673069-implementation-consultant-french-speaking',
        'CV à envoyer': 'CV_GaetanFRANCOIS_CSM.html',
        'Prétention': '70-85K€',
    },

    # Sia Partners - Consultant HR Digital IA
    {
        'Priorité': '⭐⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Consultant HR Digital & IA',
        'Entreprise': 'Sia Partners',
        'Source': 'sia-partners.com/career',
        'Contrat': 'CDI',
        'Localisation': 'Paris',
        'Remote': 'Partiel',
        'Salaire / TJM': '',
        'Durée mission': '',
        'Fit / Notes': 'Sia Partners cabinet conseil international (ex-Sia Partners, rebranded "Sia"). BU HR & Transformation + IA. Postes CDI Paris. Croisement parfait : IA x SIRH x conseil RH. Postes visibles sur site en juillet 2026. Différent du poste "HR Digital IA" déjà dans tableur - il s\'agit du poste "HR Digital & IA" actif.',
        'Lien': 'https://www.sia-partners.com/en/career/consultant-digital-hris',
        'CV à envoyer': 'CV_GaetanFRANCOIS_CSM.html',
        'Prétention': '70-85K€',
    },

    # ── ONGLET OFFRES CSM ──────────────────────────────────────────────────────

    # Lucca - Customer Success SIRH Grands Comptes (Paris)
    {
        'Priorité': '⭐⭐⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Customer Success SIRH Grands Comptes',
        'Entreprise': 'Lucca',
        'Source': 'jobs.world.luccasoftware.com / LinkedIn',
        'Contrat': 'CDI',
        'Localisation': 'Paris',
        'Remote': 'Hybride (2j/sem)',
        'Salaire / TJM': '45-55K€',
        'Durée mission': '',
        'Fit / Notes': 'Lucca éditeur SIRH SaaS, 8 700+ clients, 800+ employés. CSM GC (ARR > 14K€, 250+ employees). Implémentation + support + gestion portefeuille 10 comptes. Posté 28/07/2026. Croisement parfait SIRH+CSM. Clients : Accor, Pernod Ricard, Deezer. Anglais C1/C2 requis.',
        'Lien': 'https://jobs.world.luccasoftware.com/lucca/customer-success-sirh-grands-comptes-8d12e285-9f5c-4dcd-ba4c-661c80abe25c',
        'CV à envoyer': 'CV_GaetanFRANCOIS_CSM_EN.html',
        'Prétention': '80-95K€',
    },

    # Lucca - Customer Success SIRH Grands Comptes (Nantes)
    {
        'Priorité': '⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Customer Success SIRH Grands Comptes (Nantes)',
        'Entreprise': 'Lucca',
        'Source': 'welcometothejungle.com / jobs.world.luccasoftware.com',
        'Contrat': 'CDI',
        'Localisation': 'Nantes',
        'Remote': 'Hybride (2j/sem)',
        'Salaire / TJM': '39-48K€',
        'Durée mission': '',
        'Fit / Notes': 'Lucca éditeur SIRH SaaS. Mêmes missions que le poste Paris - portefeuille GC, implémentation, support. Nantes = intéressant géographiquement (proche Anglet vs Paris). Salaire affiché. Anglais C1/C2 requis.',
        'Lien': 'https://www.welcometothejungle.com/fr/companies/lucca/jobs/customer-success-sirh-grands-comptes-nantes_nantes_LUCCA_Na3XAao',
        'CV à envoyer': 'CV_GaetanFRANCOIS_CSM_EN.html',
        'Prétention': '80-95K€',
    },

    # Harvey AI - Enterprise CSM EMEA (Legal AI)
    {
        'Priorité': '⭐⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Enterprise Customer Success Manager, EMEA',
        'Entreprise': 'Harvey AI',
        'Source': 'harvey.ai/careers',
        'Contrat': 'CDI',
        'Localisation': 'Londres (EMEA)',
        'Remote': 'Partiel',
        'Salaire / TJM': '',
        'Durée mission': '',
        'Fit / Notes': 'Harvey AI plateforme IA pour cabinets juridiques, 1 500+ clients, 60+ pays. Enterprise CSM EMEA, intégration IA workflows juridiques. Posté juillet 2026. Profil CSM senior enterprise, 3-4 ans requis. Basé Londres mais couvre France. Fort IA.',
        'Lien': 'https://www.harvey.ai/company/careers/d911b15e-29e4-453e-b192-4201c7937e1f',
        'CV à envoyer': 'CV_GaetanFRANCOIS_CSM_EN.html',
        'Prétention': '80-95K€',
    },

    # Riot Security - CSM Enterprise France
    {
        'Priorité': '⭐⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Customer Success Manager (CSM) Enterprise - France',
        'Entreprise': 'Riot Security',
        'Source': 'welcometothejungle.com / Lever',
        'Contrat': 'CDI',
        'Localisation': 'Paris',
        'Remote': 'Hybride',
        'Salaire / TJM': '',
        'Durée mission': '',
        'Fit / Notes': 'Riot cybersécurité (phishing, awareness), 2 000+ entreprises, 2M+ employés, YC + $45M. CSM Enterprise (>5 000 employés), approche consultative. 3x revenue 2023-2026, cible 40M€ ARR 2026. Posté juillet 2026. Actif 1 semaine.',
        'Lien': 'https://jobs.lever.co/tryriot/5fa84b70-04be-4b8f-99fe-338a276a2b7e',
        'CV à envoyer': 'CV_GaetanFRANCOIS_CSM_EN.html',
        'Prétention': '80-95K€',
    },

    # Okta - Customer Success Manager Paris (IT/Cloud identity)
    {
        'Priorité': '⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Customer Success Manager',
        'Entreprise': 'Okta',
        'Source': 'welcometothejungle.com / LinkedIn',
        'Contrat': 'CDI',
        'Localisation': 'Paris',
        'Remote': 'Hybride',
        'Salaire / TJM': '',
        'Durée mission': '',
        'Fit / Notes': 'Okta IAM/identité cloud, EMEA CSM. French + Italian requis pour couvrir comptes FR et IT. Posté il y a 3 semaines. Profile: drive adoption, Success Plans, manage churn. Fit CSM B2B enterprise, mais italien requis = contrainte.',
        'Lien': 'https://www.welcometothejungle.com/fr/companies/okta/jobs/customer-success-manager_paris_mnpmts4t',
        'CV à envoyer': 'CV_GaetanFRANCOIS_CSM_EN.html',
        'Prétention': '80-95K€',
    },

    # Najar - Senior Customer Success Manager (SaaS Procurement)
    {
        'Priorité': '⭐⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Senior Customer Success Manager (F/M)',
        'Entreprise': 'Najar',
        'Source': 'welcometothejungle.com / Glassdoor',
        'Contrat': 'CDI',
        'Localisation': 'Paris',
        'Remote': 'Hybride',
        'Salaire / TJM': '',
        'Durée mission': '',
        'Fit / Notes': 'Najar plateforme procurement SaaS IA (180+ clients FR/EU, 60+ personnes). Senior CSM: Enterprise, C-level, high-ARR renewals. Mission: shaping CS practice, playbooks, mentoring. Posté juillet 2026. Fort profil senior = fit.',
        'Lien': 'https://www.welcometothejungle.com/en/companies/najar/jobs/customer-success-manager-saas-management_paris',
        'CV à envoyer': 'CV_GaetanFRANCOIS_CSM_EN.html',
        'Prétention': '80-95K€',
    },

    # Salesforce - Customer Success Manager Paris
    {
        'Priorité': '⭐⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Customer Success Manager',
        'Entreprise': 'Salesforce',
        'Source': 'careers.salesforce.com',
        'Contrat': 'CDI',
        'Localisation': 'Paris',
        'Remote': 'Hybride',
        'Salaire / TJM': '',
        'Durée mission': '',
        'Fit / Notes': 'Salesforce CRM leader mondial, Signature Success Plan. CSM "named resource" pour clients premium. Posté avril 2026. Profil senior adviseur, forte relation client. Croisement parfait CSM enterprise + tech.',
        'Lien': 'https://www.salesforce.com/company/careers/jobs/jr334868/customer-success-manager/',
        'CV à envoyer': 'CV_GaetanFRANCOIS_CSM_EN.html',
        'Prétention': '80-95K€',
    },

    # ── ONGLET OFFRES IA ────────────────────────────────────────────────────────

    # INGELINE TECHNOLOGIES - Consultant Formation / Conduite du Changement IA
    {
        'Priorité': '⭐⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Consultant Formation / Conduite du Changement IA (H/F)',
        'Entreprise': 'INGELINE TECHNOLOGIES',
        'Source': 'LinkedIn',
        'Contrat': 'CDI',
        'Localisation': 'Île-de-France',
        'Remote': 'Partiel',
        'Salaire / TJM': '',
        'Durée mission': '',
        'Fit / Notes': 'INGELINE TECHNOLOGIES conseil & formation IT. Conception et animation formations IA générative + conduite du changement. ChatGPT, Copilot. Posté il y a 3 semaines. 200+ candidatures. Profil Bac+5 formation/changement/digital. Fit parfait : IA générative + conduite du changement = coeur du profil Gaëtan.',
        'Lien': 'https://fr.linkedin.com/jobs/view/consultant-formation-conduite-du-changement-ia-h-f-at-ingeline-technologies-4426303663',
        'CV à envoyer': 'Resume_GaetanFRANCOIS_IA.html',
        'Prétention': '60-75K€',
    },

    # Michael Page - Consultant Formateur IA & Management
    {
        'Priorité': '⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Consultant Formateur - IA & Management (H/F)',
        'Entreprise': 'PME conseil formation managériale (via Michael Page)',
        'Source': 'michaelpage.fr',
        'Contrat': 'CDI',
        'Localisation': 'Lille',
        'Remote': 'Non précisé',
        'Salaire / TJM': '',
        'Durée mission': '',
        'Fit / Notes': 'PME conseil en formation managériale, création d\'offre IA en management. CDI. Conception modules IA, relation client, pédagogie. Posté 26/05/2026. Lille = contrainte géographique vs Anglet, mais remote possible à négocier. Profil IA + pédagogie = bon fit.',
        'Lien': 'https://www.michaelpage.fr/job-detail/consultant-formateur-ia-management-hf/ref/jn-032026-6962869',
        'CV à envoyer': 'Resume_GaetanFRANCOIS_IA.html',
        'Prétention': '60-75K€',
    },

    # Editions ENI - Formateur IA collectivités (freelance)
    {
        'Priorité': '⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Formateur IA - Usages outils numériques en collectivité (F/H)',
        'Entreprise': 'Editions ENI',
        'Source': 'free-work.com',
        'Contrat': 'Freelance',
        'Localisation': 'Auvergne-Rhône-Alpes',
        'Remote': 'Partiel',
        'Salaire / TJM': '',
        'Durée mission': '',
        'Fit / Notes': 'Editions ENI n°1 éditeur livres informatique. Formateur IA pour collectivités territoriales, sessions 1-3 jours. Posté mars 2026. Freelance. Secteur public. Profil formateur terrain IA générative = fit. Zone géographique éloignée d\'Anglet mais remote partiel.',
        'Lien': 'https://www.free-work.com/fr/tech-it/directeur-des-systemes-dinformation-dsi/job-mission/nous-recrutons-formateur-rice-usages-des-outils-numeriques-et-de-lia-encollectivite',
        'CV à envoyer': 'Resume_GaetanFRANCOIS_IA.html',
        'Prétention': '400-600€/j',
    },

    # mission-freelances.fr - Consultant IA Générative & Conduite du changement
    {
        'Priorité': '⭐⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Consultant IA Générative & Conduite du changement',
        'Entreprise': 'Client (via mission-freelances.fr)',
        'Source': 'mission-freelances.fr',
        'Contrat': 'Freelance',
        'Localisation': 'Paris',
        'Remote': 'Sur site Paris',
        'Salaire / TJM': '',
        'Durée mission': '',
        'Fit / Notes': 'Mission: déploiement et adoption outils IA générative (ChatGPT, Gemini, Adobe Firefly), lien stratégie globale - équipes métiers (Marketing, CRM, Retail, Studio créatif). Posté 17/06/2026. Profil: consultant freelance ou PO expérimenté transformation digitale. Fit excellent IA + conduite du changement.',
        'Lien': 'https://www.mission-freelances.fr/missions/consultant-ia-generative-conduite-du-changement-paris-87a17202/',
        'CV à envoyer': 'Resume_GaetanFRANCOIS_IA.html',
        'Prétention': '600-750€/j',
    },

    # Cegos - Consultant Formateur IA marchés publics (freelance)
    {
        'Priorité': '⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Consultant Formateur IA au service des marchés publics (H/F)',
        'Entreprise': 'Cegos',
        'Source': 'recrutement.cegos.com',
        'Contrat': 'Freelance',
        'Localisation': 'Issy-les-Moulineaux / France',
        'Remote': 'Partiel',
        'Salaire / TJM': '',
        'Durée mission': '',
        'Fit / Notes': 'Cegos organisme formation #1 FR, 1 000 formateurs réseau. Formation IA pour marchés publics (appels d\'offres, sourcing automatisé, rédaction specs). Formateur indépendant réseau externe Cegos. Posté il y a 2 mois. Profil IA générative + secteur public.',
        'Lien': 'https://recrutement.cegos.com/jobs/7672957-consultant-formateur-h-f-en-ia-au-service-des-marches-publics',
        'CV à envoyer': 'Resume_GaetanFRANCOIS_IA.html',
        'Prétention': '400-600€/j',
    },

]

if __name__ == '__main__':
    ajouter_offres(offres, verbose=True)
    print("\nTerminé. Offres ajoutées dans offres_emploi.xlsx")
