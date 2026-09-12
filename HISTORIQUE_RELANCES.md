# Historique des relances de recherche d'offres — archive

Ce fichier contient l'historique détaillé des relances de recherche (verdicts source par source, pièges découverts, slugs ATS testés) antérieures au 2026-09-05, extrait de CLAUDE.md le 2026-09-08 pour rester sous la limite de taille du fichier de contexte principal.

**CLAUDE.md ne garde en ligne que les 2 ou 3 relances les plus récentes** (état courant des sources). Ce fichier sert de mémoire longue si besoin de retrouver quand une source a été testée, pourquoi elle a été écartée, ou l'historique d'un piège déjà documenté.

### État des sources — relance du 2026-09-10

4 clusters parallèles au format habituel (FR/freelance, ATS+HRIS+USA fusionné, remote/VC EU+niches, Pays Basque). **42 offres candidates compilées, 42 ajoutées** (0 doublon inter-clusters, 0 doublon rejeté par `add_offre.py` : chaque agent avait dédoublonné en amont contre un export à plat des 2754 liens déjà en base, généré une fois avant de lancer les 4 agents). 7 lignes archivées vers Fait (6 SIRH, 1 Pays Basque). Répartition des ajouts : SIRH +12, CSM +7, IA +3, PM +6, USA +1, Pays Basque +3, NoRemote +10.

Rendement très déséquilibré une nouvelle fois : le cluster FR/freelance a produit 34 des 42 offres (20 HelloWork, 8 mission-freelances.fr, 6 free-work.com), le cluster ATS+HRIS+USA seulement 5 (sur ~150 slugs interrogés), le cluster Pays Basque 3, et le cluster remote/VC EU+niches **0** — première fois qu'un cluster entier revient bredouille malgré ~25 pistes examinées en détail, toutes déjà en base, expirées, ou non éligibles France une fois vérifiées.

**Bug de routage corrigé ce jour, à connaître** : `_is_ia()` dans `add_offre.py` testait l'appartenance des mots-clés IA (dont `LLM`) par simple sous-chaîne (`in`), sans frontière de mot. "Product Manager - Fulfillment (Order & Dropship)" contient "fuLfiLlMent", qui matchait `LLM` en sous-chaîne et routait l'offre à tort vers Offres IA. Corrigé par un regex à frontières de mot (`_IA_KEYWORDS_RE`, même principe que `_SIRH_OVERRIDE_RE` qui avait déjà eu ce même bug corrigé début septembre). La ligne Mirakl mal routée a été déplacée manuellement de Offres IA vers Offres PM après coup. **Leçon : toute liste de mots-clés courts (LLM, RH, IA, AI...) testée par sous-chaîne nue est un bug latent ; systématiquement passer par un regex `\b...\b`.**

| Source | Verdict 10/09/2026 |
|---|---|
| **hellowork.com** | Toujours la source la plus productive (20 offres) ; bon rendement Cegedim (3 postes SIRH/paie en parallèle sur différentes villes) et un excellent match AssessFirst (Account Manager full remote Europe explicite) |
| **mission-freelances.fr** | 8 offres retenues (CSM Realadvisor ×2, Founding CSM Gotam, Formateur IA Bayonne, 4 missions PM dont AI Product Manager et Product Owner IA chez Yunik) ; volume de bruit toujours très élevé (~55 missions PM e-commerce génériques non traitées individuellement, sans mention télétravail) |
| **free-work.com** | 6 offres retenues, mais rendement en télétravail décevant : les meilleurs fits fonctionnels trouvés étaient tous en télétravail partiel → NoRemote. **Correctif d'URL** : `/jobs/product-manager` redirige désormais en 301, à ne plus fetcher tel quel |
| **freelance-informatique.fr (3 pages catégorie), eursap.eu, hansonregan.com, malt.fr, apec.fr** | Entièrement à sec ou bloqués, confirmant les verdicts des jours précédents. eursap.eu confirmé bloqué par JS (les paramètres `?country=`/`?keywords=` sont ignorés, toujours le même échantillon statique de 9 offres non françaises retourné) |
| **GitLab (Greenhouse), EY, delaware (carriere.delaware.pro/jobs)** | Seules sources productives du cluster ATS/HRIS (1+1+3 offres), le reste (~150 slugs Ashby/Lever/Greenhouse, Atlassian, jobs.sap.com, Intescia, Employment Hero, Access Group UK) entièrement saturé ou déjà en base |
| **Sopra Steria, Wavestone** | Ont pour la première fois rendu du contenu en clair en curl direct (contrairement aux relances précédentes où ils étaient en JS), mais 100% postes juniors/stages/dev pur — à re-fetcher occasionnellement, le comportement du site varie |
| **HR Path (jobs.hr-path.com)** | Page rendue vide en curl ce jour, alors qu'elle avait donné 61 postes le 07/09 — comportement instable d'un jour sur l'autre, à re-tester plutôt qu'à classer définitivement bloquée |
| **welcometothejungle.com (app.wttj / Otta)** | **Nouveau constat** : tous les résultats obtenus via WebSearch affichaient "Job no longer available" au fetch direct — cet agrégateur semble indexer une forte proportion de postes déjà fermés. Vérifier systématiquement via l'ATS d'origine avant tout ajout, plutôt que de faire confiance au résultat WebSearch seul |
| **euremotejobs.com** | 403 confirmé ce jour-là ; débloqué à nouveau le 11/09/2026 (voir la relance ci-dessus pour la méthode qui a payé) — source intermittente, à retenter systématiquement même après un 403 |
| **jobs.stationf.co (Algolia), remotifyeurope.com, remoterocketship.com, weworkremotely.com, workingnomads.com, RemoteOK, Remotive, collective.work, cremedelacreme.io, boards VC (a16z/Sequoia/Balderton/Atomico), upwork, freelancer.com, Oyster/Ashby, Omnipresent, Multiplier, 365talents** | Rendement nul confirmé sur l'ensemble du cluster remote/VC/niches ; techniques d'accès toutes encore valides, mais vivier entièrement épuisé pour ce profil à ce jour |
| **SD Worx (careers.sdworx.com, flux RSS jobs.rss)** | **Nouvelle source Pays Basque confirmée productive** : 100 postes au flux RSS, Bayonne listée comme bureau éligible explicite sur un poste Product Manager Integrations — à ajouter au dispositif permanent Pays Basque, à repasser à chaque relance |
| **Pays Basque, reste des sources habituelles** | Quasi à sec par ailleurs (2 offres HelloWork génériques + 1 SD Worx) : Intescia/WANAO (18 postes, aucun à Bidart ce jour), Exakis Nelite (lien mort), SEI-Groupe LKS (candidature spontanée seulement), pays-basque-digital.fr (3 offres, déjà connues ou hors profil), Safran (piège de republication de slug reconfirmé), TotalEnergies Pau (alternance uniquement), Dassault Aviation, French Tech Pays Basque/lespepitestech.com, Arkema, Maïsadour, Teréga, Toray, Technoflex, Epta, Celsa, BMS Circuits, B.Braun, Enovis, Boardriders, Daher, Lindt Oloron : tous confirmés à sec. Piste Euralis (Consultant Fonctionnel SAP, rôle confirmé exister par 2 recherches indépendantes) non aboutie : liens LinkedIn morts (404), portail carrière `euralis.nos-recrutements.fr` gated par API 401 — à revérifier lors d'une prochaine relance |

---

### État des sources — relance du 2026-09-05

4 clusters parallèles au format habituel (FR/freelance, ATS+HRIS+USA fusionné, remote/VC EU+niches, Pays Basque). **118 offres candidates compilées, 118 ajoutées** (0 doublon inter-clusters, 0 doublon rejeté par le garde-fou `add_offre.py` : les 4 agents avaient déjà dédoublonné en amont contre les 2291 liens fournis dans un fichier de référence commun). 2 lignes archivées vers Fait (SIRH). Répartition des ajouts : SIRH +41 (dont 2 tout de suite réarchivées), CSM +9, IA +2, PM +7, Pays Basque +2, NoRemote +57.

Rendement très déséquilibré, comme d'habitude, mais cette fois le cluster ATS+HRIS+USA est retombé au plus bas jamais observé (7 offres sur ~120 slugs interrogés) : le vivier Ashby/Lever/Greenhouse est désormais quasi entièrement saturé sur les intitulés cibles, la quasi-totalité des postes "EMEA" trouvés s'étant révélés ancrés sur un seul pays hors France une fois le champ location vérifié en détail (Databricks, Chainguard, Decagon, ElevenLabs, Docker, Vanta, Coder, Deepgram). Le cluster FR/freelance reste de très loin le plus productif (98 offres sur 118, dont 49 HelloWork et 47 free-work).

> **Nouveauté méthodologique adoptée ce jour, à reconduire** : avant de lancer les 4 agents, un export à plat de tous les liens déjà en base (`_liens_existants` équivalent en Python) a été généré une seule fois dans un fichier texte partagé, que chaque agent a reçu pour dédoublonner localement avant de renvoyer ses résultats en JSON structuré (un fichier par cluster). Aucun agent n'a touché à `offres_emploi.xlsx` directement ; l'insertion a été centralisée en une seule passe via `add_offre.ajouter_offres()` après fusion et dédoublonnage cross-cluster des 4 JSON. Ça évite les conflits d'écriture entre agents parallèles et donne un point de contrôle unique avant sauvegarde.

| Source | Verdict 05/09/2026 |
|---|---|
| **hellowork.com** | Toujours la source la plus productive (49 offres) sur les mots-clés consultant SIRH / CSM / SAP HCM / SAP SuccessFactors / chef de projet SIRH / formateur IA / product manager / AMOA SIRH / consultant SAP HR |
| **free-work.com** | 47 offres sur 12 catégories + l'endpoint de recherche `?query=<mots-clés>&page=N` ; toujours très productif |
| **mission-freelances.fr** | Confirme sa quasi-saturation déjà notée le 02/09 : seulement 2 offres nouvelles sur 244 titres candidats |
| **freelance-informatique.fr** | 0 nouvelle : les 5 pages catégorie de référence (data-obf) sont entièrement saturées |
| **eursap.eu** | 0 nouvelle, le seul poste pertinent déjà en base |
| **whitehallresources.com / opusresourcing.com** | 2 pistes trouvées mais disqualifiées à la vérification : l'une exige résidence UK + statut IR35/FCSA, l'autre une autorisation de travail US et est hybride NYC malgré l'étiquette apparente |
| **API Ashby/Lever/Greenhouse (~120 slugs)** | Rendement le plus faible observé à ce jour (7 offres) ; confirme la saturation progressive documentée depuis fin août. Nouveauté : **Ashby lui-même** publie un Senior Strategic Implementation Specialist EMEA avec la France en `secondaryLocations` |
| **Constructor (Ashby)** | Sr. Customer Success Manager French Speaking, Remote-France explicite, la meilleure offre CSM de la relance |
| **euremotejobs.com** | curl de nouveau bloqué (403 sur les 4 régions), mais **WebFetch est passé sans problème** — encore une inversion de comportement, toujours tenter les deux méthodes. A produit Pennylane (Consultant Intégrateurs, full remote) et ElevenLabs (Revenue Partnerships France) après vérification que le reste était déjà en base |
| **jobs.stationf.co (Algolia)** | Très saturé, seulement 4 nouveautés (toutes hybrides/ponctuelles → NoRemote) |
| **intescia.recruitee.com/api/offers/** | 4 nouvelles offres sur 20 dans le flux, confirme le filon à faible débit permanent |
| **recrutement.cegos.com** | Le piège de republication se confirme une 4e fois (nouveaux ID = doublons déjà connus) ; une seule vraie nouveauté |
| **redglobal.com** | 0 SAP HCM/HR/CSM ce jour, confirme le rendement irrégulier déjà documenté |
| **Pays Basque, ensemble des sources habituelles** | Quasi totalement à sec (2 offres seulement sur 117 candidats HelloWork triés un par un) : EPSYL Bayonne (Chef de Projet IT) et ELI Saint-Pierre-d'Irube (Chargé de Comptes, télétravail confirmé). Safran, Teréga, Enovis, Maïsadour, Wipro Lauak, TotalEnergies Pau, 360Learning, Boardriders, B.Braun, Celsa, Technoflex, Daher, French Tech Pays Basque : tous confirmés à sec ou hors profil |
| **Boards VC (Index/Balderton/a16z/Sequoia)** | Rendement nul confirmé une nouvelle fois |
| **apec.fr** | Toujours inaccessible |

---

### État des sources — relance du 2026-08-18

Leçon principale : **les API publiques d'ATS battent tout le reste.** Un seul appel Greenhouse a rendu plus d'offres exploitables que l'ensemble des WebSearch de la journée, et les liens qui en sortent sont vifs par construction (un poste absent du JSON est fermé — **cette dernière affirmation reste vraie pour Greenhouse**, vérifiée le 19/08/2026 : un ID Greenhouse fermé redirige proprement vers `<board>?error=true`. Elle est **fausse pour Ashby** (postes "non listés" toujours candidatables) **et pour Lever/Jobgether** (listing volatil) — voir les correctifs du 19/08/2026 dans la section Ashby/Lever ci-dessus avant de marquer un lien existant comme expiré sur la seule base d'une absence dans l'API).

> **API Greenhouse — à ajouter au dispositif permanent, au même titre qu'Ashby et Lever :**
> ```bash
> curl -s "https://boards-api.greenhouse.io/v1/boards/<entreprise>/jobs"
> ```
> Chaque entrée porte `title`, `location.name` et `absolute_url`. Slugs vérifiés qui répondent : `remotecom`, `gitlab`, `samsara`, `canonical`, `grafanalabs`, `cloudflare`, `figma`, `airtable`, `gusto`, `justworks`. Un slug inconnu renvoie une réponse sans clé `jobs`.
>
> **Attention `urllib` :** l'API Ashby renvoie 403 sur les requêtes `urllib.request` de Python ; passer par `curl` (en sous-processus si besoin). Même piège probable sur les autres ATS.

| Source | Verdict 18/08/2026 |
|---|---|
| API Greenhouse `remotecom` | **Meilleur rendement de la relance** : Senior PM HRIS Integrations, Senior Workday Implementation Specialist, Senior PM Remote Build en remote France ; l'éditeur le mieux aligné du marché |
| API Greenhouse `gitlab` | Customer Success Architect EMEA avec **la France explicitement listée** en remote, plus un Senior Professional Services PM EMEA |
| API Greenhouse `grafanalabs` | Solutions Engineer France remote ; attention, la variante Senior du même poste exige l'arabe |
| API Greenhouse `canonical` | Six postes produit ouverts en même temps, tous `Home based - EMEA` |
| API Ashby | Ashby lui-même (Manager of Dedicated Implementations EMEA), Constructor (PM Customer Onboarding Experience), ElevenLabs (Enterprise Solutions Engineer France), Pennylane (CSM SAAS et Présales en remote France), Alan, RevenueCat, Supabase, Vapi |
| API Lever `jobgether` | 4 484 annonces ; filtrer `categories.location == "France"` réduit à 17 postes pertinents et règle le problème des doublons par pays |
| API carrières Atlassian | Trois postes France remote que ni LinkedIn ni les ATS de scale-ups ne remontaient : Account Manager Strategic France, Senior Services Solutions Advocate, Strategic Solutions Sales Executive |
| free-work `/jobs/sirh` | Toujours productif, mais **le télétravail n'est jamais affiché en liste** ; sans ouverture fiche par fiche, tout part en `NoRemote` |
| jobs.hr-path.com | La racine ne rend rien, mais `/job/<slug>/<id>/` se fetche bien et confirme le télétravail — un Consultant SAP SuccessFactors publié le 14/08 est ainsi remonté |
| LinkedIn pages catégories | Utile comme radar uniquement (Nexans, mc2i, Back Market, Scaltify, nonplusultra) ; aucune mention de télétravail, aucune URL d'annonce |
| eursap.eu, hansonregan.com | Une seule offre HR chacun ; rendement quasi nul deux relances de suite |
| WebSearch en général | **Le maillon faible** : beaucoup de pages agrégateur et d'articles de blog, très peu d'URLs d'annonce directes. À réserver aux sources sans API |
| welcometothejungle, upwork, collective.work, remoterocketship, weworkremotely | Rien d'exploitable ce jour ; 403 en fetch direct ou contenu déjà couvert en amont |

> **Correctif apporté à `add_offre.py` le 18/08/2026 :** `PRESALES_KEYWORDS` ne captait ni « Account Manager » seul, ni « Solutions Advocate », « Solution Architect », « Solution Advisor », « Solutions Sales Executive », ni « Présales » accentué. Ces intitulés tombaient tous dans `Offres SIRH` par défaut. Ils sont désormais routés vers `Offres CSM`, sauf marqueur SIRH/SAP dans le titre.

### État des sources — relance du 2026-09-03

4 clusters parallèles au format habituel (FR/freelance, ATS+HRIS+USA fusionné, remote/VC EU+niches, Pays Basque). **197 offres candidates compilées, 194 ajoutées** (1 doublon rejeté par le garde-fou `add_offre.py`, 2 doublons inter-clusters retirés en amont via `cle_lien()`), 22 lignes `Fait=x` archivées (12 SIRH, 10 USA). `dedoublonnage_20260902.py` relancé après coup a trouvé et fusionné **13 doublons cross-forme supplémentaires** (WTTJ fr/en, Station F, mission-freelances.fr) contre les lignes déjà existantes du classeur — utile de le relancer systématiquement après chaque insertion, pas seulement lors d'un grand nettoyage ponctuel. Le tableur passe de 2280 à 2307 lignes. Répartition des ajouts nets : SIRH +51, CSM +21 (dont -8 fusionnés ensuite), IA +10 (dont -1 fusionné), PM +17, USA +3, Pays Basque +9, NoRemote +83.

Rendement à nouveau très déséquilibré en faveur du cluster FR/freelance (148 offres sur 197, dont 95 par HelloWork seul) ; les 3 autres clusters (19 ATS/USA, 21 remote/VC/niches, 9 Pays Basque) confirment un vivier ATS/Ashby/Lever/Greenhouse de plus en plus saturé sur les intitulés cibles, avec surtout des offres déjà connues ou hors-fit géographique remontées.

| Source | Verdict 03/09/2026 |
|---|---|
| **hellowork.com** | Toujours la meilleure source, confirmé une 4e relance de suite : 95 offres retenues sur 171 fiches non-connues. **Zéro offre full remote confirmée par le texte sur ce lot** ; le télétravail total reste rare sur ce board, l'essentiel part en Partiel/Non précisé |
| **free-work.com, endpoint `?query=<mots-clés>&page=N`** | Toujours très productif (42 offres retenues sur 188 liens), dominé par du Product Manager/Owner générique parisien hybride. **Nouveau piège de slug** : `/jobs/successfactors` redirige (301 meta-refresh) vers `/jobs`, contrairement à `/jobs/sap-successfactors` qui fonctionne bien — ne pas confondre les deux formes |
| **Doublon interne free-work, nouveau pattern** | La même mission (Nexus Jobs Limited, HRIS Workday Technical Consultant Analyst, Londres) postée sous deux catégories différentes avec des slugs `-28`/`-29` quasi identiques (`administrateur-applicatif-erp-crm-sirh` et `business-analyst`) — 4e forme de doublon free-work documentée, distincte de WTTJ fr/en, Station F et Workday locale |
| **redglobal.com** | Un seul poste mais excellent : Senior AI Business Analyst fully remote EU, 6 mois + extensions — contredit le verdict à sec du 01/09 (3e passage), à repasser malgré un rendement historiquement irrégulier |
| **intescia.recruitee.com/api/offers/** | Continue de produire au coup par coup (1 nouveau poste Customer Onboarding Specialist full remote sur 19 dans le flux) — confirmé filon permanent à faible débit |
| **recrutement.cegos.com** | Piège de republication confirmé une **3e fois** : deux nouveaux ID (`7756416`, `7823110`) sont les mêmes offres déjà en base sous `7672957` et via LinkedIn. Dédoublonner sur titre + entreprise, jamais sur l'ID, reste indispensable |
| **welcometothejungle.com (vérification API)** | Entièrement saturé sur CSM/SIRH ce jour : toutes les pistes WebSearch étaient déjà en base une fois vérifiées par `api.welcometothejungle.com`. Piège du slug sans rapport reconfirmé sur MISTER IA |
| **freelance-informatique.fr, hansonregan, eursap, whitehallresources, opusresourcing, jobs.sap.com, carriere.delaware.pro, malt.fr** | Tous à sec ce jour, cohérent avec les relances précédentes |
| **Remote.com (`remotecom` sur Greenhouse)** | Meilleure prise du cluster ATS : Global Payroll Implementation Specialist, Remote-EMEA explicite, France nommée dans la fiche, 43-64K€ |
| **Nouveau piège de duplication inter-ATS** | Le poste Remote.com GPIS ci-dessus est aussi republié sur Jobgether (Lever) avec un texte reformulé ("listed on behalf of a partner company") — un même poste peut apparaître sur le board direct de l'entreprise ET sur Jobgether sous une forme différente, à surveiller comme les autres pièges de republication déjà connus |
| **Ashby, piège « secondaryLocations Europe qui résout à un seul pays »** | Se confirme sur `coder` (Europe affiché → Pologne en réalité) après Oyster ; pattern récurrent, toujours lire le détail du pays avant de retenir une offre "Europe" |
| **Lever `swile` et `ledger`** | **Revenus en ligne** après avoir été donnés `Document not found` le 01/09 — ne jamais présumer un slug définitivement mort, retester périodiquement |
| **RemoteOK, Remotive** | Toujours à sec / paramètre de recherche cassé, confirmé une nouvelle fois |
| **euremotejobs.com** | Comportement stable cette fois (curl + UA + Referer Google), 10 offres neuves sur 36 candidats bruts. Le nettoyage `utm_*` + suffixe `/application`/`/apply` avant comparaison reste indispensable (12 des 36 candidats étaient déjà en base sous ces formes) ; la fonction `cle_lien()` de `dedoublonnage_20260902.py` gère déjà ce cas correctement, pas besoin de la retoucher |
| **remoterocketship.com** | Toujours 403 en fetch direct ; **les pistes qu'il remonte via WebSearch se sont révélées fausses une fois vérifiées sur l'ATS d'origine** (Ventrata, Sprinklr) — ne jamais ajouter un résultat remoterocketship sans revérification sur l'ATS natif |
| **jobs.stationf.co (Algolia)** | Toujours fonctionnel mais très saturé : seulement 4 fiches neuves sur 532 offres, toutes Paris hybride → NoRemote |
| **Sweep des métiers de croisement (PM/TAM sur Ashby/Lever/Greenhouse par WebSearch)** | Confirmé à sec, comme le 02/09 : le vivier est saturé sur ces intitulés |
| **Pays Basque — Safran Helicopter Engines (Bordes)** | Un Chef de Projet MOA SAP S/4HANA ⭐⭐⭐⭐⭐ (migration ECC6→S/4HANA, 3 sites France + 7 filiales), trouvé via WebSearch uniquement (`safran-group.com` toujours bloqué Cloudflare, comme documenté) |
| **Pays Basque — Daher (Workday `daher.wd3`)** | En panne 502 pendant toute la relance (plusieurs tentatives espacées), alors que Teréga/Enovis sur la même infra Workday répondaient normalement — panne ponctuelle du tenant à retenter, pas une fermeture |
| **Pays Basque — jobs.arkema.com** | Nouveau portail testé, fonctionne en curl simple, 0 poste IT/PM/SIRH ce jour (Lacq/Mourenx = technicien/alternance) — à garder au dispositif permanent |
| **Pays Basque — Maïsadour, Enovis, Intescia, 360Learning, Dassault Aviation Biarritz, CAPB, French Tech Pays Basque** | Tous confirmés à sec, cohérent avec les relances précédentes |



4 clusters parallèles au format habituel. **292 offres candidates, 286 ajoutées** (6 doublons inter-clusters seulement), 22 lignes `Fait=x` archivées (12 SIRH, 10 USA), 16 lignes supprimées au dédoublonnage. Le tableur passe de 2126 à 2396 lignes. Répartition des ajouts : SIRH +98, NoRemote +97, CSM +30, IA +29, Pays Basque +21, PM +8, USA +3. Priorités : 37×⭐⭐⭐⭐⭐, 103×⭐⭐⭐⭐.

Rendement très déséquilibré : **le cluster FR/freelance a produit 231 des 286 offres à lui seul**, dont 130 par HelloWork. Les clusters ATS et remote/VC, historiquement les plus productifs, sont retombés à 14 et 20 — le vivier ATS est saturé sur les intitulés cibles.

> **Deux bugs corrigés dans les scripts ce jour, à connaître avant d'en écrire un nouveau.**
>
> **1. `add_offre.py` n'écrivait pas les dates.** Sa liste `COLS` s'arrêtait à `Prétention` alors que les onglets ont deux colonnes de plus. Toutes les offres insérées depuis la création du script avaient donc `Date trouvée` et `Date publiée` vides — **2027 lignes** dans ce cas au moment du constat. `COLS` inclut désormais `'Date trouvée', 'Date publiée'`. Les lignes historiques restent sans date (l'information est perdue, elle n'a jamais été écrite).
>
> **2. `dedoublonnage_20260902.py` comparait les liens bruts et ratait trois formes d'un même lien** : WTTJ publie la même annonce sous `/fr/` **et** `/en/`, Station F la remiroite sous le même couple organisation + slug (`jobs.stationf.co/companies/<org>/jobs/<slug>`), et Workday intercale un segment de locale (`/en-US/`, `/fr-FR/`) que la base ne stocke pas toujours. 12 annonces étaient en double de ce fait, l'annonce Joko « Account Manager (Gift Cards) » en **trois** exemplaires. Une fonction `cle_lien()` normalise désormais ces trois cas.
>
> **⚠️ Piège rencontré en écrivant ce correctif, à ne pas reproduire :** la première version de `cle_lien()` retirait la query string de toutes les URL. Or beaucoup de sites carrière portent l'identifiant de l'offre en paramètre (`mongodb.com/careers/job?id=`, `stripe.com/jobs/search?gh_jid=`, `fivetran.com/careers/job?gh_jid=`, `elastic.co/jobs?`, `databricks.com/…/job?`). La normalisation fusionnait alors des offres réellement distinctes : **69 lignes légitimes** allaient être supprimées au lieu de 16. Ne retirer la query string que pour les `utm_*`, jamais globalement.

> **⚠️ Piège d'exécution : ne jamais piper un script d'insertion dans `head`.** `python3 ajout_offres_….py | head -12` a été tué par SIGPIPE **après l'affichage mais avant la sauvegarde du classeur**, avec un `exit=0` trompeur ; le dédoublonnage suivant a donc tourné sur le classeur pré-insertion sans que rien ne le signale. Rediriger vers un fichier (`> insert.log 2>&1`) puis lire le fichier.

| Source | Verdict 02/09/2026 |
|---|---|
| **hellowork.com** | **La source la plus rentable de la relance, et de loin** : 130 offres sur 286. Confirme et amplifie la révision du 01/09. ⚠️ **Son `jobLocationType: TELECOMMUTE` est un faux ami** : il est posé dès qu'un télétravail quelconque existe, y compris « possible après la période d'essai » ou « 2 jours par semaine ». S'y fier donnait 89 full remote sur 192 ; l'analyse du texte de description en rend **2**. Le seul signal fiable est le corps de l'annonce. ⚠️ **Rate limiting au-delà de ~8 requêtes parallèles** : à 16 threads, 195 fiches sur 511 sont revenues en 403 avec un `<title>` trompeur ; un second passage à 4 threads avec backoff les a toutes récupérées. Un 403 HelloWork n'est jamais une preuve d'absence. Certaines fiches n'ont réellement aucun JSON-LD (les deux postes Epsyl) : replier sur le `<title>` + le corps du `<main>` |
| **free-work.com — endpoint de recherche jamais documenté** | **`https://www.free-work.com/fr/tech-it/jobs?query=<mots-clés>` fonctionne, et `&page=2` pagine réellement** (contrairement aux slugs catégorie). C'est ce qui a produit le gros du volume neuf. **Nouveaux slugs catégorie confirmés vivants** : `amoa`, `business-analyst`, `formateur`, `workday`, `successfactors`, `conduite-du-changement` (ces trois derniers ont donné 15/12/37 offres neuves). **Slugs morts, la note du 01/09 est périmée** : `/jobs/chef-de-projet` redirige en 301 vers `/jobs` — le bon est `chef-de-projet-informatique` ; morts aussi `chef-de-projet-si`, `customer-success`, `paie`, `product-manager`, `data-migration`. `sap-hcm` à sec (2 offres), `sap-successfactors` et `transformation-digitale` à 0. **Rate limiting** au-delà de ~30 requêtes d'affilée : espacer de 2,5 s, sinon on conclut à tort qu'une catégorie est morte. ⚠️ **Le `addressLocality` du JSON-LD est faux** : les fiches renvoient toutes `Boulogne-Billancourt`, qui est le siège de free-work, pas le lieu du poste |
| **welcometothejungle** | **Inexploitable sans l'API** : 15 archivées sur 16 vérifiées (contre 14 le 01/09). Le piège du slug incohérent se reproduit à l'identique sur MISTER IA. ⚠️ **Nouveau, plus grave que le doublon** : le slug interrogé doit être **complet, suffixe compris** (`…_paris_365TA_Y3yPxel`). Un slug tronqué (`…_paris`) ne renvoie pas d'erreur, il renvoie **une autre offre, archivée depuis 2024** |
| **mission-freelances.fr — inversion complète du verdict** | La source, donnée « très productive » depuis des semaines, est **à sec sur le profil** : sur 1352 missions listées, seules 5 contiennent SIRH/SAP/HCM/paie/Workday et **toutes sont déjà en base**. Le flux neuf est à ~90 % du marketing, du social media, du montage vidéo et de l'annotation de données. Par ailleurs **la page `/missions/` n'est pas exhaustive** : des missions accessibles par WebSearch n'y figuraient pas |
| **Le sweep des métiers de croisement est à sec** | 30 slugs Ashby et 29 Greenhouse balayés sur 29 intitulés (Solutions Engineer, TAM, Partner, Renewals, Customer Education, Engagement/Delivery, Implementation, Data Migration, Chief of Staff) : **0 nouveauté**. **La note du 01/09 (« le rendement vient de filtrer ces intitulés sur les boards déjà connus ») est périmée** : ces boards sont saturés sur ces titres aussi |
| **Workday `additionalLocations`, confirmé dans les deux sens** | Trois postes Workday Success Plans affichent Dublin ou Madrid au listing mais portent **« France, Paris »** dans la fiche, avec une fourchette France (66 300–99 500 € sur le poste Prism). Red Hat *EMEA AI Architect* s'affiche « Remote Germany » et liste **Remote France**. À l'inverse Airwallex *Staff PM GTPN (EMEA)* est ancré San Francisco. ⚠️ **« Flex » chez Workday = au moins 50 % du temps au bureau ou chez le client**, donc hybride, donc NoRemote |
| Corrections d'URL | **hansonregan** : `/jobs` rend 0 octet, il faut le slash final `/jobs/` ; fiches en `/job/<slug>/`, descriptions vides mais JSON-LD avec pays/contrat/TJM réels. **eursap** : `/jobs/` redirige en 301, utiliser `/jobs` avec `-L` ; test de fermeture fiable = le littéral `This Vacancy is now Closed`. **RED Global** : le regex de la note est faux, les IDs de fiche sont alphanumériques (`/jobs/job/<slug>/hTPEwA24`), chercher `[0-9]+` ne rend que 2 liens sur 10. **Lauak** : les liens sont en `/poste/<slug>/`, pas `/offre/`. **Maïsadour** : `recrutement.maisadour.com/sitemap.xml` renvoie un 302, le sitemap exploitable est `/fr/sitemap.xml`. **`boards-api.eu.greenhouse.io` n'existe pas** : les boards hébergés sur `job-boards.eu.greenhouse.io` (gr8tech, remotepeople) répondent sur l'API standard |
| **Pennylane a quitté Lever** | `api.lever.co/v0/postings/pennylane` renvoie `Document not found` ; le board vivant est Ashby. Un résultat WebSearch pointant vers `jobs.lever.co/pennylane/…` est un lien mort encore indexé — même schéma que la migration Lucca |
| **Strada répond de nouveau** | Workday CXS `strada.wd12` / site `Careers`, 73 postes SAP — contre la note du 01/09 qui la donnait morte (`total: None`). Aucun poste France ce jour cependant, tout est verrouillé par pays. Le tenant **Alight** (`alight.wd5`) reste en 422 |
| **ADP, Dayforce, UKG : piste à clore** | 422 sur toutes les combinaisons Workday CXS testées. Ce sont des **concurrents de Workday** et ils recrutent sur leur propre ATS — la piste ouverte le 01/09 est fermée, ne plus la retenter |
| Nouveaux slugs confirmés vivants | Greenhouse : `databricks` (859 postes, une dizaine à Paris, le plus productif de la découverte), `algolia`, `mongodb`, `twilio`, `vercel`, `mixpanel`, `amplitude`, `neo4j`, `starburst`, `mattermost`, `wikimedia`, `netlify`. Ashby : `decagon`, `coder`, `ramp`, `openai`, `cursor`, `perplexity`, `harvey`, `sierra`, `lovable`, `writer`, `langchain`, `modal`, `workos`, `warp`, `browserbase`, `e2b`, `resend`, `neon`, `pinecone`, `llamaindex`, `stytch`, `knock`, `clerk`, `weaviate`, `inngest`. Lever : `scaleway`, `agicap`, `blablacar`, `younited`, `choose` |
| **free-work `/jobs/ia` et `/jobs/ia-generative` : rendement nul pour ce profil** | 32 offres, quasi exclusivement dev/data (Python, RAG, LLM, MLOps, DevOps), la catégorie explicitement hors cible. Aucune retenue. Les 4 pistes IA remontées par WebSearch étaient toutes mortes |
| **Cegos, piège de republication confirmé une 2e fois** | « Consultant IA & Learning Design » (déjà en base) ressort sous l'ID `7823110`, « IA au service des marchés publics » sous `7756416`. La règle « dédoublonner sur titre + entreprise, jamais sur l'ID » est indispensable. Champ fiable pour le télétravail : `Statut à distance` ; les deux postes Cegos sont hybrides 2 j/sem |
| **Veeva confirme son piège une 2e fois** | 48 postes Implementation/Solution Consultant, tous ancrés sur une ville précise (Boston, Londres, Barcelone, Dublin, Copenhague, Berlin, Budapest), aucun ouvert depuis la France malgré les « (Remote) » dans les titres |
| **jobs.stationf.co** | Index Algolia toujours fonctionnel, 533 offres, 87 pertinentes. Le piège des slugs d'org se confirme **dans les deux sens** : `zola-learning-sas` et `bevolta` remontent bien dans Algolia mais renvoient du vide sur l'API WTTJ, donc écartés faute de vérification. Nouveaux slugs : `ab-tasty`, `beamy`, `mercateam`, `mindflow`, `qantev`, `greenly`, `fairly-made`, `joko-1`. Quasi tout est Paris hybride |
| **Nouveau radar Pays Basque : 360Learning a un site à Urt (64)** | Révélé par une republication HelloWork. Leur board Lever ne liste aucun poste basé à Urt, mais c'est le **second éditeur SaaS du bassin** après Intescia/WANAO, à surveiller |
| **Piège de regex à connaître** | Exclure sur le mot « engineer » seul supprime silencieusement *Solutions Engineer* et *Sales Engineer*, qui sont au cœur de la cible. L'exclusion doit être qualifiée (`software\|platform\|security\|… engineer`) |
| **Piège d'intitulé** | « Responsable Réalisation Projet SIRH » chez l'Armée de l'Air porte le bon mot-clé mais décrit un responsable systèmes numériques militaire à 1 628-2 932 €/mois avec engagement. Conservé en ⭐⭐ avec la mise en garde écrite, parce que l'intitulé ressortira à chaque relance |
| Sources saturées ou stériles ce jour | freelance-informatique.fr **totalement saturé** (9 pages catégorie décodées en `data-obf`, 73 missions distinctes, 0 nouvelle — attention, le décodage remonte aussi `/mission-freelance` qui est une page listing, à filtrer). jobs.hr-path.com rend bien ~81 postes mais **mondiaux** (Brésil, Espagne, UK, Australie, Maurice), le vivier France est saturé. jobs.sap.com : 12 postes nouveaux, tous hors profil. Atlassian (8 des 9 postes France/EMEA déjà en base), AB Tasty, NTT Data RSS (20 postes SF, tous à Hyderabad), Workable `omnipresent-group` (0 poste), Multiplier, Nagarro, Silae, delaware, Intescia (1 seul poste neuf, trop technique), Teréga et Enovis (entièrement saturés), Lauak (44 postes, tous les pertinents déjà en base), TotalEnergies Pau (le `searchByLocation` est ignoré, et les postes IT/data/IA sont tous « Débutant »), Maïsadour (production et saisonniers agricoles), remotifyeurope (massivement des gigs de notation TELUS Digital), weworkremotely (Cloudflare « Just a moment »), Boardriders et Arkema (422 Workday, comme Safran) |
| **Thread HN septembre (`49522897`)** | Vivant, 190 commentaires, mais son seul filon (ODK Senior PM) était déjà en base |
| **euremotejobs** | curl + UA + Referer Google passe (**5e inversion de comportement**). 40 offres par région sur les 4 pages. Le nettoyage `utm_*` avant comparaison est bien indispensable : 14 des 30 liens extraits étaient déjà en base |
| **Test de fermeture Ashby, confirmé dans les deux sens** | Dash0 Product Manager : absent de l'API **et** `<title>Jobs</title>` au fetch direct = réellement fermé. Le test fonctionne donc aussi pour confirmer une fermeture, pas seulement pour démentir l'API |

### État des sources — relance du 2026-09-01 (3e passage)

Troisième relance du jour, 4 clusters parallèles au format désormais stable (FR/freelance, ATS+HRIS+USA fusionné, remote/VC EU+niches, Pays Basque). **192 offres candidates, 181 ajoutées** après dédoublonnage (11 doublons inter-clusters seulement, chaque agent ayant dédoublonné en amont contre les 1891 liens en base). 1 ligne `Fait=x` archivée. Le tableur passe de 2099 à 2280 lignes. Répartition des ajouts : SIRH +42, CSM +24, IA +11, PM +5, USA +19, Pays Basque +35, NoRemote +45.

**C'est la relance la plus productive à ce jour**, et le gain vient presque entièrement de trois sources dont le verdict précédent était faux ou incomplet : hellowork.com (donné « rendement quasi nul », en réalité 27 offres d'un coup), l'API Workday CXS (notée comme simple outil de vérification, en réalité un board de découverte) et free-work sur les mots-clés généralistes plutôt que SIRH/SAP.

> **Découverte majeure — l'API Workday CXS est une source de découverte, pas seulement un outil de vérification.** Elle n'était documentée que pour confirmer le statut d'un lien existant (Strada, L-Acoustics). Or le tenant de **Workday lui-même** est un board HRIS de premier plan pour ce profil :
> ```bash
> curl -s -X POST "https://workday.wd5.myworkdayjobs.com/wday/cxs/workday/Workday/jobs" \
>   -H "Content-Type: application/json" -d '{"searchText":"HCM","limit":20,"offset":0}'
> ```
> 27 postes dont 5 en France, y compris un **Solution Consultant HCM à Paris** (avant-vente chez l'éditeur SIRH n°1, la meilleure prise du cluster) et un Senior Functional Consultant Payroll/GTA francophone. **Tenter le même motif sur les tenants ADP, Dayforce et UKG.** Site IDs à retenir : Workday = `workday.wd5`/`Workday`, Teréga = `terega.wd3`/`Sitecarriereterega` (pas `Terega_Careers`), Enovis = `enovis.wd5`/`enovis`.
>
> **Corollaire — toujours lire `additionalLocations` de la fiche, pas seulement `locationsText` du listing.** Un Senior International Product Manager Enovis affichait Freiburg au listing alors que **Bayonne était une localisation éligible** dans la fiche. C'est le piège « EMEA affiché mais ancrage pays unique », en sens inverse : ici la bonne localisation est cachée, pas surpromise.

**free-work — inversion du rendement par mot-clé.** Les catégories historiquement prioritaires sont saturées (`/jobs/sirh` : 8 nouvelles sur 45 ; `/jobs/sap-hcm` : 0/2 ; `/jobs/sap-successfactors` : 0/16) alors que les catégories généralistes ouvertes le 01/09 sont les vrais gisements neufs : **`/jobs/chef-de-projet` 16/16, `/jobs/transformation-digitale` 15/16, `/jobs/product-owner` 13/16**. Autre point acquis : **le télétravail est bien lisible sur la fiche individuelle** free-work, simplement absent du JSON-LD (`jobLocationType` toujours `None`) ; il figure dans le bandeau texte, chercher le littéral `Télétravail partiel` / `Télétravail complet`. Conséquence brutale : **26 des 27 missions free-work retenues sont en télétravail partiel**, donc routées en NoRemote.

**API Welcome to the Jungle — la vérification est devenue indispensable, pas optionnelle.** Sur cette seule relance elle a écarté **14 faux positifs** encore bien indexés par WebSearch (Silae, CGI ×2, Diptyque, Clap Partners, N2jsoft, Radio France, Mantra côté FR ; Kraken, Komeet, Opendatasoft, Sekoia, MISTER IA, France IA Montpellier côté remote), tous `archived`. **Nouveau piège associé** : le titre d'un résultat WebSearch peut pointer vers un slug sans aucun rapport — le « Formateur IA générative » de MISTER IA renvoyait vers un slug `commercial-business-developer-stage`. Vérifier que le slug correspond au titre, pas seulement que le statut est `published`.

| Source | Verdict 01/09/2026 (3e passage) |
|---|---|
| **euremotejobs.com** | Fonctionne de nouveau en curl + UA + Referer Google sur les 4 régions (~160 offres) — **4e inversion de comportement**, ne jamais présumer de la méthode. Le sélecteur fiable du lien ATS d'origine est `class="...application_button"`. **Nettoyer `?utm_source` et le suffixe `/application` ou `/apply` avant de comparer à la base**, sinon un lien déjà connu passe pour neuf (8 des 18 liens extraits étaient déjà en base) |
| **jobs.hr-path.com — correctif d'URL** | La bonne URL est **`/go/View-all-jobs/5288301/`**, qui rend ~70 offres (la racine `/jobs` ne rend rien). Deux postes France excellents (Solution Architect SuccessFactors, Workday LMS Lead) sont ouverts **sur 7 à 10 villes simultanément** : c'est un signal de souplesse géographique à exploiter en négociation, pas un poste parisien |
| **mission-freelances.fr — correctif d'URL** | `mission-freelances.fr/missions/` renvoie 404 : **il faut le `www.`** (`https://www.mission-freelances.fr/missions/`). 1347 missions en hrefs relatifs. Un filtre par mots-clés large produit 80 % de bruit (formateurs BTS commerce, chefs de projet événementiel, PM e-commerce) — filtrer serré |
| **`api.lever.co/v0/postings/jobgether`** | Fait désormais **~39 Mo** et dépasse le timeout de 120 s si on le parse en pipe. L'enregistrer en fichier d'abord, puis parser. Même précaution sur `pigment` (1,4 Mo) : les gros téléchargements Lever arrivent en JSON tronqué avec `--max-time 25`, **passer à 90 s et valider le JSON** plutôt que de conclure à un board cassé |
| **carriere.delaware.pro/jobs** | Contredit la note du matin qui donnait delaware à 0 HCM : 12 postes en clair dont un **Directeur de Projets SAP** et un **Senior Presales Manager SAP** jamais captés |
| **silae-career.teamtailor.com** | Les liens sont bien en clair en curl ; le grep initial échouait sur un motif trop strict, **le bon est `/jobs/\d+-[a-z0-9-]+`** |
| **redglobal.com** | Contredit le verdict très favorable du matin : le listing rend bien 10 fiches avec JSON-LD, mais **rien pour la France ce jour-là**. Le `/jobs/job/apply/<id>` est un doublon technique de chaque fiche, à ignorer |
| **workingnomads.com — piste close** | L'endpoint `/api/exposed_jobs/` (jamais exploré jusqu'ici) répond en 200 mais renvoie toujours **les 45 mêmes offres les plus récentes** ; `?page=` et `?category=` sont ignorés, contenu à 80 % dev/data. **Ne plus y consacrer de temps** |
| **HN « Who is hiring » septembre 2026** | Thread **`49522897`**, posté le 01/09 à 15h01 — contredit la note du matin (« pas encore posté ») : le bot poste bien le 1er du mois, simplement en milieu de journée. 127 commentaires, 1 seule prise réelle |
| **jobs.stationf.co** | L'index Algolia fonctionne, mais **l'org slug de l'index diffère parfois de celui de l'API WTTJ** : 6 candidats sur 25 ont renvoyé du vide et ont été écartés faute de vérification. Nouveaux slugs : Santé Académie = `airteach`, Klara = `mooveo`, Garantme = `garantme-1` (en plus de Tomorro=`airflow`, Joko=`joko-1`, Dastra=`dastra-1`) |
| **jobs.sap.com** | Toujours fetchable en curl direct, 17 postes France dont 12 nouveaux mais seulement 3 dans le profil. **Piège à connaître** : les postes « SAP Academy for Customer Success » (AE, CSM, Solution Advisor) forment un **programme early-career**, à vérifier avant d'investir du temps — trois lignes du tableur en dépendent déjà |
| Nouveaux slugs ATS confirmés | Greenhouse `doitintl`, `appian`, `beyondtrust` productifs. Workable exploitable via `apply.workable.com/seeq/...` (Seeq, France nommée). `lattice`, `cultureamp`, `workato`, `smartsheet`, `asana` répondent mais 100 % US/Canada |
| Slugs morts confirmés | Ashby : `deel` (0 poste, départ d'ATS confirmé), `personio`, `hibob`, `rippling`, `gong`, `miro`, `contentful`, `linear`, `mistral`, `hex`, `clay`, `attio` inexistants. Lever : `payfit`, `swile`, `spendesk`, `alma`, `leboncoin`, `doctolib`, `backmarket`, `ledger`, `malt`, `sorare` tous `Document not found`. Greenhouse : `hibob`, `deel`, `oyster`, `personio`, `clickup`, `docusign`, `zendesk`, `freshworks` à 0. **Strada Workday CXS ne répond plus** (`total: None`) |
| **Piège Oyster / doublon interne Ashby — correctif** | La note du 01/09 matin décrivait le doublon d'ID Ashby comme un simple bruit d'affichage. C'est faux : **les deux IDs peuvent être en base séparément**. Comparer chaque ID, jamais seulement l'intitulé |
| **Intermédiaires multiples sur un même besoin** | Cinq missions AMOA SIRH SuccessFactors publiées le 01/09 (INSYCO, Gamme solutions, R&S TELECOM, Octopus Group, Axande) : trois décrivent **mot pour mot le même besoin final** (campagnes 2027 entretiens/rémunération, modules EC/Recruiting/Performance/Onboarding). Idem pour deux AI Roll Out Manager à Marseille, et pour le bassin de Tarnos où Crit, Randstad, Adecco et LHH ont publié le même Business Analyst le 20/08. Ce ne sont **pas des doublons de lien** (annonces réellement distinctes, à conserver) mais il faut les traiter comme **une seule piste** au moment de candidater, et comme un signal de volume chez le client final |
| Sources à sec confirmées | freelance-informatique.fr **totalement saturé** (43 URLs data-obf décodées sur les 5 pages catégorie, 0 nouvelle — la méthode base64 fonctionne toujours) ; whitehallresources, opusresourcing, malt.fr (403), apec.fr (mur de connexion), freelance-day.eu, eursap (2 offres HR éliminatoires : Rotterdam exigeant le néerlandais, Varsovie exigeant le polonais), weworkremotely et remoterocketship (403), wellfound (303), remotifyeurope, YC, RemoteOK, Remotive, NTT Data RSS (20 postes SF, 0 France) |
| Pays Basque, à sec confirmé | Wipro Lauak (44 postes, tous hors profil — **la bonne URL est `wiprolauak.nous-recrutons.fr` en racine**, pas `nous-recrutons.fr/lauak` qui est en 404 ; le site est désormais saturé, nuancer la note « meilleur gisement ») ; Maïsadour (**la bonne méthode est `recrutement.maisadour.com/sitemap.xml`**, 43 URLs `/fr/annonce/<id>-<slug>-<CP>-<ville>` filtrables sur le code postal sans fetch ; front Nuxt sans `__NUXT_DATA__` exploitable ; 0 pertinent) ; TotalEnergies Pau (les 5 postes IT/PM/data sont des **contrats de professionnalisation** juniors) ; Arkema, Dassault Aviation, Euralis (`emploi.euralis.fr` injoignable) ; French Tech Pays Basque (annuaire 100 % JS) ; domaine `commerce` de HelloWork (68 offres, quasi 100 % porte-à-porte). Safran et Boardriders ont un tenant Workday mais leur site ID reste introuvable (422 systématique) |

### État des sources — relance du 2026-09-01 (2e passage, après élargissement du dispositif)

Deuxième relance du jour, la première après l'ajout des nouveaux postes (Engagement/Delivery Manager, Partner/Alliances Manager, Renewals/Retention, Customer Education, **chef de projet / project manager généraliste**) et des nouvelles sources. 4 clusters parallèles, 67 offres candidates, **toutes nouvelles** (0 doublon rejeté par `add_offre.py`, les 4 agents ayant dédoublonné en amont contre les 1826 liens en base). Répartition : 22 SIRH, 4 CSM, 7 IA, 5 PM, 6 USA, 7 Pays Basque, 16 NoRemote.

**L'élargissement a payé immédiatement.** Les deux meilleures prises viennent directement des nouveautés : un **SAP SuccessFactors Project Manager mainly remote chez RED Global** (⭐⭐⭐⭐⭐, source testée pour la première fois) et un **Manager Strategic Account Management French Speaking chez Atlassian en Remote-France explicite** (⭐⭐⭐⭐⭐). Le nouveau périmètre « chef de projet généraliste » a produit à lui seul une dizaine d'offres (free-work `/jobs/chef-de-projet`, missions freelance, et les deux ⭐⭐⭐⭐ du Pays Basque), et les nouveaux intitulés Partner/Alliances ont donné Chainguard France-Remote, Supabase Remote Global, Automattic et 4 postes Canonical.

> **Découverte majeure — API publique Welcome to the Jungle, le test de vivacité qui manquait.** Le fetch d'une fiche WTTJ reste bloqué (403 ou 0 octet), ce qui empêchait depuis des mois de vérifier qu'un lien WTTJ trouvé par WebSearch était encore vivant. L'API répond en curl sans blocage :
> ```bash
> curl -s "https://api.welcometothejungle.com/api/v1/organizations/<org>/jobs/<slug>"
> ```
> Elle expose `status` (`published` / `archived`), le remote exact (`fulltime` / `partial` / `punctual`), le salaire et la date. Elle a permis d'écarter 4 faux positifs encore bien indexés par WebSearch (Boond, Inqom, Coachello, Rupture-Pro, tous `archived`). **À utiliser systématiquement désormais avant d'ajouter un lien WTTJ au tableur.**

> **Nouveau filon Pays Basque — les pages catégorie locales HelloWork.** Contredit la note générale qui donnait hellowork.com à rendement quasi nul : les pages par ville et domaine se fetchent en curl et exposent les liens individuels `/fr-fr/emplois/NNNN.html`. Exemple : `hellowork.com/fr-fr/emploi/domaine_informatique-ville_bidart-64210.html`. Elles ont produit 4 des 7 offres du cluster Pays Basque, dont les deux ⭐⭐⭐⭐ (Chef de Projet SI à Bayonne, Chef de Projet Fonctionnel à Tarnos). **À repasser à chaque relance Pays Basque**, en faisant varier ville et domaine.

| Source | Verdict 01/09/2026 (2e passage) |
|---|---|
| **euremotejobs.com** | Comportement inversé pour la 3e fois : le matin WebFetch passait et curl bloquait, l'après-midi **WebFetch en 404 et curl + UA + Referer Google passe partout**. Ne jamais présumer de la méthode : tenter les deux. **Correctif d'URL** : `/job-region/europe/` n'existe pas ; les pages valides sont `/job-region/france/`, `/job-region/remote-jobs-europe/`, `/job-region/remote-jobs-emea/`, `/job-region/remote-jobs-worldwide/` |
| **API Atlassian** | Bouge encore (nouveau job ID 26296) et a donné la meilleure offre CSM de la relance — confirme définitivement qu'il faut la repasser intégralement à chaque fois |
| **eursap.eu — correctif** | Contrairement à la note du 27/08 (« impossible de construire le lien individuel »), la page `/jobs/` expose désormais **les URLs individuelles en clair** (`eursap.eu/jobs/<slug>-<id>-<pays>`) dans le HTML curl. Source redevenue exploitable proprement |
| **mission-freelances.fr — astuce** | Les liens sont en **hrefs relatifs** `/missions/<slug>/` : un regex exigeant l'URL absolue rend 0 résultat (piège à connaître). ~1356 missions sur la page listing, fiches avec JSON-LD complet où `jobLocationType: TELECOMMUTE` est un signal remote fiable. Élargir le filtre aux slugs chef-de-projet/PM/IA a donné 12 offres |
| **free-work `/jobs/chef-de-projet`** | Fonctionne en fetch direct (16 offres, JSON-LD complet) mais **la pagination `?page=2` renvoie la page 1**, contrairement à `/jobs/sirh`. 6 offres retenues sur 16, le reste étant du dev/cyber pur |
| **RemotifyEurope** | Contredit le verdict « 403, WebSearch uniquement » : **curl + UA passe désormais**, pages server-rendered avec cartes `aria-label="Job posting: <titre> at <entreprise>"` et liens `/listing/<uuid>`. Mais beaucoup d'annonces périmées et le lien apply n'est pas exposé — utile en radar, à recroiser par API ATS |
| **Thread HN « Who is Hiring » septembre** | **Pas encore posté** au 01/09 : le bot a publié le thread d'août le 3 août (49156683), pas le 1er. À retenter dans les jours qui suivent le début du mois plutôt que le 1er |
| **workingnomads.com** | curl passe (200) mais listing 100% JS sans lien de fiche dans le HTML ; **un endpoint `/api/exposed_jobs/` existe et n'a pas été exploré** — piste pour une prochaine fois. remoterocketship.com toujours en 403 |
| Nouveaux intitulés sur les API ATS | Les recherches Renewals/Partner/Customer Education en direct sur Ashby/Greenhouse remontent surtout du US-only ou de l'ancrage Londres/Amsterdam (Mixpanel, Highspot, NetBox, Absorb, Chainalysis, Ema, tous écartés après vérification). **Le rendement réel vient du filtrage de ces intitulés sur les boards déjà connus**, pas de nouvelles recherches par titre |
| Sources saturées ce jour | free-work `/jobs/sirh`, `/sap-hcm`, `/sap-successfactors` ; les 5 pages catégorie freelance-informatique (data-obf) ; hansonregan ; eursap ; Wipro Lauak (45 postes, tous les pertinents déjà en base) ; Maïsadour (le **sitemap `/fr/sitemap.xml`** est la bonne méthode, `/offres-emploi` est en 404, mais les ~60 annonces sont hors profil) |
| Pays Basque, rendement nul confirmé | TotalEnergies Pau (deadlines dépassées), Euralis (`recrute.euralis.fr` ENOTFOUND), Epta Hendaye (offre repérée morte en 410), B.Braun, Safran (WebSearch ne rend que des alternances). Teréga et Enovis répondent bien **via leur API Workday CXS**, à réutiliser, mais leurs postes pertinents sont déjà en base |
| **La French Tech Pays Basque** | Le domaine `frenchtechpaysbasque.fr` **redirige (301) vers `frenchtech-paysbasque.com`**, parfaitement fetchable. **Pas de page emplois** ; l'annuaire `/ecosysteme` liste ~150 membres et sert de radar. Rendement direct nul : startups trop petites, celles qui recrutent publient sur LinkedIn seulement |

### État des sources — relance du 2026-09-01

Relance en 4 clusters parallèles. **Incident à noter : les 4 agents sont tombés en échec au premier lancement sur "monthly spend limit" (plafond de dépenses API mensuel), avant même de produire un résultat exploitable ; un second lancement immédiat a fonctionné normalement.** Si ça se reproduit, ne pas insister en boucle : le prévenir à l'utilisateur plutôt que de relancer indéfiniment.

18 offres candidates compilées (4 remote/VC EU, 0 Pays Basque, 3 ATS+HRIS+USA, 11 FR/freelance), 16 ajoutées après passage dans `add_offre.py` (1 doublon ignoré : Remote People CSM EMEA, déjà ajouté la veille). 7 lignes `Fait=x` archivées.

**euremotejobs.com : le blocage curl est revenu.** Contrairement à la note du 31/08 qui donnait la méthode curl + User-Agent + Referer Google comme fonctionnelle, le cluster remote/VC de ce jour a constaté un 403 systématique en curl direct, y compris avec ces headers ; **WebFetch passe en revanche sans problème, fiches individuelles comprises**. Ce site alterne donc son comportement selon la méthode utilisée d'une relance à l'autre ; tenter WebFetch en premier recours désormais si curl échoue, plutôt que d'abandonner la source.

**Nouveaux slugs/boards confirmés vivants** : Greenhouse `gr8tech` reste productif avec un 2e poste distinct le même jour (Senior Account Manager, ID différent de l'Operations Account Manager déjà en base ; bien vérifier l'ID complet, pas seulement l'entreprise, avant de conclure à un doublon) ; Ashby `n8n` expose la France via le champ `secondaryLocations` plutôt que dans la location principale, à vérifier systématiquement sur les boards Ashby quand la location affichée semble restreindre à une seule ville ; Ashby `notabene` a un 2e poste distinct (Solutions Architect Lead) en plus du CSM déjà en base, remote sans restriction. Nouveau board freelance direct trouvé : `freelance-day.eu` (mission SIRH/SAP SF francilienne, onsite). Nouveaux ATS d'éditeurs français repérés via le radar LinkedIn : `careers.abtasty.com` (AB Tasty, CSM), `emplois.weavy.fr` (Weavy Consulting, cabinet SIRH) — tous deux à ATS propriétaire, hors Ashby/Lever/Greenhouse, donc invisibles aux WebSearch `site:jobs.ashbyhq.com` habituels.

**SmartRecruiters confirmé peu fiable une fois vérifié en détail** : Nagarro (slug `Nagarro1`, 881 postes) a semblé prometteur mais chacune des 3 pistes France s'est révélée fausse une fois la fiche complète lue (le poste CSM SAP S/4HANA Paris est en réalité hybride avec déplacements malgré le flag `remote: true` de l'API, le Product Support Specialist est junior, le Consultant SAP Senior porte sur FICO/SD/MM/PP et non HR/HCM). Retenir la leçon : sur les gros ATS multi-pays comme SmartRecruiters, le champ `remote` de l'API ne suffit jamais, il faut lire la fiche complète.

**Maïsadour (Pays Basque)** : le portail `recrutement.maisadour.com` publie régulièrement des postes IT/data/digital pertinents (Data Steward, Chef de Projet SI, Coordinateur Cyber), mais l'index de recherche contient beaucoup d'offres déjà expirées ; à repasser systématiquement à chaque relance Pays Basque en vérifiant chaque lien au fetch direct avant ajout, plutôt qu'à écarter après un passage infructueux.

**Rendement nul confirmé une nouvelle fois** : Dassault Aviation Anglet/Biarritz, TotalEnergies Pau, Sanofi Mourenx, Veolia Pau, Boardriders/Quiksilver, Celsa, Technoflex, Toray, Lindt & Sprüngli Oloron (portails carrière vides ou hors profil sur ce périmètre géographique précis) ; freelance-informatique.fr et jobs.hr-path.com totalement saturés (0 offre nouvelle sur les 8 pages catégorie et les 4 postes HR Path revérifiés) ; opusresourcing.com, whitehallresources.com, apec.fr toujours infructueux.

### État des sources — relance du 2026-08-31

Relance en 4 clusters parallèles (FR/freelance, API ATS+HRIS+USA fusionné, remote/VC EU+niches, Pays Basque), format désormais stable depuis plusieurs relances. 41 offres candidates compilées par les agents (déjà dédoublonnées par chacun contre les liens existants), **39 ajoutées** après passage dans `add_offre.py` (2 doublons ignorés automatiquement : Teréga et Lauak, déjà présents dans "Pays Basque" malgré la vérification openpyxl de l'agent — le garde-fou automatique reste donc indispensable même quand l'agent a fait sa propre vérification). 42 lignes `Fait=x` archivées au passage (32 dans Offres CSM, 10 dans Offres USA).

**euremotejobs.com reste la source la plus productive du cluster remote/VC** (7 offres sur 8 dans ce cluster) : la méthode curl + User-Agent navigateur + Referer Google continue de fonctionner sur les pages `/job-region/...` et `/jobs/remote-*-jobs`, et chaque fiche expose le vrai lien ATS d'origine (Greenhouse/Ashby/SmartRecruiters) dans le bouton "Apply for job".

**Nouveaux slugs ATS confirmés vivants, à ajouter au dispositif permanent** : Greenhouse `mozilla` (Senior PM Mobile, France remote explicite, excellent fit), `chartbeatinc`, `gr8tech` (board sur `job-boards.eu.greenhouse.io`, pas le domaine standard), `remotepeople` (idem, `.eu.greenhouse.io`), `testlio`, `axon` (US, TAM France-Remote explicite malgré le secteur défense/sécurité) ; Lever `appfollow` (CSM remote Europe générique) ; SmartRecruiters `Nagarro1` (SuccessFactors Employee Central, France explicite — premier board SmartRecruiters vraiment productif à ce jour, à garder en tête pour les futurs consultants SAP/SF) ; Ashby `notabene` (ancrage réel Londres malgré le titre EMEA, éligibilité France à vérifier avant candidature).

**Confirmations utiles** : le piège "EMEA affiché mais ancrage pays unique" repéré sur Fivetran le 30/08 se reproduit sur Grafana Labs (déjà connu, variante avec exigence Arabe) et Notabene — toujours lire le champ location brut de l'API plutôt que le titre du poste. Greenhouse `processstreet` publie des dizaines de doublons "Account Executive (Remote)" avec des req ID différents le même jour, signal de bruit à surveiller plutôt qu'un vivier fiable. L'API carrières Atlassian, donnée comme changeant systématiquement dans les notes précédentes, est restée stable cette fois (aucun nouveau poste) — confirme qu'il ne faut jamais présumer d'un sens fixe (mouvant ou stable) sans revérifier à chaque relance. `jobs.world.luccasoftware.com/lucca` renvoie 401 Unauthorized en accès API direct (à retenter via WebSearch plutôt que l'API la prochaine fois). Lever `yassir` a désormais un board vide (poste fermé).

**Rendement nul confirmé une nouvelle fois** : boards VC (Index Ventures, Balderton, Atomico, a16z, Sequoia, Ribbit), wellfound.com, workatastartup/Y Combinator, cremedelacreme.io (toujours non listable, matching inversé confirmé), weworkremotely.com (403 systématique), remoterocketship.com/remotifyeurope.com/workingnomads.com en fetch direct (WebSearch uniquement). Le thread HN "Who is Hiring" d'août 2026 a été localisé (`#49156683`, à retenir pour la prochaine fois) mais n'a produit aucune offre exploitable après vérification individuelle.

### État des sources — relance du 2026-08-30

Relance en 4 clusters parallèles (FR/freelance, API ATS+HRIS+USA fusionné, remote/VC EU+niches, Pays Basque). 19 offres nouvelles ajoutées sur un peu plus de 400 offres candidates compilées, très fort recouvrement inter-clusters confirmé une nouvelle fois (la plupart des postes trouvés via Ashby/Lever/Greenhouse et le radar LinkedIn/WTTJ étaient déjà en base avant même de lancer les recherches).

**Nouveau slug Greenhouse très productif : `automatticcareers` (Automattic, WordPress/WooCommerce/Tumblr/Beeper/Newspack).** Entreprise US totalement distribuée "regardless of location", bande salariale globale payée en devise locale ; a donné 6 offres exploitables d'un coup (CSM, TAM x2, PM x2, Account Director), toutes routées vers Offres USA. À garder au dispositif permanent au même titre que `remotecom` et `gitlab`.

**euremotejobs.com sort du statut "403, à écarter" : voir la note mise à jour dans le tableau des boards remote plus haut** — un `curl` avec User-Agent navigateur passe alors que WebFetch reste bloqué, et expose les liens ATS d'origine en clair dans le HTML. A produit Tenable (Channel Account Manager, France-Remote confirmé) et Upsun/ex-Platform.sh (Customer Retention Manager, France listée nommément) en un seul passage.

**Autre confirmation** : Yassir (jobs.lever.co/Yassir) reste un bon fit HRIS Implementation Project Manager Paris/remote, déjà capté par une relance antérieure (doublon ignoré cette fois-ci) — slug Lever à garder en tête si le poste se libère à nouveau ailleurs.

**Rendement nul confirmé une nouvelle fois** : Index Ventures (certificat TLS invalide), Balderton (portail JS "Powered by Consider"), Atomico (429 puis lien mort), Ribbit Capital (404), collective.work (flux non filtrable), upwork.com/freelancer.com (marketplaces sans URL de poste stable, pas des boards), workingnomads.com et remoterocketship.com (pages catégorie JS, WebSearch ne remonte que des agrégateurs génériques). Cabinets de conseil et éditeurs HRIS classiques (ADP, SD Worx, Cegid, Talentia, Personio) toujours saturés, passage rapide suffisant.

### État des sources — relance du 2026-08-28

Relance exhaustive en 4 clusters parallèles (FR/freelance, API ATS+HRIS+USA fusionné, remote/VC EU + niches IA/PM/TAM, Pays Basque) : 222 offres candidates compilées (107 + 94 + 17 + 4). **Dédoublonnage automatique via `add_offre.ajouter_offres()` : 199 doublons ignorés, seulement 23 offres réellement nouvelles ajoutées.** Ce taux de doublon très supérieur à l'habitude s'explique par un état du tableur déjà à jour d'une session précédente non commitée au moment de cette relance (le fichier portait des modifications non poussées avant même le lancement des 4 clusters) : la plupart des offres retrouvées par les agents étaient donc déjà en base. Le garde-fou automatique a fonctionné exactement comme prévu, sans aucune intervention manuelle de dédoublonnage. 15 lignes archivées vers Fait au passage (3 SIRH, 1 CSM, 6 PM, 5 Pays Basque).

**Nouveaux slugs ATS confirmés vivants, à ajouter au dispositif permanent** : Ashby `checkly` (Senior Sales Engineer Europe, trouvé via HN Who's Hiring), `swans`, `pencil` (toujours excellent, PM EMEA). Lever `distru` (PM remote Americas & Europe, via HN), `veeva` (Implementation Consultant Paris confirmé). Greenhouse `cribl` (Partner Solutions Engineer France explicite), `abnormal.ai`/`abnormalsecurity`, `cloudbeds`, `processstreet`, `sourcegraph91` (URL de careers propre plutôt que job-boards.greenhouse.io pour Cribl et Fivetran, ex. `cribl.io/job-detail/?gh_jid=...`, `fivetran.com/careers/job?gh_jid=...`).

**Confirmations utiles** :
- API Atlassian a de nouveau bougé (nouveaux ID 25524, 26840) et a produit 2 postes jamais captés (Enterprise Solutions Engineer French, EMEA Solutions Engineering Manager) — confirme qu'il faut le repasser intégralement à chaque relance.
- Le piège Ashby "délisté mais vivant" (posts absents de l'API publique mais candidatables via lien direct) s'est reproduit une 3e fois avec Synthesia (Strategic CSM French Speaking, trouvé via WebSearch puis vérifié vivant au fetch direct) — après Owkin (19/08) et un cas similaire courant. À traiter comme un pattern récurrent, pas une exception.
- Safran-group.com est protégé par Cloudflare (403 systématique en curl et WebFetch, y compris avec User-Agent navigateur) — seule option pour ce site : WebSearch pour l'URL, sans vérification de vivacité possible par fetch direct.
- Wipro Lauak (`nous-recrutons.fr`) confirmé comme le meilleur gisement du Pays Basque pour ce profil (aéronautique), à repasser systématiquement ; l'agroalimentaire et la chimie/énergie du bassin restent quasi stériles pour des postes hors technique/production.
- Canonical reste UK-basé (Londres), jamais à router vers Offres USA malgré son volume de postes Home based - Worldwide/EMEA ; Dataiku (dual Paris/New York) et PostHog (US, YC) confirmés comme Offres USA.



Deuxième relance exhaustive le même jour, appliquant la fusion recommandée ci-dessous entre les clusters « API ATS + éditeurs HRIS » et « USA remote worldwide » (un seul agent pour les deux). 4 clusters au total (FR/freelance, ATS+HRIS+USA fusionné, remote/VC EU + niches IA/PM, Pays Basque 2e passage) : 39 + 34 + 5 + 7 = 85 offres candidates, **toutes confirmées nouvelles** par les agents (dédoublonnage contre les ~1750 liens déjà en base fait en amont par chaque agent via openpyxl, puis re-vérifié par `add_offre.py` à l'insertion : 0 doublon rejeté). 1 ligne archivée vers Fait.

La fusion ATS+HRIS/USA a bien fonctionné : un seul agent a couvert les deux à la fois sans dédoublonnage manuel supplémentaire à faire ensuite, confirmant la leçon du 27/08 matin. À reconduire dans ce format pour les prochaines relances.

**Nouveaux slugs ATS confirmés vivants et productifs** : Greenhouse `cribl` (excellent — `Partner Solutions Engineer, Southern Europe | Remote - France` explicite, société US) ; Ashby `supabase` (le meilleur filon de la relance : 4 postes tagués littéralement `"Remote, Anywhere"` sans aucune contrainte géographique, y compris un 5ᵉ poste PM du même board explicitement `(Bay Area based)` malgré le même tag générique — rappel qu'il faut toujours lire le suffixe du titre, jamais se fier au seul tag). Testés mais rendement nul (Remote-US strict) : Ashby `aiwyn`, `vantage`, `propelus` ; Greenhouse `relativity`, `salesloft`, `6sense`.

**freelance-informatique.fr — 2 nouvelles pages catégorie à ajouter aux pages de référence permanentes**, trouvées via le sitemap `sitemap_index_thematiques.xml` et jamais testées avant ce jour : `categorie-autres-progiciels-rh-240` et `categorie-progiciels-de-paie-239`. Elles ont donné 9 offres d'un coup (dont 2 avec télétravail confirmé, Formateur/Expert Silae) alors que les 3 pages catégorie habituelles étaient totalement à sec (0/30).

**welcometothejungle.com — nouvel angle rentable** : les recherches CSM/PM habituelles sont désormais saturées, mais élargir aux intitulés « technical account manager »/« solutions engineer » a sorti 8 offres jamais vues sous cet angle sur ce board (Scaleway, Komeet, Dataiku, Sirdata, Opendatasoft, Sekoia x2). À garder comme requête systématique désormais, au même titre que CSM/PM/SIRH/IA.

**Dataiku, convention confirmée** : le poste « Technical Account Manager - France » trouvé via WTTJ (donc hors du cluster ATS+USA) a bien été routé vers l'onglet « Offres USA » manuellement, conformément à la convention déjà établie (dual HQ Paris/New York, traité comme USA) — cette convention doit s'appliquer même quand l'offre est trouvée par un cluster autre que le cluster USA.

**Confirmations négatives (déjà notées, revérifiées ce jour)** : Himalayas.app toujours inutilisable en fetch direct (chaque URL `/companies/.../jobs/...` a rendu une page listing générique sans rapport avec le poste demandé) ; Index Ventures toujours mort (404 sur `/startup-jobs/...`) ; Atlassian (iCIMS) exceptionnellement stable cette fois (8/9 ID déjà connus, un seul nouveau poste) — contredit la note du 26/08 qui donnait le board comme changeant systématiquement, à revérifier sans présumer d'un sens fixe la prochaine fois ; Remotive API toujours dégradée (paramètre de recherche ne filtre plus rien) ; RemoteOK toujours quasi nul pour ce profil ; Jobgether (Lever, filtré France) toujours aussi volumineux (176 offres) mais désormais saturé (3 non-connues seulement, aucune pertinente) deux jours de suite.

**Gap de routage `add_offre.py` — corrigé depuis** : les intitulés « Account Director », « Sales Enablement », « Customer Enablement », « Account Executive » figurent désormais dans `PRESALES_KEYWORDS` et sont routés vers « Offres CSM » (vérifié le 01/09/2026).

### État des sources — relance du 2026-08-27

Relance exhaustive menée en 4 recherches parallèles (boards FR/freelance, API ATS + éditeurs HRIS, boards remote/VC EU, USA remote worldwide). Environ 250 offres candidates compilées entre les 4 rapports, avec un très fort recouvrement croisé cette fois : les clusters « API ATS + éditeurs HRIS » et « USA remote worldwide » interrogent en grande partie les mêmes API (Ashby, Lever, Greenhouse) et se recoupaient sur des dizaines de postes identiques (Chainguard, Dataiku, GitLab, Remote.com, Canonical, Pennylane, Camunda, Jobgether...). Après dédoublonnage automatique par `add_offre.py` (qui compare aussi contre les ~1750 liens déjà en base), **62 offres nouvelles ajoutées**, 12 lignes archivées vers Fait.

**Leçon d'organisation pour les prochaines relances :** vu ce recouvrement, les deux clusters « ATS/HRIS » et « USA worldwide » gagneraient à être fusionnés en un seul cluster de recherche (avec juste une note de vigilance supplémentaire sur l'éligibilité internationale pour les entreprises US), plutôt que lancés séparément — cela réduirait le travail de dédoublonnage manuel post-recherche sans perte de couverture.

| Source | Verdict 27/08/2026 |
|---|---|
| free-work.com `/jobs/sirh` | 36 offres au total sur le site, mais seule la page 1 (16 offres) a été fetchée par l'agent faute de temps — pages 2 et 3 restent un gisement pour une prochaine relance |
| eursap.eu/jobs | Le fetch direct ne rend qu'un titre + une référence interne, jamais d'URL individuelle cliquable — impossible de construire le lien sans deviner, donc ces offres n'ont pas pu être ajoutées cette fois ; à creuser (peut-être un pattern d'URL fixe à découvrir) |
| Veeva (Lever) | Expose une centaine de postes Product Manager/Solution Consultant en Europe avec `workplaceType: remote`, mais ce remote est presque toujours lié à une résidence dans un pays précis (UK/DE/ES/IE) et non ouvert depuis la France malgré l'étiquette « remote » — seul le poste Paris explicite a été retenu ; bon exemple à garder en tête du piège `isRemote: true` qui ne garantit rien |
| Atlassian (iCIMS) | Board de nouveau changé (nouveaux ID 25256/26057/26241/26063/25503/26380) — confirme qu'il faut toujours le repasser intégralement à chaque relance, jamais réutiliser d'anciens ID |
| Alan (Ashby) | Bascule constatée : tous les postes actuels sont tagués Hybrid, y compris ceux titrés « Anywhere in France » — contrairement aux relances précédentes qui y trouvaient du full remote ; à revérifier plutôt que de supposer un fond permanent |
| 3 liens free-work.com sourcés par WebSearch | Confirmés morts au fetch direct (page « offre supprimée ou expirée ») — rappel que les résultats WebSearch sur free-work doivent systématiquement être vérifiés par fetch direct avant ajout, jamais pris tels quels |
| mission-freelances.fr | Toujours très productif (35 offres exploitables), mais 1 lien mort identifié (`formateur-ia-et-no-code-paris-0c1654e1`) |
| HR Path (jobs.hr-path.com) | Une nouvelle fiche « Consultant SIRH (H/F) Workday • Oracle HCM • SAP SuccessFactors » publiée le 25/08/2026 a été captée dès le lendemain via `/job/<slug>/<id>/` — confirme que cette URL de recherche vaut le coup à chaque relance malgré un rendement habituellement faible |
| HN Algolia (thread mensuel « Who is hiring ») | Tentative infructueuse : l'agent n'a pas réussi à localiser l'ID du thread d'août 2026 via l'API Algolia (résultats retournés dataient de 2025) — méthode à fiabiliser avant la prochaine tentative, sinon repasser par une recherche manuelle de l'ID de thread |
| Nouveaux slugs ATS confirmés vivants | Ashby : `pencil`, `dash0`, `deepgram`, `fieldguide`, `mural`, `socket`, `tilla`, `zip`, `n8n`. Lever : `superside` (Global remote explicite), `veeva`, `teramind`. Greenhouse : `customerio`, `samsara`, `degreed`, `fivetran`, `abnormalsecurity`/`abnormal.ai`, `canonical`, `dataiku`, `chainguard`, `gitlab`, `grafanalabs`, `remotecom` — tous à garder au dispositif permanent |

### État des sources — relance du 2026-08-26

Relance exhaustive menée en 4 recherches parallèles (boards FR/freelance, API ATS + éditeurs HRIS, boards remote/VC EU + niches, USA remote worldwide/EMEA) : 185 offres candidates compilées, 163 doublons filtrés automatiquement par `add_offre.py` (essentiellement des reprises d'une même annonce entre 2 ou 3 clusters, plus un fort recouvrement avec la relance de la veille), **22 offres nouvelles ajoutées**. En préalable, 16 lignes marquées Fait=x dans Offres SIRH ont été archivées vers Fait.

Rendement plus faible qu'à l'accoutumée côté FR/freelance (0 offre nouvelle sur 79 candidates du cluster boards FR/freelance : free-work, freelance-informatique.fr et mission-freelances.fr avaient déjà été entièrement captés par la relance du 25/08, la veille) — signe que ces boards se rafraîchissent vite mais que deux relances à moins de 24h d'écart se recoupent presque totalement sur ce cluster. Le rendement est resté correct côté API ATS/USA (22 offres sur 96 candidates de ces deux clusters), notamment parce que de nouveaux slugs Greenhouse non testés avant ce jour (`canonical`, `dataiku`, `elastic`, `sourcegraph91`) et l'API carrières Atlassian (qui rebouge à chaque relance) ont produit des postes non encore vus.

Ordre d'insertion utilisé pour gérer le chevauchement entre le cluster USA et les clusters EMEA classiques : le cluster USA a été inséré en premier dans `add_offre.py`, afin qu'une offre trouvée à la fois avec et sans le marqueur `Onglet='Offres USA'` (GitLab, Dataiku, Remote.com, Ashby, Chainguard, tous basés aux USA) soit routée vers Offres USA plutôt que vers l'onglet métier classique.

Nouveaux slugs ATS qui répondent, à ajouter au dispositif permanent : Greenhouse `canonical` (attention, Canonical/Ubuntu est basé à Londres, **pas** une entreprise USA malgré son volume de postes remote worldwide — ne jamais router vers Offres USA), `dataiku` (dual HQ Paris/New York, traité comme USA), `elastic`, `sourcegraph91` (slug inhabituel, trouvé via HN Who's Hiring), `chainguard`, `customerio` ; Ashby `hackerone`, `mural`, `pylon-labs`, `siena` (rendement faible mais confirmés vivants).

| Source | Verdict 26/08/2026 |
|---|---|
| Détection remote sur Greenhouse | Certains éditeurs (Canonical) encodent le remote en `"Home based - EMEA"` / `"Home based - Worldwide"` plutôt qu'avec le mot "remote" — la détection automatique doit chercher ces deux formulations, pas seulement "remote" |
| Ashby, fiabilité du JSON embarqué | Le JSON brut d'une page Ashby (`workplaceType`, `locationName`) est plus fiable que le titre du poste : plusieurs intitulés "EMEA" (Vapi, Omni, Docker x2) se sont révélés Hybrid sur une ville précise (Amsterdam, Dublin, Angleterre) une fois le JSON vérifié |
| Strada / Alight | Migration confirmée vers deux tenants Workday CXS distincts : `alight.wd5.myworkdayjobs.com` (Alight) et `strada.wd12.myworkdayjobs.com` (Strada) ; toute URL `careers.alight.com/strada/.../job/...` est désormais morte |
| weworkremotely.com | De nouveau bloqué (403/redirection Cloudflare) sur toutes les pages testées, y compris les fiches individuelles — contredit la note du 25/08 qui le donnait fiable en fetch direct ; à revérifier à chaque relance plutôt que de supposer un état stable |
| Remotive (API) | Le paramètre `category` de son API ne filtre plus rien : les 4 catégories testées renvoient exactement le même flux générique bruité |
| Y Combinator Jobs (ycombinator.com/jobs/role/...) | Le filtre de rôle est cassé pour `customer-success-manager` (renvoie des postes d'ingénieur logiciel) ; fonctionne correctement pour `product-manager` |
| HN "Who is Hiring" via l'API Algolia | Bonne source pour la recherche USA remote worldwide : a permis de retrouver Chainguard, Sourcegraph, Checkly et PostHog. Passer par l'API Algolia du thread mensuel plutôt que par hnhiring.com (403 systématique) |
| hellowork.com | Un lien individuel trouvé par WebSearch confirmé mort (HTTP 410) — rendement quasi nul confirmé une nouvelle fois |
| opusresourcing.com, apec.fr, collective.work, malt.fr, freelancer.com/jobs/sap/ | Rendement nul confirmé une nouvelle fois sur les 5 (mur de connexion pour apec, flux non filtrable pour collective.work, malt.fr est un annuaire de profils pas un board de missions) |
| HR Path (jobs.hr-path.com) | Le poste "Consultant SAP SuccessFactors" a le télétravail confirmé par fetch direct de la fiche ; le poste générique "Consultant SIRH (Workday/Oracle HCM/SF)" ne mentionne que des "possibilités de télétravail", donc laissé en Remote ambigu plutôt que confirmé |

### État des sources — relance du 2026-08-25

Relance exhaustive menée en 4 recherches parallèles (FR/freelance, API ATS + éditeurs HRIS, boards remote/VC EU, USA + niches IA/PM) : 238 offres candidates compilées, 186 doublons filtrés automatiquement par `add_offre.py` (dédoublonnage inter-clusters compris), **52 offres nouvelles ajoutées**.

En préalable, 18 lignes marquées Fait=x (dont Docker Senior Implementation Engineer et Loft Orbital Sales Systems Engineer, deux offres mal routées en Offres SIRH par simple correspondance de mot-clé sur "Implementation"/"Systems Engineer" alors que ces entreprises n'ont aucun rapport avec le SIRH) traînaient dans Offres SIRH et Offres USA depuis des relances précédentes ; déplacées vers Fait avant l'ajout.

Nouveaux slugs ATS qui répondent, à ajouter au dispositif permanent : Ashby `gorgias` (CSM/AM Paris, statut remote non précisé) ; Lever `pigment` (CSM/TAM/PM hybride Paris), `insiderone` (PM Martech remote Europe multi-pays), `superside` (AM/PM remote **Global** explicite, éditeur creative-as-a-service) ; Greenhouse `fivetran` (SE senior EMEA), `processstreet` (CSM Jr remote confirmé ouvert hors USA).

| Source | Verdict 25/08/2026 |
|---|---|
| API Greenhouse `remotecom` | Toujours l'éditeur le mieux aligné, désormais avec un poste France explicitement nommé (`Remote-France`) en plus des habituels `Remote-EMEA` |
| API Lever `jobgether` (filtré France) | 9 postes pertinents dont un excellent croisement PM+HRIS interne et un Data Migration Lead ; toujours nécessaire de filtrer sur `categories.location == "France"` |
| freelance-informatique.fr, décodage `data-obf` | Toujours très productif : les 3 pages catégorie de référence ont donné une trentaine d'URLs individuelles, dont plusieurs neuves |
| hansonregan.com | Bon jour exceptionnel : 4 offres SAP/CSM full remote "Anywhere" chez un même client final anonymisé, dont un TJM à 750€/j |
| welcometothejungle.com (WebSearch) | Bon rendement CSM full remote (AssessFirst, Namastay, Boost...), mais **plusieurs liens à revérifier au clic** : le fetch direct d'une fiche WTTJ reste bloqué, les résultats WebSearch n'ont pu être confirmés qu'au niveau titre/snippet |
| mission-freelances.fr | Toujours très productif côté Formateur IA et CSM full remote, y compris un "Founding Customer Success Manager" qui valorise directement le statut de co-fondateur |
| LinkedIn radar (HRIS/CSM France) | A remonté un HR Tech Run Lead **chez L'Oréal** (ancien compte de Gaëtan 10 ans côté SAP HR) et un croisement HRIS x IA x pre-sales chez Arago ; reste un radar, jamais de mention de télétravail fiable |
| SD Worx | Confirmé une nouvelle fois : les 3 liens trouvés par WebSearch étaient tous morts (404/410) au fetch direct malgré leur bonne indexation |
| Cegid | `jobs.cegid.com` répond en HTTP 200 mais affiche "offre non en ligne" — un 200 ne suffit pas à garantir qu'une offre Cegid est vivante, vérifier le texte de la page |
| Lucca | Confirmé migré vers `jobs.world.luccasoftware.com/lucca` ; toute URL `jobs.lever.co/lucca` est désormais mort (404), y compris certains résultats WebSearch encore indexés sous l'ancien ATS |
| weworkremotely.com | Fetch direct désormais fiable pour trancher vivant/mort : une annonce vivante rend un 200 avec le bon titre, une annonce fermée redirige silencieusement vers la homepage (403 Cloudflare) — méthode utilisée pour écarter Vidalytics et Nearcut sans ambiguïté |
| Boards VC EU (Balderton, Atomico, a16z, Sequoia, Ribbit) | Rendement nul confirmé une nouvelle fois |
| Cabinets de conseil (passage rapide) | Conforme à la note du 19/08 : vivier saturé, seul Sia Partners a donné 2 postes non encore en base |
| ADP, Talentia Software | Rendement nul confirmé : ADP ne propose que Bucarest/US, Talentia n'a toujours pas de board public exploitable |
| Volet USA : critère remote worldwide vs US-only | Appliqué strictement ; a exclu des dizaines de postes par ailleurs excellents (Vanta, Merge, Hex, Notion, Planhat, Intercom, Persona, Gainsight, quasi tous Remote-US ou ville US précise sans ouverture internationale) |
| RemoteOK, Remotive, Built In, TopCSJobs, Product Manager Job Board | Rendement toujours très faible pour la recherche USA (API dégradée ou quasi 100% Remote-US strict), conforme au verdict du 22/08 |

### État des sources — relance du 2026-08-21

Relance menée en 4 recherches parallèles (boards FR/freelance, API ATS + éditeurs HRIS, boards remote/VC/LinkedIn, IA/PM/niche) : 129 offres candidates compilées, 71 doublons filtrés contre les ~1250 liens déjà en base (dont 1 lien SD Worx confirmé mort en HTTP 410), **58 offres nouvelles ajoutées**.

En préalable à cette relance, 3 lignes marquées « x » en colonne Fait (statuts pourvu/refusé/Postulé) traînaient depuis une édition manuelle du tableur non committée ; elles ont été déplacées vers l'onglet Fait avant l'ajout, conformément à la règle habituelle.

Nouveaux slugs ATS qui répondent, à ajouter au dispositif permanent : Ashby `pencil` (PM EMEA full remote, très bon fit), `dash0`, `zip`, `socket`, `mural`, `ironcladhq`. Greenhouse `degreed` (Senior Implementation Consultant UK Remote, éditeur LMS/HR-tech, excellent fit sectoriel). `teramind`, `contentsquare`, `qonto` confirmés productifs sur Lever (déjà notés le 19/08).

> **Leçon méthodologique : ne jamais faire confiance à un UUID Ashby tronqué rapporté par un agent.** Un agent a renvoyé un identifiant partiel (« cfe36a59, 3bd8a6ab, e51e28e4, 4886fd85 ») pour 4 postes Photoroom au lieu de l'URL complète. Complèter soi-même l'UUID par pattern-matching serait fabriquer un lien invalide. Réflexe correct : requêter directement `curl -s "https://api.ashbyhq.com/posting-api/job-board/<entreprise>"` pour récupérer les `jobUrl` complets avant tout ajout au tableur, plutôt que de faire confiance à un extrait de texte d'agent qui a pu tronquer une liste.

| Source | Verdict 21/08/2026 |
|---|---|
| API Ashby (`pencil`, `dash0`, `zip`, `socket`, `mural`, `ironcladhq`, `alan`, `pennylane`, `photoroom`, `constructor`, `vanta`, `docker`) | Toujours la source la plus productive ; plusieurs annonces très fraîches (publiées 20/08) captées le lendemain (Cohere CSM France, Constructor AM DACH, Docker Implementation Engineer EMEA) |
| API Lever (`360learning`, `veeva`, `jobgether` filtré France) | 360Learning a donné 6 postes en un seul appel (Account Manager, 2x Solutions Engineer/Consultant, Solution Expert, Technical Consultant, Solution Deployment Manager) ; Jobgether reste volatil mais toujours rentable une fois filtré |
| API Greenhouse (`customerio`, `chainguard`, `pandadoc`, `cloudbeds`, `canonical`, `gitlab`, `abnormalsecurity`, `degreed`) | Chainguard a donné un Enterprise Sales Engineer **France explicitement remote**, la meilleure offre CSM de la relance |
| API Atlassian | Board de nouveau changé (nouveaux ID 25256, 26057, 26241, 26249, 25170, 25552, 24899, +3 nouveaux 25434/25775/26063) ; confirme qu'il faut le repasser à chaque relance sans exception |
| free-work.com `/jobs/sirh` | Toujours le meilleur rendement côté FR/freelance : 17 offres SIRH nouvelles en un seul passage |
| welcometothejungle.com (via WebSearch) | 6 offres PM/IA nouvelles trouvées (Side, Inqom, RISE, Follow, Mantra, Webmyday), toutes avec télétravail total confirmé dans le texte de l'annonce |
| freelance-informatique.fr, décodage `data-obf` | Vivier confirmé saturé : les 3 pages catégorie de référence n'ont donné aucune URL nouvelle ce jour |
| SD Worx | 1 des 3 liens trouvés (`careers.sdworx.com/jobs/7538308`) était mort (HTTP 410 direct) malgré son apparition en WebSearch ; les 2 autres (dont un via welcometothejungle) sont vivants |
| Vanta (Ashby) | Conflit entre agents : l'un a rapporté 4 postes French Market/French Fluency comme vivants, l'autre les a vérifiés morts (titre générique "Jobs") sauf un DACH différent. Par prudence les 4 douteux n'ont pas été ajoutés, seul le DACH vérifié vivant l'a été. Illustre une fois de plus qu'un résultat WebSearch sur Ashby doit systématiquement être revérifié par fetch direct avant ajout, jamais pris tel quel |

### État des sources — relance du 2026-08-20

Relance menée en 4 recherches parallèles (boards francophones/freelance, API ATS + éditeurs HRIS, boards remote/VC/LinkedIn, IA/PM/métiers de niche) : environ 212 offres candidates compilées, 110 déjà en base, **102 offres nouvelles ajoutées**.

Nouveaux slugs ATS qui répondent, à ajouter au dispositif permanent : Ashby `vanta` (très productif, EMEA/France, GRC/Solutions Engineer francophone), `n8n`, `constructor`, `photoroom`, `fieldguide`, `docker`, `qdrant.tech`, `omni`, `swans`, `americanoperator`. Lever `scality` (Paris, hybride), `veeva`, `brevo`, `360learning`, `loftorbital`. Greenhouse `gitlab`, `canonical`, `grafanalabs`, `abnormalsecurity`, `cloudflare` (déjà connus, toujours productifs). **Lucca a migré d'ATS** : remplacer toute référence `jobs.lever.co/lucca` par `jobs.world.luccasoftware.com/lucca`.

| Source | Verdict 20/08/2026 |
|---|---|
| API Ashby (vanta, n8n, elevenlabs, alan, pennylane, ashby, camunda, dash0, zip, tilla, cohere) | Le meilleur rendement de la relance, comme d'habitude ; `vanta` découvert ce jour est un filon fort (French Market Pre-Sales, Solutions Engineer francophone) |
| API Lever `jobgether` (filtré France) | 14 postes pertinents remontés (PM, CSM, TAM, Data Migration) ; toujours nécessaire de filtrer `categories.location == "France"` pour éviter les doublons pays |
| API Greenhouse `remotecom` | Toujours l'éditeur le mieux aligné : implémentation Workday, PM HRIS/payroll/billing, Solutions Consultant Payroll EMEA |
| API carrières Atlassian | Le board a de nouveau bougé depuis le 19/08 (nouveaux job ID : 25256, 26057, 26241, 26249, 25170, 25552, 24899) — confirme qu'il faut le repasser à chaque relance |
| freelance-informatique.fr, décodage `data-obf` | Toujours fiable ; les 3 pages catégorie de référence ont donné 30 URLs individuelles valides |
| free-work.com `/jobs/sirh`, `/jobs/sap-hcm`, `/jobs/sap-successfactors`, `/jobs/ia` | Toujours très productif en fetch direct (pagination comprise) |
| **free-work.com `/jobs/product-manager`** | **URL cassée** : renvoie un listing générique non filtré (~7500 offres IT hétéroclites) au lieu des offres Product Manager. Utiliser `/jobs/product-owner` à la place (fonctionne, mais dominé par du hors-profil hors SIRH/RH) |
| **cremedelacreme.io** | **Ce n'est pas un board de listing** : le site fonctionne en matching inversé (le client soumet un besoin, reçoit 3 profils sous 48h), aucune page de missions à parcourir. À retirer de la liste des boards à fetcher à chaque relance ; le garder seulement comme profil freelance à tenir à jour |
| **apec.fr** | Confirmé non-fetchable : mur de connexion systématique, même sur les URLs de résultats de recherche |
| **opusresourcing.com** | Rendement nul confirmé une nouvelle fois (aucune offre SAP HCM/SF/Workday/SIRH, seulement du hors-profil) |
| **freelancer.com** | Correctif : `/jobs/sap/` se fetche désormais directement sans blocage (contrairement au verdict du 06/08), simplement aucune offre HR/HCM n'y figurait ce jour |
| mission-freelances.fr/missions/ | De nouveau fonctionnelle (le 404 du 19/08 était temporaire) mais les liens individuels ne se rendent pas via WebFetch (JS) — à retenter en curl brut si besoin |
| **Index Ventures — URLs `indexventures.com/startup-jobs/...`** | Périmées (404), y compris pour des postes Remote.com encore ouverts. Préférer directement l'API Greenhouse `remotecom` |
| collective.work | Le fetch direct de `/jobs` ne filtre plus sur mots-clés (flux générique non filtrable), contrairement à la note du 13/08 — à vérifier via WebSearch ciblé plutôt que fetch direct |
| Owkin (Ashby) | Le poste Senior CSM signalé le 19/08 comme "délisté mais vivant" a définitivement disparu, y compris de la page directe — fermeture confirmée |
| weworkremotely.com, remoterocketship.com | Fetch direct confirmé bloqué (403) une nouvelle fois ; WebSearch reste la seule voie fonctionnelle |
| himalayas.app | Confirmé : usage radar uniquement, jamais d'URL Himalayas comme lien final (redirection silencieuse vers listing général si poste fermé) |
| Decathlon Digital | Faux positif à connaître : un "Product Manager SAP HR" vu sur LinkedIn correspond en réalité à un PM SAP S/4 Supply Chain, pas RH |

### État des sources — relance du 2026-08-19

Relance menée en 4 recherches parallèles (boards francophones/freelance, cabinets de conseil, éditeurs HRIS/partenaires SAP, APIs ATS + boards remote/VC) : 40 offres nouvelles ajoutées sur ~1150 liens déjà en base.

**Cabinets de conseil (Big4/Big3/IT services/HR-spécialisés) : vivier désormais saturé pour ce profil.** Passage en revue des 25 cabinets de la liste CLAUDE.md → 0 offre nouvelle exploitable ; toutes les annonces SIRH/SAP HR trouvées (HR Path, Sia Partners, EY) étaient déjà dans le tableur, et les pistes apparemment neuves (Infosys, Strada, IBM, Mercer, Sopra Steria, Colombus, Ayming) se sont révélées mortes ou hors France au clic. **Ne plus consacrer un cluster de recherche entier à cette catégorie à chaque relance ; un passage ponctuel toutes les 2-3 relances suffit.**

Nouveaux slugs Ashby/Lever/Greenhouse qui répondent, à ajouter au dispositif permanent : `pencil` (Product Manager EMEA remote, excellent fit), `dash0`, `camunda` (Sales Engineer), `zip`, `tilla`, `cohere`, `vibe` (Ashby) ; `teramind`, `contentsquare`, `remofirst`, `qonto`, `aircall` (Lever). `deel` sur Ashby renvoie désormais 0 offre — Deel a changé d'ATS, ne plus s'y fier pour ce board.

| Source | Verdict 19/08/2026 |
|---|---|
| `free-work.com/jobs/sap-successfactors` | Page non fetchée jusqu'ici, très productive (10 missions SuccessFactors LINKWAY/BI Solutions/Tenth Revolution en un seul appel) — ajoutée à la liste standard |
| freelance-informatique.fr, décodage `data-obf` | Toujours fiable ; la page catégorie `mission-sap-hr-461` a donné 19 URLs individuelles dont 5 nouvelles |
| hansonregan.com | Rendement faible en volume mais a produit la meilleure offre de la relance (SAP ECS Client Relationship Manager, remote "Anywhere", 750€/j) |
| API Ashby `alan`, `pennylane` | Confirmés bons filons récurrents : Alan (assurtech FR remote-friendly) a des postes CSM/AM/PM à chaque relance ; Pennylane pareil côté CSM |
| API Atlassian | 5 postes UK remote nouveaux (Senior Principal CSM Strategic, Principal CSM Strategic, Enterprise AM Southern Europe, CSM Mid-Market\|DX, Support AM), non captés le 18/08 malgré une relance déjà axée sur cette API — **repasser dessus vaut le coup même en relance rapprochée**, le board bouge vite |
| API Personio | 429 Too Many Requests — pas de board Ashby/Lever/Greenhouse alternatif identifié |
| SD Worx | careers.sdworx.com et sa page welcometothejungle en 403/410 systématique |
| mission-freelances.fr/missions/ | **404 constaté le 19/08/2026** — la structure du site a changé depuis les relances précédentes qui la donnaient fonctionnelle ; à vérifier avant de la refetcher telle quelle |
| weworkremotely.com | Confirmé bloqué même en `curl` direct avec User-Agent (0 octet retourné) — passer systématiquement par WebSearch |

### État des sources — relance du 2026-08-13

Écarts constatés par rapport au tableau du 07/08 :

| Source | Verdict 13/08/2026 |
|---|---|
| free-work.com `/jobs/sirh` (pages 1 à 3) et `/jobs/sap-hcm` | Confirmé meilleur rendement ; la pagination `?page=2` et `?page=3` fonctionne et rend 16 offres complètes par page |
| `fr.linkedin.com/jobs/hris-emplois` | **La page la plus riche de toute la relance** : ~60 offres avec entreprise, ville et date ; sert de radar pour identifier qui recrute, puis fetcher le site carrière |
| jobs.hr-path.com | La racine `/jobs` ne rend aucune annonce ; passer par `/go/View-all-jobs/5288301/` ou par les missions HR Path listées sur free-work |
| freelance-informatique.fr | `/missions-sirh` et `/missions/sirh` renvoient 404 ; les annonces restent accessibles par WebSearch sur une URL de mission précise |
| actongroup.com | **Le domaine répond à nouveau** (il était ENOTFOUND le 07/08) ; les URLs `/offre/...` sont exploitables |
| careers.alight.com/strada | Postes France (Colombes) accessibles par WebSearch, URLs directes valides |
| jobs.smartrecruiters.com/Arago + careers.flatchr.io | Deux canaux distincts pour les mêmes postes Arago ; les deux fetchables |
| collective.work | **À inclure désormais** : les URLs `/job/<slug>` sont indexées et exploitables (missions SIRH full remote et PMO IA) |
| hansonregan.com | Répond, mais une seule annonce SAP HR ce jour-là (SF LMS, Portugal) |
| eursap.eu/jobs | Deux postes HR seulement, dont un Global SAP HRIS Manager à 145 K€ en Allemagne |
| upwork.com, apec.fr, jobs.sap.com | Aucune offre France exploitable extraite ce jour ; contenu derrière login ou pages de recherche génériques |

> **⚠️ himalayas.app — ne jamais utiliser une URL d'annonce comme lien du tableur (constaté le 14/08/2026).**
> Quand une annonce est fermée, `himalayas.app/companies/<entreprise>/jobs/<slug>` **redirige silencieusement vers le listing général** au lieu de renvoyer une 404. La page paraît valide au fetch, donc un lien mort passe inaperçu à la collecte et ne se révèle qu'au clic. Vérification du 14/08 : **8 des 9 liens Himalayas du tableur étaient morts**, dont un déjà marqué « À postuler ».
> Les pages entreprise `himalayas.app/companies/<entreprise>` restent valides, elles.
> **Méthode à appliquer :** se servir de Himalayas uniquement comme radar pour repérer qui recrute, puis remonter à l'ATS de l'entreprise (Greenhouse, Lever, Ashby) et mettre **cette** URL dans le tableur. Même précaution pour les agrégateurs du même type (startup.jobs, ziprecruiter, jobsora, yubhub) : ils republient des annonces fermées longtemps après.
> Contre-exemple utile : Remote.com publie sur `job-boards.greenhouse.io/remotecom` ; un ID Greenhouse qui redirige vers le board signifie que le poste est fermé.

### État des sources — relance du 2026-08-07

Ce qui a réellement produit des offres exploitables, par ordre de rendement :

| Source | Verdict 07/08/2026 |
|---|---|
| free-work.com `/jobs/sirh` et `/jobs/sap-hcm` | **Meilleur rendement de la relance** ; listings complets avec dates et URLs |
| LinkedIn pages catégories (SuccessFactors Paris, SAP HCM, consultant SIRH, CSM France) | Toujours le meilleur moyen d'identifier **qui recrute** ; pas d'URLs d'annonce, il faut ensuite chercher le site carrière de l'entreprise |
| eursap.eu `/jobs` | ✅ fetch direct, donne titres + réfs + URLs complètes |
| jobs.lever.co et jobs.ashbyhq.com via WebSearch | ✅ postes remote EMEA réels avec URLs directes |
| welcometothejungle.com via WebSearch | ✅ efficace (`welcometothejungle "consultant SIRH" ... 2026`) ; le fetch direct d'une fiche reste en 403 |
| mission-freelances.fr `/missions/` | ✅ liste les missions IA et formateur ; TJM et durée derrière login |
| careers.alight.com/strada + careers.stradaglobal.com | Postes trouvés via WebSearch ; le fetch direct de la page carrière ne rend aucune offre |
| jobs.sephora.com, jobs.cmacgm-group.com, emplois.kpmg.fr, sia-partners.com | ✅ URLs d'annonce directement exploitables |
| eursap.eu, hansonregan.com | hansonregan répond mais n'affichait **aucun poste HR/HCM** ce jour-là |
| opusresourcing.com | Répond, mais **une seule annonce au total** (hors profil) — rendement quasi nul |
| whitehallresources.com | Répond, mais les annonces affichées **datent de janvier 2025** — contenu périmé |
| apply.deloitte.com | « 0 job » avec les filtres SIRH ; passer par LinkedIn (Deloitte publie bien des postes SuccessFactors à La Défense, Lille, Strasbourg) |
| jobs.hr-path.com, jobs.eramet.com, careers.qima.com, careers.soprasteria.fr | Pages **rendues en JS** ou 404 ; passer par WebSearch ou LinkedIn |
| weworkremotely.com, euremotejobs.com, remoterocketship.com | **403 en fetch direct** ; passer par WebSearch |
| himalayas.app | 403 en fetch, mais **bien indexé par WebSearch** — utiliser `himalayas "customer success" Europe remote` |
| boards.greenhouse.io via WebSearch | Remonte des annonces mais souvent **anciennes** ; vérifier chaque lien avant de candidater |
| apec.fr, malt.fr, upwork.com, freelancer.com, jobs.indexventures.com, careers.balderton.com | Aucune offre exploitable extraite ce jour ; contenu derrière login ou pages génériques |
| act-on-group.com | **Domaine injoignable (ENOTFOUND)** — ACT-ON HRIS publie sur LinkedIn, passer par là |

---


### État des sources — relance du 2026-09-07

4 clusters parallèles au format habituel (FR/freelance, ATS+HRIS+USA fusionné, remote/VC EU+niches, Pays Basque). **47 offres candidates compilées, 47 ajoutées** (0 doublon inter-clusters, 0 doublon rejeté par `add_offre.py` : chaque agent avait dédoublonné en amont contre un export à plat des 2410 liens déjà en base, généré une fois avant de lancer les 4 agents et fourni en fichier partagé, méthode déjà adoptée le 05/09). 0 ligne archivée vers Fait (aucune ligne `x`/`Expiré` en attente ce jour). Répartition des ajouts : SIRH +17, CSM +14, IA +2, PM +6, NoRemote +8, Pays Basque +0.

Rendement très déséquilibré, comme d'habitude : le cluster FR/freelance a produit 32 des 47 offres à lui seul (21 par hellowork.com), confirmant que ce board reste la source la plus rentable. Les clusters ATS+HRIS+USA (2 offres sur ~100 slugs interrogés) et Pays Basque (0 offre) confirment la saturation quasi totale déjà documentée les jours précédents ; le cluster remote/VC/niches (13 offres) reste dans la moyenne basse habituelle.

| Source | Verdict 07/09/2026 |
|---|---|
| **hellowork.com** | Toujours la source la plus productive (21 offres retenues sur 91 fiches nouvelles) ; aucun télétravail total confirmé explicitement dans le texte de ces annonces (routées en `Non précisé`, restent en onglet métier conformément à la règle du 18/08) |
| **free-work.com** | 8 offres retenues sur 131 liens de catégories, dont 2 en télétravail 100% confirmé dans le texte (les offres en télétravail partiel identifiées ont été exclues avant même l'insertion) |
| **mission-freelances.fr** | Confirme sa saturation déjà notée le 05/09 : seulement 3 offres retenues après filtrage du bruit marketing/e-commerce habituel |
| **freelance-informatique.fr, eursap.eu, hansonregan.com, redglobal.com, jobs.sap.com, recrutement.cegos.com, silae-career.teamtailor.com, carriere.delaware.pro** | Tous à sec ou entièrement redondants ce jour (le piège de republication Cegos reconfirmé une 5e fois) |
| **jobs.hr-path.com** | 61 postes nouveaux mais tous finance/ABAP technique/administratif, aucun fit fonctionnel — le vivier France pertinent pour ce profil semble épuisé |
| **whitehallresources.com** | Un poste SAP HR/Payroll Consultant trouvé mais disqualifié : Inside IR35 + FCSA Umbrella + résidence UK obligatoire (max 6 mois hors UK sur 5 ans) — même piège que les relances précédentes |
| **API Ashby/Lever/Greenhouse (~100 slugs)** | Rendement quasi nul confirmé, tous les candidats déjà en base ; plusieurs rôles à ancrage pays unique (DACH/Spain/Istanbul/Romania chez 360Learning/Insider/Teramind) écartés à juste titre |
| **API Atlassian** | Toujours mobile et productive : Strategic Solutions Sales Executive ITSM/ESM Southern Europe, France explicitement en Remote, la meilleure offre de toute la relance (⭐⭐⭐⭐⭐) |
| **Creative Force (Malte)** | Nouveau slug/source trouvé via HN Who's Hiring + Remotive : SaaS Product Support Jedi, full remote Europe UTC+1/+2 |
| **Worldly (Ashby)** | Nouveau slug confirmé vivant : CSM Sustainability/Fashion Supply Chains, Remote Europe/UK explicite dans la fiche, bon fit |
| **jobs.stationf.co (Algolia)** | **Piège technique découvert ce jour** : la clé API doit être envoyée dans l'en-tête `X-Algolia-API-Key` **telle qu'affichée en base64 dans le HTML**, pas décodée — décoder la clé produit un 403 "Invalid Application-ID or API key" qui fait croire à tort que la source est morte |
| **AB Tasty** | Publie plusieurs rôles simultanément (Senior KAM Enterprise US, CSM Germany, Solutions Engineer UK) mais aucun n'a d'éligibilité France confirmée ce jour — à revérifier périodiquement plutôt qu'à écarter définitivement |
| **Pays Basque, ensemble des sources habituelles** | **Confirmation d'une saturation quasi totale** : Teréga, Enovis, Intescia/WANAO, 360Learning (Urt), Maïsadour, Arkema, Safran, Dassault Aviation, TotalEnergies Pau, Daher, B.Braun, Euralis, Boardriders, Lindt Oloron, Sanofi Mourenx, Veolia, Toray, Wipro Lauak (structure du site à revérifier, plus de liens `/poste/` extraits en curl simple ce jour) : tous à sec ou déjà en base. Deux nouvelles pistes testées et négatives : `pays-basque-digital.fr` (offres listées toutes expirées) et `emploi-paysbasque.fr` (aucune offre pertinente sur 5611 annoncées) |
| **Boards VC (a16z/Sequoia/Balderton/Atomico), upwork/freelancer, weworkremotely, workingnomads, Weavy** | Rendement nul confirmé une nouvelle fois |

---

### État des sources — relance du 2026-09-08

4 clusters parallèles au format habituel (FR/freelance, ATS+HRIS+USA fusionné, remote/VC EU+niches, Pays Basque). **44 offres candidates compilées, 44 ajoutées** (0 doublon inter-clusters, 0 doublon rejeté par `add_offre.py` : chaque agent avait dédoublonné en amont contre un export à plat des 2456 liens déjà en base, généré une fois avant de lancer les 4 agents). 47 lignes archivées vers Fait (statuts `x`/`Expiré` en attente, dont 26 en Pays Basque). Un passage de `dedoublonnage_20260902.py` après coup a trouvé et fusionné 6 doublons cross-forme supplémentaires, sans rapport avec le lot du jour (mission-freelances.fr et WTTJ déjà présents en double dans le classeur). Répartition des ajouts : SIRH +14, CSM +9, PM +3, USA +2, Pays Basque +2, NoRemote +14, IA +0.

Rendement très déséquilibré une nouvelle fois : le cluster FR/freelance a produit 28 des 44 offres (18 par hellowork.com, 8 par free-work.com), confirmant sa position de source la plus rentable. Les 3 autres clusters (9 ATS/USA, 5 remote/VC/niches, 2 Pays Basque) confirment une saturation quasi totale sur les intitulés cibles.

| Source | Verdict 08/09/2026 |
|---|---|
| **hansonregan.com** | **Correctif d'URL** : `/jobs/` redirige désormais vers `/sap-jobs/` — à utiliser directement lors des prochaines relances |
| **free-work.com, endpoint `?query=<mots-clés>&page=N`** | Rendement quasi nul ce jour (0-2 résultats), contredisant la note du 02/09 qui le donnait très productif — comportement à revérifier, peut-être un changement récent côté site |
| **Jobgether (Lever), piège de republication** | Reconfirmé plusieurs fois : des offres françaises retrouvées via `api.lever.co/v0/postings/jobgether` filtré France se sont révélées être des republications d'offres déjà captées sous l'ATS d'origine (Remote.com GPIS, Canonical Open Source Alliances) — toujours vérifier le contenu avant d'insérer un résultat Jobgether |
| **Ashby `attio`** | Revenu vivant, contrairement à la note du 01/09 qui le donnait mort — ne jamais présumer un slug définitivement fermé, retester périodiquement |
| **Worldly (Ashby)** | Confirme un excellent fit : Account Manager Supply Chain ESG, Remote explicite US/UK/Europe avec la France nommée, la meilleure offre USA de la relance |
| **redglobal.com** | 4 postes nouveaux mais tous disqualifiés à la vérification (ancrage pays unique Allemagne/Inde/Pologne-Suisse malgré le flag `TELECOMMUTE`) — confirme qu'il faut toujours lire le détail du pays, jamais se fier au seul flag |
| **HelloWork, free-work, mission-freelances.fr, freelance-informatique.fr, eursap, intescia, silae, delaware, jobs.hr-path.com, recrutement.cegos.com (piège de republication reconfirmé une 6e fois), apec.fr, malt.fr** | Verdicts habituels reconfirmés (HelloWork et free-work productifs sur leurs catégories ciblées, le reste à sec ou déjà saturé) |
| **Pays Basque, ensemble des sources habituelles** | Quasi totalement à sec (2 offres sur ~130 candidats HelloWork triés) : seule source productive une nouvelle fois. Teréga, Enovis, Intescia, Maïsadour, Wipro Lauak, Arkema, Safran, TotalEnergies Pau, Dassault Aviation, Daher, B.Braun, Euralis, Toray, Lindt, Technoflex, Celsa, Epta, Quiksilver/Boardriders, French Tech Pays Basque, 360Learning Urt : tous confirmés à sec |
| **Boards remote EU (euremotejobs, remotifyeurope, remoterocketship, workingnomads, RemoteOK, Remotive), boards VC (a16z/Sequoia/Balderton/Index), jobs.stationf.co** | Rendement nul à quasi nul confirmé une nouvelle fois ; remoterocketship reste bloqué (403) en curl et WebFetch |

## Relance du 2026-09-09

4 clusters parallèles au format habituel (FR/freelance, ATS+HRIS+USA fusionné, remote/VC EU+niches, Pays Basque). **42 offres candidates compilées, 42 ajoutées** (0 doublon inter-clusters, 0 doublon rejeté par `add_offre.py` : chaque agent avait dédoublonné en amont contre un export à plat des 2496 liens déjà en base, généré une fois avant de lancer les 4 agents). 25 lignes archivées vers Fait (statuts `x`/`Expiré` en attente : 21 SIRH, 2 USA, 2 Pays Basque). Répartition des ajouts : SIRH +3, CSM +12, IA +5, PM +2, USA +3, Pays Basque +4, NoRemote +13.

Rendement en net repli par rapport aux jours précédents (42 offres contre 44 le 08/09 et 47 le 07/09, mais avec un déséquilibre encore plus marqué) : le cluster FR/freelance a produit 32 des 42 offres (20 HelloWork, 7 free-work, 5 mission-freelances.fr), les 3 autres clusters confirmant une saturation quasi totale (4 ATS/HRIS/USA sur ~35 slugs interrogés, 2 remote/VC/niches, 4 Pays Basque). Signe notable : le cluster CSM a bien mordu ce jour grâce à une vague de postes "Solution/Solutions Engineer" chez des ESN et éditeurs de taille moyenne (AssessFirst, Shippeo, Almatech, Vusion, Arrow ECS, GALILEO RH, Darwin Partners), un gisement jusque-là peu exploité.

| Source | Verdict 09/09/2026 |
|---|---|
| **hellowork.com** | Toujours la source la plus productive (20 offres) ; le gisement "Solutions Engineer"/"Solution Engineer" côté ESN françaises (hors éditeurs SaaS classiques) s'est révélé riche ce jour |
| **free-work.com** | 7 offres, endpoint `?query=` toujours peu productif comme noté le 08/09, catégories `/jobs/sirh` et `/jobs/sap-hcm` restent la meilleure entrée |
| **mission-freelances.fr** | 5 nouveautés, dont le filon formateur IA qui continue de produire alors que SIRH/CSM/PM sont saturés |
| **freelance-informatique.fr, eursap.eu, freelance-day.eu** | Entièrement à sec, toutes les pages de référence saturées |
| **hansonregan.com** | Correctif confirmé : `/jobs/` redirige en 301 vers `/sap-jobs/`, fonctionne en non-www ; postes déjà connus |
| **whitehallresources.com / opusresourcing.com** | Nouveaux pièges UK/US reconfirmés (résidence UK sans mention remote, poste Workday pour cabinet d'avocats US hors profil FR) |
| **redglobal.com** | 1 poste SuccessFactors trouvé mais ancré Pologne hybride, écarté |
| **apec.fr** | Toujours inaccessible (200 mais page JS coquille vide) |
| **API Ashby/Lever/Greenhouse (~35 slugs)** | Rendement quasi nul, vivier très saturé ; seul ClickUp (Ashby) a produit une nouveauté (Principal PM, éligibilité internationale à confirmer) |
| **GitLab (Greenhouse)** | Director Customer Success EMEA avec la France explicite, la meilleure offre USA de la relance |
| **Hightouch (Greenhouse)** | Solutions Engineer Enterprise EMEA, bon fit USA |
| **Cabinets de conseil (Deloitte, KPMG, Capgemini, Sopra Steria, Wavestone)** | Deloitte en redirection morte, KPMG 404, Capgemini/Sopra Steria/Wavestone en JS non exploitables sans navigateur ; seul EY a produit une nouveauté (Consultant Gestion de projets Paie) |
| **recrutement.cegos.com** | Piège de republication reconfirmé une nouvelle fois (nouvel ID = doublon déjà connu) |
| **jobs.stationf.co (Algolia)** | Piège technique confirmé : la clé API doit être envoyée telle qu'affichée en base64 dans le header `X-Algolia-API-Key`, jamais décodée, sous peine de faux 403. A produit 2 postes Joko (Lead PM Business Lines + Lead PM AI Platform), full remote France/Espagne |
| **remoterocketship.com** | N'est plus bloqué en 403, mais les mentions "worldwide remote" testées se sont révélées Allemagne-only une fois le détail vérifié ; piège de mention trompeuse reconfirmé |
| **euremotejobs.com, workingnomads.com, weworkremotely.com, remotifyeurope.com, RemoteOK, Remotive, collective.work, cremedelacreme.io, boards VC (Index/Balderton/a16z/Sequoia), upwork/freelancer, wellfound/workatastartup** | Rendement nul confirmé, tout candidat déjà en base ou disqualifié |
| **Pays Basque, ensemble des sources habituelles** | Quasi à sec de nouveau (4 offres via HelloWork/pays-basque-digital.fr) : Chef de Projet SI Bayonne (Crit, ⭐⭐⭐⭐), Business Analyst CSAT Tarnos (Randstad, probable Safran), Formateur Logiciel Lescar, Chargée de compte ELI. Intescia/WANAO, Safran Bordes/Tarnos, Wipro Lauak (43 postes balayés), Dassault Aviation, Arkema, Teréga, TotalEnergies Pau, Enovis, B.Braun, Boardriders, Daher, Euralis, Maïsadour, 360Learning Urt, French Tech Pays Basque : tous confirmés à sec ou hors profil. Nouveau piège noté : un même poste Wipro Lauak réapparaît sous un slug d'URL différent à chaque régénération du site, à traiter comme republication et non comme nouvelle offre |
