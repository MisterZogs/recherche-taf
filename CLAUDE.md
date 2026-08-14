# CLAUDE.md – Recherche d'emploi Gaëtan FRANÇOIS

## Comportement au démarrage

À chaque fois que Claude est lancé dans ce dossier, il doit systématiquement proposer en début de conversation : "Veux-tu que je relance une recherche d'offres sur tous les sites et que j'ajoute les nouvelles trouvées dans `offres_emploi.xlsx` ?"

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
- **Formateur IA / Consultant IA générative** - former entreprises à l'IA générative, conduite du changement IA, acculturation IA (sans data science pur) — onglet dédié "Offres IA" dans le tableur
- **IA × SIRH / IA × RH** - consultant ou chef de projet à l'intersection IA et RH/SIRH (ex : déploiement IA dans SIRH, programme IA transformation RH)

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
| remoteok.com | Board remote monde — **US-centré, résultats France rares** (28/07/2026) — ne pas inclure dans les relances sauf besoin spécifique |
| weworkremotely.com | Board remote monde — rechercher "customer success" — URL : weworkremotely.com/categories/remote-customer-success-jobs |
| remotive.com | Board remote monde — **US-centré, résultats France rares** (28/07/2026) — ne pas inclure dans les relances sauf besoin spécifique |
| euremotejobs.com | Board remote EU — rechercher "customer success" ou "HRIS" |
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
| Lever | jobs.lever.co — WebSearch `site:jobs.lever.co "customer success manager" remote France` | Qonto, Aircall, autres scale-ups FR |
| Greenhouse | boards.greenhouse.io — WebSearch `site:boards.greenhouse.io "customer success" remote France` | Typeform, autres |

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
| `https://www.free-work.com/fr/tech-it/jobs/sirh/paris` | Même liste filtrée sur Paris |

Le schéma `/fr/tech-it/jobs/<mot-clé>` se généralise (`/jobs/ia`, `/jobs/ia-generative`, `/jobs/transformation-digitale`, `/jobs/mistral`) ; tenter d'autres mots-clés au besoin. En complément, les WebSearch restent utiles pour attraper les annonces indexées hors catégorie :
- `site:free-work.com AMOA SIRH OR "chef de projet SIRH" mission France 2026`
- `site:free-work.com SAP HCM OR SuccessFactors OR SIRH mission freelance 2026`

> **Note :** Ne pas fetcher les catégories dev pur (`/lead-developer/`, `/developpeur-autre-langage-*/`, `/product-owner/`) — elles contiennent surtout des postes hors profil (LangChain, RAG, MLOps).

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

## Règles de gestion du tableur offres_emploi.xlsx

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

---

## Notes diverses

- Photo CV : `PHOTO-2023-12-09-21-52-05 4.jpg` (portrait fond blanc, déc. 2023)
- L'Oréal est classé 370e au Fortune Global 500 (2023)
- Cominty : poste hybride Paris mais Gaëtan veut full remote — à négocier en entretien
- SAP Taulia Londres : question visa UK à clarifier (poste remote depuis FR possible)
- "Preferred name" sur les formulaires = Gaëtan
