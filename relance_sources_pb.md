# Cluster Pays Basque + Bordeaux — sources à interroger

Lire d'abord `relance_regles_communes.md`. Fichier de sortie : donné dans la consigne
de lancement (vérifier s'il existe déjà avant de commencer, voir règles communes).

**Chaque offre de ce cluster doit porter `"Onglet": "Pays Basque"`, sans exception**
(y compris les offres Bordeaux).

## Règle spéciale : cet onglet échappe au filtre télétravail

Les entreprises du bassin (moins d'1h15 de route de Biarritz) sont pertinentes même en
présentiel/hybride. Indiquer honnêtement `Remote` (Présentiel/Hybride/Full remote) sans
jamais écarter une offre pour ce motif dans ce cluster.

**Exception inverse pour Bordeaux/périphérie** (Mérignac, Pessac, Talence, Bègles,
Bruges, Le Bouscat, Villenave-d'Ornon) : trop loin pour un présentiel régulier, donc ne
retenir QUE si le texte de l'offre confirme explicitement 3 jours ou plus de télétravail
par semaine (hybride 3j+, télétravail majoritaire, full remote). Télétravail non précisé
ou 1-2j/semaine = ne pas ajouter du tout (ni dans Pays Basque, ni ailleurs).

## Entreprises cibles (grands groupes, chercher `"<entreprise>" carrières OR emploi
<ville> 2026` en repli systématique si la page carrière est en JS)

TotalEnergies Pau, Arkema Lacq, Teréga Pau, Toray Carbon Fibers Lacq, Safran Helicopter
Engines Bordes/Tarnos, Dassault Aviation Anglet/Biarritz, Groupe Lauak Hasparren,
Euralis Lescar, Maïsadour Mont-de-Marsan, Lindt & Sprüngli Oloron-Sainte-Marie, B.Braun
Saint-Jean-de-Luz, DJO Global/Enovis Mouguerre, Epta France Hendaye, Quiksilver/
Boardriders Saint-Jean-de-Luz, Celsa France Bayonne.

## Sources confirmées productives, à repasser en priorité

- **SD Worx RSS** : `careers.sdworx.com/services/rss/job/?keywords=<mot-clé>` — chercher
  mentions Bayonne/Bidart. Flux parfois mort (404), retester quand même (déjà vu
  fonctionner puis mourir puis refonctionner).
- **Intescia/WANAO** : `intescia.recruitee.com/api/offers/` — JSON direct, chercher
  Bidart. Rendement très variable (0 à plusieurs postes).
- **Technopole Izarbel (Bidart)** : annuaire officiel
  `technopolepaysbasque.fr/fr/4-sites-technopolitains/izarbel/entreprises.html` (~79
  entreprises). Repasser en priorité SEI-Groupe LKS, IS Decisions, Sophia Genetics
  (candidatures spontanées acceptées, à retester si 0 poste ouvert la dernière fois).
- **French Tech Pays Basque** : `frenchtechpaysbasque.fr`, radar startups locales.

## Extension Bordeaux

Utiliser api.francetravail.io (filtre localisation Bordeaux/33), hellowork.com (page
métier+ville Bordeaux), free-work.com, mission-freelances.fr, welcometothejungle.com, et
les API Ashby/Lever/Greenhouse pour les scale-ups bordelaises repérées par WebSearch.

## Postes ciblés

Mêmes familles que le reste du dispositif (SIRH/SAP, CSM/Account Manager, Formateur IA,
Product Manager, avant-vente technique, chef de projet généraliste) — pas besoin d'être
aussi strict sur l'intitulé que pour le reste du tableur, vivier local restreint.
