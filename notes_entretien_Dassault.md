PRÉSENTATION
L'Oréal 10 ans / 40+ pays / SF EC, freelance 7 ans, disponible 10 août

CADRER
périmètre de pays ?
plusieurs vagues par groupes de pays
Europe Ouest, Est, LATAM, APAC
en dev qual prod

règles de gestion pays par pays
specs fonctionnelles
définir les règles métier puis
la coordination avec l'intégrateur:
sur les MDF (metadata framework comme type de contrat)
et les Business Rules (CDD à CDI, workflow de validation)



QUESTIONS À POSER
-cloud souverain ou cloud classique hébergé aux US ?
-donnée maître PeopleSoft ou Meta4 ? interface entre les 2 ?
-référentiel de postes dans PeopleSoft ? ou seulement Jobs ?
-prévoit-on une phase de nettoyage des données en amont avant de faire la data migration ?
prévoir un data cleaning avec l'aide des RH, les impliquer
-quel historique de données reprendre ?
-est-ce qu'il y a beaucoup de spécificités pays et sont-elles bien cadrées et pas déjà couvertes par le standard ?
-meta4 maintenu + interface EC, ou remplacé par ECP ? si ECP ça couvre tous vos pays ?
si ECP, projet de migration de paie à part entière, sinon maintenir interface
-qui est l'intégrateur
-Taleo remplacé par SF Recruiting ?

POINTS D'ATTENTION
-impliquer les RH en faisant des ateliers avec les pays pour bien comprendre les règles de gestion
-impliquer les RH pour le data check et le data cleansing notamment
-impliquer les RH et les key users pour la recette
-impliquer la Finance et la DRH pour avoir le mapping BU PeopleSoft avec hiérarchie SF 
-PeopleSoft très configurable : définir quoi faire des champs custo
-spécificités pays nécessaires ? ou déjà couvertes par le standard ?




BIEN DÉFINIR LE MODÈLE ORGANISATIONNEL
position, job classification, cost center, department, division
SAP : Job -> Position -> Org Unit qui porte le Cost Center
SF pareil mais le Cost Center est indépendant
le CC peut être assigné où on veut (departement, position, job)

DONNEES SF
Core HR : personal information, employment information, job information, compensation information
Gestion organisationnelle : positions, foundation objects.
Workflows et Business Rules côté cadrage fonctionnel.
Reprise de données depuis PeopleSoft
Intégrations descendantes vers la paye et vers un outil de gestion des temps
- Personal data (nom, adresse, données personnelles)
- Employment data (contrat, statut, temps de travail)
- Job & Organisation data (position, département, cost center, manager)
- Compensation data (salaire de référence)