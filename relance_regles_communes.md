# Règles communes à toute relance de recherche d'offres (Gaëtan FRANÇOIS)

Ce fichier + le fichier `relance_sources_<cluster>.md` correspondant sont TOUT ce qu'un
agent de relance doit lire avant de démarrer. Ne pas lire `CLAUDE.md` en entier : trop
volumineux, ça consomme le budget de session pour rien. Les infos utiles à la recherche
d'offres sont ici et dans le fichier sources du cluster.

## Profil (résumé)

Gaëtan FRANÇOIS, Anglet, disponible immédiatement, 100% remote en priorité absolue.
15 ans CSM / SIRH / gestion de comptes enterprise. 14 ans SAP (dont 10 ans compte
L'Oréal mondial, SAP HR 40+ pays). A été Product Manager (jamais "co-fondateur" ni
"CEO" — ce mot est interdit partout) chez WallOfTraders.com (marketplace B2B/B2C crypto
trading) : roadmap, spécifications, tests produit, UX/parcours utilisateur, SEO/paid
social, gestion de communauté. Langues : FR natif, EN courant, ES/PT intermédiaire.

Postes ciblés (toutes familles, un même agent peut chercher plusieurs familles à la
fois) : SIRH/SAP HCM/SuccessFactors/HR Access, chef de projet SIRH, AMOA, consultant
migration de données, pre-sales/solution advisor SAP, Customer Success Manager senior,
Account Manager, Technical Account Manager, Solutions Engineer/Consultant, Chief of
Staff, Founding/Head of CS, Product Manager/Owner (priorité remote absolue), UX/UI/
Product Designer, SEO/GEO/AEO Manager, Formateur IA/consultant IA générative, chef de
projet/Project Manager généraliste (IT, transformation digitale).

Le TJM/salaire n'est JAMAIS un critère de filtrage ni de note. Ne jamais écarter une
offre ou une source pour rémunération basse.

## Format de sortie (identique pour tous les clusters)

Liste de dicts JSON avec exactement ces clés :
`Priorité, Statut, Fait, Poste, Entreprise, Source, Lien, Contrat, Localisation, Remote,
Salaire / TJM, Durée mission, Fit / Notes, CV à envoyer, Prétention, Date trouvée, Date
publiée`

Plus, seulement si applicable : `Onglet` (valeurs possibles : `"Offres USA"`,
`"Offres CH-NL"`, `"Pays Basque"` — ne jamais mettre autre chose, le routage des autres
onglets est automatique par mot-clé de titre) et `RemoteExempt` (`true`, réservé aux
missions SIRH/SAP en Suisse, voir fichier sources ATS).

- `Priorité` : `"⭐"` à `"⭐⭐⭐⭐⭐"`, réfléchie et réelle (fit avec le profil), jamais un
  défaut mécanique basé sur le remote ou la présence de mots-clés.
- `Statut` : date ISO `YYYY-MM-DD` de publication si connue, sinon la date du jour
  (date de la relance).
- `Fait` : toujours laissé vide (chaîne vide ou absent).
- `Contrat` : toujours une chaîne de caractères. Si la source donne une liste (ex.
  JSON-LD HelloWork `['INTERN', 'FULL_TIME']`), la convertir en texte
  (`", ".join(...)`) avant de l'écrire.
- `Date trouvée` : date du jour de la relance.
- `Prétention` : laisser vide sauf donnée salariale déjà connue.
- `CV à envoyer` : propose le CV le plus adapté (voir la liste des CV dans CLAUDE.md si
  besoin d'un rappel — mais en général `Resume_GaetanFRANCOIS_SIRH.pdf`/`_EN` pour SIRH,
  `Resume_GaetanFRANCOIS_PM_EN/FR.pdf` pour PM, `_UXLead` pour UX, `_SEO` pour SEO,
  `CV_GaetanFRANCOIS_CSM_FR/_EN.pdf` pour CSM générique).

## Exclusions obligatoires

- **Stage / alternance / entry-level** : exclure tout titre matchant
  `alternance|alternant|stage|stagiaire|apprenti|pfe|entry.level|jeune dipl[oô]m[ée]`
  (insensible à la casse). Un titre "Junior" n'est pas exclu mais reçoit ⭐ maximum.
- **Jamais un lien de page catégorie/listing en colonne `Lien`.** Uniquement des liens
  d'offre individuelle. Si la seule chose trouvée est une page catégorie, soit chercher
  le lien individuel réel (ex. décodage `data-obf` pour freelance-informatique.fr, ou
  `free-work.com/fr/companies/<slug>/jobs` pour retrouver le lien d'un client connu),
  soit ne pas ajouter l'offre.
- Ne pas retenir une offre déjà couverte de façon quasi identique par une autre ligne du
  même cluster (doublon interne : même lien, ou même paire Entreprise+Poste normalisée).
  Le parent refait un dédoublonnage global à la fusion, donc pas besoin d'être
  paranoïaque, juste éviter les doublons évidents en cours de route.

## Filtre télétravail

Indiquer honnêtement dans `Remote` ce que dit l'offre (Full remote / Hybride Nj/semaine
/ Présentiel / Non précisé). **Ne pas trier soi-même vers NoRemote** : le routage
automatique d'`add_offre.py` s'en charge à l'insertion, sauf pour le cluster Pays Basque
(qui échappe totalement au filtre, voir son fichier sources) et sauf mention contraire
dans le fichier sources du cluster (ex. exception SIRH/SAP Suisse).

## Écriture incrémentale (règle de survie critique)

**Toutes les 3 à 5 offres trouvées**, réécrire le fichier JSON de sortie complet
(liste de tous les dicts accumulés jusque-là) avec le tool Write. Ne jamais attendre la
fin pour écrire : en cas de coupure de session ou de limite atteinte, seul ce qui a été
écrit sur disque est récupérable.

**Ne jamais toucher `offres_emploi.xlsx` directement** (pas d'appel à
`add_offre.ajouter_offres()`). Le parent fait un merge + une seule passe d'insertion
après que tous les clusters sont terminés, pour éviter les écritures concurrentes sur le
classeur.

## En cas de reprise après coupure de session

**Avant de relancer une recherche, vérifier si un fichier de sortie existe déjà pour ce
cluster** (même nom de fichier que celui indiqué dans la consigne). S'il existe, le
charger et continuer à l'accumuler dedans plutôt que de repartir de zéro ou d'écrire
sous un autre nom — le 24/09/2026, une reprise mal gérée a fait tourner deux instances
du même cluster en parallèle sur le même fichier, provoquant une écriture concurrente
(rien n'a été perdu grâce à l'écriture incrémentale, mais ça a gaspillé du budget de
session en travail dupliqué).

## À la fin

Répondre avec un résumé court : nombre d'offres par source, total, meilleures pépites
(⭐⭐⭐⭐⭐).
