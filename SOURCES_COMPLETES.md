# Sources de recherche d'offres — référence complète

Détail exhaustif de toutes les sources testées (verdicts, méthodes de fetch, pièges
techniques), extrait de CLAUDE.md le 25/09/2026 pour alléger le fichier chargé à
chaque démarrage de session (voir CLAUDE.md, section "Où trouver le reste").

**Ce fichier n'est pas lu par les agents de relance** (ils utilisent uniquement
`relance_regles_communes.md` + `relance_sources_<cluster>.md`, qui sont la version
condensée et à jour). Celui-ci sert de mémoire de référence détaillée pour toi (Gaëtan)
et pour la mise à jour ponctuelle des fichiers `relance_sources_*.md` : quand une
source change de comportement, mettre à jour ici ET dans le fichier `relance_sources_*.md`
du cluster concerné.

---

## Sites de recrutement ciblés

| Site | Spécialité |
|------|-----------|
| hansonregan.com | Recrutement SAP & IT, EMEA + monde, CDI + contrats |
| talentlakeit.com | SAP exclusivement, contrats Europe, 42k consultants SAP - contact direct (pas de board public) |
| belsberg.com | RH & HR Tech, Benelux, CDI + missions |
| movementgroup.uk | SAP + HR Tech + Executive, monde, CDI + contrats |
| free-work.com | Missions freelance & CDI IT/SAP, France, board public accessible |
| eursap.eu | N°1 SAP Europe, 21 pays dont France, CDI + contrats, board public, SAP HR/HCM/SF |
| freelance-informatique.fr | Missions freelance SAP/SIRH France, portage salarial, board public |
| **api.francetravail.io** | **API officielle France Travail (ex-Pôle emploi), la meilleure source ajoutée depuis longtemps** — compte développeur créé par Gaëtan le 09/09/2026, identifiants dans `.env` (jamais committé) |
| fr.jooble.org | Agrégateur FR, liens individuels réels (internes ou redirection vers le site source) — ajouté le 09/09/2026, bloqué par Cloudflare en curl, passer par WebFetch |
| fr.jobrapido.com | Agrégateur FR, liens individuels via `open.app.jobrapido.com/fr/<id>` — ajouté le 09/09/2026, bloqué par Cloudflare en curl, passer par WebFetch |
| jobijoba.com | Agrégateur FR gros volume, liens individuels `/fr/annonce/54/<hash>` — ajouté le 09/09/2026, beaucoup de quasi-doublons (même annonce déclinée sur 5-6 villes), prévoir un budget de tri |
| mindtheproduct.com/jobs | Board Product Manager dédié (plateforme Getro), liens `/jobs/listing/<slug>-<hash>/` — ajouté le 09/09/2026, rendement faible pour ce profil (quasi exclusivement US/UK), passage rapide occasionnel suffit |

> **API France Travail — méthode complète (testée et opérationnelle le 09/09/2026).** Compte développeur créé sur francetravail.io, application "Recherche emploi personnelle" abonnée à l'API "Offres d'emploi v2". Identifiants stockés dans `.env` à la racine du projet (`FRANCE_TRAVAIL_CLIENT_ID`, `FRANCE_TRAVAIL_CLIENT_SECRET`), fichier listé dans `.gitignore`, **ne jamais le committer**.
> ```bash
> # 1. Obtenir un token OAuth2 (durée de vie ~1500s)
> curl -s -X POST "https://entreprise.francetravail.fr/connexion/oauth2/access_token?realm=%2Fpartenaire" \
>   -d "grant_type=client_credentials&client_id=${FRANCE_TRAVAIL_CLIENT_ID}&client_secret=${FRANCE_TRAVAIL_CLIENT_SECRET}&scope=api_offresdemploiv2 o2dsoffre"
> # 2. Rechercher (motsCles, sort=1 pour trier par date)
> curl -s -G "https://api.francetravail.io/partenaire/offresdemploi/v2/offres/search" \
>   -H "Authorization: Bearer <token>" --data-urlencode "motsCles=consultant SIRH"
> ```
> Réponse JSON riche par offre : `intitule`, `entreprise.nom`, `lieuTravail.libelle`, `typeContratLibelle`, `salaire.libelle` (montant exact souvent présent), `dateCreation`, `romeLibelle`, et surtout **`origineOffre.urlOrigine`** qui est le lien individuel stable à utiliser comme `Lien` (`https://candidat.francetravail.fr/offres/recherche/detail/<id>`, jamais une page catégorie). **Pas de champ dédié pour le télétravail** : à déduire du texte de `description` (regex sur "télétravail", "hybride", "100% remote"...), comme pour les autres sources.
> **Piège HTTP** : une recherche sans résultat renvoie **204 No Content** (corps vide), pas un tableau JSON vide — un parsing JSON naïf lève une exception sur ce cas, il faut le traiter comme "0 résultat" et non comme une erreur.
> Premier balayage complet le 09/09/2026 sur 13 mots-clés : 236 offres uniques brutes, 114 retenues après filtre métier + dédoublonnage. Très bon rendement sur SIRH/AMOA/SAP et Product Manager, correct sur Customer Success, faible sur Technical Account Manager (peu d'offres françaises portent cet intitulé littéral sur France Travail).
>
> **Piège de dédoublonnage propre à l'intégration multi-sources du 09/09/2026, à généraliser** : une même offre réelle peut être republiée sur France Travail, Jooble, Jobrapido et le site de l'employeur avec quatre URLs différentes (ex. "Consultant technico-fonctionnel HR Access" chez HR DNA, vu à la fois via free-work.com et via France Travail). Le dédoublonnage habituel d'`add_offre.py` ne compare que l'URL exacte, donc ce cas lui échappe. Lors de cette intégration, un dédoublonnage supplémentaire par **paire (entreprise, poste) normalisée** (minuscule, sans `H/F`/`F/H`, ponctuation retirée) a été fait en amont de l'insertion et a écarté 25 doublons de ce type. À refaire à la main (ou scripter) à chaque fois que plusieurs agrégateurs sont interrogés dans la même relance.
>
> **Monster et Indeed sont inexploitables en fetch direct (testé le 09/09/2026), y compris via les agrégateurs ci-dessus.** Monster.fr / monster.com/fr : les URLs de recherche redirigent en 301 mort vers la page d'accueil, qui répond elle-même 403. Indeed (fr.indeed.com) : 403 "Security Check" systématique en curl ET en WebFetch, seul WebSearch `site:fr.indeed.com` reste utilisable en radar. Sur les échantillons testés (Jooble, Jobrapido, Jobijoba), aucun des trois n'a republié de fiche Indeed ou Monster identifiable ; ils restent malgré tout de bons agrégateurs indépendants (liens individuels réels, pas des pages catégorie), donc gardés au dispositif pour leur propre contenu. Cadreo et RegionsJob redirigent en 301 vers HelloWork (déjà couvert, aucune valeur propre) ; Optioncarriere est bloqué par un challenge Cloudflare Turnstile ; Careerjet.fr a un certificat SSL expiré ; StepStone et Keljob sont injoignables (timeout / connexion refusée) ; Trovit.fr n'a plus de volet emploi identifiable en France. À retester périodiquement, ces blocages techniques peuvent se lever.

> **⚠️ RÈGLE ABSOLUE — ne jamais mettre une URL de page catégorie dans la colonne Lien.** Erreur constatée à plusieurs reprises (dernière fois le 19/08/2026, 25 lignes fautives corrigées d'un coup) : une page catégorie (plusieurs missions listées, ex. `mission-sap-hr-461`, `mission-sirh-2293`, `mission-consultant-sap-hcm-n14525`, `chef-de-projet-sirh-freelance-n112`, `cv-mission-*-fNNNNN`) est collée comme lien pour une offre précise, alors qu'elle mène en réalité à une liste qui change dans le temps — cliquable, donc jamais détectée comme lien mort, mais fausse. **Signe qui doit alerter avant tout ajout : une URL freelance-informatique.fr valide pour une offre individuelle est TOUJOURS de la forme `mission-<titre>-<5 à 7 chiffres>-de` (nouveau schéma) ou `mission-<titre>-<YYMMDD><lettre><NNN>` (ancien schéma, ex. `260507I001`). Si l'URL n'a pas cette forme (elle finit par `-n<chiffres>`, `-e<chiffres>`, `-freelance-n<chiffres>`, ou commence par `cv-mission-`), c'est une page catégorie : il faut décoder les `data-obf` (méthode ci-dessous) pour trouver l'URL individuelle correspondante avant d'ajouter la ligne, jamais copier l'URL de la catégorie telle quelle.**
>
> **Astuce freelance-informatique.fr — décodage des liens `data-obf` (trouvée le 19/08/2026).** Les pages catégorie (ex. `mission-consultant-sap-hcm-n14525`, `mission-sap-hr-hcm-925`, `mission-consultant-sap-successfactors-n16465`, `chef-de-projet-sirh-freelance-n112`) affichent plusieurs missions dans un carrousel, mais les liens "Voir la mission" n'ont pas de `href` classique : `curl` et WebFetch ne remontent que le texte, jamais l'URL. L'URL réelle est encodée en base64 dans un attribut `data-obf` sur le `<span>`, décodé en JS au clic. Un simple `curl` suffit pour la récupérer, sans navigateur :
> ```python
> import re, base64
> html = requests.get(url, headers={"User-Agent": "Mozilla/5.0 ..."}).text
> for m in re.findall(r'data-obf="([^"]+)"[^>]*>Voir la mission', html):
>     print("https://www.freelance-informatique.fr" + base64.b64decode(m).decode())
> ```
> Chaque page catégorie liste 9 à 20 missions avec doublons entre catégories proches (SAP HCM / SAP HR-HCM se recoupent beaucoup). Les pages missions individuelles (`mission-<titre>-<id>-de`) n'ont pas de JSON-LD `JobPosting` ; titre, ville et durée se lisent dans la balise `<meta name="description">`, et un `(Télétravail)` dans `twitter:title`/`og:title` est le seul signal fiable de télétravail confirmé (sinon "non précisé", reste dans l'onglet métier par défaut). Le client est presque toujours anonymisé ("N/C").
>
> **Vérification systématique à chaque relance (demandée par Gaëtan le 19/08/2026) :** décoder ces pages catégorie avec la méthode `data-obf` ci-dessus et vérifier que chacune des missions individuelles qu'elles listent est bien présente dans `offres_emploi.xlsx` (n'importe quel onglet) :
> - `https://www.freelance-informatique.fr/chef-de-projet-sirh-freelance-n112`
> - `https://www.freelance-informatique.fr/categorie-modules-sap-hr-238` (trouvée le 19/08/2026 via le sitemap `sitemap_index_thematiques.xml` ; page profils freelances SAP HR, mais contient aussi un widget "missions récentes" avec des liens `data-obf` exploitables)
> - `https://www.freelance-informatique.fr/categorie-progiciels-sirh-222` (même sitemap, même mécanisme, widget missions SIRH)
>
> Ces pages sont explicitement citées par Gaëtan comme référence à recontrôler à chaque fois, pas seulement lors d'une relance générale — donc même sur une demande ponctuelle qui ne mentionne pas freelance-informatique.fr. Ajouter les missions manquantes ; si tout est déjà connu, le dire simplement sans rien ajouter.
>
> **Pour découvrir d'autres pages catégorie du même type** (au cas où le site en ajoute), le sitemap `https://www.freelance-informatique.fr/sitemaps/sitemap_index_thematiques.xml` liste les pages `categorie-*` ; celles pertinentes se repèrent par leur `<title>` ("Freelances SAP HR", "Freelances SIRH"...), pas par leur slug seul. Les sitemaps `sitemap_index_metiers.xml` (pages `job-*`) et `sitemap_index_technologies_missions.xml` (pages `mission-<techno>-<id>` type `mission-sap-hr-461`, `mission-sirh-2293`) sont les deux autres sources de pages catégorie à connaître.
| malt.fr | Plateforme freelance FR - profil actif : https://www.malt.fr/profile/gf1 |
| geojobs.ai | Board dédié GEO/AI-search — ajouté le 11/09/2026, confirmé productif dès le premier test (1 mission GEO/AEO pure retenue sur 9 examinées, ELIA Atelier) ; le reste des postes indexés est Allemagne/UK on-site ou hybride pur — à repasser à chaque relance SEO/GEO |
| whitehallresources.com | SAP recrutement UK/Europe (dont France), SAP SF + SAP HR, CDI + contrats, board public |
| opusresourcing.com | Spécialiste HCM (SAP SF, SAP HCM, Workday), UK/Europe dont France/Espagne/Italie |
| apec.fr | CDI cadres France, utile pour CSM et postes seniors |
| deel.com/careers | Plateforme RH/paie globale (HRIS tout-en-un, 150+ pays) — postes CSM, Solutions Consultant HRIS, Implementation Consultant, remote — board JS-rendu, passer par jobs.ashbyhq.com/deel ou builtin.com/company/deel/jobs |
| lehibou.com | N°1 freelance IT/Tech grands comptes France (CAC40 + ETI), 140k consultants, missions avg 18 mois — SAP HR, SIRH, chef de projet — site direct bloqué (403), chercher via free-work.com/fr/companies/lehibou/jobs ou WebSearch "lehibou.com mission SIRH" |
| comet.co | Plateforme freelance tech France (50k+ freelances certifiés), Paris/Lyon/Lille/Nantes — missions SIRH, AMOA, SAP — site nécessite auth, chercher via free-work.com/fr/tech-it/jobs/sirh (missions Comet bien référencées) |
| ergalis.com / up-skills.fr | Groupe Actual — Ergalis (recrutement IT/RH) + Up Skills (cadres & experts) — CDI Chef/Directeur de Projet SIRH, postes publiés sur welcometothejungle.com/fr/companies/ergalis/jobs |
| njoyn.com | ATS propriétaire CGI — "Invalid request" en fetch direct (27/07/2026) — utiliser WebSearch `CGI "consultant SIRH" OR "SAP HCM" France emploi 2026` ou welcometothejungle.com/fr/companies/cgi/jobs |
| glassdoor.fr | Board généraliste FR + avis salariés — données salariales réelles utiles pour cibler les prétentions ; offres CSM, Account Manager, SAP (bloquer scraping direct, passer par WebSearch "glassdoor.fr actuaire CSM" ou glassdoor.com/Job/france-...) |
| hellowork.com | **Source majeure, révisée le 01/09/2026 (3e passage) — l'ancien verdict « rendement quasi nul » est périmé.** Trois familles d'URL se fetchent en curl + UA navigateur et rendent les liens individuels `/fr-fr/emplois/NNNN.html` en clair : (1) **recherche par mots-clés** `hellowork.com/fr-fr/emploi/recherche.html?k=<mots-clés>&st=date&c=CDI` — 30 offres par requête, a donné 27 offres sur les seules requêtes « consultant SIRH » et « customer success manager » ; (2) **page métier + ville** `emploi/metier_<intitulé>-ville_<ville>-<CP>.html` — le vrai gisement du cluster Pays Basque ; (3) **page domaine + ville** `emploi/domaine_<domaine>-ville_<ville>-<CP>.html`. Chaque fiche porte un **JSON-LD `JobPosting` complet** (titre, entreprise, ville, `datePosted`, `validThrough`, `baseSalary`) : un seul curl par offre suffit à tout extraire et à prouver la vivacité (~3 fiches sur 30 n'en ont pas, le `<title>` sert alors de repli). Slugs `metier_` qui répondent : `chef-de-projet`, `chef-de-projet-informatique`, `chef-de-projet-si`, `chef-de-projet-erp`, `business-analyst`, `consultant-sirh`, `consultant-fonctionnel`, `formateur`, `account-manager`, `data-analyst`, `product-manager`. En 404 : `customer-success-manager`, `product-owner`, `amoa`, `responsable-de-projet`. Seuls `domaine_` valides : `informatique`, `commerce`, `industrie`, `graphisme`, `recherche`, `telecom` (pas de `rh`, `direction_management`, `commercial`). Bonus : HelloWork republie les postes Safran de Bordes et Tarnos, ce qui **contourne le Cloudflare de safran-group.com** |
| welcometothejungle.com | N°1 FR + EU, meilleur board pour remote/senior — filtres remote, contrat, niveau — URL : app.welcometothejungle.com/jobs?remoteOnly=true — rechercher "customer success manager", "consultant SIRH", "formateur IA" |
| collective.work | Plateforme freelance senior tech FR — missions SIRH, data, consulting. **Testé pour la première fois le 23/09/2026 : rendement nul en pratique.** La page d'accueil et les pages de listing/recherche (`/jobs`, `/jobs/fr/sirh`, `/search?q=`) sont bloquées par un challenge Cloudflare Turnstile (page "Just a moment...", même en HTTP 200), donc aucune découverte systématique de mission possible. Seules les pages de mission individuelles (`/job/<slug>` ou `/jobs/fr/<slug>`) se fetchent directement en curl + UA navigateur, mais uniquement si l'URL est déjà connue (via WebSearch `site:collective.work`). Les 2 seules missions SIRH/SAP trouvées ainsi (`success-factor-and-core-hr-sap-jkxz`, `gestionnaire-paie-sap-hf-gsb2`) étaient toutes deux expirées (`expirationDate` passée) et republiées d'ailleurs (`"source":"FREE_WORK"`, entreprises Comet et HR Path, déjà couvertes par free-work.com et jobs.hr-path.com dans le dispositif) — le JSON `__NEXT_DATA__` de chaque fiche individuelle expose ce champ `source` et un `company.name`, utile pour repérer une republication. **Ne pas retester en systématique tant que le blocage Cloudflare des pages de listing persiste ; à revérifier ponctuellement (le blocage peut se lever comme pour d'autres sites du dispositif).** |
| cremedelacreme.io | Freelance senior tech FR — TJM affiché, missions curated — missions SIRH, consulting |
| wellfound.com | Startups monde, filtres remote + salaire — ex-AngelList ; rechercher "customer success" remote |
| workatastartup.com | Y Combinator — énorme volume startups, filtres remote + data — rechercher "customer success" ou "HRIS" |
| ai-jobs.net | ~~Board spécialisé IA/ML~~ — **peu utile pour ce profil** : contenu dev/data pur (MLOps, RAG, Python), aucun poste formateur IA non-technique trouvé (27-28/07/2026) — ne pas inclure dans les relances |
| remoteok.com | Board remote monde — US-centré (28/07/2026) — peu utile pour les relances FR/SIRH, mais **à inclure pour la recherche USA** (voir section « Recherche USA »), en filtrant sur le remote ouvert à l'international |
| weworkremotely.com | Board remote monde — rechercher "customer success" — URL : weworkremotely.com/categories/remote-customer-success-jobs |
| remotive.com | Board remote monde — US-centré (28/07/2026) — peu utile pour les relances FR/SIRH, mais **à inclure pour la recherche USA** (voir section « Recherche USA »), en filtrant sur le remote ouvert à l'international |
| euremotejobs.com | Board remote EU — rechercher "customer success" ou "HRIS" — **403 en WebFetch, mais un `curl` avec User-Agent navigateur passe et rend le HTML complet avec les liens ATS d'origine (Lever/Greenhouse/SmartRecruiters)** (trouvé le 30/08/2026) ; a produit Tenable et Upsun (France remote confirmés) en un seul passage — désormais à fetcher en curl direct à chaque relance plutôt qu'à écarter |
| himalayas.app | Remote world — salaire souvent affiché — rechercher "customer success manager" ou "HRIS" — **403 en fetch direct le 05-06/08/2026**, passer par WebSearch |
| redglobal.com | **RED Global — confirmé productif dès le premier test (01/09/2026), à repasser à chaque relance** : `curl` direct sur `/jobs` rend ~10 postes avec slugs individuels `/jobs/job/<slug>/<id>` et JSON-LD `JobPosting` complet par fiche. Le paramètre `?search=` est ignoré (listing unique non filtrable). A produit un SAP SuccessFactors Project Manager mainly remote ⭐⭐⭐⭐⭐ |
| ignitesap.com | ~~IgniteSAP~~ — **pas de board public** (01/09/2026) : `/jobs` en 404, `/recruitment-jobs/` ne liste que les postes internes de recruteurs Ignite — ne plus tester |
| amoriabond.com / computerfutures.com / emagine.org | Rendement quasi nul (01/09/2026) : Amoria Bond a un board `/jobs/` mais recherche JS non filtrable et 0 SAP HR ce jour ; Computer Futures en 403 — **les missions SThree France se captent via free-work et mission-freelances** ; Emagine est une SPA JS sans URL d'offre dans le sitemap — passage très rapide ou skip |
| cadremploi.fr | **Inutilisable** (01/09/2026) : 403 en curl ET WebFetch, WebSearch `site:cadremploi.fr` ne remonte rien — ne plus tester |
| jobs.sap.com | SAP lui-même — **confirmé le 01/09/2026 : fetch direct curl de `jobs.sap.com/go/SAP-Jobs-in-France/850401/` rend 17 postes France avec URLs individuelles en clair** (Client Delivery Manager, Solution Advisor, Concur...) — à repasser à chaque relance |
| api.adzuna.com | API gratuite agrégeant les boards FR — nécessite une clé (app_id + app_key sur developer.adzuna.com) ; le site adzuna.fr est en 403 systématique (01/09/2026), donc **inutilisable tant que la clé n'est pas créée par Gaëtan** |
| jobs.stationf.co | **Très bon filon, à ajouter au dispositif permanent (01/09/2026)** : board WelcomeKit rendu JS, mais **index Algolia public interrogeable en curl** — app `CSEKHVMS53`, index `wk_cms_jobs_production_careers`, clé API dans le HTML de `/search` (`<input id="algolia_api_key">`). 538 offres, ~44 pertinentes. Piège : les slugs d'org diffèrent des noms affichés (Tomorro=`airflow`, Joko=`joko-1`, Dastra=`dastra-1`, Zola=`zola-learning-sas`). Quasi tout est Paris hybride → NoRemote |
| freelance-day.eu | Homepage fetchable en curl (~6 missions `/mission/<slug>/` avec Remote OUI/NON, durée, régie en clair) mais `/missions/` est JS — passage rapide homepage seulement (01/09/2026) |
| recrutement.cegos.com | **Nouveau filon formateur IA, trouvé le 01/09/2026 (3e passage)** : ATS Teamtailor, `/jobs` fetchable en curl (16 offres en clair) et **flux `/jobs.rss` disponible**. Cegos ouvre régulièrement des vacations de consultant-formateur IA. **Piège** : Cegos republie la même offre sous un nouvel ID (« Consultant formateur en IA au service des marchés publics » existe sous `7672957` en base et sous `7756416` sur le site) — dédoublonner sur titre + entreprise, jamais sur l'ID seul |
| intescia.recruitee.com | **Nouveau filon Pays Basque, trouvé le 01/09/2026 (3e passage)** : `intescia.recruitee.com/api/offers/` rend 21 postes en JSON avec ville, télétravail et date. Groupe SaaS de business intelligence dont la filiale **WANAO est basée à Bidart** ; 3 postes locaux d'un coup, dont un « Formateur Customer Success Management ». **Le seul éditeur SaaS du bassin qui recrute régulièrement sur les intitulés cibles** — à ajouter au dispositif permanent Pays Basque |
| workdispo.com / freelanceradar.co / mission-freelance.com | Repérés le 01/09/2026 : workdispo expose des fiches fetchables en curl (TJM, télétravail, date en clair) mais la mission testée était expirée ; freelanceradar a des pages catégorie fetchables **sans aucun lien de mission individuelle dans le HTML** (listing JS, radar seulement). Noter que `mission-freelance.com` est un site distinct de `mission-freelances.fr` |

### Boards remote évalués le 06/08/2026 — liste des 27 plateformes

Liste soumise par Gaëtan. Verdict après test de chacune : la plupart sont des agrégateurs qui republient WeWorkRemotely, RemoteOK ou Greenhouse, déjà couverts en amont. Ne pas toutes les repasser en revue à chaque relance ; se limiter à celles marquées « à inclure » ou « à retenter » ci-dessous.

> **Rappel de critère (06/08/2026) :** le **TJM n'est pas un critère de filtrage**. Gaëtan prend n'importe quel TJM. Ne jamais écarter une plateforme, une mission ou une offre au motif que la rémunération est basse ou inférieure aux fourchettes cibles. Les fourchettes de la section « Attentes salariales » servent à préparer la négociation, pas à trier les offres.

| Site | Verdict 06/08/2026 |
|------|-------------------|
| remotees.com | **Redirige (301) vers weworkremotely.com** — pur alias, aucun contenu propre |
| europeremotely.com | HTTP 439, fetch bloqué |
| nodesk.co | HTTP 403 |
| justremote.co | Pages catégories JS sans offres ; « Power Search » derrière paywall |
| jobspresso.co | 404 sur les URLs catégories |
| remote4me.com | 404 |
| pangian.com | 404 sur la page emplois ; offres indexées datant de 2019-2023 |
| remotehabits.com | Offres indexées **obsolètes (2019-2023)**, niveaux junior, salaires en GBP 22-25k |
| remotecrew.io | Aucun résultat indexé |
| skipthedrive.com | 404 (attention : la liste indiquait `skipthechive.com`, domaine erroné) |
| remote.co | Timeout en fetch |
| workingnomads.com | **À retenter** — pages Europe existent (`/remote-customer-success-jobs-europe`) mais rendues en JS ; passer par WebSearch |
| remoteok.io/europe, remoteok.io/asia | Alias de remoteok.com, déjà classé US-centré |
| flexjobs.com | **Abonnement payant**, contenu inaccessible |
| toptal.com | Réseau de talents sur cooptation, pas un board ; process d'admission long |
| upwork.com | **À inclure dans les relances** — missions SAP SuccessFactors et formation IA réellement présentes ; fetch direct en 403, passer par WebSearch `upwork.com "SAP SuccessFactors" OR "AI trainer" consultant project 2026` |
| freelancer.com | **À inclure dans les relances** — volume SAP faible mais des gigs de formation SuccessFactors apparaissent ; fetch direct fonctionne sur `/jobs/sap/` |
| outsourcely.com | Domaine injoignable (ENOTFOUND) le 06/08/2026 |
| simplyhired.com, virtualvocations.com | **US uniquement** |
| angel.co | Ancien domaine d'AngelList, redirige vers wellfound.com (déjà couvert) |
| linkedin.com | Déjà couvert ; voir la méthode LinkedIn plus bas |
| remotive.com, weworkremotely.com, remoteok.com | Déjà présents dans le tableau ci-dessus |

**Sous-produit utile de cette évaluation** — deux boards Europe non listés par Gaëtan sont remontés plusieurs fois et méritent un test ciblé :

| Site | Note |
|------|------|
| remoterocketship.com | **À retenter** — pages Europe filtrées par métier et séniorité (`/country/europe/jobs/senior-customer-success/`) ; 403 en fetch direct, passer par WebSearch |
| remotifyeurope.com | **À retenter** — board remote EU par catégorie ; 403 en fetch direct, passer par WebSearch |

### ATS directs (à interroger via WebSearch ou fetch direct)
| ATS | URL / méthode | Ce qu'on cherche |
|-----|--------------|-----------------|
| AshbyHQ | jobs.ashbyhq.com — WebSearch `site:jobs.ashbyhq.com "customer success" remote` | Scale-ups modernes : Owkin, ElevenLabs, Plain, Vibe... |

> **Astuce Ashby — API publique (trouvée le 14/08/2026).** Les pages `jobs.ashbyhq.com/<entreprise>/<uuid>` sont rendues en JS : un fetch ne rend que le titre. Passer par l'API publique, qui renvoie en JSON **tous les postes ouverts avec leur description complète, la localisation et l'URL** :
> ```bash
> curl -s "https://api.ashbyhq.com/posting-api/job-board/<entreprise>?includeCompensation=true"
> ```
> Le `<entreprise>` est le segment de l'URL du board (ex. `constructor`, `elevenlabs`, `n8n`). C'est le moyen le plus fiable de vérifier qu'un poste est **encore ouvert** et de lire les prérequis sans navigateur.
>
> **⚠️ Correctif du 19/08/2026 : un poste absent du JSON n'est PAS forcément fermé.** Ashby permet de rendre un poste "non listé" sur le board public (retiré du JSON de l'API) tout en le laissant parfaitement candidatable via son lien direct. Cas réel : `jobs.ashbyhq.com/owkin/a2332329-a5da-4bc3-a6eb-ea8bbc49e637` (Senior CSM, excellent fit) absent de l'API le 19/08 mais toujours vivant avec bouton "Apply" actif au fetch direct de la page. Repéré 4 fois par des relances précédentes puis marqué Expiré à tort lors d'un nettoyage automatique basé sur l'API seule. **Pour vérifier la fermeture réelle d'un lien Ashby déjà dans le tableur, ne jamais se fier à l'absence dans l'API : fetcher l'URL directement.** Deux signaux fiables au fetch direct (curl suffit, pas besoin de navigateur) :
> - Balise `<title>` générique `"Jobs"` (pas de nom de poste) → réellement fermé.
> - Balise `<title>` avec le nom du poste (ex. `"Senior Customer Success Manager @ Owkin"`) → poste vivant, même si absent du JSON de l'API.
>
> L'API Ashby reste fiable pour découvrir de **nouveaux** postes (elle ne peut évidemment lister que ce qu'elle contient) ; c'est seulement comme preuve de fermeture d'un lien existant qu'elle ne suffit pas.
| Lever | jobs.lever.co — WebSearch `site:jobs.lever.co "customer success manager" remote France` | Qonto, Aircall, autres scale-ups FR |

> **Astuce Lever — API publique (trouvée le 14/08/2026).** Même logique que l'API Ashby :
> ```bash
> curl -s "https://api.lever.co/v0/postings/<entreprise>?mode=json"
> ```
> Renvoie tous les postes ouverts en JSON avec `text` (titre), `categories.location`, `workplaceType` (`remote` / `hybrid` / `onsite`) et `hostedUrl`. Un slug inconnu renvoie `{"ok":false,"error":"Document not found"}`, ce qui permet aussi de tester rapidement le bon nom de board.
> **Attention Jobgether** : ce board republie la même offre dupliquée par pays (jusqu'à neuf lignes pour un seul poste). Filtrer sur la variante France avant d'ajouter au tableur, sinon le tableur se remplit de doublons.
>
> **⚠️ Correctif du 19/08/2026 : le listing Jobgether est volatil, son absence à un instant T ne prouve pas la fermeture.** Avec ~4500 postes et une pagination/rotation qui change d'un appel à l'autre, un poste peut disparaître d'un appel API puis réapparaître dans un appel ultérieur le même jour sans avoir jamais été fermé côté employeur. 14 offres Jobgether (+1 Vendavo) ont ainsi été marquées Expiré à tort le 19/08 avant d'être restaurées. Pour vérifier la fermeture réelle d'un lien Lever déjà dans le tableur, fetcher l'URL directement plutôt que de recroiser avec l'API : un lien mort renvoie une page dont le `<title>` est `"Not found – 404 error"` ; un lien vivant contient le texte "Apply for this job" et le titre réel du poste.
| Greenhouse | boards.greenhouse.io — WebSearch `site:boards.greenhouse.io "customer success" remote France` | Typeform, autres |
| Atlassian (iCIMS) | `curl -s "https://www.atlassian.com/endpoint/careers/listings"` | CSM Principal / Senior Principal France, Solutions Engineer, Customer Success Architect |

> **Astuce Atlassian — API carrières publique (trouvée le 17/08/2026).** Atlassian publie sur iCIMS, donc rien de ce qu'il ouvre n'apparaît sur Ashby, Lever ou Greenhouse ; c'est ce qui a fait manquer ses postes lors de la relance du 17/08. Un seul appel rend les 271 postes ouverts en JSON :
> ```bash
> curl -s "https://www.atlassian.com/endpoint/careers/listings"
> ```
> Chaque entrée porte `title`, `locations` (liste, avec les zones remote autorisées du type `Remote - France`), `category`, `overview` et `portalJobPost.portalUrl` (le lien iCIMS à mettre dans le tableur). Filtrer sur `Remote - France` dans `locations` remonte directement les postes ouverts depuis la France. **À inclure dans chaque relance** : Atlassian tient en permanence des postes CSM Strategic France et Solutions Engineer EMEA.
>
> **Leçon plus générale :** les gros éditeurs sur ATS propriétaire (iCIMS, Workday, SmartRecruiters, SuccessFactors) échappent entièrement aux recherches `site:jobs.ashbyhq.com` / `site:jobs.lever.co` / `site:boards.greenhouse.io`. Chercher leur page carrière ou leur API dédiée, jamais s'en remettre aux seuls ATS de scale-ups.

### Boards VC (portfolio startups bien financées)

> **Note (27/07/2026) :** jobs.indexventures.com (erreur TLS), careers.balderton.com, jobs.a16z.com, jobs.sequoiacap.com — tous en pages JS sans contenu scrappable. Utiliser WebSearch : `site:jobs.indexventures.com "customer success"`, etc.

| VC | URL / méthode | Ce qu'on cherche |
|----|-----|-----------------|
| Index Ventures | WebSearch `site:jobs.indexventures.com "customer success" OR HRIS remote` | CSM, HRIS, remote startups portfolio |
| Balderton | WebSearch `site:careers.balderton.com "customer success" OR consultant remote EU` | CSM, consultant, remote EU |
| Atomico | atomico.com/careers-at-portfolio | CSM, HRIS, remote EU |
| a16z | WebSearch `site:jobs.a16z.com "customer success" remote` | CSM senior, remote world |
| Sequoia | WebSearch `site:jobs.sequoiacap.com "customer success" OR HRIS` | CSM, HRIS, startups |
| Ribbit (fintech) | ribbitcap.com/companies | CSM fintech/HRIS — **testé le 23/09/2026 : pas de board carrières ni de page "companies" avec offres exploitable, uniquement des articles sur le fonds et son portefeuille (Affirm, Brex, Coinbase, Nubank, Revolut, Robinhood...). Pour toucher ce portefeuille, il faudrait tester les ATS de chaque société individuellement (déjà fait pour certaines par ailleurs), pas Ribbit lui-même — rendement nul confirmé, ne pas retester en tant que source directe** |

---

## Cabinets de conseil - Pages carrière directes

À fetcher directement lors de chaque relance de recherche. Postes ciblés : **Consultant SIRH / SAP HCM / SuccessFactors**, **Chef de projet SIRH**, **AMOA**, **Pre-sales / Solution Advisor HR Tech**, **CSM Enterprise**, **Formateur IA / Consultant IA**.

### Big 4 (audit + conseil)
| Cabinet | URL carrière | Ce qu'on cherche |
|---------|-------------|-----------------|
| Deloitte | `https://apply.deloitte.com/careers/SearchJobs/?3_56_3=300060` | Consultant SIRH, SAP HCM, Chef de projet RH, Formateur IA — **testé le 23/09/2026 : URL redirige vers une page d'accueil générique US, aucun résultat de recherche exploitable en fetch direct.** WebSearch confirme un poste réel "HR Transformation Consultant - SAP SuccessFactors (F/H)" à Saint-Ouen-l'Aumône, mais sans lien direct vérifiable — passer par WebSearch ponctuellement, pas de méthode fiable trouvée |
| PwC | WebSearch `"PwC" consultant SAP HR OR SIRH OR AMOA France emploi 2026` — URL 403, aucun poste France identifié (27-28/07/2026) — relancer ponctuellement | Consultant SAP HR, AMOA SIRH, transformation RH |
| EY | `https://careers.ey.com/ey/search/?q=SIRH+SAP&locationsearch=France` | Consultant SAP SuccessFactors, SAP HCM, AMOA |
| KPMG | **URL corrigée le 23/09/2026 : `https://emplois.kpmg.fr/`** (l'ancienne URL `kpmg.com/fr/fr/...` est en 404). Testé le 23/09/2026 : page JS non exploitable en fetch direct (SPA sans contenu texte). Un poste "Manager Consultant SIRH F/H" repéré via WebSearch/LinkedIn le même jour était déjà expiré (`trk=expired_jd_redirect`) | Consultant SIRH, SAP RH, transformation digitale RH |

### Big 3 (stratégie)
| Cabinet | URL carrière | Ce qu'on cherche |
|---------|-------------|-----------------|
| McKinsey | `https://www.mckinsey.com/fr/careers` | Expert RH / People Analytics / transformation digitale — **testé le 23/09/2026 : connexion échoue en curl (timeout), WebSearch ne remonte que des publications de recherche (HR Monitor 2026) et la page carrières générique, aucun poste concret identifiable — rendement nul confirmé, ne pas relancer souvent** |
| BCG | WebSearch — URL 404, postes génériques non extractibles (27-28/07/2026) — **relancer peu utile**, profil trop junior ciblé | Consultant transformation RH, digital HR |
| Bain | WebSearch — URL 404, postes génériques non extractibles (27-28/07/2026) — **relancer peu utile** | Consultant transformation RH, expertise SAP |

### IT Services & Conseil global
| Cabinet | URL carrière | Ce qu'on cherche |
|---------|-------------|-----------------|
| Accenture | WebSearch `"Accenture" consultant SAP HCM SuccessFactors SIRH France CDI 2026` — postes SAP SF trouvés US/NZ uniquement, pas France (28/07/2026) — relancer ponctuellement | SAP HCM, SuccessFactors, Consultant SIRH, CSM |
| Capgemini | `https://www.capgemini.com/fr-fr/jobs/` | SAP HR, SIRH, Chef de projet SIRH, AMOA (ancienne URL retournait 404) |
| IBM Consulting | `https://www.ibm.com/fr-fr/employment/` | SAP SuccessFactors, HRIS Consultant, AI Transformation — **testé le 23/09/2026 : page d'accueil générique en fetch direct, aucun listing exploitable.** WebSearch remonte plusieurs postes SAP SuccessFactors réels (Bois-Colombes) mais le lien LinkedIn trouvé était déjà expiré (`trk=expired_jd_redirect`) — à retester via WebSearch ponctuellement en cherchant un lien direct `ibm.com/careers` plutôt que LinkedIn |
| Sopra Steria | `https://careers.soprasteria.fr/` | Consultant SAP HR/HCM/SF, Chef de projet SIRH |
| CGI | `https://cgi.njoyn.com/corp/xweb/xweb.asp?CLID=21001` | SAP HCM, SIRH (ATS propriétaire, déjà référencé) |
| Atos / Eviden | WebSearch `"Eviden" OR "Atos" consultant SAP HR SuccessFactors France 2026` — ECONNREFUSED, aucun poste France identifié (27-28/07/2026) — relancer ponctuellement | SAP HR, SuccessFactors, AMOA SIRH |
| Wavestone | `https://www.wavestone.com/fr/rejoindre-wavestone/nos-offres/` | Consultant transformation RH, SIRH, IA RH |
| TCS | `https://www.tcs.com/careers/global/search-apply` | SAP HCM, SuccessFactors, HRIS Consultant (WebSearch "TCS SAP HCM France careers") |
| Infosys | `https://career.infosys.com/jobdesc?jobReferenceCode=INFSRNJP00199` | SAP SuccessFactors, HCM (WebSearch "Infosys SAP HR France") |
| Wipro | `https://careers.wipro.com/careers-home/jobs?search=SAP+HCM` | SAP HCM, SIRH |
| HCL Technologies | `https://www.hcltech.com/careers` | SAP HR, HCM, SF (WebSearch "HCL SAP SuccessFactors France") |
| Tech Mahindra | `https://careers.techmahindra.com/Search?q=SAP+HR` | SAP HR, HCM — **testé le 23/09/2026 : aucun poste France identifiable via WebSearch, offres SAP SuccessFactors trouvées toutes en Inde (Hyderabad/Bengaluru/Pune) — rendement nul confirmé** |

### Cabinets RH / HR Tech spécialisés
| Cabinet | URL carrière | Ce qu'on cherche |
|---------|-------------|-----------------|
| HR Path | `https://jobs.hr-path.com/jobs` | Consultant SAP HCM, SuccessFactors, AMOA SIRH — très ciblé |
| Mercer | **Découverte majeure du 23/09/2026 : le recrutement SIRH de Mercer France passe par `convictionsrh.com`, pas `careers.mercer.com` (page JS non exploitable).** ConvictionsRH, cabinet SIRH historique, a rejoint Mercer/Marsh en août 2025 et reste la marque de recrutement pour ce périmètre. **Endpoint REST WordPress exploitable en curl : `https://www.convictionsrh.com/wp-json/wp/v2/job?per_page=50`** (renvoie titre, lien, date de chaque offre en JSON, sans avoir besoin de parser le HTML). 14 offres trouvées le 23/09 (12 retenues après exclusion stage/alternance/offre 2023 périmée), 8 nouvelles ajoutées à Offres SIRH — **à fetcher systématiquement désormais** | Consultant SIRH, transformation RH, SAP |
| Aon | `https://jobs.aon.com/jobs?q=SAP+HR&location=France` | HR Consulting, SIRH, données RH — **testé le 23/09/2026 : page JS non exploitable en fetch direct (spinner de chargement). WebSearch ne remonte aucun poste SAP HR/SIRH propre à Aon (uniquement ACT-ON GROUP, déjà connu) — rendement nul confirmé** |
| Willis Towers Watson (WTW) | `https://careers.wtwco.com/en/jobs?q=SAP+HR&location=France` | Consultant RH, transformation SIRH — **testé le 23/09/2026 : URL directe en 404. WebSearch confirme 57 postes WTW en France mais rien de spécifique SIRH/SAP identifié, un poste "Consultant Confirmé / Chef de Projet Work & Rewards" (compensation, pas SIRH) repéré sur Workopia sans confirmation de vivacité — rendement faible, à retester ponctuellement** |
| Korn Ferry | `https://jobs.kornferry.com/?search=SAP+HR+France` | Consultant RH, SIRH, talent management — **testé le 23/09/2026 : URL directe injoignable (timeout). WebSearch ne remonte aucun poste SIRH/SAP concret en France, seulement des pages génériques — rendement nul confirmé** |
| Sia Partners | WebSearch `"Sia Partners" consultant SIRH SAP IA France CDI 2026` | Consultant IA, transformation RH, AMOA SIRH (URL directe retournait 404) |
| Forvis Mazars | **URL corrigée le 23/09/2026 : `https://recrutement-fr.forvismazars.com/`** (l'ancienne URL mazars.fr est en 404). Testé le 23/09/2026 : site en Next.js SPA, aucune donnée de poste dans le HTML initial (chargement JS). Un poste réel "Consultant Manager/Senior Manager/Directeur SAP" (Levallois-Perret) trouvé via WebSearch mais le lien direct redirige vers la liste générique — pas de méthode fiable trouvée pour extraire les postes individuels, à retester avec Claude in Chrome si besoin | Consultant SIRH, transformation RH |
| Oliver Wyman | `https://careers.oliverwyman.com/search/?q=HR+SAP&locationsearch=France` | Conseil RH, transformation digitale — **testé le 23/09/2026 : page vide en fetch direct (0 octet de contenu texte). Le recrutement passe en réalité par `careers.marsh.com/fr/fr/oliver-wyman` (Oliver Wyman fait partie du groupe Marsh, comme ConvictionsRH/Mercer) mais cette page aussi est vide en fetch direct — profil recruté surtout junior/stagiaire d'après WebSearch, peu de fit pour un consultant senior, rendement faible confirmé** |
| Roland Berger | `https://www.rolandberger.com/fr/Careers/Open-positions/` | Conseil stratégique RH, transformation IA — **testé le 23/09/2026 (URL corrigée en `/fr/Locations/France/Career/`) : page fetchable mais sans liste de postes dans le HTML (JS). WebSearch ne remonte que des postes stagiaire/junior consultant, rien pour un profil senior — rendement nul confirmé pour ce profil** |
| Colombus Consulting | WebSearch `"Colombus Consulting" SIRH SAP AMOA emploi France 2026` | AMOA SIRH, SAP, transformation RH (URL directe retournait 404) |
| Eleven (ex-Eurogroup) | WebSearch `"Eleven Advisory" OR "Eurogroup Consulting" consultant RH SIRH France CDI 2026` | Conseil RH, SIRH, transformation (site ECONNREFUSED) |
| Ayming | WebSearch — URL 404, aucun poste France identifié (27-28/07/2026) — relancer ponctuellement | Conseil RH, SIRH, performance |

> **Note WebSearch :** Pour les sites qui bloquent le fetch direct (TCS, Infosys, Wipro, HCL), utiliser WebSearch avec `"[cabinet] SAP HCM OR SuccessFactors consultant France 2026"`.

---

## Éditeurs HRIS & Partenaires d'implémentation SAP - Pages carrière directes

Catégorie distincte des cabinets de conseil : ce sont des **éditeurs de logiciels HRIS** et des **intégrateurs SAP spécialisés**. Postes ciblés : **CSM / Account Manager**, **Implementation Consultant**, **Solution Advisor / Pre-sales**, **Consultant SAP HCM/SF**, **Chef de projet HRIS**.

### Partenaires SAP HR / Intégrateurs spécialisés
| Entreprise | URL carrière | Ce qu'on cherche |
|-----------|-------------|-----------------|
| Strada (ex-Alight / ex-NGA Human Resources) | `https://careers.alight.com/strada` — WebSearch `"Strada" OR "Alight" consultant SAP HCM France 2026` | CSM, SAP HCM Consultant, Implementation Consultant — 1er partenaire mondial SAP HR. **Rebrand 2024 : la division SAP HCM s'appelle désormais Strada.** Postes France à Colombes, fetch direct fonctionne sur careers.alight.com/strada |
| Zalaris | **URL corrigée le 23/09/2026 : `https://jobs.zalaris.com/`** (careers.zalaris.com en 404). Testé le 23/09/2026 via `/search/` : 37 postes ouverts, **0 en France**, tout ancré Chennai/Frankfurt/Gdynia/Granada/Helsinki/Riga/Weybridge (recrutement par pays comme la plupart des éditeurs HRIS internationaux) — rendement nul confirmé, ne pas relancer souvent | SAP HR/HCM Consultant, Project Manager, Payroll Consultant — spécialiste SAP HR Europe nordique + DACH + France |
| Rizing (groupe Verizon) | WebSearch `"Rizing" SAP HCM SuccessFactors consultant France emploi 2026` | SAP HCM / SuccessFactors Consultant — postes hors France identifiés (28/07/2026), relancer ponctuellement |
| Inetum (ex-GFI) | WebSearch `"Inetum" consultant SAP HR HCM SIRH France CDI 2026` | Consultant SAP HR, Chef de projet SIRH, AMOA SIRH — acteur majeur SAP France (site ECONNREFUSED) |
| Expleo | `https://www.expleo.com/fr/carrieres/nos-offres/` | Consultant SAP HR, Chef de projet SIRH — consulting technique France |
| Randstad Digital (ex-Ausy) | WebSearch `"Randstad Digital" SAP HCM SuccessFactors consultant France 2026` | SAP HCM, SuccessFactors, AMOA SIRH — **testé le 23/09/2026 : postes SAP SuccessFactors trouvés quasi tous en Allemagne (Munich), rien de spécifique France identifié — rendement faible confirmé** |
| Alten | WebSearch `"Alten" consultant SAP HR HCM SIRH France CDI 2026` | Consultant SAP HR/HCM, Chef de projet SIRH — SSII France (site en 403) |
| delaware | **La vraie URL France est `carriere.delaware.pro/jobs`** (`careers.delaware.pro` est en ENOTFOUND) — 12 postes le 01/09/2026, tous SAP FICO/SD/MM/S4, **aucun HCM/SF** ; les postes SuccessFactors indexés sont en Belgique (fr-be) |
| NTT Data Business Solutions (ex-itelligence) | **Flux RSS exploitable** : `careers.nttdata-solutions.com/services/rss/job/?keywords=successfactors` — mais tous les postes SF sont Inde/Allemagne/UK/Malaisie le 01/09/2026, 0 France et 0 remote worldwide |
| ~~LeverX~~ | `career.leverx.com` existe mais **toutes les fiches SF indexées renvoient 404** (annonces périmées) — rendement nul le 01/09/2026 |

### Éditeurs HRIS (postes CSM / Pre-sales / Implémentation)
| Entreprise | URL carrière | Ce qu'on cherche |
|-----------|-------------|-----------------|
| ADP | WebSearch `ADP "customer success" OR "implementation consultant" OR "solution advisor" France emploi 2026` | CSM Senior, Implementation Consultant HRIS, Solution Advisor — HRIS global (URL directe en 404, passer par welcometothejungle.com/fr/companies/adp/jobs) |
| SD Worx | WebSearch `"SD Worx" implementation consultant OR CSM France emploi 2026` | Implementation Consultant, Customer Success, SAP HR — paie/RH Europe (URL directe en 404) |
| Ceridian / Dayforce | WebSearch `"Dayforce" OR "Ceridian" CSM OR "implementation consultant" France 2026` — URL directe en 404 (27/07/2026) | CSM Senior, Implementation Consultant, Solution Consultant HRIS |
| Workday | `https://workday.wd5.myworkdayjobs.com/Workday` | CSM Enterprise, Implementation Consultant, Pre-sales HCM — profil senior (URL redirigée) — **testé le 23/09/2026 : page vide en fetch direct (9KB, shell JS). WebSearch confirme des postes CSM/Implementation EMEA réels (ex. "Sr Customer Success Manager" sur myworkdayjobs.com) mais aucune mention France explicite trouvée — à retester via l'API CXS Workday (`POST /wday/cxs/workday/Workday/jobs`) lors d'une prochaine relance plutôt que le fetch HTML direct** |
| Cornerstone OnDemand | WebSearch `"Cornerstone OnDemand" CSM OR "customer success" France 2026` — aucun poste France (28/07/2026) — relancer ponctuellement | CSM Senior, Account Manager — talent management SaaS |
| ServiceNow | `https://careers.servicenow.com/jobs/` | CSM Senior, Solution Consultant HR Service Delivery — **testé le 23/09/2026 : 403 en fetch direct. WebSearch confirme des postes CSM/Solution Consultant EMEA réels mais aucune ville France explicite trouvée (Allemagne/Suisse/Israël mentionnés) — à retester avec un filtre France plus précis** |
| UKG (Ultimate Kronos) | WebSearch `"UKG" CSM OR "implementation consultant" France 2026` — aucun poste France (28/07/2026) — relancer ponctuellement | Implementation Consultant, CSM, HCM consultant |
| Cegid | WebSearch `"Cegid" consultant SIRH OR CSM OR chef projet emploi France 2026` | CSM, Chef de projet SIRH, Implementation Consultant — éditeur SIRH FR (URL directe en 404) |
| Talentia Software | WebSearch `"Talentia Software" consultant SIRH emploi France 2026` | Consultant SIRH, Implementation, CSM — éditeur RH/Finance FR |
| Lucca | WebSearch `"Lucca" CSM OR "customer success" OR implémentation emploi France 2026` | CSM, Account Manager, Implementation — SIRH SaaS France (URL directe en 404) |
| Payfit | WebSearch `"Payfit" CSM OR "customer success" OR "account manager" emploi France 2026` | CSM, Account Manager — paie/SIRH SaaS France (URL directe ECONNREFUSED) |
| Personio | WebSearch `"Personio" CSM OR "customer success" France emploi 2026` | CSM Senior, Account Executive, Implementation — SIRH PME Europe (URL directe en 404) |
| Oyster | **ATS = Ashby, slug `oyster`** (confirmé le 01/09/2026, 26 postes) : `curl -s "https://api.ashbyhq.com/posting-api/job-board/oyster"` | EOR remote worldwide, même famille que Deel/Remote.com. **Deux pièges** : le board porte parfois deux ID différents pour un même titre (doublon interne Ashby, pas deux postes) ; et les pays secondaires listés (PT/ES/PL/ZA) n'incluent pas toujours la France, éligibilité à confirmer |
| Omnipresent | **ATS = Workable, slug `omnipresent-group`** (pas `omnipresent`) : `apply.workable.com/api/v1/widget/accounts/omnipresent-group` — compte vivant mais 0 poste public le 01/09/2026 ; les postes indexés sur startup.jobs sont périmés |
| Multiplier | **ATS = kula.ai** : `careers.kula.ai/usemultiplier` (fetchable en WebFetch, 80+ postes) ; le board Breezy `usemultiplier.breezy.hr` est vide. Rendement nul France le 01/09/2026 : CSM/Solutions tous APAC/NAMER/Inde, EMEA onsite Londres |
| ~~Papaya Global / Atlas HXM~~ | **À écarter** (01/09/2026) : Papaya n'a aucun ATS public (Comeet probable, token requis ; site en 403) et ses postes indexés sont Israël/US ; aucun board trouvé pour Atlas HXM (le slug Ashby `atlas` est une autre société) |
| 365Talents | **Publie sur WTTJ** (01/09/2026) : la page `/fr/companies/365talents/jobs` est en 403 WebFetch, mais **la liste des offres est en clair dans le HTML de `365talents.com/en/careers/`** et les fiches WTTJ se vérifient par curl + UA navigateur. Éditeur IA×RH (Lyon) — Global Alliance Manager + KAM captés, mais télétravail occasionnel seulement |
| Silae | **ATS = Teamtailor, `silae-career.teamtailor.com/jobs`, fetchable en curl direct** (liste + fiches avec télétravail affiché) — confirmé le 01/09/2026 ; éditeur paie français, postes onboarding/consultant, tous hybrides 2j/sem à ce jour |
| ~~Neobrain / PeopleSpheres / Eurécia~~ | Rendement nul le 01/09/2026 (pages carrière en 404 ou JS, page WTTJ PeopleSpheres non rendue en curl) — passage rapide seulement |

---

## Catégories free-work.com à fetcher systématiquement

**Problème identifié (2026-07-08) :** les WebSearch `site:free-work.com` ne remontent pas les pages de catégories `/job-mission/`. Il faut les fetcher directement, URL par URL, à chaque relance.

**Mise à jour (2026-07-27) :** les 5 URLs `/job-mission/` SIRH retournent toutes 404 — la structure du site a changé. Utiliser à la place les WebSearch suivantes pour SIRH/SAP :
- `site:free-work.com SAP HCM OR SAP HR OR SuccessFactors OR SIRH mission freelance France`
- `site:free-work.com AMOA SIRH OR "chef de projet SIRH" mission France`

Les URLs `/jobs/ia` et `/jobs/ia-generative` fonctionnent encore (fetch direct).

### Catégories IA / Chef de projet (onglets "Offres IA" + "Offres SIRH")
| URL à fetcher | Ce qu'on y trouve |
|---|---|
| `https://www.free-work.com/fr/tech-it/jobs/ia` | Missions IA (recherche transversale) — ✅ fonctionne |
| `https://www.free-work.com/fr/tech-it/jobs/ia-generative` | Missions IA générative spécifiquement — ✅ fonctionne |

### Catégories SIRH / SAP — nouvelles URLs qui fonctionnent (vérifié 2026-08-07)

Les anciennes URLs `/job-mission/<catégorie>/` sont bien mortes, mais free-work expose les mêmes listings sous `/fr/tech-it/jobs/<mot-clé>`. **Ces deux pages sont les plus rentables de toute la relance** : elles rendent titre, entreprise, lieu, TJM, durée, date de publication et URL de chaque mission d'un seul fetch.

| URL à fetcher | Ce qu'on y trouve |
|---|---|
| `https://www.free-work.com/fr/tech-it/jobs/sirh` | Missions et CDI SIRH — AMOA, chef de projet, transformation RH, Product Manager SIRH — ✅ fonctionne |
| `https://www.free-work.com/fr/tech-it/jobs/sap-hcm` | Missions SAP HCM / SuccessFactors / paie / GTA — ✅ fonctionne |
| `https://www.free-work.com/fr/tech-it/jobs/sap-successfactors` | Missions SuccessFactors dédiées (ONB, SP, PMGM, RCM, LMS, ECP...) — pas encore dans la liste standard avant le 19/08/2026, a rendu 10 missions LINKWAY/BI Solutions/Tenth Revolution en un seul fetch — **à fetcher systématiquement désormais, au même titre que `/jobs/sirh` et `/jobs/sap-hcm`** |
| `https://www.free-work.com/fr/tech-it/jobs/sirh/paris` | Même liste filtrée sur Paris |

Le schéma `/fr/tech-it/jobs/<mot-clé>` se généralise (`/jobs/ia`, `/jobs/ia-generative`, `/jobs/transformation-digitale`, `/jobs/mistral`) ; tenter d'autres mots-clés au besoin. En complément, les WebSearch restent utiles pour attraper les annonces indexées hors catégorie :
- `site:free-work.com AMOA SIRH OR "chef de projet SIRH" mission France 2026`
- `site:free-work.com SAP HCM OR SuccessFactors OR SIRH mission freelance 2026`

> **Note :** Ne pas fetcher les catégories dev pur (`/lead-developer/`, `/developpeur-autre-langage-*/`, `/product-owner/`) — elles contiennent surtout des postes hors profil (LangChain, RAG, MLOps).

> **Historique complet des relances antérieures au 2026-09-23 : voir `HISTORIQUE_RELANCES.md`** (déplacé le 2026-09-08, complété au fil des relances suivantes, la plus récente déplacée étant celle du 17-18/09). Ce fichier garde les verdicts détaillés source par source, les pièges découverts et les slugs ATS testés depuis le 07/08/2026. **Seules les deux relances les plus récentes doivent rester ci-dessous ; à chaque nouvel ajout, déplacer la plus ancienne des deux vers `HISTORIQUE_RELANCES.md`.**

## Sites de recherche IA (onglet "Offres IA")

**À inclure systématiquement dans chaque relance de recherche**, en parallèle des recherches SIRH/CSM.

| Site | Ce qu'on y cherche |
|------|-------------------|
| free-work.com/fr/tech-it/jobs/ia | Missions freelance IA, AMOA IA, PMO IA, consultant IA générative |
| free-work.com/fr/tech-it/jobs/ia-generative | Missions IA générative spécifiquement |
| mission-freelances.fr/missions/ | Missions formateur IA, consultant IA, conduite du changement IA |
| welcometothejungle.com | CDI formateur IA, consultant acculturation IA (recherche "formateur IA" ou "consultant IA générative") |
| fr.linkedin.com/jobs/formateur-intelligence-artificielle-emplois-france | Offres formateur IA |
| WebSearch | `formateur IA freelance mission France remote 2026`, `consultant IA générative conduite du changement freelance`, `"IA x SIRH" OR "IA RH" consultant formateur France` |

**Profils ciblés dans cet onglet :**
- Formateur IA / Facilitateur IA générative (100% remote en priorité)
- Consultant conduite du changement IA (sans data science pur — pas Python, pas RAG, pas MCP)
- PMO / Chef de projet programme IA (croisement SAP/SIRH + IA = différenciant)
- Acculturation IA pour équipes RH ou SIRH

**Routing dans add_offre.py :** Les offres dont le titre contient "Formateur IA", "Formation IA", "IA générative", "Intelligence Artificielle", "AI Trainer", "GenAI", "LLM" ou "Prompt" sont automatiquement routées vers l'onglet "Offres IA".

---

## Outils annexes de recherche d'emploi (notés le 09/09/2026, pas des sources d'offres)

Ces trois sites ne sont pas des boards à interroger pour trouver des offres ; ce sont des outils que Gaëtan veut garder sous la main pour le processus de candidature lui-même.

| Outil | Description |
|---|---|
| **tealhq.com** | Plateforme de recherche d'emploi tout-en-un (Teal) : CRM de candidatures (suivi statut/relances/salaire), extension Chrome qui sauvegarde automatiquement les offres depuis LinkedIn/Indeed, générateur de CV IA avec matching de mots-clés contre une offre, accès à des offres sourcées directement depuis les ATS des entreprises (plus fraîches qu'un agrégateur classique). Freemium. |
| **interview.talently.ai/mock-interview** | Talently AI : simulateur d'entretien d'embauche par IA, entretiens virtuels avec questions adaptées à une fiche de poste (prédéfinie ou collée par l'utilisateur), feedback détaillé instantané sur les réponses. Version gratuite pour démarrer, fonctionnalités avancées payantes. |
| **jobscan.co** | Jobscan : optimisation de CV pour les filtres ATS. Le "Resume Scanner" compare un CV à une offre précise et donne un score de compatibilité + les compétences/mots-clés manquants. Propose aussi un générateur de CV/LM IA, l'optimisation de profil LinkedIn, un "Auto Apply" et un suivi de candidatures. Outils de base gratuits, abonnement payant pour la suite complète. |

---

## Quatre recherches ajoutées le 14/08/2026

Ces métiers correspondent à des compétences réelles du parcours qu'aucune recherche ne captait. **À inclure dans chaque relance**, au même titre que SIRH, CSM, IA et PM. Elles se rangent dans les onglets existants, sans onglet dédié.

### Solutions Engineer / Sales Engineer / Solutions Consultant → onglet "Offres CSM"
Le manque le plus net du dispositif précédent. Gaëtan a l'avant-vente (appel d'offres d'infogérance L'Oréal gagné chez ALTI-TCS), le bagage d'ingénieur, la posture face aux grands comptes et l'anglais courant. Jusqu'ici seuls les postes pre-sales estampillés SAP étaient captés, alors que ce métier existe chez tous les éditeurs SaaS.
- WebSearch `site:jobs.ashbyhq.com "solutions engineer" remote EMEA`
- WebSearch `site:jobs.lever.co "sales engineer" OR "solutions consultant" remote France`
- API Ashby et Lever sur les éditeurs déjà repérés

### Technical Account Manager → onglet "Offres CSM"
Croisement compte enterprise et technicité ; le profil y répond mieux qu'au CSM pur. Plusieurs annonces CSM acceptent d'ailleurs le TAM comme expérience équivalente.
- WebSearch `"technical account manager" remote EMEA OR France 2026`

### Implementation Consultant / Onboarding Manager / Professional Services → onglet "Offres SIRH"
Quinze ans passés à faire exactement cela. Ces intitulés passaient à travers les filtres quand ils ne portaient ni « HRIS » ni « Customer Success ».
- WebSearch `"implementation consultant" OR "onboarding manager" remote Europe SaaS 2026`
- WebSearch `"professional services consultant" remote France OR EMEA`

### Data Migration Lead → onglet "Offres SIRH"
OnePayroll et la migration FMC sur huit pays valent au-delà de SAP. Chercher la compétence sur tout ERP ou SIRH, pas seulement SAP HR vers SuccessFactors.
- WebSearch `"data migration" lead OR consultant ERP OR HRIS remote France 2026`

> **Routage automatique** (`add_offre.py`) : les intitulés Solutions Engineer, Sales Engineer, Solutions Consultant, Pre-Sales et Technical Account Manager partent en `Offres CSM`, **sauf** s'ils portent un marqueur SIRH ou SAP ; « Principal Solution Advisor SuccessFactors » et « Pre-Sales Consultant SAP HCM » restent donc dans `Offres SIRH`. Implementation Consultant, Onboarding Manager et Data Migration Lead tombent dans `Offres SIRH` par défaut.

---

### Où chercher
| Source | Méthode |
|---|---|
| **API Ashby** | `curl -s "https://api.ashbyhq.com/posting-api/job-board/<entreprise>"` ; la méthode la plus fiable, voir l'astuce plus haut |
| jobs.ashbyhq.com | WebSearch `site:jobs.ashbyhq.com "product manager" remote EMEA` |
| jobs.lever.co | WebSearch `site:jobs.lever.co "product manager" remote France OR EMEA` |
| boards.greenhouse.io | WebSearch `site:boards.greenhouse.io "product manager" remote Europe` |
| welcometothejungle.com | WebSearch `welcometothejungle "product manager" CDI télétravail total 2026` |
| free-work.com | `https://www.free-work.com/fr/tech-it/jobs/product-owner` et `/jobs/product-manager` |
| wellfound.com, workatastartup.com | Startups, filtres remote |
| Boards VC (Index, Balderton, a16z, Sequoia) | WebSearch `site:jobs.indexventures.com "product manager" remote` |

### Où chercher
Mêmes sources que pour PM (API Ashby/Lever/Greenhouse, welcometothejungle.com, free-work.com), avec ces catégories/mots-clés en plus :
| Source | Méthode |
|---|---|
| free-work.com | Les URLs `/jobs/product-designer`, `/jobs/ux-ui`, `/jobs/ux`, `/jobs/ui` redirigent toutes en 301 (n'existent pas) — utiliser l'endpoint de recherche `?query=UX designer` / `?query=product designer` / `?query=design system` à la place, confirmé productif le 10/09/2026. Les missions UX/UI passent aussi parfois dans les catégories dev (`/job-mission/lead-developer/`, source de l'offre Linkup Partner du 10/09/2026), donc ne pas se limiter aux seules catégories produit |
| hellowork.com | Recherche par mots-clés "UX designer" ou "UI designer" (très productif) ; **éviter "product designer" seul**, presque entièrement pollué par les postes "Concepteur" (ingénierie mécanique/électrique) |
| jobs.ashbyhq.com, jobs.lever.co, boards.greenhouse.io | WebSearch `site:jobs.ashbyhq.com "product designer" OR "UX lead" remote EMEA`, idem Lever/Greenhouse ; l'API Ashby directe fonctionne aussi bien sur les slugs déjà connus (voir verdicts ci-dessous) |
| welcometothejungle.com | WebSearch `welcometothejungle "product designer" OR "UX designer" CDI télétravail total 2026` |
| dribbble.com/jobs | Fetch direct fonctionne (200, ~97 offres en clair), mais sans localisation/mention remote dans le listing — nécessite un fetch fiche par fiche pour qualifier chaque poste, à approfondir lors d'une prochaine relance |
| weworkremotely.com (catégorie design) | **Bloqué** : 403 en fetch direct sur la page catégorie et sur les fiches individuelles ; passer par WebSearch en radar uniquement |

### Où chercher

Mêmes sources que pour PM/UX (API Ashby/Lever/Greenhouse, welcometothejungle.com, free-work.com, hellowork.com), avec ces mots-clés spécifiques :
| Source | Méthode |
|---|---|
| hellowork.com | Recherche par mots-clés "SEO Manager", "Responsable SEO", "Consultant SEO" |
| free-work.com | Endpoint `?query=SEO` / `?query=GEO` / `?query=référencement` (les catégories `/jobs/<mot-clé>` dédiées SEO n'existent probablement pas, suivre la même logique que pour UX qui a montré que ces catégories produit/design redirigent en 301) |
| jobs.ashbyhq.com, jobs.lever.co, boards.greenhouse.io | WebSearch `site:jobs.ashbyhq.com "SEO Manager" OR "Head of SEO" remote EMEA`, idem Lever/Greenhouse |
| welcometothejungle.com | WebSearch `welcometothejungle "SEO Manager" OR "Responsable SEO" CDI télétravail total 2026` |
| WebSearch générique | `"GEO manager" OR "generative engine optimization" remote 2026`, `"AEO specialist" remote 2026` — discipline encore rare, à surveiller plutôt qu'à s'attendre à un fort volume |

### Où chercher

| Source | Méthode |
|---|---|
| **API Ashby / Lever / Greenhouse** (dispositif habituel) | Mêmes commandes `curl` que d'habitude ; filtrer sur les entreprises basées aux USA et sur les mentions remote internationales dans `location`/`categories.location`/`workplaceType` |
| **TopCSJobs** (topcsjobs.com/remote-customer-success-jobs) | Board dédié 100% Customer Success remote, mis à jour quotidiennement, CSM à CS Director |
| **Built In** (builtin.com/jobs/remote/customer-success, /jobs/remote/product) | Board tech US par ville + filtre remote national ; bonne couverture CSM et PM |
| **Product Manager Job Board** (productmanagerjobboard.com) | Board dédié Product Manager, filtrer sur remote |
| **startup.jobs** (startup.jobs/product-manager-jobs, et recherche libre CSM/HRIS) | Agrégateur startups, filtres remote |
| **Y Combinator Jobs** (ycombinator.com/jobs, filtrable par rôle : `/jobs/role/product-manager/remote`) | Alternative/complément à workatastartup.com pour le même vivier YC |
| **Wellfound** (wellfound.com/role/r/product-manager, /role/r/customer-success-manager) | Déjà utilisé, filtrer explicitement sur remote worldwide |
| **HN Who's Hiring via HNHIRING** (hnhiring.com/locations/remote) | Indexe le fil mensuel Hacker News "Who is Hiring", très riche en startups remote-first, filtre remote déjà appliqué |
| **RemoteOK** (remoteok.com) | **Revirement de règle** : précédemment exclu des relances FR pour être « trop US-centré » — c'est exactement la cible de cette recherche USA, à inclure désormais |
| **Remotive** (remotive.com) | Même revirement que RemoteOK : source US-centrée, désormais pertinente pour cet onglet |
| **We Work Remotely** (weworkremotely.com) | Déjà utilisé en radar via WebSearch (403 en fetch direct) ; bon vivier US |
| **Boards VC portfolio US** | a16z (jobs.a16z.com, déjà connu), Sequoia (jobs.sequoiacap.com, déjà connu), General Catalyst (jobs.generalcatalyst.com), Accel (jobs.accel.com), Bessemer (talent.bvp.com), NEA (jobs.nea.com), Lightspeed (jobs.lsvp.com), Greylock (jobs.greylock.com) — la plupart tournent sur la plateforme Getro, structure d'URL similaire ; à tester via WebSearch `site:<domaine> "customer success" OR "product manager" remote` si le fetch direct échoue |
| **Indeed US, ZipRecruiter, Glassdoor US** | Volumes énormes, filtrer sur remote + mots-clés métier ; utiles pour le radar salarial (Glassdoor) en plus des offres |
| **LinkedIn** (linkedin.com/jobs, sans filtre géographique France) | Même méthode radar que d'habitude ; filtrer sur `f_WT=2` (remote) sans `f_TPR` géographique pour capter les US |

### Où chercher

| Source | Méthode |
|---|---|
| **API Ashby / Lever / Greenhouse** (dispositif habituel) | Mêmes commandes `curl` que d'habitude ; filtrer sur les entreprises basées en Suisse (Zurich, Genève, Lausanne, Zoug, Bâle) ou aux Pays-Bas (Amsterdam, Rotterdam, Utrecht, Eindhoven) et sur les mentions remote internationales |
| **jobs.ch** | Premier board généraliste suisse (équivalent local d'Indeed/APEC), filtrer sur télétravail/remote |
| **jobup.ch** | Board suisse romande, bon pour Genève/Lausanne |
| **indeed.ch** | Probablement bloqué comme les autres Indeed déjà testés (403), à vérifier une fois |
| **nationaljobs.ch, jobsuisse.ch** | Boards suisses secondaires, à tester |
| **nationalevacaturebank.nl** | Board généraliste néerlandais, filtrer sur "thuiswerken"/"remote" |
| **indeed.nl** | Probablement bloqué comme les autres Indeed déjà testés (403), à vérifier une fois |
| **jobbird.com, werkzoeken.nl** | Boards néerlandais secondaires, à tester |
| **welcometothejungle.com** | Filtrer sur Suisse/Pays-Bas dans les résultats, même piège `archived_at` déjà documenté à vérifier avant tout ajout |
| **Boards VC EU** (Index Ventures a un fort ancrage suisse/genevois, Atomico a un fort ancrage néerlandais) | WebSearch `site:jobs.indexventures.com "customer success" OR "product manager" Switzerland OR remote`, idem Atomico pour les Pays-Bas |
| **LinkedIn** | Même méthode radar que d'habitude (catégories `fr.linkedin.com/jobs/...-emplois` sans filtre géo, ou `f_WT=2` remote), en ajoutant Suisse/Pays-Bas comme mots-clés de localisation |

### Éditeurs SaaS/HR Tech connus avec forte présence CH ou NL, à tester en priorité
- **Suisse** : Bexio, Abacus (éditeurs ERP/RH suisses), Klara, On (marque mais probablement pas remote), Temenos (fintech genevoise, gros effectif), SAP (bureau Zurich/Genève, déjà couvert par jobs.sap.com), Adecco Group (siège Zurich)
- **Pays-Bas** : Adyen, Mollie, Messagebird/Bird, Elastic (racines néerlandaises), Randstad (siège Diemen), Booking.com (Amsterdam, gros effectif, probablement CSM/PM en volume)

### Éditeurs HRIS/HR Tech ciblés par zone

| Zone | Éditeurs à tester (ATS à identifier : Ashby/Lever/Greenhouse/Workday/ATS propriétaire) |
|---|---|
| **Canada** | Ceridian/Dayforce (déjà testé côté USA, siège réellement à Toronto), Humi, PandaPay, Knit People, Wagepoint, Collage HR, Rise People, League (benefits), Clearco (pas HR mais HQ Toronto à titre de radar ATS) |
| **UK** (indépendamment de la recherche EMEA générique) | HiBob (siège Londres/Tel Aviv, déjà testé mais à repasser), Zellis, MHR (Midland HR), CIPHR, Access PeopleHR, Personio (DE mais forte présence UK), Breathe HR, Sage HR (UK), IRIS Software Group / Cascade HR |
| **Australie** | Employment Hero, Deputy, ELMO Software (ELMO Cloud HR & Payroll), Ento, KeyPay/YouPay, HROnboard |
| **APAC / Singapour** | Darwinbox (Inde, gros concurrent SAP SuccessFactors/Workday en Asie), PeopleStrong (Inde), Sleekr/Mekari (Indonésie), Talenox (Singapour), HReasily (Singapour), Deel/Multiplier (déjà couverts côté USA mais à repasser sous cet angle) |

### Méthode de recherche
- WebSearch `site:jobs.ashbyhq.com "HRIS" OR "customer success" remote Europe -location:US` puis vérifier l'éligibilité France sur chaque fiche
- WebSearch `"<éditeur>" careers remote Europe OR "remote worldwide" 2026` pour chaque éditeur ci-dessus dont l'ATS n'est pas encore identifié
- Une fois l'ATS trouvé (souvent Greenhouse ou Lever pour les scale-ups canadiennes/australiennes), l'ajouter au balayage systématique de slugs au même titre que les slugs déjà connus (voir sections API Ashby/Lever/Greenhouse plus haut)
- Portails carrière directs quand ils existent (ex. `careers.dayforce.com`, `employmenthero.com/careers`)

### Entreprises ciblées (liste fournie par Gaëtan le 27/08/2026)

**Énergie / chimie — bassin de Lacq / Pau**
- TotalEnergies – Pau (centre scientifique et technique R&D)
- Arkema – Lacq (production de produits chimiques)
- Teréga (ex-TIGF) – Pau (transport et stockage de gaz naturel)
- Toray Carbon Fibers Europe – Lacq (fabrication de fibres de carbone)
- Sanofi, Yara, Veolia, Sobegi, Abengoa, Rexam – bassin de Lacq (environ 150 entreprises industrielles, ~8 000 emplois sur le bassin)

**Aéronautique / spatial**
- Safran Helicopter Engines (siège, ex-Turbomeca) – Bordes, près de Pau (2 500+ salariés, leader mondial turbomoteurs hélicoptères)
- Safran Helicopter Engines – Tarnos (1 500 salariés, site basque)
- Dassault Aviation – Anglet/Biarritz (900 salariés)
- Groupe Lauak – Hasparren (1 100 salariés Europe)
- Daher – Territoire d'Industrie Lacq-Pau-Tarbes

**Agroalimentaire**
- Euralis – Lescar (Pau) (~5 300 collaborateurs, coopérative agricole/agroalimentaire)
- Maïsadour – Haut-Mauco (Mont-de-Marsan) (~4 300 salariés, CA >1,4 Md€ en 2023)
- Lindt & Sprüngli – Oloron-Sainte-Marie (850 salariés)

**Santé / medtech (Pays Basque)**
- B.Braun – Saint-Jean-de-Luz (2 000 salariés France)
- DJO Global / Enovis France – Mouguerre
- Technoflex – Bidart

**Industrie / textile / production (Pays Basque)**
- Epta France – Hendaye (560 salariés)
- Quiksilver (Boardriders) – Saint-Jean-de-Luz (600 salariés)
- Tribord (Decathlon) – Hendaye
- Celsa France – Bayonne (201 salariés, 496 M€)
- BMS Circuits – Mouguerre

### Où chercher
Ces entreprises sont pour la plupart de grands groupes avec un site carrière propre (souvent Workday, SuccessFactors Recruiting, ou un ATS maison) : privilégier le fetch direct de leur page carrière filtrée par ville (Pau, Lacq, Tarnos, Bordes, Bayonne, Anglet, Hendaye, Mouguerre, Saint-Jean-de-Luz, Bidart, Mont-de-Marsan, Oloron-Sainte-Marie, Lescar), et WebSearch `"<entreprise>" carrières OR emploi <ville> 2026` en repli. Pour les groupes internationaux (TotalEnergies, Safran, Sanofi, Veolia, Dassault Aviation, Lindt & Sprüngli), utiliser leur portail carrière global avec un filtre de localisation plutôt qu'une page dédiée au site local, qui n'existe généralement pas.

En complément des grands groupes industriels, passer aussi par **La French Tech Pays Basque** (frenchtechpaysbasque.fr, ou WebSearch `"French Tech Pays Basque" startup recrute 2026`) comme radar des startups locales (Bayonne/Anglet/Biarritz/Bidart) — ajouté le 01/09/2026, jamais testé.

## Méthode de recherche LinkedIn (importante)

Les recherches directes `site:linkedin.com/jobs "mot-clé"` retournent surtout des pages catégories génériques, pas les annonces individuelles. LinkedIn bloque aussi les fetches directs sur les URLs de postes.

**Méthode efficace en 3 étapes :**

1. **Fetcher les pages de résultats LinkedIn par catégorie** (pas de recherche texte) — ces URLs fonctionnent et affichent une liste d'offres avec entreprises et dates :
   - `https://fr.linkedin.com/jobs/successfactors-emplois-région-de-paris-france`
   - `https://fr.linkedin.com/jobs/customer-success-manager-emplois-france`
   - `https://fr.linkedin.com/jobs/hris-emplois`
   - `https://fr.linkedin.com/jobs/consultant-sirh-emplois`
   - `https://fr.linkedin.com/jobs/sap-hcm-emplois`

2. **Identifier les entreprises qui recrutent** dans cette liste (titre + entreprise + date visible), puis chercher leurs **sites de recrutement directs** (ex : jobs.sap.com, jobs.hr-path.com, smartrecruiters.com/ACT-ON, etc.) — ces sites sont publics et bien fetchables.

3. **Fetcher la page "Jobs in France" de l'entreprise** sur son propre site careers pour trouver les postes ouverts avec tous les détails (titre exact, description, remote, date).

**Exemple concret :** La page LinkedIn SAP SuccessFactors Paris a révélé "Principal Solution Advisor (HCM)" chez SAP → fetch de `jobs.sap.com/go/SAP-Jobs-in-France/850401/` → trouvé 2 postes HCM ouverts postés le 17/06/2026 (Principal Solution Advisor HCM + Customer Success Partner Expert HXM).

**Limite de l'approche catégorie France :** Les URLs de catégories `fr.linkedin.com/jobs/...-emplois-france` sont géo-filtrées et ne remontent pas les postes ciblant EMEA sans pays précis (ex : CoachHub remote DE/ES/UK, Dataminr Londres). Pour capturer ces offres, ajouter un fetch sans filtre géo ou avec geoId EMEA :
- `https://fr.linkedin.com/jobs/customer-success-manager-emplois` (sans `-france`)
- `https://www.linkedin.com/jobs/search/?keywords=Customer+Success+Manager&f_WT=2&f_TPR=r604800` (remote, 7 derniers jours, monde entier)

> **Seconde limite, constatée le 17/08/2026 :** même sans filtre géographique, une page catégorie LinkedIn n'affiche qu'une dizaine d'annonces sur les 600 et quelques que le compteur annonce. Elle sert donc à repérer **qui recrute**, jamais à balayer un marché. Ce jour-là, les deux postes Atlassian *Principal CSM Strategic France* en remote France n'apparaissaient sur aucune des pages catégories fetchées ; ils n'ont été trouvés qu'en interrogeant l'API carrières d'Atlassian. Quand une entreprise cible est connue, aller directement à son ATS plutôt que d'espérer que LinkedIn la remonte.

---

