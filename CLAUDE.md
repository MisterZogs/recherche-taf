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
| njoyn.com | ATS propriétaire CGI — offres SIRH/SAP non indexées ailleurs, chercher directement sur cgi.njoyn.com/corp/xweb/xweb.asp?CLID=21001 |

---

## Catégories free-work.com à fetcher systématiquement

**Problème identifié (2026-07-08) :** les WebSearch `site:free-work.com` ne remontent pas les pages de catégories `/job-mission/`. Il faut les fetcher directement, URL par URL, à chaque relance.

### Catégories SIRH / SAP (onglet "Offres SIRH")
| URL à fetcher | Ce qu'on y trouve |
|---|---|
| `https://www.free-work.com/fr/tech-it/job-mission/administrateur-applicatif-erp-crm-sirh/` | SIRH, SAP HR, Responsable SIRH, PMO SIRH, Chef de projet SIRH |
| `https://www.free-work.com/fr/tech-it/job-mission/consultant-erp-ms-dynamics-oracle-sage-sap/` | Missions SAP SuccessFactors, SAP HCM, SAP HR |
| `https://www.free-work.com/fr/tech-it/job-mission/consultant-moa-amoa/` | AMOA SIRH, AMOA IA/Data, Business Analyst RH |

### Catégories IA / Chef de projet (onglets "Offres IA" + "Offres SIRH")
| URL à fetcher | Ce qu'on y trouve |
|---|---|
| `https://www.free-work.com/fr/tech-it/job-mission/assistant-chef-de-projet/` | Chef de projet IA, Chef de projet SIRH, Chef de projet Formation IA |
| `https://www.free-work.com/fr/tech-it/job-mission/consultant/` | Consultant IA agentique, Formateur IA, Consultant transformation |
| `https://www.free-work.com/fr/tech-it/job-mission/consultant-decisionnel-bi-powerbi-sas-tableau/` | PMO programme IA, PMO SIRH |
| `https://www.free-work.com/fr/tech-it/jobs/ia` | Missions IA (recherche transversale) |
| `https://www.free-work.com/fr/tech-it/jobs/ia-generative` | Missions IA générative spécifiquement |

> **Note :** Ne pas fetcher les catégories dev pur (`/lead-developer/`, `/developpeur-autre-langage-*/`, `/product-owner/`) — elles contiennent surtout des postes hors profil (LangChain, RAG, MLOps).

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
