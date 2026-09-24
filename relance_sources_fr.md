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
| **mission-freelances.fr** | `mission-freelances.fr/missions/` en un seul curl + UA navigateur (liste complète ~1400-1500 missions sur une page, pas de pagination). Attention aux doublons croisés avec HelloWork/free-work (les cartes ne portent que la source de republication, pas l'entreprise réelle). |
| **free-work.com** | Catégories qui fonctionnent : `/fr/tech-it/jobs/sirh`, `/jobs/sap-hcm`, `/jobs/sap-successfactors`, `/jobs/ia`, `/jobs/ia-generative`. Pour PM/UX/SEO, utiliser l'endpoint `?query=<mot-clé>` (ex. `?query=product manager`, `?query=UX designer`, `?query=SEO`). Quand un client est identifié par ailleurs, `free-work.com/fr/companies/<slug>/jobs` liste ses missions ouvertes en clair. |
| **freelance-informatique.fr** | 3 pages catégorie à toujours vérifier : `chef-de-projet-sirh-freelance-n112`, `categorie-modules-sap-hr-238`, `categorie-progiciels-sirh-222`. Les liens "Voir la mission" sont encodés en base64 dans l'attribut `data-obf` sur un `<span>` (pas de `href` classique) : `re.findall(r'data-obf="([^"]+)"[^>]*>Voir la mission', html)` puis `base64.b64decode(...).decode()` préfixé par `https://www.freelance-informatique.fr`. Site parfois lent : mettre un `--max-time 8` par requête individuelle. |
| **convictionsrh.com** (Mercer/ConvictionsRH, recrutement SIRH) | `curl -s "https://www.convictionsrh.com/wp-json/wp/v2/job?per_page=50"` — JSON direct, titre+lien+date. |

## Sources à tester en repli rapide (rendement faible ou nul confirmé, passage <2min)

malt.fr (0 mission publique scrapée, profils freelances seulement) ; collective.work
(bloqué Cloudflare Turnstile sur le listing) ; freelance-day.eu (homepage seule
fetchable, `/missions/` en JS).

## Règle absolue sur les liens

Ne jamais mettre une URL de page catégorie/listing en colonne Lien. Signal d'alerte
freelance-informatique.fr : une URL de mission individuelle valide est TOUJOURS de la
forme `mission-<titre>-<5-7 chiffres>-de` ou `mission-<titre>-<YYMMDD><lettre><NNN>` —
toute autre forme (`-n<chiffres>`, `-e<chiffres>`, `cv-mission-*`) est une page
catégorie, décoder les `data-obf` pour trouver le lien individuel.
