# -*- coding: utf-8 -*-
"""Première relance USA du 22/08/2026 : offres d'entreprises basées aux USA,
ouvertes au télétravail international (pas US-only). Onglet dédié 'Offres USA'.
"""

from add_offre import ajouter_offres

CV_CSM = "CV_GaetanFRANCOIS_CSM_EN.pdf"
CV_SIRH_EN = "Resume_GaetanFRANCOIS_SIRH_EN.pdf"
CV_PM_EN = "Resume_GaetanFRANCOIS_PM_EN.pdf"
CV_PM_PLATFORM = "Resume_GaetanFRANCOIS_PM_Platform_EN.pdf"
CV_ASHBY = "Resume_GaetanFRANCOIS_Ashby_EN.pdf"
CV_DATAMIG = "Resume_GaetanFRANCOIS_DataMigrationLead_EN.pdf"
CV_CONSTRUCTOR = "Resume_GaetanFRANCOIS_Constructor_EN.pdf"

USA = "Offres USA"

OFFRES = [
    # ── CSM / TAM / Solutions Engineer ──
    dict(Onglet=USA, Poste="Strategic Customer Success Manager - EMEA", Entreprise="Ashby",
         Source="API Ashby", Lien="https://jobs.ashbyhq.com/ashby/1cf7c730-caba-4fc3-8b98-52a0735ef14b",
         Contrat="CDI", Localisation="San Francisco, USA", Remote="Remote - European Union", **{"Salaire / TJM": "N/C"},
         Priorité="⭐⭐⭐⭐⭐", **{"Fit / Notes": "CSM stratégique, book ~20 comptes, remote UE confirmé"}, **{"CV à envoyer": CV_CSM}),
    dict(Onglet=USA, Poste="Mid-Market Customer Success Manager - EMEA", Entreprise="Ashby",
         Source="API Ashby", Lien="https://jobs.ashbyhq.com/ashby/62d4f71e-f56c-447a-a965-a9c2ea8eac5e",
         Contrat="CDI", Localisation="San Francisco, USA", Remote="Remote - European Union", **{"Salaire / TJM": "N/C"},
         Priorité="⭐⭐⭐⭐", **{"Fit / Notes": "CSM mid-market, remote UE confirmé"}, **{"CV à envoyer": CV_CSM}),
    dict(Onglet=USA, Poste="Customer Success Engineer", Entreprise="Hightouch",
         Source="API Greenhouse", Lien="https://job-boards.greenhouse.io/hightouch/jobs/5770046004",
         Contrat="CDI", Localisation="San Francisco, USA", Remote="Remote (Europe)", **{"Salaire / TJM": "N/C"},
         Priorité="⭐⭐⭐⭐", **{"Fit / Notes": "CSM technique, remote Europe confirmé"}, **{"CV à envoyer": CV_CSM}),
    dict(Onglet=USA, Poste="Solutions Engineer, Mid-Market, EMEA", Entreprise="Hightouch",
         Source="API Greenhouse", Lien="https://job-boards.greenhouse.io/hightouch/jobs/5990367004",
         Contrat="CDI", Localisation="San Francisco, USA", Remote="EMEA", **{"Salaire / TJM": "N/C"},
         Priorité="⭐⭐⭐⭐", **{"Fit / Notes": "Avant-vente technique, proche profil ALTI-TCS/L'Oréal"}, **{"CV à envoyer": CV_CSM}),
    dict(Onglet=USA, Poste="Technical Account Manager, EMEA", Entreprise="Hightouch",
         Source="API Greenhouse", Lien="https://job-boards.greenhouse.io/hightouch/jobs/6146017004",
         Contrat="CDI", Localisation="San Francisco, USA", Remote="Europe", **{"Salaire / TJM": "N/C"},
         Priorité="⭐⭐⭐⭐", **{"Fit / Notes": "TAM, remote Europe confirmé"}, **{"CV à envoyer": CV_CSM}),
    dict(Onglet=USA, Poste="Solutions Engineer, Enterprise (Pre-Sales) - German speaking", Entreprise="Hightouch",
         Source="API Greenhouse", Lien="https://job-boards.greenhouse.io/hightouch/jobs/5852695004",
         Contrat="CDI", Localisation="San Francisco, USA", Remote="Europe", **{"Salaire / TJM": "N/C"},
         Priorité="⭐⭐", **{"Fit / Notes": "Remote Europe confirmé mais exige l'allemand courant (lacune de langue)"}, **{"CV à envoyer": CV_CSM}),
    dict(Onglet=USA, Poste="Customer Success Architect, EMEA", Entreprise="GitLab",
         Source="API Greenhouse", Lien="https://job-boards.greenhouse.io/gitlab/jobs/8561952002",
         Contrat="CDI", Localisation="USA (tout-remote, Nasdaq)", Remote="Remote, France explicite", **{"Salaire / TJM": "N/C"},
         Priorité="⭐⭐⭐⭐⭐", **{"Fit / Notes": "France explicitement listée, CSA senior orienté ROI/exec relationships"}, **{"CV à envoyer": CV_CSM}),
    dict(Onglet=USA, Poste="Manager, Customer Success Managers, EMEA", Entreprise="GitLab",
         Source="API Greenhouse", Lien="https://job-boards.greenhouse.io/gitlab/jobs/8613199002",
         Contrat="CDI", Localisation="USA (tout-remote)", Remote="Remote, Austria/Germany", **{"Salaire / TJM": "N/C"},
         Priorité="⭐⭐⭐", **{"Fit / Notes": "Manager CSM EMEA ; éligibilité France à confirmer (pays listés AT/DE)"}, **{"CV à envoyer": CV_CONSTRUCTOR}),
    dict(Onglet=USA, Poste="Customer Success Architect, CEUR", Entreprise="GitLab",
         Source="API Greenhouse", Lien="https://job-boards.greenhouse.io/gitlab/jobs/8646852002",
         Contrat="CDI", Localisation="USA (tout-remote)", Remote="Remote, Germany", **{"Salaire / TJM": "N/C"},
         Priorité="⭐⭐", **{"Fit / Notes": "Europe Centrale ; éligibilité France à confirmer"}, **{"CV à envoyer": CV_CSM}),
    dict(Onglet=USA, Poste="Senior Pre-Sales Solutions Engineer - Europe", Entreprise="Deepgram",
         Source="API Ashby", Lien="https://jobs.ashbyhq.com/deepgram/7ac1a5bc-f305-4f2a-a547-394566a549b2",
         Contrat="CDI", Localisation="San Francisco, USA", Remote="EU - Remote", **{"Salaire / TJM": "N/C"},
         Priorité="⭐⭐⭐⭐", **{"Fit / Notes": "Avant-vente technique, startup Voice AI Series C, croisement IA"}, **{"CV à envoyer": CV_CSM}),

    # ── HRIS / SIRH / Data Migration ──
    dict(Onglet=USA, Poste="Senior Workday Implementation Specialist", Entreprise="Remote.com",
         Source="API Greenhouse", Lien="https://job-boards.greenhouse.io/remotecom/jobs/7548213003",
         Contrat="CDI", Localisation="San Francisco, USA", Remote="Remote-EMEA", **{"Salaire / TJM": "75 000-84 000€/an"},
         Priorité="⭐⭐⭐⭐⭐", **{"Fit / Notes": "Implémentation Workday HCM paie mondiale, recoupe directement l'expertise migration de données SIRH (OnePayroll, 8 pays)"}, **{"CV à envoyer": CV_ASHBY}),
    dict(Onglet=USA, Poste="Customer Success Manager (EMEA)", Entreprise="Oyster HR",
         Source="API Ashby", Lien="https://jobs.ashbyhq.com/oyster/3670104d-08c8-48eb-a7ef-205efb7d920f",
         Contrat="CDI", Localisation="San Francisco, USA", Remote="EMEA (France non citée explicitement)", **{"Salaire / TJM": "N/C"},
         Priorité="⭐⭐⭐", **{"Fit / Notes": "CSM senior, éditeur EOR ; éligibilité France à confirmer en candidature"}, **{"CV à envoyer": CV_CSM}),

    # ── Product Manager ──
    dict(Onglet=USA, Poste="Senior Product Manager, Remote Build", Entreprise="Remote.com",
         Source="API Greenhouse", Lien="https://job-boards.greenhouse.io/remotecom/jobs/7331443003",
         Contrat="CDI", Localisation="San Francisco, USA", Remote="Remote-France explicite", **{"Salaire / TJM": "$60,000-$151,650"},
         Priorité="⭐⭐⭐⭐⭐", **{"Fit / Notes": "France nommée explicitement, éditeur HRIS le mieux aligné, salaire affiché en USD"}, **{"CV à envoyer": CV_PM_PLATFORM}),
    dict(Onglet=USA, Poste="Product Manager, Billing Platform", Entreprise="Remote.com",
         Source="API Greenhouse", Lien="https://job-boards.greenhouse.io/remotecom/jobs/7885108003",
         Contrat="CDI", Localisation="San Francisco, USA", Remote="Remote-EMEA", **{"Salaire / TJM": "$50,000-$112,300"},
         Priorité="⭐⭐⭐⭐", **{"Fit / Notes": "Billing/opérations RH-paie multi-pays, salaire affiché en USD"}, **{"CV à envoyer": CV_PM_PLATFORM}),
    dict(Onglet=USA, Poste="Product Manager, Contractor Management", Entreprise="Remote.com",
         Source="API Greenhouse", Lien="https://job-boards.greenhouse.io/remotecom/jobs/7885031003",
         Contrat="CDI", Localisation="San Francisco, USA", Remote="Remote-EMEA", **{"Salaire / TJM": "N/C"},
         Priorité="⭐⭐⭐⭐", **{"Fit / Notes": "Contractor management, proche opérations RH multi-pays"}, **{"CV à envoyer": CV_PM_PLATFORM}),
    dict(Onglet=USA, Poste="Senior Product Manager, Agentic AI Assistants (EMEA)", Entreprise="Deel",
         Source="ATS propriétaire Deel", Lien="https://jobs.deel.com/deel/job-details/d06475eb-fe54-429c-bed0-20d3eadbe94c/overview",
         Contrat="CDI", Localisation="San Francisco, USA", Remote="France explicitement listée (+ DE/IT/PT/RO/EE/IE/IL/UAE/UK)", **{"Salaire / TJM": "OTE en USD, non affiché"},
         Priorité="⭐⭐⭐⭐⭐", **{"Fit / Notes": "Double fit PM x IA générative, France explicitement listée, éditeur EOR/HRIS mondial"}, **{"CV à envoyer": CV_PM_PLATFORM}),
    dict(Onglet=USA, Poste="Staff Product Manager, Deel IT", Entreprise="Deel",
         Source="ATS propriétaire Deel", Lien="https://jobs.deel.com/deel/job-details/607441dd-c469-43d1-b2cf-5e0c6b7ec20b/overview",
         Contrat="CDI", Localisation="San Francisco, USA", Remote="France listée (+ UK/UAE/ES/DE/LU/BE/IE/IL/TR)", **{"Salaire / TJM": "N/C"},
         Priorité="⭐⭐⭐⭐", **{"Fit / Notes": "PM Staff, France listée, éditeur EOR/HRIS mondial"}, **{"CV à envoyer": CV_PM_PLATFORM}),
    dict(Onglet=USA, Poste="Lead Product Manager", Entreprise="Oyster HR",
         Source="API Ashby", Lien="https://jobs.ashbyhq.com/oyster/20b0c812-255e-433b-99bb-2d1f399f0c7a",
         Contrat="CDI", Localisation="San Francisco, USA", Remote="EMEA", **{"Salaire / TJM": "N/C"},
         Priorité="⭐⭐⭐⭐", **{"Fit / Notes": "Lead PM, éditeur EOR concurrent de Remote.com, remote EMEA"}, **{"CV à envoyer": CV_PM_PLATFORM}),
    dict(Onglet=USA, Poste="Product Manager", Entreprise="Linear",
         Source="API Ashby", Lien="https://jobs.ashbyhq.com/linear/86abcce0-04b2-405c-9a8e-e0ca84813914",
         Contrat="CDI", Localisation="San Francisco, USA", Remote="Europe", **{"Salaire / TJM": "N/C"},
         Priorité="⭐⭐", **{"Fit / Notes": "Outil de gestion de projet orienté développeurs (lacune connue), remote Europe confirmé"}, **{"CV à envoyer": CV_PM_PLATFORM}),

    # ── IA / croisement IA (Dataiku, Cresta, PostHog, Checkly via HN) ──
    dict(Onglet=USA, Poste="Senior Product Manager", Entreprise="Dataiku",
         Source="API Greenhouse", Lien="https://job-boards.greenhouse.io/dataiku/jobs/5812604004",
         Contrat="CDI", Localisation="USA", Remote="France, Remote explicite", **{"Salaire / TJM": "N/C"},
         Priorité="⭐⭐⭐⭐⭐", **{"Fit / Notes": "Éditeur IA authentique, France Remote explicitement listée"}, **{"CV à envoyer": CV_PM_PLATFORM}),
    dict(Onglet=USA, Poste="Product Manager – Business Applications", Entreprise="Dataiku",
         Source="API Greenhouse", Lien="https://job-boards.greenhouse.io/dataiku/jobs/6122317004",
         Contrat="CDI", Localisation="USA", Remote="France, Remote explicite", **{"Salaire / TJM": "N/C"},
         Priorité="⭐⭐⭐⭐⭐", **{"Fit / Notes": "Éditeur IA authentique, France Remote explicitement listée"}, **{"CV à envoyer": CV_PM_PLATFORM}),
    dict(Onglet=USA, Poste="Technical Account Manager - France", Entreprise="Dataiku",
         Source="API Greenhouse", Lien="https://job-boards.greenhouse.io/dataiku/jobs/6148352004",
         Contrat="CDI", Localisation="France (Paris) / Remote", Remote="France, Remote explicite", **{"Salaire / TJM": "N/C"},
         Priorité="⭐⭐⭐⭐⭐", **{"Fit / Notes": "TAM France explicite, éditeur IA authentique"}, **{"CV à envoyer": CV_CSM}),
    dict(Onglet=USA, Poste="Forward Deployed Product Manager - AI Agent (EMEA)", Entreprise="Cresta",
         Source="API Greenhouse", Lien="https://job-boards.greenhouse.io/cresta/jobs/5068157008",
         Contrat="CDI", Localisation="UK (Remote)", Remote="UK (Remote), périmètre EMEA suggéré", **{"Salaire / TJM": "N/C"},
         Priorité="⭐⭐⭐", **{"Fit / Notes": "PM produit IA agentique EMEA ; éligibilité France à confirmer"}, **{"CV à envoyer": CV_PM_PLATFORM}),
    dict(Onglet=USA, Poste="Sales Enablement Manager, EMEA", Entreprise="Cresta",
         Source="API Greenhouse", Lien="https://job-boards.greenhouse.io/cresta/jobs/5181786008",
         Contrat="CDI", Localisation="UK (Remote)", Remote="UK (Remote), périmètre EMEA suggéré", **{"Salaire / TJM": "N/C"},
         Priorité="⭐⭐⭐", **{"Fit / Notes": "Enablement commercial EMEA, éditeur IA conversationnelle ; éligibilité France à confirmer"}, **{"CV à envoyer": CV_CSM}),
    dict(Onglet=USA, Poste="Technical Customer Success Manager - EMEA", Entreprise="PostHog",
         Source="HN Who's Hiring + API Ashby", Lien="https://jobs.ashbyhq.com/posthog/0be1b52c-2401-4ae2-b7fc-5d018c1ff96f",
         Contrat="CDI", Localisation="Distribuée, all-remote", Remote="Remote (EMEA), GMT-8 à GMT+2", **{"Salaire / TJM": "N/C"},
         Priorité="⭐⭐⭐⭐", **{"Fit / Notes": "CSM technique, entreprise all-remote confirmée, fuseau France dans la fourchette"}, **{"CV à envoyer": CV_CSM}),
    dict(Onglet=USA, Poste="Technical Account Manager - EMEA", Entreprise="PostHog",
         Source="HN Who's Hiring + API Ashby", Lien="https://jobs.ashbyhq.com/posthog/b42fd20b-b647-4f42-b725-b29ca472cba8",
         Contrat="CDI", Localisation="Distribuée, all-remote", Remote="Remote (EMEA), GMT-8 à GMT+2", **{"Salaire / TJM": "N/C"},
         Priorité="⭐⭐⭐⭐", **{"Fit / Notes": "TAM, même vivier que le CSM PostHog ci-dessus"}, **{"CV à envoyer": CV_CSM}),
    dict(Onglet=USA, Poste="Senior Sales Engineer (remote, Europe)", Entreprise="Checkly",
         Source="HN Who's Hiring + API Ashby", Lien="https://jobs.ashbyhq.com/checkly/0dea9c4c-cecd-48d2-803a-56e3cfa1a873",
         Contrat="CDI", Localisation="Remote-first, équipe distribuée Europe/US", Remote="Remote (UTC+1 to UTC+2)", **{"Salaire / TJM": "Bandes salariales publiées (non extraites)"},
         Priorité="⭐⭐⭐⭐", **{"Fit / Notes": "Fuseau horaire France exact, avant-vente/onboarding technique"}, **{"CV à envoyer": CV_CSM}),
]

if __name__ == "__main__":
    ajouter_offres(OFFRES)
