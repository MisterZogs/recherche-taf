# CLAUDE.md – Recherche d'emploi Gaëtan FRANÇOIS

## Comportement au démarrage

À chaque fois que Claude est lancé dans ce dossier, il doit systématiquement proposer en début de conversation : "Veux-tu que je relance une recherche d'offres sur tous les sites et que j'ajoute les nouvelles trouvées dans `offres_emploi.xlsx` ?"

**Mémoire entre sessions : ce fichier est la seule mémoire qui survit.** Une nouvelle session ne se souvient de rien de ce qui a été dit ou fait dans une conversation précédente, seul ce que ce fichier contient est relu à chaque lancement. Toute leçon durable trouvée en session (une erreur méthodologique identifiée, une source qui se comporte différemment de ce qui était noté, une règle métier précisée ou corrigée par Gaëtan) doit être écrite ici avant la fin de la session, immédiatement quand elle est découverte plutôt que remise à plus tard. Ne pas se contenter de la dire dans le chat en pensant que « la prochaine fois » on y pensera : il n'y aura pas de prochaine fois qui s'en souvienne si ce n'est pas écrit ici.

---

## Contexte général

Gaëtan FRANÇOIS (gaetan8francois@gmail.com) est en recherche d'emploi.
Basé à **Anglet**, disponible immédiatement, souhaite du **100% remote**.
Cible : postes **Customer Success Manager Senior**, CDI ou Freelance, FR ou EN.
Cible également : postes **SIRH / HRIS**, **SAP RH / SAP HR**, **SAP HCM**, **SAP SuccessFactors**, en tant que **consultant** (freelance/mission) ou **CDI**.

Autres postes ciblés :
- **Chef de projet SIRH** - projets mondiaux, RFP, go-live, migration de données
- **MOA / Business Analyst SIRH** - spécifications fonctionnelles, lien métier/dev, recette, TNR
- **Consultant en migration de données SAP** - expertise SAP HR → SAP SuccessFactors
- **Formateur / Training Manager SIRH** - formation utilisateurs-clés, transfert de connaissances
- **Pre-sales / Solution Consultant HR Tech** - expertise technique SAP + face client grands comptes
- **Product Owner SIRH** - expérience startup + lien métier/dev + spécifications fonctionnelles
- **Account Manager / KAM HR Tech** - pour éditeurs SIRH, profil technique + grands comptes
- **Product Manager / Product Owner** - postes produit chez les éditeurs SaaS, **priorité absolue au 100% remote** — onglet dédié "Offres PM" dans le tableur
- **Solutions Engineer / Sales Engineer / Solutions Consultant** - avant-vente technique chez les éditeurs SaaS, tous secteurs — va dans l'onglet "Offres CSM"
- **Technical Account Manager** - gestion de compte enterprise à composante technique — va dans l'onglet "Offres CSM"
- **Implementation Consultant / Onboarding Manager / Professional Services** - déploiement client chez un éditeur SaaS, y compris hors RH — va dans l'onglet "Offres SIRH"
- **Data Migration Lead / Consultant migration de données** - tous ERP et SIRH, sans se limiter à SAP — va dans l'onglet "Offres SIRH"
- **Formateur IA / Consultant IA générative** - former entreprises à l'IA générative, conduite du changement IA, acculturation IA (sans data science pur) — onglet dédié "Offres IA" dans le tableur
- **IA × SIRH / IA × RH** - consultant ou chef de projet à l'intersection IA et RH/SIRH (ex : déploiement IA dans SIRH, programme IA transformation RH)
- **Chief of Staff** (auprès d'un CEO/fondateur de startup) - valorise directement l'expérience de co-fondateur (WallOfTraders.com), combinée à la rigueur process/enterprise du parcours SAP — ajouté le 22/08/2026 ; va dans l'onglet "Offres CSM". Attention : ces postes se pourvoient surtout par réseau et sont souvent hybrides/sur site auprès du fondateur, à vérifier au cas par cas avant de retenir une offre non-remote
- **Founding / Head of Customer Success (0→1)** - construction de la fonction CS dans une startup seed/Series A, capitalise sur l'expérience "a déjà construit un truc de zéro" chez WallOfTraders.com — ajouté le 22/08/2026 ; va dans l'onglet "Offres CSM" (déjà capté par les mots-clés "Customer Success"/"CSM")

---

## Profil

- 15 ans d'expérience en Customer Success / SIRH / gestion de comptes enterprise
- 14 ans d'expérience SAP, dont 10 ans sur le compte L'Oréal mondial (SAP HR, 40+ pays)
- Co-fondateur WallOfTraders.com (startup SaaS B2C, crypto trading)
- Formation ML / Deep Learning (Coursera, Python)
- Usage quotidien des outils IA générative
- Langues : Français (natif), Anglais (courant), Espagnol (intermédiaire), Portugais (intermédiaire)
- Loisirs : Course à pied, Surf, Tennis, Salle de sport, Échecs, Voyages, Lecture quotidienne

---

## Fichiers du projet

### CV visuels (format sidebar sombre + photo – style Gregory Debargue)
| Fichier | Usage |
|---------|-------|
| `Resume_GaetanFRANCOIS.html/.pdf` | CV visuel générique EN |
| `Resume_GaetanFRANCOIS_SIRH_EN.html/.pdf` | CV visuel ciblé HRIS/SAP EN — pour postes internationaux (Group HRIS Manager, SAP pre-sales, EMEA) |
| `Resume_GaetanFRANCOIS_SIRH.html/.pdf` | CV visuel ciblé SIRH/SAP FR — pour missions freelance et postes FR |
| `Resume_GaetanFRANCOIS_PM_EN.html/.pdf` | **CV Product Manager EN de référence** ; WallOfTraders.com en tête, sidebar produit, sous-titre descriptif du parcours - pour tout poste produit en anglais |
| `Resume_GaetanFRANCOIS_PM_FR.html/.pdf` | Version française du CV Product Manager - pour les éditeurs français dont l'annonce est rédigée en français |
| `Resume_GaetanFRANCOIS_PM_Platform_EN.html/.pdf` | CV Product Manager EN orienté **plateforme B2B technique** ; sidebar avec intégration système, migration de données, analyse de cause racine, Python/SQL/C++ - pour Camunda, Constructor, et les postes Core Platform / Data Orchestration |
| `Resume_GaetanFRANCOIS_Constructor_EN.html/.pdf` | CV visuel CSM EN orienté **encadrement d'équipe** ; sous-titre neutre, sidebar sans jargon SAP - à réutiliser pour tout poste de Manager / Head of Customer Success chez un éditeur SaaS non-RH |
| `Resume_GaetanFRANCOIS_Ashby_EN.html/.pdf` | CV visuel EN orienté **déploiement client et professional services** ; dérivé du CV Constructor, avec migration de données et go-live remontés dans la sidebar et une ligne HR Platforms conservée (utile chez un éditeur qui vend aux équipes RH ou recrutement) - à réutiliser pour tout poste Manager of Implementations / Professional Services / Onboarding chez un éditeur SaaS |
| `Resume_GaetanFRANCOIS_Cominty.html/.pdf` | CV visuel Cominty EN |
| `Resume_GaetanFRANCOIS_Cominty_FR.html/.pdf` | CV visuel Cominty FR |

### CV plats (format Areti/Taulia)
| Fichier | Usage |
|---------|-------|
| `CV_GaetanFRANCOIS_CSM.html/.pdf` | CV générique FR |
| `CV_GaetanFRANCOIS_CSM_EN.html/.pdf` | CV générique EN |
| `CV_GaetanFRANCOIS_Areti_FR.html/.pdf` | CV ciblé Areti Group FR |
| `CV_GaetanFRANCOIS_Areti_EN.html/.pdf` | CV ciblé Areti Group EN |
| `CV_GaetanFRANCOIS_Taulia_FR.html/.pdf` | CV ciblé SAP Taulia FR |
| `CV_GaetanFRANCOIS_Taulia_EN.html/.pdf` | CV ciblé SAP Taulia EN |
| `CV_GaetanFRANCOIS_Cominty_FR.html/.pdf` | CV ciblé Cominty FR |
| `CV_GaetanFRANCOIS_Cominty_EN.html/.pdf` | CV ciblé Cominty EN |

### Lettres de motivation
| Fichier | Usage |
|---------|-------|
| `CoverLetter_Taulia` / `.pdf` | LM SAP Taulia EN |
| `CoverLetter_Cominty` / `.pdf` | LM Cominty FR (longue) |
| `CoverLetter_Cominty_Short` | LM Cominty FR courte (<600 car.) |

### Autres
| Fichier | Usage |
|---------|-------|
| `offres_emploi.xlsx` | Tableur principal de suivi des offres, avec priorité, statut, TJM, liens — c'est ici qu'on ajoute toutes les nouvelles offres trouvées |
| `photo_cv.jpg` | Photo portrait (déc. 2023), utilisée dans les CV visuels |
| `greg` | Fichier offres partagé par un contact |

---

## Génération PDF (WeasyPrint)

```bash
# CV plats (avec marges)
DYLD_LIBRARY_PATH=/opt/homebrew/lib python3 -c "
from weasyprint import HTML, CSS
page = CSS(string='@page { size: A4; margin: 1.5cm 1.8cm; }')
HTML(filename='fichier.html').write_pdf('fichier.pdf', stylesheets=[page])
"

# CV visuels sidebar (pleine page, pas de marges)
DYLD_LIBRARY_PATH=/opt/homebrew/lib python3 -c "
from weasyprint import HTML, CSS
page = CSS(string='@page { size: A4; margin: 0; }')
HTML(filename='fichier.html').write_pdf('fichier.pdf', stylesheets=[page])
"
```

> Pré-requis : `brew install pango` (résout l'erreur libgobject-2.0-0)

---


## Règles d'écriture des lettres de motivation

- **Toujours utiliser le skill `/humanizer`** sur le texte final de chaque LM avant de la livrer
- **Pas de formule de négation** : éviter "isn't", "don't", "not X but Y", "wasn't X; it was Y" — reformuler en positif
- **Pas de tiret** (ni `–` ni `-`) : utiliser un point-virgule à la place — les tirets sont un marqueur IA
- **Point-virgule** : ponctuation privilégiée pour relier deux idées à la place d'un tiret
- **Ton direct, humain**, pas de formule creuse ("Je vous écris pour exprimer...")
- **Pas de liste à puces** dans les LM
- **Ouverture** : commencer par un fait concret, pas une déclaration d'intention
- **Concession honnête** sur les lacunes = crédibilité
- **Conclusion courte** : "J'aurais plaisir à en discuter avec vous." ou "I'd genuinely enjoy a conversation about the role." — ne pas rallonger
- **WallOfTraders.com** (toujours avec `.com`)
- **Longueur** : 4-5 paragraphes max

---

## Choix stylistiques CV

- **Localisation** : Anglet (pas Paris)
- **Disponibilité** : Remote (pas "hybrid setup")
- **Langues** : Espagnol et Portugais à 50% (intermédiaire)
- **Formation** : "Applied Mathematics" (EN) / "Calcul Scientifique" (FR)
- **Loisirs** : Course à pied, Surf, Tennis, Salle de sport, Échecs, Voyages, Lecture quotidienne
- **Tirets** : utiliser `-` uniquement, jamais `–`
- **WallOfTraders.com** : toujours avec `.com`
- **Rôle chez WallOfTraders.com** : écrire **« Co-fondateur & Product Manager »** (EN : « Co-founder & Product Manager »). Ne jamais écrire CEO, Directeur Général, DG ni Associé. Gaëtan y était réellement Product Manager ; ce rôle est un atout à faire valoir sur toute candidature produit, jamais une lacune à concéder.
- **Orthographe anglaise** : britannique partout (organisations, centralisation, programme, programmes)

### Règle importante : un CV ciblé ne doit pas coller à l'offre

Quand Gaëtan demande un CV pour une offre précise, **le CV ne doit pas se lire comme une réponse point par point à l'annonce**. Un recruteur qui sent le CV écrit pour son offre le décrédibilise.

Concrètement, à ne pas faire :
- Reprendre les intitulés de la fiche de poste dans le bloc compétences de la sidebar (ex : une offre qui demande « HR Operating Model, governance, stakeholder management » ne doit pas produire des compétences « HR governance & decision routing », « Global core model vs local arbitration »)
- Réordonner les bullets pour qu'ils suivent l'ordre des responsabilités de l'annonce
- Formuler un bullet de façon à répondre visiblement à un prérequis (ex : ajouter « reviewing their output until quality held » parce que l'annonce demande de superviser un junior)
- Aligner le sous-titre sur le titre du poste visé

Ce qu'il faut faire à la place :
- Garder une **boîte à outils naturelle de consultant** dans les compétences, et un sous-titre descriptif du parcours réel
- Conserver un ordre de bullets naturel : livraison de programme d'abord, puis les autres facettes du poste
- **Faire remonter la matière pertinente sans la surjouer** : si l'offre parle d'ateliers et d'encadrement, ces éléments doivent être présents dans le CV parce qu'ils font partie du parcours, formulés de façon neutre
- Le travail de mise en correspondance avec l'annonce se fait dans **la lettre de motivation**, pas dans le CV

Rappel lié : voir aussi la règle « ne jamais recopier le langage d'une offre dans un CV ; chaque bullet décrit l'expérience réelle avec ses propres mots ».

---

## Attentes salariales

**Fourchettes cibles validées par Gaëtan :**
- CSM Senior / Account Manager : 80-95K€
- Pre-sales / Solution Advisor SAP : 95-115K€
- Consultant SIRH senior / Chef de projet : 70-85K€ (CDI) ou 650-750€/j (freelance)
- Group HRIS Manager : 90-110K€

**Postes spécifiques :**
- SAP Taulia : viser 100-110K€ (fourchette 85-110K€)
- Cominty : 60-75K€ (fourchette affichée)

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
| whitehallresources.com | SAP recrutement UK/Europe (dont France), SAP SF + SAP HR, CDI + contrats, board public |
| opusresourcing.com | Spécialiste HCM (SAP SF, SAP HCM, Workday), UK/Europe dont France/Espagne/Italie |
| apec.fr | CDI cadres France, utile pour CSM et postes seniors |
| deel.com/careers | Plateforme RH/paie globale (HRIS tout-en-un, 150+ pays) — postes CSM, Solutions Consultant HRIS, Implementation Consultant, remote — board JS-rendu, passer par jobs.ashbyhq.com/deel ou builtin.com/company/deel/jobs |
| lehibou.com | N°1 freelance IT/Tech grands comptes France (CAC40 + ETI), 140k consultants, missions avg 18 mois — SAP HR, SIRH, chef de projet — site direct bloqué (403), chercher via free-work.com/fr/companies/lehibou/jobs ou WebSearch "lehibou.com mission SIRH" |
| comet.co | Plateforme freelance tech France (50k+ freelances certifiés), Paris/Lyon/Lille/Nantes — missions SIRH, AMOA, SAP — site nécessite auth, chercher via free-work.com/fr/tech-it/jobs/sirh (missions Comet bien référencées) |
| ergalis.com / up-skills.fr | Groupe Actual — Ergalis (recrutement IT/RH) + Up Skills (cadres & experts) — CDI Chef/Directeur de Projet SIRH, postes publiés sur welcometothejungle.com/fr/companies/ergalis/jobs |
| njoyn.com | ATS propriétaire CGI — "Invalid request" en fetch direct (27/07/2026) — utiliser WebSearch `CGI "consultant SIRH" OR "SAP HCM" France emploi 2026` ou welcometothejungle.com/fr/companies/cgi/jobs |
| glassdoor.fr | Board généraliste FR + avis salariés — données salariales réelles utiles pour cibler les prétentions ; offres CSM, Account Manager, SAP (bloquer scraping direct, passer par WebSearch "glassdoor.fr actuaire CSM" ou glassdoor.com/Job/france-...) |
| hellowork.com | Grand board généraliste FR (ex-RegionsJob/Cadreo) — bonne couverture CDI IT/SIRH cadres France ; complémentaire à APEC ; URLs `/fr-fr/emplois/[métier].html` retournaient 404 le 27/07/2026 — utiliser WebSearch `site:hellowork.com consultant SIRH OR "customer success"` |
| welcometothejungle.com | N°1 FR + EU, meilleur board pour remote/senior — filtres remote, contrat, niveau — URL : app.welcometothejungle.com/jobs?remoteOnly=true — rechercher "customer success manager", "consultant SIRH", "formateur IA" |
| collective.work | Plateforme freelance senior tech FR — missions SIRH, data, consulting — profil à activer |
| cremedelacreme.io | Freelance senior tech FR — TJM affiché, missions curated — missions SIRH, consulting |
| wellfound.com | Startups monde, filtres remote + salaire — ex-AngelList ; rechercher "customer success" remote |
| workatastartup.com | Y Combinator — énorme volume startups, filtres remote + data — rechercher "customer success" ou "HRIS" |
| ai-jobs.net | ~~Board spécialisé IA/ML~~ — **peu utile pour ce profil** : contenu dev/data pur (MLOps, RAG, Python), aucun poste formateur IA non-technique trouvé (27-28/07/2026) — ne pas inclure dans les relances |
| remoteok.com | Board remote monde — US-centré (28/07/2026) — peu utile pour les relances FR/SIRH, mais **à inclure pour la recherche USA** (voir section « Recherche USA »), en filtrant sur le remote ouvert à l'international |
| weworkremotely.com | Board remote monde — rechercher "customer success" — URL : weworkremotely.com/categories/remote-customer-success-jobs |
| remotive.com | Board remote monde — US-centré (28/07/2026) — peu utile pour les relances FR/SIRH, mais **à inclure pour la recherche USA** (voir section « Recherche USA »), en filtrant sur le remote ouvert à l'international |
| euremotejobs.com | Board remote EU — rechercher "customer success" ou "HRIS" — **403 en WebFetch, mais un `curl` avec User-Agent navigateur passe et rend le HTML complet avec les liens ATS d'origine (Lever/Greenhouse/SmartRecruiters)** (trouvé le 30/08/2026) ; a produit Tenable et Upsun (France remote confirmés) en un seul passage — désormais à fetcher en curl direct à chaque relance plutôt qu'à écarter |
| himalayas.app | Remote world — salaire souvent affiché — rechercher "customer success manager" ou "HRIS" — **403 en fetch direct le 05-06/08/2026**, passer par WebSearch |

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
| Ribbit (fintech) | ribbitcap.com/companies | CSM fintech/HRIS |

---

## Cabinets de conseil - Pages carrière directes

À fetcher directement lors de chaque relance de recherche. Postes ciblés : **Consultant SIRH / SAP HCM / SuccessFactors**, **Chef de projet SIRH**, **AMOA**, **Pre-sales / Solution Advisor HR Tech**, **CSM Enterprise**, **Formateur IA / Consultant IA**.

### Big 4 (audit + conseil)
| Cabinet | URL carrière | Ce qu'on cherche |
|---------|-------------|-----------------|
| Deloitte | `https://apply.deloitte.com/careers/SearchJobs/?3_56_3=300060` | Consultant SIRH, SAP HCM, Chef de projet RH, Formateur IA |
| PwC | WebSearch `"PwC" consultant SAP HR OR SIRH OR AMOA France emploi 2026` — URL 403, aucun poste France identifié (27-28/07/2026) — relancer ponctuellement | Consultant SAP HR, AMOA SIRH, transformation RH |
| EY | `https://careers.ey.com/ey/search/?q=SIRH+SAP&locationsearch=France` | Consultant SAP SuccessFactors, SAP HCM, AMOA |
| KPMG | `https://kpmg.com/fr/fr/home/carrieres/offres-d-emploi.html` | Consultant SIRH, SAP RH, transformation digitale RH |

### Big 3 (stratégie)
| Cabinet | URL carrière | Ce qu'on cherche |
|---------|-------------|-----------------|
| McKinsey | `https://www.mckinsey.com/fr/careers` | Expert RH / People Analytics / transformation digitale |
| BCG | WebSearch — URL 404, postes génériques non extractibles (27-28/07/2026) — **relancer peu utile**, profil trop junior ciblé | Consultant transformation RH, digital HR |
| Bain | WebSearch — URL 404, postes génériques non extractibles (27-28/07/2026) — **relancer peu utile** | Consultant transformation RH, expertise SAP |

### IT Services & Conseil global
| Cabinet | URL carrière | Ce qu'on cherche |
|---------|-------------|-----------------|
| Accenture | WebSearch `"Accenture" consultant SAP HCM SuccessFactors SIRH France CDI 2026` — postes SAP SF trouvés US/NZ uniquement, pas France (28/07/2026) — relancer ponctuellement | SAP HCM, SuccessFactors, Consultant SIRH, CSM |
| Capgemini | `https://www.capgemini.com/fr-fr/jobs/` | SAP HR, SIRH, Chef de projet SIRH, AMOA (ancienne URL retournait 404) |
| IBM Consulting | `https://www.ibm.com/fr-fr/employment/` | SAP SuccessFactors, HRIS Consultant, AI Transformation |
| Sopra Steria | `https://careers.soprasteria.fr/` | Consultant SAP HR/HCM/SF, Chef de projet SIRH |
| CGI | `https://cgi.njoyn.com/corp/xweb/xweb.asp?CLID=21001` | SAP HCM, SIRH (ATS propriétaire, déjà référencé) |
| Atos / Eviden | WebSearch `"Eviden" OR "Atos" consultant SAP HR SuccessFactors France 2026` — ECONNREFUSED, aucun poste France identifié (27-28/07/2026) — relancer ponctuellement | SAP HR, SuccessFactors, AMOA SIRH |
| Wavestone | `https://www.wavestone.com/fr/rejoindre-wavestone/nos-offres/` | Consultant transformation RH, SIRH, IA RH |
| TCS | `https://www.tcs.com/careers/global/search-apply` | SAP HCM, SuccessFactors, HRIS Consultant (WebSearch "TCS SAP HCM France careers") |
| Infosys | `https://career.infosys.com/jobdesc?jobReferenceCode=INFSRNJP00199` | SAP SuccessFactors, HCM (WebSearch "Infosys SAP HR France") |
| Wipro | `https://careers.wipro.com/careers-home/jobs?search=SAP+HCM` | SAP HCM, SIRH |
| HCL Technologies | `https://www.hcltech.com/careers` | SAP HR, HCM, SF (WebSearch "HCL SAP SuccessFactors France") |
| Tech Mahindra | `https://careers.techmahindra.com/Search?q=SAP+HR` | SAP HR, HCM |

### Cabinets RH / HR Tech spécialisés
| Cabinet | URL carrière | Ce qu'on cherche |
|---------|-------------|-----------------|
| HR Path | `https://jobs.hr-path.com/jobs` | Consultant SAP HCM, SuccessFactors, AMOA SIRH — très ciblé |
| Mercer | `https://careers.mercer.com/en/search-jobs?q=SIRH+SAP&country=FR` | Consultant SIRH, transformation RH, SAP |
| Aon | `https://jobs.aon.com/jobs?q=SAP+HR&location=France` | HR Consulting, SIRH, données RH |
| Willis Towers Watson (WTW) | `https://careers.wtwco.com/en/jobs?q=SAP+HR&location=France` | Consultant RH, transformation SIRH |
| Korn Ferry | `https://jobs.kornferry.com/?search=SAP+HR+France` | Consultant RH, SIRH, talent management |
| Sia Partners | WebSearch `"Sia Partners" consultant SIRH SAP IA France CDI 2026` | Consultant IA, transformation RH, AMOA SIRH (URL directe retournait 404) |
| Forvis Mazars | `https://www.mazars.fr/Home/Carrieres/Nos-offres-d-emploi` | Consultant SIRH, transformation RH |
| Oliver Wyman | `https://careers.oliverwyman.com/search/?q=HR+SAP&locationsearch=France` | Conseil RH, transformation digitale |
| Roland Berger | `https://www.rolandberger.com/fr/Careers/Open-positions/` | Conseil stratégique RH, transformation IA |
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
| Zalaris | `https://www.zalaris.com/careers/` | SAP HR/HCM Consultant, Project Manager, Payroll Consultant — spécialiste SAP HR Europe nordique + DACH + France |
| Rizing (groupe Verizon) | WebSearch `"Rizing" SAP HCM SuccessFactors consultant France emploi 2026` | SAP HCM / SuccessFactors Consultant — postes hors France identifiés (28/07/2026), relancer ponctuellement |
| Inetum (ex-GFI) | WebSearch `"Inetum" consultant SAP HR HCM SIRH France CDI 2026` | Consultant SAP HR, Chef de projet SIRH, AMOA SIRH — acteur majeur SAP France (site ECONNREFUSED) |
| Expleo | `https://www.expleo.com/fr/carrieres/nos-offres/` | Consultant SAP HR, Chef de projet SIRH — consulting technique France |
| Randstad Digital (ex-Ausy) | WebSearch `"Randstad Digital" SAP HCM SuccessFactors consultant France 2026` | SAP HCM, SuccessFactors, AMOA SIRH |
| Alten | WebSearch `"Alten" consultant SAP HR HCM SIRH France CDI 2026` | Consultant SAP HR/HCM, Chef de projet SIRH — SSII France (site en 403) |

### Éditeurs HRIS (postes CSM / Pre-sales / Implémentation)
| Entreprise | URL carrière | Ce qu'on cherche |
|-----------|-------------|-----------------|
| ADP | WebSearch `ADP "customer success" OR "implementation consultant" OR "solution advisor" France emploi 2026` | CSM Senior, Implementation Consultant HRIS, Solution Advisor — HRIS global (URL directe en 404, passer par welcometothejungle.com/fr/companies/adp/jobs) |
| SD Worx | WebSearch `"SD Worx" implementation consultant OR CSM France emploi 2026` | Implementation Consultant, Customer Success, SAP HR — paie/RH Europe (URL directe en 404) |
| Ceridian / Dayforce | WebSearch `"Dayforce" OR "Ceridian" CSM OR "implementation consultant" France 2026` — URL directe en 404 (27/07/2026) | CSM Senior, Implementation Consultant, Solution Consultant HRIS |
| Workday | `https://workday.wd5.myworkdayjobs.com/Workday` | CSM Enterprise, Implementation Consultant, Pre-sales HCM — profil senior (URL redirigée) |
| Cornerstone OnDemand | WebSearch `"Cornerstone OnDemand" CSM OR "customer success" France 2026` — aucun poste France (28/07/2026) — relancer ponctuellement | CSM Senior, Account Manager — talent management SaaS |
| ServiceNow | `https://careers.servicenow.com/jobs/` | CSM Senior, Solution Consultant HR Service Delivery |
| UKG (Ultimate Kronos) | WebSearch `"UKG" CSM OR "implementation consultant" France 2026` — aucun poste France (28/07/2026) — relancer ponctuellement | Implementation Consultant, CSM, HCM consultant |
| Cegid | WebSearch `"Cegid" consultant SIRH OR CSM OR chef projet emploi France 2026` | CSM, Chef de projet SIRH, Implementation Consultant — éditeur SIRH FR (URL directe en 404) |
| Talentia Software | WebSearch `"Talentia Software" consultant SIRH emploi France 2026` | Consultant SIRH, Implementation, CSM — éditeur RH/Finance FR |
| Lucca | WebSearch `"Lucca" CSM OR "customer success" OR implémentation emploi France 2026` | CSM, Account Manager, Implementation — SIRH SaaS France (URL directe en 404) |
| Payfit | WebSearch `"Payfit" CSM OR "customer success" OR "account manager" emploi France 2026` | CSM, Account Manager — paie/SIRH SaaS France (URL directe ECONNREFUSED) |
| Personio | WebSearch `"Personio" CSM OR "customer success" France emploi 2026` | CSM Senior, Account Executive, Implementation — SIRH PME Europe (URL directe en 404) |

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

**Un gap de routage repéré dans `add_offre.py`** (non corrigé, à garder en tête) : les intitulés « Account Director » (Superside), « Sales Enablement Manager » (Canonical) et « Customer Enablement Manager » (Figma) ne matchent aucun des mots-clés CSM/PRESALES_KEYWORDS actuels et sont retombés par défaut dans « Offres SIRH », alors qu'il s'agit clairement de postes commerciaux/CSM. Si ce type d'intitulé revient souvent, envisager d'élargir `PRESALES_KEYWORDS` avec « Account Director », « Sales Enablement », « Customer Enablement ».

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

## Recherche Product Manager (onglet "Offres PM")

**À inclure systématiquement dans chaque relance**, au même titre que SIRH, CSM et IA.

Gaëtan **était Product Manager** chez WallOfTraders.com : il possédait la roadmap, décidait de ce qui partait, rédigeait les spécifications et validait chaque fonctionnalité contre l'usage réel. C'est une expérience produit à part entière, à faire valoir comme telle. Voir la règle sur le rôle WallOfTraders.com plus bas.

**Critère numéro un : le remote.** Prioriser les postes 100% remote, puis remote EMEA ou remote depuis la France. Un poste produit sur site à Paris descend d'au moins deux étoiles par rapport au même poste en full remote.

### Postes ciblés
- Product Manager / Senior Product Manager chez un éditeur SaaS B2B ou B2C
- Product Owner (hors SIRH, qui reste dans l'onglet "Offres SIRH")
- Product Manager sur des sujets **onboarding, adoption, intégration, customer experience** ; c'est l'intersection la plus crédible avec le parcours
- Head of Product / Product Lead dans une structure de petite taille
- Product Manager sur un produit IA ; croisement à double intérêt avec l'onglet IA

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

### CV à envoyer
`Resume_GaetanFRANCOIS_PM_EN.pdf` est le **CV Product Manager de référence** : WallOfTraders.com placé en premier, sidebar orientée produit (Product Ownership, spécifications fonctionnelles, interface métier/développement), sous-titre descriptif du parcours.

`Resume_GaetanFRANCOIS_PM_Platform_EN.pdf` est la variante pour les **produits plateforme B2B techniques** (Camunda, Constructor, postes Core Platform, Data Activation, Data Orchestration) : même parcours, mais la sidebar et les bullets font remonter l'intégration système, la migration de données, l'analyse de cause racine et la pratique Python/SQL/C++, qui restent en arrière-plan dans le CV PM générique. Sur un produit métier vertical ou B2C, garder `PM_EN`.

`Resume_GaetanFRANCOIS_PM_FR.pdf` est la version française du CV de référence. **Choisir la langue sur celle de l'annonce, pas sur le pays** : un éditeur français qui publie en français (360Learning, Side, Inqom, RISE, Follow) attend un CV français, alors que Camunda, Constructor, Pennylane et les republications Jobgether se traitent en anglais.

### Lacune à connaître
Sur un poste produit **orienté développeurs** (SDK, API, instrumentation de tracking, attribution, outillage dev), Gaëtan n'a pas d'expérience ; c'est la seule concession honnête à faire en lettre de motivation. Ne jamais écrire qu'il n'a pas d'expérience produit, ce serait faux.

---

## Recherche USA (onglet dédié "Offres USA") — ajoutée le 22/08/2026

**À inclure systématiquement dans chaque relance**, au même titre que SIRH, CSM, IA et PM. Demande de Gaëtan : les salaires US, notamment dans les startups, sont nettement supérieurs aux fourchettes FR/EU de la section « Attentes salariales ». Cet onglet capte les offres d'**entreprises basées aux USA**, tous métiers confondus (CSM, SIRH/HRIS, PM, IA/formation), du moment qu'elles sont ouvertes au télétravail depuis la France.

### Critère de filtrage : le remote « worldwide », pas le remote « US only »

**Le point le plus important de cette recherche.** Une offre marquée « Remote » aux USA n'est pas automatiquement candidatable : beaucoup de postes remote américains exigent d'être **basé aux États-Unis ou autorisé à y travailler** (raisons fiscales/légales, payroll US uniquement). Gaëtan est basé en France, sans autorisation de travail US ni projet de relocalisation.

Ne retenir que les offres explicitement ouvertes à l'international : mentions **« Remote - Worldwide »**, **« Remote - Anywhere »**, **« Remote - Global »**, **« Remote - EMEA »**, **« Remote - Europe »**, **« Remote (International) »**, ou une entreprise déjà connue comme employeur international (souvent via une EOR type Deel/Remote.com/Oyster en arrière-plan). Écarter (ou envoyer vers `NoRemote` avec une note) toute offre marquée **« Remote - US only »**, **« Must be based in the US »**, **« US work authorization required »**, **« Remote (US) »** sans mention d'ouverture internationale.

En cas de doute sur une offre par ailleurs excellente, la garder avec priorité réduite et une note explicite (« éligibilité internationale à confirmer ») plutôt que de la perdre.

### Postes ciblés (mêmes familles que d'habitude, formulées à l'américaine)

- **Customer Success Manager / Senior CSM / Enterprise CSM** — le marché US regorge de CSM senior remote-first, secteur le plus actif
- **Technical Account Manager, Solutions Engineer, Sales Engineer, Solutions Consultant** — avant-vente technique, même logique que l'onglet CSM habituel
- **Implementation Consultant, Onboarding Manager, Professional Services Consultant, Data Migration Lead** — déploiement client, tout éditeur SaaS/HRIS
- **HRIS Manager, HRIS Consultant, People Systems Manager, Workday/SAP Consultant** — l'équivalent US du SIRH ; marché plus orienté Workday que SAP HCM
- **Product Manager / Senior PM / Group PM**, en particulier onboarding/adoption/customer experience, ou produit IA
- **AI Enablement Manager, AI Adoption Lead, GenAI Trainer, Applied AI Consultant, Customer Education (AI)** — équivalent US du « Formateur IA » ; le marché américain formule rarement ce rôle comme « trainer », plutôt comme « enablement » ou « adoption ». **Correctif du 22/08/2026** : en pratique, ce titre littéral est presque toujours soit US-only, soit onsite, soit trop technique (LLMOps/RAG) une fois vérifié fiche par fiche — rendement faible confirmé sur la première relance. Ne pas y consacrer plus qu'un passage rapide ; préférer chercher PM/TAM/CSM chez des éditeurs authentiquement IA (Dataiku, Cresta, PostHog...), qui donnent de bien meilleurs résultats sur ce même besoin de croisement IA
- **Chief of Staff** (auprès d'un CEO/fondateur de startup US) — ajouté le 22/08/2026, va dans "Offres USA" ; valorise le statut de co-fondateur WallOfTraders.com. Ces postes sont encore plus souvent sur site qu'en France (proximité du fondateur exigée) : vérifier le remote avec la même rigueur que les autres titres avant de retenir
- **Founding / Head of Customer Success (0→1)** — ajouté le 22/08/2026, va dans "Offres USA" ; construction de la fonction CS dans une startup seed/Series A, capitalise sur l'expérience fondateur

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

### CV et prétentions
Utiliser les CV EN habituels selon le métier (CSM générique, SIRH EN, PM EN/Platform EN, Ashby EN pour implémentation). Une fois de premières offres USA trouvées, consulter Glassdoor/levels.fyi sur l'intitulé exact pour calibrer la colonne Prétention en USD ; ne pas extrapoler de chiffres avant d'avoir des données réelles sur des postes comparables.

### État des sources — première relance USA du 22/08/2026

Leçon principale, valable pour toutes les sources US sans exception : **le champ `isRemote: true` des API Ashby/Greenhouse/Lever ne garantit jamais l'éligibilité internationale**, il indique seulement l'absence d'obligation de présence au bureau. Toujours lire le champ `location`/`categories.location` et, en cas de doute, le corps de la description (souvent une phrase explicite type « Candidates must reside in the United States »). Un `Remote (US)` ou une ville US dans `location` sans mention EMEA/Europe/Worldwide = à écarter.

| Source | Verdict 22/08/2026 |
|---|---|
| **Éditeurs EOR/HRIS eux-mêmes** (Remote.com, Deel, Oyster) | **La source la plus fiable** : leur modèle économique les pousse à publier des bandes salariales et une éligibilité par pays très explicites. Remote.com (`remotecom` sur Greenhouse) reste l'éditeur le mieux aligné, y compris sur des postes Workday Implementation Specialist purement SIRH |
| GitLab (`gitlab` sur Greenhouse) | Bon rendement : au moins un poste avec **la France listée nommément** (Customer Success Architect EMEA) |
| Ashby (son propre board, `ashby`) et Hightouch (`hightouch`) | Bon rendement CSM/TAM/SE EMEA, France incluse dans "European Union"/"Europe" |
| Dataiku (`dataiku` sur Greenhouse) | Éditeur IA authentique avec plusieurs postes **"France, Remote" explicite** — le meilleur niveau de garantie possible |
| PostHog, Checkly (via HN Who's Hiring, confirmés sur Ashby) | Bon rendement, fuseaux horaires EMEA/UTC+1-2 compatibles France |
| Deepgram (`deepgram` sur Ashby) | Un poste avant-vente EU-remote trouvé |
| **API Ashby/Lever/Greenhouse des éditeurs HRIS US "classiques"** (Rippling, Gusto, Justworks, HiBob, Lattice, Culture Amp, Workday, UKG, Paycor, Paylocity, Namely, Zenefits, TriNet...) | Rendement quasi nul : soit pas de board public, soit postes verrouillés US-only/pays unique. Ne pas y consacrer trop de temps à chaque relance, un passage rapide suffit |
| RemoteOK, Remotive | Rendement décevant sur cette première tentative (0 correspondance HRIS, 403 sur CSM) malgré le changement de règle qui les autorise désormais — à retenter, le contenu tourne vite sur ces boards |
| Built In (`/jobs/remote/customer-success`, `/jobs/remote/product`) | **Quasiment 100% Remote-US strict** malgré le nom « remote » — rendement très faible pour ce critère spécifique, à garder en dernier recours |
| Wellfound, workatastartup.com/Y Combinator, startup.jobs, Product Manager Job Board | Quasi exclusivement Remote-US ou pays unique (hors France) une fois vérifié fiche par fiche ; utiles comme radar mais peu d'ajouts concrets |
| TopCSJobs | Bon board pour repérer des pistes, mais les liens directs vers les ATS d'origine ne sont pas exposés au fetch — passer ensuite par l'API du board d'origine plutôt que par TopCSJobs lui-même |
| HNHIRING (fetch direct) | 403 systématique — passer par l'API Algolia du thread HN "Who is hiring" directement (id de thread à retrouver chaque mois) plutôt que par hnhiring.com |
| Boards VC (a16z, General Catalyst, Accel, BVP, NEA, LSVP, Greylock) | Republient surtout les mêmes offres Remote.com/Deel déjà captées ailleurs ; BVP/NEA/LSVP/Greylock non scrapables in fine — rendement très faible, passage rapide suffit |
| "AI Enablement Manager" et variantes littérales | Voir la note dans la section « Postes ciblés » ci-dessus : rendement faible, presque toujours US-only/onsite/trop technique |

---

## Recherche grosses entreprises du Sud-Ouest (onglet dédié "Pays Basque") — ajoutée le 27/08/2026

**À inclure systématiquement dans chaque relance**, au même titre que SIRH, CSM, IA, PM et USA. Demande de Gaëtan le 27/08/2026 : cibler les grosses entreprises du Sud-Ouest situées à **1h15 de route maximum de Biarritz** (donc jusqu'au bassin de Pau/Lacq et Mont-de-Marsan), tous métiers confondus parmi ceux ciblés par son profil (CSM, SIRH/SAP, PM, Formateur IA, gestion de compte, avant-vente technique...).

### Règle de routage : cet onglet échappe volontairement au filtre télétravail

**Point le plus important de cette recherche, à ne jamais oublier.** Le reste du dispositif (`add_offre.py`) envoie systématiquement dans `NoRemote` toute offre qui exclut le télétravail total (hybride, partiel, présentiel). **Cette règle ne s'applique pas à l'onglet "Pays Basque"** : ces offres sont pertinentes précisément parce qu'elles sont locales et à distance de trajet raisonnable, pas malgré leur caractère présentiel. Une offre chez TotalEnergies à Pau en présentiel reste dans "Pays Basque", elle ne part jamais dans NoRemote.

Techniquement : marquer `'Onglet': 'Pays Basque'` dans le dict passé à `ajouter_offres()`. Ce marqueur est vérifié en priorité absolue, avant même le filtre télétravail (voir `add_offre.py`, section "Ajout" de `ajouter_offres()`). L'onglet a été créé manuellement par Gaëtan dans le tableur le 27/08/2026 avec les mêmes colonnes que les autres onglets métier.

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

### Postes ciblés dans cet onglet
Mêmes familles que le reste du dispositif : Customer Success / Account Manager, Chef de projet SIRH / SAP HR / SAP HCM / SuccessFactors, Product Manager / Product Owner, Formateur IA / Consultant IA générative, Solutions Engineer / Technical Account Manager, Implementation Consultant, mais aussi plus largement tout poste de gestion de projet, gestion de compte, transformation digitale ou IT compatible avec le profil, vu qu'il s'agit d'un vivier local restreint (pas la peine d'être aussi strict sur l'intitulé que pour le reste du tableur).

### Où chercher
Ces entreprises sont pour la plupart de grands groupes avec un site carrière propre (souvent Workday, SuccessFactors Recruiting, ou un ATS maison) : privilégier le fetch direct de leur page carrière filtrée par ville (Pau, Lacq, Tarnos, Bordes, Bayonne, Anglet, Hendaye, Mouguerre, Saint-Jean-de-Luz, Bidart, Mont-de-Marsan, Oloron-Sainte-Marie, Lescar), et WebSearch `"<entreprise>" carrières OR emploi <ville> 2026` en repli. Pour les groupes internationaux (TotalEnergies, Safran, Sanofi, Veolia, Dassault Aviation, Lindt & Sprüngli), utiliser leur portail carrière global avec un filtre de localisation plutôt qu'une page dédiée au site local, qui n'existe généralement pas.

---

## Règles de gestion du tableur offres_emploi.xlsx

### ⚠️ RÈGLE ABSOLUE — un lien partagé par plusieurs offres différentes est presque toujours un lien générique, jamais une vraie coïncidence (posée le 21/08/2026)

**Une vraie page d'offre individuelle ne peut jamais correspondre à deux postes différents.** Si la colonne Lien contient la même URL sur deux lignes dont le Poste et/ou l'Entreprise diffèrent réellement, ce lien est presque toujours une page de recherche/catégorie/listing qui a été collée par erreur à la place du lien individuel de chaque offre — exactement le même bug que celui déjà documenté pour freelance-informatique.fr, mais qui s'est avéré bien plus répandu à l'audit du 21/08/2026 : trouvé sur **43 URLs partagées touchant environ 140 lignes**, notamment :
- Pages de recherche **Indeed** (`fr.indeed.com/q-<mots-clés>-emplois.html`)
- Pages catégorie **LinkedIn** (`fr.linkedin.com/jobs/<mot-clé>-emplois...`) — déjà documentées plus bas comme sources de *radar* uniquement, mais utilisées à tort comme Lien final à de nombreuses reprises
- Pages catégorie **free-work.com** de la forme `/fr/tech-it/jobs/<mot-clé>` (à ne pas confondre avec les pages individuelles `/fr/tech-it/job-mission/<catégorie>/<slug>`, qui sont légitimes)
- La page listing **mission-freelances.fr/missions/** (sans slug individuel)

**Avant chaque relance ou chaque nouvel ajout, vérifier qu'aucun lien n'est partagé par deux offres au Poste/Entreprise différents.** Méthode : regrouper toutes les lignes de tous les onglets par valeur de colonne Lien, et pour chaque lien partagé par plus d'une ligne, comparer Poste et Entreprise après normalisation des mentions d'anonymisation (« N/C », « n.c. », « client anonymisé »...). Si au moins deux lignes ont une Entreprise clairement différente pour le même Lien, c'est le bug : il faut retrouver l'URL individuelle réelle de chaque offre (nouvelle recherche ciblée sur le titre + l'entreprise), et si elle est introuvable (poste probablement pourvu depuis), **ne jamais réutiliser le lien générique** : vider la cellule Lien et documenter la raison dans Fit / Notes plutôt que de laisser un lien trompeur.

Cas à part : un lien partagé par des lignes au Poste et à l'Entreprise quasi identiques (juste une reformulation du même intitulé) n'est pas ce bug-là mais un doublon de ligne classique (la même offre individuelle réellement ajoutée deux fois) — cas moins grave, à nettoyer en supprimant la ligne redondante plutôt qu'en cherchant un nouveau lien.

**Audit du 21/08/2026 : correctif appliqué aux onglets actifs.** 43 liens génériques touchaient 172 lignes au total. Les 45 lignes des onglets actifs (Offres SIRH/CSM/IA/PM) ont été corrigées : 27 liens individuels retrouvés et vérifiés (200 + titre exact), 13 offres non retrouvables (probablement pourvues, lien vidé et documenté), 5 doublons de vraies offres fusionnés en une seule ligne. **Les 127 lignes restantes dans NoRemote et Fait n'ont pas été traitées** (offres déjà écartées ou déjà traitées, priorité plus faible) — à reprendre au fil de l'eau ou lors d'une prochaine session dédiée.

Astuces trouvées pendant cet audit, à réutiliser :
- Un lien LinkedIn qui redirige vers `...?trk=expired_jd_redirect` est une preuve fiable qu'une offre est fermée (`curl -s -o /dev/null -w "%{url_effective}" -L <url>` pour le détecter sans navigateur).
- Le flux RSS carrière `career.<entreprise>.com/services/rss/job/?keywords=<mot-clé>` fonctionne très bien sur les sites SuccessFactors (Nexans, Eramet, Syensqo...) pour retrouver l'URL individuelle exacte sans passer par une recherche JS.
- L'**API Workday CXS** (`<tenant>.wdX.myworkdayjobs.com/wday/cxs/<tenant>/<site>/job/<path>`) confirme fiablement titre et statut d'un poste (fonctionne pour Strada, L-Acoustics) ; certains tenants la bloquent systématiquement (403 sur toute combinaison, cas de Valeo) — dans ce cas se contenter d'un fetch HTML 200 + titre correspondant, sans garantie à 100 %.
- Une redirection interne vers la page listing générique du site carrière (ex. `career.groupeetam.com` → 410 Gone, `talents.mc2i.fr` → redirection vers `/nos-offres`) est un signal de fermeture aussi fiable qu'un lien LinkedIn expiré.
- **Correctif à une note antérieure** : `mission-freelances.fr/missions/` n'est **pas** trop JS pour être scrapée comme indiqué précédemment — un simple `curl` avec un User-Agent navigateur retourne tous les liens individuels en clair dans le HTML source. Idem pour `free-work.com/fr/companies/<slug>/jobs`, qui liste en clair toutes les missions ouvertes d'une entreprise donnée : c'est la méthode la plus fiable pour retrouver un lien individuel free-work quand on connaît le nom du client, à privilégier sur le décodage `data-obf` qui reste réservé à freelance-informatique.fr.

### Déduplication contre l'onglet Fait — désormais automatique dans add_offre.py (corrigé le 21/08/2026)

**`add_offre.py` ne vérifiait jusqu'ici jamais qu'un lien n'existait pas déjà dans le classeur avant de l'ajouter.** La fonction `ajouter_offres()` se contentait d'archiver les lignes `Fait=x` et d'ajouter les nouvelles offres reçues, sans jamais comparer leur Lien à l'existant. Le nettoyage restait un geste manuel (construire la liste des liens déjà présents avant chaque relance), qui dépendait entièrement de la rigueur de la session en cours — et plusieurs sessions passées, en particulier les scripts ponctuels `ajout_offres_YYYYMMDD.py`, ne le faisaient pas. Audit du 21/08/2026 : **27 offres avec un lien individuel réel étaient présentes à la fois dans un onglet actif (ou NoRemote) et dans Fait**, généralement parce qu'un poste avait été ajouté, puis traité et archivé, puis réajouté par erreur lors d'une relance ultérieure. Toutes supprimées (la ligne Fait, à jour sur le statut, a été conservée).

**Correctif définitif** : `_liens_existants(wb)` scanne désormais les 6 onglets (y compris Fait) au début de `ajouter_offres()`, et toute offre dont le Lien existe déjà nulle part dans le classeur est ignorée silencieusement (message `= [doublon ignoré]` en mode verbose) plutôt qu'ajoutée une seconde fois. **Ce garde-fou est désormais automatique et ne dépend plus de la rigueur manuelle d'une session** : tant que l'insertion passe par `add_offre.ajouter_offres()`, un lien déjà connu — actif, NoRemote ou déjà classé Fait — ne peut plus être réinséré. Continuer à utiliser cette fonction (plutôt que d'écrire des scripts ponctuels qui manipulent le classeur directement) pour bénéficier de ce contrôle.

### Filtre télétravail (règle prioritaire, posée le 14/08/2026, révisée le 18/08/2026)

**`NoRemote` ne reçoit que les offres qui excluent explicitement le télétravail total.** Ce filtre s'applique **avant** le routage par métier.

Valeurs qui partent dans `NoRemote` :
- **Hybride et partiel** sous toutes leurs formes (`Hybride`, `Partiel`, `Hybride 2j/sem`, `Partiel (3j/sem)`...). Décision explicite de Gaëtan le 14/08/2026 : le télétravail partiel ne suffit pas, et il l'a reconfirmée le 18/08.
- **Présentiel**, `Sur site` et `Non`.

Valeurs qui **restent** dans les onglets métier :
- Le télétravail confirmé : `Oui` et ses variantes entre parenthèses, `Full remote`, `Remote`, `Remote-first`, `Remote Europe`, `100% remote`, `Télétravail total`, `yes`, `En ligne`.
- **L'information manquante**, depuis la révision du 18/08/2026 : cellule vide, `n.p.`, `nc`, `N/C`, `Non précisé`, `À vérifier`, `À clarifier`, `À confirmer`, `Non confirmé`. Une offre dont le télétravail n'est pas renseigné n'est plus écartée ; elle reste dans son onglet métier, à charge de clarifier au moment de candidater.

Un marqueur d'hybride l'emporte sur la présence du mot « remote » : `Hybride (3j remote + 2j sur site)` part dans `NoRemote`.

La fonction `accepte_remote()` d'`add_offre.py` implémente cette règle et le routage est automatique. Effet de la révision du 18/08 : 261 offres sont remontées de `NoRemote` vers les onglets métier (158 SIRH, 56 IA, 44 CSM, 3 PM), et `NoRemote` est passé de 747 à 486 lignes, désormais uniquement de l'hybride, du partiel et du présentiel.

- **Six onglets d'offres** : `Offres SIRH`, `Offres CSM`, `Offres IA`, `Offres PM`, `Offres USA` (ajouté le 22/08/2026), `NoRemote`, plus `Fait`. (L'onglet `Légende` a été supprimé le 14/08/2026 ; ne pas le recréer. L'onglet `En process` est une zone de travail manuelle de Gaëtan pour une négociation en cours, hors dispositif `add_offre.py` : ne jamais l'automatiser ni la vider.) Le routage est automatique dans `add_offre.py` : **USA d'abord** (dès qu'une offre vient d'une entreprise basée aux USA — marqueur explicite `Onglet='Offres USA'` dans le dict, ou détection sur la Localisation), puis IA, puis CSM, puis PM, sinon SIRH. Une offre Product Manager dont l'intitulé porte aussi un marqueur SIRH ou SAP (« Product Owner HRIS », « Product Manager SIRH ») reste dans `Offres SIRH` ; le métier prime sur le titre. Le filtre télétravail (`NoRemote`) reste prioritaire sur tout, y compris sur USA : une offre USA non ouverte au remote international part dans `NoRemote`, pas dans `Offres USA`.
- **Ne jamais supprimer une ligne** du tableau, même si une offre semble expirée ou hors profil — changer le statut à la place.
- **Toujours trier par priorité décroissante** (⭐⭐⭐⭐⭐ en premier) après chaque ajout de nouvelles offres. Préserver les styles de couleur des cellules lors du tri.
- **Appliquer la couleur de fond** à la colonne Priorité pour chaque nouvelle ligne ajoutée : rouge (⭐⭐⭐⭐⭐), orange (⭐⭐⭐⭐), jaune/or (⭐⭐⭐), vert (⭐⭐), gris (⭐).

---

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

## Notes diverses

- Photo CV : `PHOTO-2023-12-09-21-52-05 4.jpg` (portrait fond blanc, déc. 2023)
- L'Oréal est classé 370e au Fortune Global 500 (2023)
- Cominty : poste hybride Paris mais Gaëtan veut full remote — à négocier en entretien
- SAP Taulia Londres : question visa UK à clarifier (poste remote depuis FR possible)
- "Preferred name" sur les formulaires = Gaëtan
- **the-ultracoaching.com / ULTRA (Marvin Ndiaye) — évalué le 28/08/2026, hors profil.** Coaching business pour dirigeants de PME (CA > 250k€), pas un éditeur SaaS/HR Tech. Recrute des "Closer" (vente) et des "coach" (accompagnement hebdo 16 semaines, appel d'1h/semaine avec plan d'action) via un portail séparé `jobs.ultra-mastermind.com` (souvent hors service, HTTP 503, ou "site rendu indisponible" — bâti sur Manus). Fit partiel sur le rôle de coach (relationnel client, suivi régulier, proche du CSM ; l'expérience de co-fondateur WallOfTraders.com y est un vrai atout), mais secteur hors cible (pas de SIRH/SaaS/IA) et rémunération probablement à dominante variable/commission comme les postes commerciaux du même board. Non ajouté au tableur ; ne pas relancer sauf si Gaëtan élargit explicitement vers le coaching business.
