# Cluster FR / freelance — sources à interroger

Lire d'abord `relance_regles_communes.md`. Fichier de sortie : donné dans la consigne
de lancement (vérifier s'il existe déjà avant de commencer, voir règles communes).

## Sources confirmées productives (à interroger systématiquement)

| Source | Méthode |
|---|---|
| **api.francetravail.io** | OAuth2 : `POST https://entreprise.francetravail.fr/connexion/oauth2/access_token?realm=%2Fpartenaire` avec `grant_type=client_credentials&client_id=${FRANCE_TRAVAIL_CLIENT_ID}&client_secret=${FRANCE_TRAVAIL_CLIENT_SECRET}&scope=api_offresdemploiv2 o2dsoffre` (identifiants dans `.env` à la racine, jamais committer). Recherche : `GET https://api.francetravail.io/partenaire/offresdemploi/v2/offres/search?motsCles=<mot-clé>&sort=1`. Lien = `origineOffre.urlOrigine`. **204 No Content = 0 résultat, pas une erreur.** Balayer ~15-20 mots-clés (SIRH, SAP HCM, SuccessFactors, consultant SIRH, chef de projet SIRH, AMOA, customer success, account manager, product manager, UX designer, product designer, SEO manager, formateur IA, chef de projet, project manager...). Source la plus productive à chaque relance. |
| **hellowork.com** | `curl` + UA navigateur. Recherche mots-clés : `hellowork.com/fr-fr/emploi/recherche.html?k=<mots-clés>&st=date&c=CDI`. Page métier+ville : `emploi/metier_<intitulé>-ville_<ville>-<CP>.html`. **Astuce rapide (23/09) : l'`aria-label` des cartes de résultats sur la page de recherche porte déjà titre/ville/entreprise/contrat/salaire/télétravail, pas besoin d'ouvrir chaque fiche.** Sinon JSON-LD `JobPosting` complet par fiche individuelle. |
| **jobijoba.com** | `emploi/<mot-clé>` (PAS `/fr/emplois?q=` ni `/fr/offres-emploi/<mot-clé>`, ça donne 404). Beaucoup de quasi-doublons par ville pour la même offre : dédoublonner par titre+entreprise, en ignorant la ville. |
| **fr.jobrapido.com** | `curl -L` + UA navigateur (WebFetch direct = 403). Liens individuels `open.app.jobrapido.com/fr/<id>`. |
| **fr.jooble.org** | Bloqué en curl direct (Cloudflare) : passer par WebFetch. |
| **mission-freelances.fr** | `www.mission-freelances.fr/missions/` (le préfixe `www.` est obligatoire depuis le 30/09/2026 : sans lui, 404) en un seul curl + UA navigateur (liste complète ~1400-1500 missions sur une page, pas de pagination). Attention aux doublons croisés avec HelloWork/free-work (les cartes ne portent que la source de republication, pas l'entreprise réelle). |
| **free-work.com** | Catégories qui fonctionnent : `/fr/tech-it/jobs/sirh`, `/jobs/sap-hcm`, `/jobs/sap-successfactors`, `/jobs/ia`, `/jobs/ia-generative`. Pour PM/UX/SEO, utiliser l'endpoint `?query=<mot-clé>` (ex. `?query=product manager`, `?query=UX designer`, `?query=SEO`). Quand un client est identifié par ailleurs, `free-work.com/fr/companies/<slug>/jobs` liste ses missions ouvertes en clair. |
| **freelance-informatique.fr** | 3 pages catégorie à toujours vérifier, SANS le préfixe `/mission-freelance/` (corrigé le 30/09/2026 : juste `freelance-informatique.fr/<slug>` directement) : `chef-de-projet-sirh-freelance-n112`, `categorie-modules-sap-hr-238`, `categorie-progiciels-sirh-222`. Les liens "Voir la mission" sont encodés en base64 dans l'attribut `data-obf` sur un `<span>` (pas de `href` classique) : `re.findall(r'data-obf="([^"]+)"[^>]*>Voir la mission', html)` puis `base64.b64decode(...).decode()` préfixé par `https://www.freelance-informatique.fr`. Site parfois lent : mettre un `--max-time 8` par requête individuelle. |
| **convictionsrh.com** (Mercer/ConvictionsRH, recrutement SIRH) | `curl -s "https://www.convictionsrh.com/wp-json/wp/v2/job?per_page=50"` — JSON direct, titre+lien+date. |
| **collective.work, précisions du 06/10/2026** : le détail d'une fiche se lit dans `props.pageProps.project` ; ~40 missions « cmu… » sont des postes internationaux (US, Inde, Pologne), ne garder que ceux ouverts à l'Europe/France ; `workPreferences` peut contredire HelloWork/jobijoba sur la même mission (le cas Lead Integration SAP SuccessFactors : hybride 3j non négociable côté collective) : indiquer l'hybride en cas de doute. Liens `/jobs/view/` LinkedIn acceptés en dernier recours si vérifiés actifs. choisirleservicepublic.gouv.fr : les liens sont des URLs absolues, ne pas utiliser un regex relatif. michaelpage.fr : fiches sans JSON-LD, lire le titre et la page HTML. jooble/jobrapido/freelance-informatique : 0 nouveau le 06/10. |
| **collective.work** (débloqué le 06/10/2026, ~1 500 missions freelance et CDI) | Plus de blocage Cloudflare. `curl` + UA navigateur sur `https://www.collective.work/jobs/fr?search=<mot-clé>` (**`search=`, pas `q=`/`query=`/`skills=`**, qui sont ignorés), puis `&page=2`, `&page=3`... Les missions sont dans le JSON `<script id="__NEXT_DATA__">` : `props.pageProps.dehydratedState.queries[0].state.data.results.projects` (30 par page ; champs `slug`, `name`, `sumUp`, `description`, `workPreferences` = `REMOTE`/`HYBRID`/`ON_SITE`, `expirationDate`, `contractTypes`, `isPermanentContract`). Lien = `https://www.collective.work/jobs/fr/<slug>`. **Un slug inexistant renvoie aussi 200** : la vivacité se juge sur `expirationDate`, pas sur le code HTTP. Le 06/10 : AMOA SIRH, Chef de projet SIRH, Product Manager SIRH senior, Lead Integration SAP SuccessFactors, Consultant SAP HCM Time (remote), plusieurs SuccessFactors en remote, CSM remote. Mots-clés : `SIRH`, `SuccessFactors`, `SAP HCM`, `HR Access`, `customer success`, `product manager`, `product owner`, `chef de projet`. Beaucoup de missions viennent d'ESN qui republient aussi sur free-work/mission-freelances : dédoublonner par Entreprise+Poste. `workPreferences` = `REMOTE` → Remote `Full remote` ; `HYBRID` → `Hybride` (NoRemote après routage). |
| **jobs.stationf.co** (réintégré le 06/10/2026, 45 offres historiques) | Board WelcomeKit rendu en JS, mais **index Algolia public interrogeable en curl** : app `CSEKHVMS53`, index `wk_cms_jobs_production_careers`, clé API à lire dans le HTML de `https://jobs.stationf.co/search` (`<input id="algolia_api_key">`). ~540 offres, ~40 pertinentes. Piège : les slugs d'org diffèrent des noms affichés (Tomorro=`airflow`, Joko=`joko-1`). Quasi tout est Paris hybride, donc NoRemote après routage, mais ça reste à remonter. |
| **michaelpage.fr** (ajouté le 06/10/2026) | `curl` + UA navigateur sur `https://www.michaelpage.fr/jobs/<mot-clé>` (ex. `sirh`, `sap-hcm`, `customer-success`, `chef-de-projet-sirh`). Liens individuels en clair : `/job-detail/<slug>/ref/jn-<MMYYYY>-<id>` (retirer le paramètre `?ng-src=...`). Surtout du CDI client final (Responsable SIRH, Manager de transition paie/SIRH), télétravail souvent partiel. |
| **choisirleservicepublic.gouv.fr** (ajouté le 06/10/2026) | `curl` + UA sur `https://choisirleservicepublic.gouv.fr/nos-offres/filtres/mot-cles/<mot-clé>/` (ex. `SIRH`, `chef de projet SIRH`). Liens individuels `/offre-emploi/<slug>-reference-<ref>/`, ~20 par page. Offres SIRH du secteur public (chargé de projet SIRH, administrateur fonctionnel SIRH) : télétravail presque toujours partiel (→ NoRemote), mais utile pour les postes Pays Basque/Landes/Pyrénées-Atlantiques (à mettre alors dans le cluster PB). |
| **LinkedIn (radar uniquement)** (réintégré le 06/10/2026, ~200 offres historiques) | Ne sert qu'à repérer **qui recrute** : une page catégorie n'affiche qu'une dizaine d'offres. Fetch `https://fr.linkedin.com/jobs/<mot-clé>-emplois` (sans `-france`, pour avoir aussi l'EMEA) avec `successfactors`, `sap-hcm`, `hris`, `consultant-sirh`, `customer-success-manager`. Puis aller chercher l'offre sur l'ATS ou le site carrière de l'entreprise repérée et mettre CE lien-là. **Jamais un lien `linkedin.com/jobs/...-emplois` en colonne Lien.** Un lien LinkedIn individuel `/jobs/view/<id>` est acceptable en dernier recours. |

## Sources à tester en repli rapide (rendement faible ou nul confirmé, passage <2min)

malt.fr (0 mission publique scrapée, profils freelances seulement) ; freelance-day.eu (homepage seule
fetchable, `/missions/` en JS).

**Testés le 06/10/2026 et non exploitables, ne pas y passer de temps :** hays.fr
(résultats en JS, aucun lien d'offre dans le HTML), robertwalters.fr (403), fed-human.fr
(timeout, ancienne URL en 410), silkhom.com (pas de fiches individuelles, juste des
billets hebdomadaires), kicklox.com (app Algolia en JS sur `app.kicklox.com`),
freelancerepublik.com et littlebigconnection.com (pas de liste publique de missions),
cremedelacreme.io (missions réservées aux membres), freelancermap.fr (timeout).

**Adzuna (agrège Indeed/Monster, bloqués en direct) — clé active depuis le 06/10/2026, à
interroger systématiquement.** Identifiants dans `.env` (`ADZUNA_APP_ID`/`ADZUNA_APP_KEY`,
jamais committer ni afficher). Requête :
`https://api.adzuna.com/v1/api/jobs/fr/search/1?app_id=$ADZUNA_APP_ID&app_key=$ADZUNA_APP_KEY&what=<mot-clé>&results_per_page=50&sort_by=date&max_days_old=14`
(pagination par le numéro après `/search/`). Champs : `title`, `company.display_name`,
`location.display_name`, `created`, `redirect_url`. Lien = `redirect_url` sans les
paramètres `utm_*` (forme `https://www.adzuna.fr/details/<id>`, page d'offre individuelle
valide). 3 371 résultats pour `SIRH` le 06/10, beaucoup de stages/alternances et de
gestion de paie à filtrer. Plan « Trial Access » : quotas limités, rester à ~20-30
requêtes par relance (mêmes mots-clés que France Travail). Pour la Suisse/Pays-Bas,
remplacer `/fr/` par `/ch/` ou `/nl/`.
