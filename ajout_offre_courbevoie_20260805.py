"""
Ajout ponctuel de la mission Chef de Projet SIRH / AMOA SIRH à Courbevoie
(freelance-informatique.fr, réf. 260716H003), marquée Fait ('x').

Le second appel à ajouter_offres avec une liste vide déclenche l'archivage,
qui déplace la ligne vers l'onglet Fait.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from add_offre import ajouter_offres

offres = [
    {
        'Priorité': '⭐⭐⭐⭐',
        'Statut': '',
        'Fait': 'x',
        'Poste': 'Chef de Projet SIRH / AMOA SIRH',
        'Entreprise': 'N/C (via freelance-informatique.fr)',
        'Source': 'freelance-informatique.fr',
        'Contrat': 'Mission freelance',
        'Localisation': 'Courbevoie (92026)',
        'Remote': 'Non indiqué (sur site)',
        'Salaire / TJM': 'N/C',
        'Durée mission': '6 mois',
        'Fit / Notes': "Réf. 260716H003, publiée le 16/07/2026, démarrage 01/09/2026. Le périmètre couvre le recueil des besoins des directions RH et la coordination entre RH, DSI et éditeurs jusqu'à la mise en production, avec SAP SuccessFactors et SmartRecruiters cités ainsi que la recette et la conduite du changement ; le fit fonctionnel est donc élevé. L'annonce n'indique aucun télétravail et le site est à Courbevoie, ce qui pose un problème depuis Anglet. Contact : Anais NAESSENS, 01 80 87 54 30.",
        'Lien': 'https://www.freelance-informatique.fr/mission-chef-de-projet-sirh-amoa-sirh-sur-courbevoie-260716H003',
        'CV à envoyer': 'Resume_GaetanFRANCOIS_SIRH.html',
        'Prétention': '650-750€/j',
    },
]

ajouter_offres(offres)

# Second passage : archive la ligne 'x' vers l'onglet Fait.
ajouter_offres([])
