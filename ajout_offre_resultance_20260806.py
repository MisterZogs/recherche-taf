"""
Ajout de l'offre Resultance - Senior HR Transformation Consultant (LinkedIn 4448991282).
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from add_offre import ajouter_offres

offres = [
    {
        'Priorité': '⭐⭐⭐⭐⭐',
        'Statut': '',
        'Fait': '',
        'Poste': 'Senior HR Transformation Consultant',
        'Entreprise': 'Resultance',
        'Source': 'LinkedIn',
        'Contrat': 'Freelance / indépendant (CDD de mission)',
        'Localisation': 'Union européenne',
        'Remote': '100% remote',
        'Salaire / TJM': 'Non affiché',
        'Durée mission': 'Sept. à déc. 2026, extension possible ; 2 à 3 jours par semaine',
        'Fit / Notes': "Cabinet de conseil né au Luxembourg, présent en France, Belgique et Royaume-Uni, 51 à 200 salariés, qui adosse une part de ses honoraires aux résultats obtenus. La mission porte sur la refonte du modèle opérationnel RH et des processus de bout en bout : animation d'ateliers de conception, consolidation des processus sur tous les piliers RH, définition des rôles et de la gouvernance, feuille de route de transformation et conduite du changement, plus la supervision d'un consultant junior. Les 7 à 10 ans demandés couvrent explicitement l'implémentation SIRH, donc les quinze ans sur SAP HR répondent au critère ; l'expérience de supervision de l'équipe Inde chez ALTI répond au volet encadrement, et le passage en cabinet est présenté comme un atout fort. Le format à temps partiel et en remote intégral permet de cumuler avec une autre mission. Offre publiée le 05/08/2026, déjà 67 candidats, réponse annoncée sous une semaine ; candidature simplifiée LinkedIn. Recruteuse : Olga Adam, Talent Acquisition Manager. Point d'entrée réseau : Ludovic Van Sinay, relation de 3e degré et ancien de L'Oréal, à contacter avant de postuler.",
        'Lien': 'https://www.linkedin.com/jobs/view/4448991282/',
        'CV à envoyer': 'Resume_GaetanFRANCOIS_Resultance.pdf',
        'Prétention': 'À discuter',
    },
]

ajouter_offres(offres)
