"""
Ajout des offres trouvées sur upwork.com et freelancer.com le 2026-08-06.

Ces plateformes avaient été écartées à tort plus tôt dans la journée au motif
d'un TJM bas ; le TJM n'est pas un critère de filtrage. Après vérification,
elles portent bien des missions dans le périmètre.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from add_offre import ajouter_offres

offres = [

    # ── ONGLET OFFRES IA ───────────────────────────────────────────────────────

    # Upwork — AI Governance Consultant / Trainer, formation en entreprise
    {
        'Priorité': '⭐⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'AI Governance Consultant / Trainer - Corporate Training & Mentoring',
        'Entreprise': 'n.c. (via Upwork)',
        'Source': 'upwork.com',
        'Contrat': 'Freelance',
        'Localisation': 'Remote',
        'Remote': '100% remote (sessions live)',
        'Salaire / TJM': 'Horaire ou au projet',
        'Durée mission': '3 à 6 mois, moins de 30h par semaine',
        'Fit / Notes': "Mission de formation et de mentorat en entreprise sur la gouvernance de l'IA : cadres de gouvernance, risques d'implémentation en entreprise, gouvernance des LLM et de l'IA générative, traçabilité des données. Les sessions se tiennent en visio et le rythme de moins de 30h par semaine laisse la place à une autre mission en parallèle. Le volet conformité et gestion des risques dépasse la pratique actuelle et demandera une mise à niveau ; le volet formation et acculturation correspond en revanche pleinement. Renouvellement possible annoncé.",
        'Lien': 'https://www.upwork.com/freelance-jobs/apply/Governance-Consultant-Trainer-for-Corporate-Training-Hands-Mentoring_~022054488514687863860/',
        'CV à envoyer': 'Resume_GaetanFRANCOIS_IA.html',
        'Prétention': 'À discuter',
    },

    # ── ONGLET OFFRES SIRH ─────────────────────────────────────────────────────

    # Upwork — Workday Consultant, intégration plateforme HR Tech
    {
        'Priorité': '⭐⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Workday Consultant - HR Tech Platform Integration (SuccessFactors, Oracle, SmartRecruiters)',
        'Entreprise': 'n.c. (via Upwork)',
        'Source': 'upwork.com',
        'Contrat': 'Freelance',
        'Localisation': 'Remote',
        'Remote': '100% remote',
        'Salaire / TJM': 'À définir',
        'Durée mission': '',
        'Fit / Notes': "Mission d'intégration entre une plateforme HR Tech et les principaux SIRH du marché, SuccessFactors compris. La connaissance des flux entrants et sortants d'Employee Central est directement mobilisable, et le sujet d'intégration multi-SIRH rejoint le travail mené sur OneProfile. Workday occupe la première place de l'intitulé, donc bien vérifier la part réellement Workday avant de se positionner.",
        'Lien': 'https://www.upwork.com/freelance-jobs/apply/Workday-Consultant-Needed-for-Tech-Platform-Integration-SuccessFactors-Oracle-SmartRecruiters_~022036657906124703044/',
        'CV à envoyer': 'Resume_GaetanFRANCOIS_SIRH_EN.html',
        'Prétention': 'À discuter',
    },

    # Freelancer.com — Formation SAP EC & Payroll Integration
    {
        'Priorité': '⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Formateur SAP Employee Central & Payroll Integration',
        'Entreprise': 'n.c. (via Freelancer.com)',
        'Source': 'freelancer.com',
        'Contrat': 'Freelance',
        'Localisation': 'Remote',
        'Remote': '100% remote',
        'Salaire / TJM': '~488 $ (enchère moyenne)',
        'Durée mission': 'Court, 4 jours restants pour candidater',
        'Fit / Notes': "Le client cherche un praticien SuccessFactors expérimenté pour dispenser une formation sur Employee Central et son intégration paie de bout en bout. C'est exactement le périmètre des go-live OneProfile et OnePayroll ; peu de profils peuvent enseigner cette intégration pour l'avoir livrée en production sur 40 pays. Le budget est faible et la mission courte, mais le format se prête à une première référence de formateur SAP, utile pour ouvrir le segment formation. Date limite proche, à traiter vite.",
        'Lien': 'https://www.freelancer.com/jobs/sap/',
        'CV à envoyer': 'Resume_GaetanFRANCOIS_SIRH_EN.html',
        'Prétention': 'À discuter',
    },
]

ajouter_offres(offres)
