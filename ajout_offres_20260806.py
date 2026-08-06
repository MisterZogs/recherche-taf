"""
Ajout des offres trouvées lors de la recherche exhaustive du 2026-08-06.

Passe menée un jour après celle du 05/08, donc volume nouveau limité : la
plupart des annonces remontées étaient déjà dans le tableur. L'effort a porté
en priorité sur les sources qui avaient échoué la veille et sur celles qui
n'avaient pas encore été couvertes.

Sources couvertes : free-work.com (SIRH, SAP HCM, IA), LinkedIn (SuccessFactors
France, HRIS, SAP HCM), welcometothejungle.com, jobs.ashbyhq.com, jobs.lever.co,
job-boards.greenhouse.io, mission-freelances.fr, collective.work, malt.fr,
recrutement-fr.forvismazars.com, capgemini.com, kpmg.fr, zalaris.com,
himalayas.app, wellfound.com, glassdoor.fr, efinancialcareers.

Sites toujours en erreur : zalaris.com/career (404), kpmg.fr offres (404),
capgemini.com/fr-fr/jobs (page de navigation sans offres), himalayas.app
(listing sans postes de la cible), collective.work AI Evangelist (offre retirée).
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
import add_offre
from add_offre import ajouter_offres

POSTES_IA = {
    'Chef de Produit Plateforme IA',
}
_is_ia_orig = add_offre._is_ia
add_offre._is_ia = lambda poste: poste in POSTES_IA or _is_ia_orig(poste)


offres = [

    # ── ONGLET OFFRES CSM ──────────────────────────────────────────────────────

    # Remote.com — Pay Customer Success Manager, Mid-Market / Enterprise
    {
        'Priorité': '⭐⭐⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Pay Customer Success Manager, Mid-Market / Enterprise',
        'Entreprise': 'Remote.com',
        'Source': 'job-boards.greenhouse.io',
        'Contrat': 'CDI',
        'Localisation': 'Remote (monde)',
        'Remote': '100% remote',
        'Salaire / TJM': '',
        'Durée mission': '',
        'Fit / Notes': "Remote.com n'a aucun bureau et recrute en remote intégral, ce qui règle la contrainte d'Anglet. Le poste porte sur la paie et le SIRH auprès de comptes mid-market et enterprise, donc exactement le croisement Customer Success et SIRH construit en quinze ans. C'est la meilleure trouvaille de la journée ; deux autres postes Remote.com sont déjà suivis dans le tableur, penser à coordonner les candidatures pour ne pas arriver en doublon auprès du même recruteur.",
        'Lien': 'https://job-boards.greenhouse.io/remotecom/jobs/7753146003',
        'CV à envoyer': 'Resume_GaetanFRANCOIS_SIRH_EN.html',
        'Prétention': '85-95K€',
    },

    # RemoFirst — Customer Success Manager EMEA
    {
        'Priorité': '⭐⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Customer Success Manager EMEA',
        'Entreprise': 'RemoFirst',
        'Source': 'jobs.lever.co',
        'Contrat': 'CDI',
        'Localisation': 'EMEA (remote)',
        'Remote': '100% remote',
        'Salaire / TJM': '',
        'Durée mission': '',
        'Fit / Notes': "Plateforme d'emploi international couvrant la paie et la conformité multi-pays, terrain proche de OnePayroll chez L'Oréal. Le poste couvre la zone EMEA en remote. Un poste Scaled CSM EMEA chez RemoFirst figure déjà dans le tableur ; vérifier s'il s'agit d'une ouverture distincte avant de postuler aux deux.",
        'Lien': 'https://jobs.lever.co/remofirst/99b6bcf0-c14b-4806-aadc-b27d41119445',
        'CV à envoyer': 'Resume_GaetanFRANCOIS.html',
        'Prétention': '80-90K€',
    },

    # Remote.com — CSM SMB EMEA
    {
        'Priorité': '⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Customer Success Manager, SMB - EMEA',
        'Entreprise': 'Remote.com',
        'Source': 'job-boards.greenhouse.io',
        'Contrat': 'CDI',
        'Localisation': 'EMEA (remote)',
        'Remote': '100% remote',
        'Salaire / TJM': '',
        'Durée mission': '',
        'Fit / Notes': "Même employeur entièrement distribué, mais sur le segment SMB. Le portefeuille de petits comptes se situe en dessous du niveau de séniorité visé et la rémunération suit. À garder en repli si le poste Mid-Market et Enterprise ne donne rien.",
        'Lien': 'https://job-boards.greenhouse.io/remotereferralboardinternaluseonly/jobs/7793430003',
        'CV à envoyer': 'Resume_GaetanFRANCOIS.html',
        'Prétention': '70-80K€',
    },

    # Mento — Founding Customer Success Manager
    {
        'Priorité': '⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Founding Customer Success Manager',
        'Entreprise': 'Mento',
        'Source': 'job-boards.greenhouse.io',
        'Contrat': 'CDI',
        'Localisation': 'Remote',
        'Remote': 'Remote',
        'Salaire / TJM': '',
        'Durée mission': '',
        'Fit / Notes': "Poste fondateur du Customer Success chez Mento, distinct du Customer Success Coach déjà ajouté hier. Le mandat de création de la fonction rejoint l'expérience de co-fondateur de WallOfTraders.com. Vérifier l'éligibilité géographique, plusieurs annonces Mento ciblent le Royaume-Uni et l'Irlande.",
        'Lien': 'https://job-boards.greenhouse.io/mento/jobs/4606205005',
        'CV à envoyer': 'Resume_GaetanFRANCOIS.html',
        'Prétention': '80-90K€',
    },

    # Spring Health — Customer Success Manager remote
    {
        'Priorité': '⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Customer Success Manager',
        'Entreprise': 'Spring Health',
        'Source': 'job-boards.greenhouse.io',
        'Contrat': 'CDI',
        'Localisation': 'Remote',
        'Remote': '100% remote',
        'Salaire / TJM': '',
        'Durée mission': '',
        'Fit / Notes': "Éditeur de santé mentale en entreprise, vendu aux directions RH ; l'interlocuteur est donc le même que sur les projets SIRH. Le poste est affiché en remote complet. Vérifier que le recrutement ne se limite pas aux États-Unis, ce qui est fréquent chez cet éditeur.",
        'Lien': 'https://job-boards.greenhouse.io/springhealth66/jobs/4543797005',
        'CV à envoyer': 'Resume_GaetanFRANCOIS.html',
        'Prétention': '80-90K€',
    },

    # Censys — Customer Success Manager
    {
        'Priorité': '⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Customer Success Manager',
        'Entreprise': 'Censys',
        'Source': 'job-boards.greenhouse.io',
        'Contrat': 'CDI',
        'Localisation': 'Remote',
        'Remote': 'Remote',
        'Salaire / TJM': '',
        'Durée mission': '',
        'Fit / Notes': "Éditeur de cybersécurité avec un produit très technique, ce qui joue plutôt en faveur du profil technico-fonctionnel. Le domaine reste éloigné du SIRH et l'entreprise est américaine ; l'éligibilité depuis la France est à confirmer avant d'investir du temps.",
        'Lien': 'https://job-boards.greenhouse.io/censys/jobs/8541249002',
        'CV à envoyer': 'Resume_GaetanFRANCOIS.html',
        'Prétention': '80-90K€',
    },

    # Digitevent — Customer Success Manager Paris
    {
        'Priorité': '⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Customer Success Manager - CSM',
        'Entreprise': 'Digitevent',
        'Source': 'welcometothejungle.com',
        'Contrat': 'CDI',
        'Localisation': 'Paris',
        'Remote': 'Télétravail occasionnel',
        'Salaire / TJM': '',
        'Durée mission': '',
        'Fit / Notes': "Éditeur SaaS événementiel, démarrage annoncé au 24/08/2026. Le télétravail est seulement occasionnel, ce qui entre en conflit direct avec l'objectif 100% remote. À traiter en volume plutôt qu'en priorité.",
        'Lien': 'https://www.welcometothejungle.com/fr/companies/digitevent/jobs/customer-success-manager-csm_paris',
        'CV à envoyer': 'Resume_GaetanFRANCOIS.html',
        'Prétention': '70-80K€',
    },

    # WizVille — Customer Success Manager B2B
    {
        'Priorité': '⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Customer Success Manager B2B (H/F/X)',
        'Entreprise': 'WizVille',
        'Source': 'welcometothejungle.com',
        'Contrat': 'CDI',
        'Localisation': 'Paris',
        'Remote': 'À vérifier',
        'Salaire / TJM': '',
        'Durée mission': '',
        'Fit / Notes': "Éditeur SaaS de gestion de la satisfaction client, portefeuille B2B avec des enseignes multi-sites. La logique de comptes multi-entités rappelle le contexte L'Oréal. Le poste est parisien et le niveau de séniorité affiché reste modéré.",
        'Lien': 'https://www.welcometothejungle.com/fr/companies/wizville/jobs/customer-success-manager-b2b-h-f-x_paris_WIZVI_eZQzwrL',
        'CV à envoyer': 'Resume_GaetanFRANCOIS.html',
        'Prétention': '70-80K€',
    },

    # ── ONGLET OFFRES SIRH ─────────────────────────────────────────────────────

    # Onepoint — Leader SIRH
    {
        'Priorité': '⭐⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Leader SIRH H/F',
        'Entreprise': 'Onepoint',
        'Source': 'LinkedIn',
        'Contrat': 'CDI',
        'Localisation': 'Paris',
        'Remote': 'À vérifier',
        'Salaire / TJM': '',
        'Durée mission': '',
        'Fit / Notes': "Poste de leader de l'offre SIRH chez Onepoint, publié il y a une semaine. Le niveau dépasse celui du Consultant SIRH déjà suivi chez le même cabinet ; c'est un rôle de référent qui correspond mieux aux quinze ans d'expérience. Onepoint recrute aussi sur un Consultant Learning & IA déjà présent dans le tableur, ce qui montre l'ouverture du cabinet sur le croisement IA et RH.",
        'Lien': 'https://fr.linkedin.com/jobs/successfactors-emplois-france',
        'CV à envoyer': 'Resume_GaetanFRANCOIS_SIRH.html',
        'Prétention': '85-100K€',
    },

    # Eramet — Spécialiste SIRH Groupe Core RH, Learning & Development
    {
        'Priorité': '⭐⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Spécialiste SIRH Groupe - Core RH, Learning & Development H/F',
        'Entreprise': 'Eramet',
        'Source': 'LinkedIn',
        'Contrat': 'CDI',
        'Localisation': 'Paris',
        'Remote': 'À vérifier',
        'Salaire / TJM': '',
        'Durée mission': '',
        'Fit / Notes': "Troisième variante du poste de Spécialiste SIRH Groupe chez Eramet, après Core RH Recrutement et Talent Performance déjà suivies. Le groupe minier reconstruit visiblement toute son équipe SIRH, ce qui laisse plusieurs portes d'entrée. Le module Learning est celui où l'expérience de formation des RH européens L'Oréal se raconte le mieux.",
        'Lien': 'https://fr.linkedin.com/jobs/successfactors-emplois-france',
        'CV à envoyer': 'Resume_GaetanFRANCOIS_SIRH.html',
        'Prétention': '75-90K€',
    },

    # Forvis Mazars — Consultant senior ou manager transformation RH et SIRH
    {
        'Priorité': '⭐⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Consultant senior ou manager en transformation RH et SIRH',
        'Entreprise': 'Forvis Mazars',
        'Source': 'recrutement-fr.forvismazars.com',
        'Contrat': 'CDI',
        'Localisation': 'Lyon',
        'Remote': 'Hybride',
        'Salaire / TJM': '',
        'Durée mission': '',
        'Fit / Notes': "L'équipe HR Consulting de Lyon cherche des profils expérimentés sur la transformation RH et le SIRH. Le périmètre annoncé couvre l'expression de besoin, les études de faisabilité, le choix de solution SIRH puis le pilotage du déploiement et la conduite du changement, ce qui recoupe le parcours point par point. L'annonce ouvre explicitement sur un grade manager, donc négociable vers le haut. Lyon reste loin d'Anglet, d'où l'importance de clarifier l'hybride.",
        'Lien': 'https://recrutement-fr.forvismazars.com/',
        'CV à envoyer': 'Resume_GaetanFRANCOIS_SIRH.html',
        'Prétention': '75-90K€',
    },

    # Lightspeed Commerce — Field Implementation Consultant
    {
        'Priorité': '⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Field Implementation Consultant (English & French Speaking)',
        'Entreprise': 'Lightspeed Commerce',
        'Source': 'jobs.ashbyhq.com',
        'Contrat': 'CDI',
        'Localisation': 'Paris',
        'Remote': 'À vérifier',
        'Salaire / TJM': '',
        'Durée mission': '',
        'Fit / Notes': "Poste d'implémentation bilingue chez un éditeur de solutions de commerce. Le métier d'implémentation et de formation client correspond au parcours, mais le produit relève du point de vente et non du SIRH. Le niveau affiché est junior, ce qui limite fortement l'intérêt salarial.",
        'Lien': 'https://jobs.ashbyhq.com/lightspeedhq/fd526348-4577-4c0f-bd0d-f87f3c110b86',
        'CV à envoyer': 'Resume_GaetanFRANCOIS.html',
        'Prétention': '65-75K€',
    },

    # ── ONGLET OFFRES IA ───────────────────────────────────────────────────────

    # Formateur / Formatrice en IA Générative — Île-de-France
    {
        'Priorité': '⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Formateur / Formatrice en Intelligence Artificielle Générative',
        'Entreprise': 'n.c. (via mission-freelances.fr)',
        'Source': 'mission-freelances.fr',
        'Contrat': 'Freelance',
        'Localisation': 'Île-de-France',
        'Remote': 'Présentiel ou distanciel',
        'Salaire / TJM': '',
        'Durée mission': '',
        'Fit / Notes': "Animation de formations certifiantes sur l'usage responsable de l'IA générative, avec sessions possibles à distance. Deux prérequis administratifs bloquent aujourd'hui : un numéro de déclaration d'activité de formateur et idéalement la certification RS6776. Obtenir un NDA est faisable et ouvrirait tout le segment formation certifiante ; c'est le vrai enseignement de cette annonce, au delà de la mission elle-même. Publiée le 25/06/2026.",
        'Lien': 'https://www.mission-freelances.fr/missions/formateur-formatrice-en-intelligence-artificielle-generative-ile-de-france-a5471a52/',
        'CV à envoyer': 'Resume_GaetanFRANCOIS_IA.html',
        'Prétention': '700-900€/j',
    },

    # JCW Search — Chef de Produit Plateforme IA
    {
        'Priorité': '⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Chef de Produit Plateforme IA',
        'Entreprise': 'JCW Search Ltd',
        'Source': 'free-work.com',
        'Contrat': 'Freelance',
        'Localisation': 'Paris',
        'Remote': 'Partiel',
        'Salaire / TJM': '610-1110€/j',
        'Durée mission': '',
        'Fit / Notes': "Mission publiée le 05/08/2026, avec un TJM très au-dessus de la fourchette cible. Le rôle consiste à définir la vision et la feuille de route d'une plateforme IA, ce qui rejoint l'expérience produit ; la partie industrialisation LLMOps demande en revanche un socle technique que le profil n'a pas. À tenter uniquement si l'annonce complète confirme un poste de pilotage et non d'ingénierie.",
        'Lien': 'https://www.free-work.com/fr/tech-it/jobs/ia',
        'CV à envoyer': 'Resume_GaetanFRANCOIS_IA.html',
        'Prétention': '800-900€/j',
    },
]

ajouter_offres(offres)
