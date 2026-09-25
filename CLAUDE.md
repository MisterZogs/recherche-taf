# CLAUDE.md – Recherche d'emploi Gaëtan FRANÇOIS

## Comportement au démarrage

À chaque fois que Claude est lancé dans ce dossier, il doit systématiquement proposer en début de conversation : "Veux-tu que je relance une recherche d'offres sur tous les sites et que j'ajoute les nouvelles trouvées dans `offres_emploi.xlsx` ?"

**Mémoire entre sessions : ce fichier est la seule mémoire qui survit.** Une nouvelle session ne se souvient de rien de ce qui a été dit ou fait dans une conversation précédente, seul ce que ce fichier contient est relu à chaque lancement. Toute leçon durable trouvée en session (une erreur méthodologique identifiée, une source qui se comporte différemment de ce qui était noté, une règle métier précisée ou corrigée par Gaëtan) doit être écrite ici avant la fin de la session, immédiatement quand elle est découverte plutôt que remise à plus tard. Ne pas se contenter de la dire dans le chat en pensant que « la prochaine fois » on y pensera : il n'y aura pas de prochaine fois qui s'en souvienne si ce n'est pas écrit ici.

## Méthode de lancement d'une relance (posée le 24/09/2026, pour tenir dans une seule session)

**Ne jamais lancer les 4 clusters de relance en `fork`.** Un fork hérite de tout le contexte de la conversation en cours, y compris l'intégralité de ce fichier CLAUDE.md (plusieurs milliers de lignes) : lancer 4 forks revient à payer 4 fois le coût de lecture de ce fichier avant même le premier appel réseau. Sur la relance du 24/09/2026, ça a suffi à épuiser tout le budget de la session alors qu'aucune autre tâche n'avait été faite.

**Utiliser 4 agents `general-purpose` frais** (pas fork), un par cluster (FR/freelance, ATS+HRIS+USA+CH-NL, remote/VC EU+cabinets/éditeurs, Pays Basque+Bordeaux). Chaque agent reçoit une consigne courte qui lui dit de lire uniquement `relance_regles_communes.md` puis son fichier `relance_sources_<cluster>.md` (`relance_sources_fr.md`, `relance_sources_ats.md`, `relance_sources_remote.md`, `relance_sources_pb.md`) — jamais CLAUDE.md en entier. Ces fichiers contiennent le résumé du profil, le format de sortie, les exclusions, le filtre remote et la liste condensée des sources (URL/endpoint + verdict en une ligne, sans la narration historique). Préciser dans la consigne le nom du fichier JSON de sortie attendu (`relance_<date>_cluster_<nom>.json`).

Après complétion des 4 clusters : fusionner avec un script (voir `merge_relance.py`, réutilisable (`python3 merge_relance.py <date YYYYMMDD>`), dédoublonnage par lien exact + paire Entreprise/Poste normalisée + exclusion stage/alternance en filet de sécurité), puis une seule passe `add_offre.ajouter_offres()` sur le fichier fusionné. Ne jamais laisser un cluster écrire directement dans `offres_emploi.xlsx`.

**Si la limite de session est atteinte pendant qu'un cluster tourne encore** : avant d'envoyer un message pour relancer, vérifier l'état du fichier JSON de sortie de ce cluster (il doit déjà contenir du contenu grâce à l'écriture incrémentale). Reprendre l'agent existant (`SendMessage` vers son id) plutôt que d'en relancer un nouveau à l'aveugle : le 24/09/2026, une reprise mal gérée a fait tourner deux instances du même cluster en parallèle sur le même fichier de sortie (récupéré sans perte grâce à l'écriture incrémentale, mais budget de session gaspillé en travail dupliqué).

Garder à jour `relance_sources_<cluster>.md` au fil des relances (déplacer une source qui devient morte/productive dans la bonne section) et reporter le même changement dans `SOURCES_COMPLETES.md` (voir section suivante) plutôt que dans ce fichier CLAUDE.md — les deux doivent rester cohérents, mais `relance_sources_*.md` est la version condensée réellement lue par les agents de relance.

---

## Où trouver le reste (fichiers de référence)

Ce fichier a été allégé le 25/09/2026 : il pesait ~1200 lignes chargées intégralement
à chaque démarrage de session, même hors relance. Il ne garde maintenant que les
règles toujours utiles (démarrage, méthode de relance, profil, fichiers CV/LM, style
d'écriture, salaires, critères de routage par onglet, règles du tableur).

Le détail des sources (URLs, méthodes de fetch, verdicts site par site) vit dans des
fichiers séparés, lus seulement quand c'est utile :
- `relance_sources_<cluster>.md` + `relance_regles_communes.md` : version condensée et
  à jour, c'est ce que lisent les agents de relance (jamais CLAUDE.md en entier).
- `SOURCES_COMPLETES.md` : version détaillée avec tous les verdicts et pièges
  techniques par source ; à consulter pour comprendre le contexte d'une source ou pour
  mettre à jour `relance_sources_*.md`.
- `HISTORIQUE_RELANCES.md` : journal chronologique des relances passées (offres
  trouvées, sources testées, incidents).

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
- **UX Designer / UI Designer / Product Designer / UX Lead** - ajouté le 10/09/2026, valorise le rôle réel de responsable UX chez WallOfTraders.com (maquettes, parcours utilisateur, tests utilisateurs) et la pratique du vibe coding (Claude Code) sur Lifaia.com/ArchiKK.com depuis 2025 — onglet dédié "Offres UX" dans le tableur, priorité au 100% remote comme pour PM
- **SEO Manager / Responsable SEO / SEO Lead / GEO Specialist / AEO Specialist** - ajouté le 11/09/2026, valorise le pilotage SEO réel de WallOfTraders.com (cocons sémantiques, campagnes paid social, mesure de l'acquisition), avec extension aux postes hybrides SEO/GEO émergents (optimisation pour les moteurs de réponse IA) — onglet dédié "Offres SEO" dans le tableur, voir la section "Recherche SEO/GEO" plus bas pour le détail
- **Solutions Engineer / Sales Engineer / Solutions Consultant** - avant-vente technique chez les éditeurs SaaS, tous secteurs — va dans l'onglet "Offres CSM"
- **Technical Account Manager** - gestion de compte enterprise à composante technique — va dans l'onglet "Offres CSM"
- **Implementation Consultant / Onboarding Manager / Professional Services** - déploiement client chez un éditeur SaaS, y compris hors RH — va dans l'onglet "Offres SIRH"
- **Data Migration Lead / Consultant migration de données** - tous ERP et SIRH, sans se limiter à SAP — va dans l'onglet "Offres SIRH"
- **Formateur IA / Consultant IA générative** - former entreprises à l'IA générative, conduite du changement IA, acculturation IA (sans data science pur) — onglet dédié "Offres IA" dans le tableur
- **IA × SIRH / IA × RH** - consultant ou chef de projet à l'intersection IA et RH/SIRH (ex : déploiement IA dans SIRH, programme IA transformation RH)
- **Chief of Staff** (auprès d'un CEO/fondateur de startup) - valorise directement l'expérience de co-fondateur (WallOfTraders.com), combinée à la rigueur process/enterprise du parcours SAP — ajouté le 22/08/2026 ; va dans l'onglet "Offres CSM". Attention : ces postes se pourvoient surtout par réseau et sont souvent hybrides/sur site auprès du fondateur, à vérifier au cas par cas avant de retenir une offre non-remote
- **Founding / Head of Customer Success (0→1)** - construction de la fonction CS dans une startup seed/Series A, capitalise sur l'expérience "a déjà construit un truc de zéro" chez WallOfTraders.com — ajouté le 22/08/2026 ; va dans l'onglet "Offres CSM" (déjà capté par les mots-clés "Customer Success"/"CSM")
- **Engagement Manager / Delivery Manager** (professional services chez un éditeur SaaS ou intégrateur) - livraison de programme + relation client, le cœur du rôle tenu sur le compte L'Oréal — ajouté le 01/09/2026 ; va dans l'onglet "Offres SIRH" (routage par défaut, même famille qu'Implementation Consultant)
- **Partner Manager / Alliances Manager** (écosystème SAP ou HR Tech) - 14 ans SAP + gestion de grands comptes — ajouté le 01/09/2026 ; va dans "Offres CSM" (routé via PRESALES_KEYWORDS)
- **Renewals Manager / Customer Retention Manager** - famille adjacente au CSM (l'offre Upsun du 30/08 portait ce titre) — ajouté le 01/09/2026 ; va dans "Offres CSM"
- **Customer Education / Customer Training Manager** chez un éditeur SaaS, y compris hors SIRH - l'expérience de formation utilisateurs-clés vaut chez n'importe quel éditeur — ajouté le 01/09/2026 ; va dans "Offres CSM"
- **Chef de projet / Project Manager généraliste** (IT, transformation digitale, déploiement, PMO) - demande de Gaëtan du 01/09/2026 : ne plus se limiter au chef de projet SIRH, tout poste de chef de projet ou project manager compatible avec le profil est à retenir — va dans "Offres SIRH" (routage par défaut). Tester `free-work.com/fr/tech-it/jobs/chef-de-projet` (le schéma `/jobs/<mot-clé>` se généralise) et ajouter les WebSearch `"chef de projet" mission freelance remote France 2026` / `"project manager" SaaS remote EMEA 2026` aux relances

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

> **⚠️ Dossiers miroirs pour l'envoi aux recruteurs (identifiés le 15/09/2026) — à resynchroniser à chaque modification d'un CV source.** La plupart des CV listés ci-dessous ont un dossier du même nom à la racine (ex. `Resume_GaetanFRANCOIS_Octime/`, `CV_GaetanFRANCOIS_CSM/`) qui contient une **copie du PDF renommée en `Resume_GaetanFRANCOIS.pdf` ou `CV_GaetanFRANCOIS.pdf`** (nom générique, sans le suffixe qui révèle le ciblage), destinée à être jointe telle quelle à un email de candidature. Ces copies ne sont **pas** régénérées automatiquement quand le CV source change : 19 dossiers de ce type ont été retrouvés désynchronisés le 15/09/2026 (encore sur l'ancienne version avec « Co-founder », les barres de langue et Location/Availability) lors d'une correction appliquée à tous les CV. **Après toute modification en masse d'un CV existant (pas juste sa création), vérifier `find . -maxdepth 1 -type d \( -iname "Resume_GaetanFRANCOIS_*" -o -iname "CV_GaetanFRANCOIS_*" \)` et recopier chaque PDF source mis à jour vers son dossier miroir correspondant.**

### CV visuels (format sidebar sombre + photo – style Gregory Debargue)
| Fichier | Usage |
|---------|-------|
| `Resume_GaetanFRANCOIS.html/.pdf` | CV visuel générique EN |
| `Resume_GaetanFRANCOIS_SIRH_EN.html/.pdf` | CV visuel ciblé HRIS/SAP EN — pour postes internationaux (Group HRIS Manager, SAP pre-sales, EMEA) |
| `Resume_GaetanFRANCOIS_SIRH.html/.pdf` | CV visuel ciblé SIRH/SAP FR — pour missions freelance et postes FR |
| `Resume_GaetanFRANCOIS_SIRH2/Resume_GaetanFRANCOIS_SIRH2.html` (PDF généré sous le nom `Resume_GaetanFRANCOIS.pdf`, dans ce même dossier, pour l'envoi aux recruteurs ; à ne pas confondre avec le CV générique EN de la racine qui portait ce nom) | **Variante technico-fonctionnelle du CV SIRH FR** (créée le 01/09/2026, dossier dédié avec sa propre copie de `photo_cv.jpg`) : même structure que `SIRH`, mais le sous-titre, le profil, l'expérience L'Oréal 2018-2025 et l'expérience ALTI-TCS mettent en avant le **profil technico-fonctionnel**, la **maîtrise experte d'Excel**, le **traitement de très gros volumes de données**, les **chargements en masse d'Excel vers SAP** et les **reportings SAP vers Excel**. À utiliser sur les missions qui insistent sur la reprise/migration de données, le reporting ou le lien métier/technique |
| `Resume_GaetanFRANCOIS_SIRH2/Resume_GaetanFRANCOIS_SIRH2_EN.html/.pdf` | **Version anglaise du CV SIRH technico-fonctionnel** (créée le 01/09/2026, même dossier) : mêmes ajouts que la version FR (sous-titre « Senior HRIS Consultant, Functional & Technical », profil, L'Oréal 2018-2025 et ALTI-TCS orientés Excel avancé, gros volumes, mass uploads Excel vers SAP et reporting SAP vers Excel), orthographe britannique. Pour les postes HRIS internationaux à composante migration/reporting |
| `Resume_GaetanFRANCOIS_PM_EN.html/.pdf` | **CV Product Manager EN de référence** ; WallOfTraders.com en tête, sidebar produit, sous-titre descriptif du parcours - pour tout poste produit en anglais |
| `Resume_GaetanFRANCOIS_PM_FR.html/.pdf` | Version française du CV Product Manager - pour les éditeurs français dont l'annonce est rédigée en français |
| `Resume_GaetanFRANCOIS_PM_Platform_EN.html/.pdf` | CV Product Manager EN orienté **plateforme B2B technique** ; sidebar avec intégration système, migration de données, analyse de cause racine, Python/SQL/C++ - pour Camunda, Constructor, et les postes Core Platform / Data Orchestration |
| `Resume_GaetanFRANCOIS_Constructor_EN.html/.pdf` | CV visuel CSM EN orienté **encadrement d'équipe** ; sous-titre neutre, sidebar sans jargon SAP - à réutiliser pour tout poste de Manager / Head of Customer Success chez un éditeur SaaS non-RH |
| `Resume_GaetanFRANCOIS_Ashby_EN.html/.pdf` | CV visuel EN orienté **déploiement client et professional services** ; dérivé du CV Constructor, avec migration de données et go-live remontés dans la sidebar et une ligne HR Platforms conservée (utile chez un éditeur qui vend aux équipes RH ou recrutement) - à réutiliser pour tout poste Manager of Implementations / Professional Services / Onboarding chez un éditeur SaaS |
| `Resume_GaetanFRANCOIS_Presales_EN.html/.pdf` | **CV visuel EN dédié Solutions Consultant / Software Presales / Solutions Engineer (Presales)** (créé le 14/09/2026, dérivé du CV Ashby). Sous-titre « Enterprise SaaS Delivery & Technical Presales - International Accounts », sidebar Expertise réordonnée avec RFP/RFI/Competitive Bids, Technical Discovery & Scoping et Demos & Proof-of-Concept en tête. Le bullet ALTI-TCS L'Oréal est scindé pour faire ressortir l'appel d'offres gagné contre les prestataires en place (2014) comme un vrai succès avant-vente, et le bullet L'Oréal 2018-2025 sur le rôle de liaison business/développeurs est remonté en premier. À réutiliser pour tout poste Solutions Consultant, Software Presales Consultant, Solutions Architect (pre-sales) ou Senior Solutions Engineer (Presales) chez un éditeur SaaS, sans jargon RH pour rester générique (Synthesia, Manufacturo, Pigment, GitLab, Medallia, Basikon et postes similaires) |
| `Resume_GaetanFRANCOIS_Kiween.html/.pdf` | CV visuel ciblé rôle de consultant digital indépendant (créé le 05/09/2026 pour KIWEEN) : sous-titre et profil mis en avant sur l'acquisition digitale/SEO et la relation grands comptes, sidebar Compétences réordonnée dans le même sens ; bullet SEO/acquisition de WallOfTraders.com remonté en tête de l'expérience. À réutiliser pour tout poste de conseil en stratégie digitale, growth ou acquisition où le profil PM générique ne suffit pas à faire ressortir ce volet |
| `Resume_GaetanFRANCOIS_Cominty.html/.pdf` | CV visuel Cominty EN |
| `Resume_GaetanFRANCOIS_Cominty_FR.html/.pdf` | CV visuel Cominty FR |
| `Resume_GaetanFRANCOIS_UXLead.html/.pdf` | CV visuel FR pour les postes **Product Designer / UX Lead** (créé le 10/09/2026 pour une mission Linkup Partner via free-work.com) : sous-titre et profil (raccourci le même jour) mettent en avant le rôle réel de responsable UX chez WallOfTraders.com (conception des maquettes/parcours utilisateur, tests utilisateurs informels via la communauté de traders, cohérence visuelle/ergonomique), sidebar Compétences réordonnée avec la conception UX et **Claude Code (vibe coding)** en tête. Une entrée d'expérience 2025 met en avant **Lifaia.com** (assistant santé personnel) et **ArchiKK.com** (outils IA pour architectes), deux produits que Gaëtan a vibe-codés en solo avec Claude Code, du wireframe au produit en ligne. À réutiliser pour tout poste de design produit/UX où ce volet du rôle WallOfTraders.com et la capacité à shipper vite avec l'IA générative doivent être mis en avant |
| `Resume_GaetanFRANCOIS_UXLead_EN.html/.pdf` | **Version anglaise du CV UX Lead** (créée le 11/09/2026), orthographe britannique, même structure et même contenu que la version FR. À utiliser sur les offres UX/Product Designer rédigées en anglais (Everai, WunderGraph, Pixie Services et autres offres remote EU/international captées dans les relances) |
| `Resume_GaetanFRANCOIS_SEO/Resume_GaetanFRANCOIS_SEO.html/.pdf` (dossier dédié créé le 21/09/2026, avec sa propre copie de `photo_cv.jpg`) | **CV visuel FR dédié aux offres SEO/GEO et Marketing/Acquisition** (créé le 12/09/2026, dérivé du template UX Lead ; élargi le 12/09/2026 le même jour à la demande de Gaëtan pour couvrir marketing, Facebook Ads, Google Ads, acquisition, réseaux sociaux, gestion de communauté), sur la base des volets réels de son rôle chez WallOfTraders.com. Sous-titre « Responsable Marketing, Acquisition & SEO - Product Manager », profil et premier bullet WallOfTraders.com réécrits pour faire remonter SEO (cocons sémantiques, maillage interne, netlinking), Facebook Ads/Google Ads et gestion de communauté (Telegram, newsletters), sidebar Compétences réordonnée en conséquence. Reste du CV inchangé (L'Oréal, ALTI-TCS, formation) |
| `Resume_GaetanFRANCOIS_SEO/Resume_GaetanFRANCOIS_SEO_EN.html/.pdf` (même dossier dédié) | **Version anglaise du CV SEO/GEO/Marketing** (créée le 16/09/2026, orthographe britannique), pour les offres SEO/GEO/AEO rédigées en anglais chez des éditeurs internationaux (créée pour Reedsy et ElevenLabs) |
| `Resume_GaetanFRANCOIS_Intescia.html/.pdf` | **CV FR dédié Product Marketing Manager** (créé le 16/09/2026, dérivé du CV SEO), sous-titre « Produit & Marketing - Roadmap, Acquisition et Croissance SaaS », profil et sidebar réordonnés pour foregrounder Product Ownership et positionnement/lancement de fonctionnalités avant le volet marketing pur, WallOfTraders.com présenté comme une marketplace B2B/B2C avec mention de la tarification des abonnements décidée par Gaëtan. Créé pour Intescia/WANAO, réutilisable pour tout poste Product Marketing Manager |
| `Resume_GaetanFRANCOIS_DevAndConnect.html/.pdf` | **CV FR dédié coordination digitale/programmes internationaux** (créé le 16/09/2026, dérivé du CV CSM générique FR), sous-titre « Chef de Projet - Coordination Digitale & Programmes Internationaux », pour les missions de coordination transverse multi-marchés type CRM/e-commerce/activation sans lien SIRH direct |

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

### Style d'écriture personnel de Gaëtan (source : `NotesCoverLetter`, ajouté le 08/09/2026)

**Portée : ces règles s'appliquent à tout texte généré au nom de Gaëtan pour répondre à un recruteur, pas seulement aux lettres de motivation formelles : réponses à des formulaires de candidature, questions comportementales d'entretien écrites, messages email/LinkedIn à un recruteur.** Le fichier `NotesCoverLetter` à la racine du projet contient ses réponses réelles à des questions de recruteurs, en français et en anglais ; ne jamais le réécrire, le relire pour se recalibrer avant de générer un texte important.

**Traits communs aux deux langues :**
- **Ouverture par un fait concret et vérifiable** (nombre d'années, poste, produit), jamais par une déclaration d'intention. Ex. FR : « Ingénieur de formation, j'ai 15 ans d'expérience... ». Ex. EN : « The most workflow-intensive platform I've built is WallOfTraders.com... ».
- **Langage de propriété directe** sur ses réalisations : « I owned X end to end » / « je portais la feuille de route de bout en bout », souvent suivi de deux-points et d'une liste en une phrase (jamais de puces) qui déroule concrètement ce que « owned » veut dire.
- **Preuve par les chiffres et les faits, jamais par l'adjectif** : « 10 000 utilisateurs », « 40 pays », « 15 ans », « cinq consultants » plutôt que « une solide expérience » ou « un grand nombre ». Bannir les qualificatifs creux (« passionné », « dynamique », « motivé ») sans un fait derrière pour les justifier.
- **Preuve par l'anecdote et le mécanisme, jamais par l'affirmation abstraite** : plutôt que d'affirmer qu'il sait cadrer un besoin, il raconte le mécanisme concret (le métier et le développeur qui comprennent une spécification différemment ; comment fonctionnait le copy trading via connexion API). Reproduire ce réflexe : une anecdote factuelle vaut mieux qu'une compétence citée dans l'abstrait.
- **Concession honnête sur une lacune**, formulée sans détour puis immédiatement suivie d'une solution pratique. Ex. : « Je n'ai pas d'expérience sur le module PMGM mais je peux suivre une formation avant la mission si cela me permet de l'obtenir. »
- **Phrases courtes et déclaratives.** De temps en temps, une phrase quasi aphoristique qui résume une leçon : « You don't have to like your product, you need to make sure your customers like it. »
- **Logistique mentionnée brièvement en fin de texte, sans développement** : localisation, disponibilité, mobilité, préférence remote.
- **Aucun jargon marketing/corporate** (« synergie », « leverage », enthousiasme générique de type « fast-paced dynamic environment »). L'intérêt pour un poste ou un produit se justifie par un détail précis (ex. le paragraphe sur Juno, l'assistant IA de Joko, qui explique pourquoi ce cas d'usage précis l'intéresse), jamais par de l'enthousiasme générique sans objet.

**Spécificités françaises** (missions freelance SIRH dans `NotesCoverLetter`) :
- Registre très direct et transactionnel, encore plus court qu'en anglais : « Bonjour, » puis directement le fait, puis la disponibilité/mobilité, puis « Bien cordialement » ou « Cordialement » et la signature.
- Formule de clôture type : « Je reste à votre disposition pour un échange téléphonique si cela peut aider à clarifier mon profil. » ou « J'aurais plaisir à en discuter avec vous. »
- Corriger silencieusement les fautes de frappe des notes brutes (ex. « technicol-fonctionnel » → « technico-fonctionnel », « pédagoque » → « pédagogue ») : le fond du style est à conserver, pas les coquilles.

**Spécificités anglaises** :
- Plus narratif que le français sur les réponses longues (questions comportementales d'entretien) : souvent construites en 2-3 paragraphes, le fait/contexte, le mécanisme concret, la leçon ou le résultat chiffré.
- Clôture de lettre type : « Kind regards, » puis « Gaëtan FRANÇOIS » (nom de famille en majuscules).

**Modèles de lettres de motivation** : voir le dossier `CoverLetterTemplates/` (créé le 08/09/2026, révisé le 08/09/2026 après précision de Gaëtan) — 6 modèles Set A construits à partir du contenu réel de `NotesCoverLetter` (SIRH/PO/CSM × FR/EN) et 6 modèles Set B qui ajoutent un vrai paragraphe original en plus.

**Règle de traduction croisée (précisée par Gaëtan le 08/09/2026) : tout le contenu de `NotesCoverLetter`, quelle que soit sa langue d'origine, est réutilisable dans l'autre langue par traduction, y compris dans les modèles Set A.** Ce n'est pas une solution de repli pour combler un manque, c'est la méthode normale : un fait qui n'existe qu'en anglais dans les notes (ex. le détail du projet de migration SAP HR vers SuccessFactors, l'encadrement de l'équipe ALTI/TCS) est traduit et inséré tel quel dans les lettres françaises, et réciproquement. Grâce à cette règle, les 6 modèles Set A sont désormais tous construits en piochant dans l'intégralité des deux corpus, pas seulement dans la langue cible.

---

## Choix stylistiques CV

- **Localisation** : Anglet (pas Paris)
- **Disponibilité** : Remote (pas "hybrid setup")
- **Langues** : Espagnol et Portugais à 50% (intermédiaire)
- **Formation** : "Applied Mathematics" (EN) / "Calcul Scientifique" (FR)
- **Loisirs** : Course à pied, Surf, Tennis, Salle de sport, Échecs, Voyages, Lecture quotidienne
- **Tirets** : utiliser `-` uniquement, jamais `–`
- **WallOfTraders.com** : toujours avec `.com`
- **Rôle chez WallOfTraders.com (révisé le 15/09/2026, annule la règle précédente) : ne plus jamais écrire « Co-fondateur »/« Co-founder »/« Cofondateur ».** Gaëtan a demandé le retrait de ce mot dans tous les CV (introduction, titres de poste, bandeau de gauche) le 15/09/2026 : un statut de co-fondateur peut être décrié par certains recruteurs (perception de manque d'expérience du salariat classique, risque de départ, etc.). Écrire simplement **« Product Manager »** comme titre de poste chez WallOfTraders.com (EN et FR identiques). Le reste de l'expérience (roadmap, spécifications, tests produit, gestion de communauté, SEO/acquisition) reste inchangé et continue de porter la preuve d'ownership sans avoir besoin du mot "fondateur". Ne jamais écrire CEO, Directeur Général, DG ni Associé non plus (règle inchangée). **Précision du 17/09/2026, suite à un rattrapage sur `CoverLetterTemplates/` : l'interdiction porte sur le mot lui-même, dans n'importe quel sens, pas seulement sur le titre de Gaëtan.** Plusieurs modèles de lettre de motivation utilisaient encore « mon cofondateur »/« my cofounder's » pour désigner une tierce personne technique (dans une phrase du type « je ne code pas, c'était la partie de mon cofondateur »), en pensant que la règle ne visait que le titre de Gaëtan lui-même. Ce n'est pas le cas : ne jamais écrire "cofondateur"/"co-founder"/"cofounder" nulle part dans un CV ou une LM, y compris pour parler d'un tiers. Pour la concession honnête « je ne code pas », reformuler sans nommer de cofondateur (ex. « l'équipe technique s'en chargeait » / « the technical team owned that side »).
- **Nature exacte de WallOfTraders.com (précisé le 16/09/2026) : c'était une marketplace, pas une simple plateforme B2C.** Elle mettait en relation des traders professionnels (B2B, qui proposaient leurs trades à copier) et des particuliers (B2C, qui payaient un abonnement pour les copier automatiquement). Gaëtan décidait lui-même de la tarification des abonnements B2C. Point à faire valoir explicitement (pas juste "B2B/B2C") sur les postes orientés product marketing, pricing/monétisation ou marketplace ; voir `Resume_GaetanFRANCOIS_Intescia.html` pour un exemple de formulation.
- **Bandeau de gauche (contact), révisé le 15/09/2026** : ne plus afficher Location/Localisation ni Availability/Disponibilité (potentiellement éliminatoires côté recruteur/ATS). Le bloc Contact ne contient plus que Email et **Téléphone/Phone : +33 6 75 97 51 62**.
- **Langues dans le bandeau de gauche, révisé le 15/09/2026** : ne plus utiliser de barres graphiques de niveau (`lang-bar-track`/`lang-bar-fill`), mal interprétées par certains ATS de tri de CV. Afficher le niveau en texte à droite du nom de la langue (classe `.lang-level`, flex `justify-content: space-between`) : Native/Natif (100%), Fluent/Courant (80%), Intermediate/Intermédiaire (50%), Basic/Notions (20%, allemand). CSS de référence dans `Resume_GaetanFRANCOIS_Presales_EN.html`, appliqué à tous les CV le 15/09/2026.
- **Orthographe anglaise** : britannique partout (organisations, centralisation, programme, programmes)
- **Expérience 2016-2018 (IA, Machine Learning & Robotique), corrigée le 21/09/2026** : le champ poste doit toujours être **« R&D »** (jamais « Projets personnels »/« Personal Projects », qui minimise la valeur de l'expérience en la présentant comme un loisir) et le champ lieu doit toujours être **« Bordeaux »** (jamais « R&D » utilisé comme lieu, ni « Personnel »). Le bullet Machine Learning doit dire **« prédictions hippiques »/« horse racing predictions »**, jamais « prédiction financière »/« financial prediction ». Appliqué sur les 38 CV (HTML, PDF, DOCX, dossiers miroirs inclus) le 21/09/2026 ; à répercuter sur tout nouveau CV créé à partir d'un gabarit existant.

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

### CV à envoyer
`Resume_GaetanFRANCOIS_PM_EN.pdf` est le **CV Product Manager de référence** : WallOfTraders.com placé en premier, sidebar orientée produit (Product Ownership, spécifications fonctionnelles, interface métier/développement), sous-titre descriptif du parcours.

`Resume_GaetanFRANCOIS_PM_Platform_EN.pdf` est la variante pour les **produits plateforme B2B techniques** (Camunda, Constructor, postes Core Platform, Data Activation, Data Orchestration) : même parcours, mais la sidebar et les bullets font remonter l'intégration système, la migration de données, l'analyse de cause racine et la pratique Python/SQL/C++, qui restent en arrière-plan dans le CV PM générique. Sur un produit métier vertical ou B2C, garder `PM_EN`.

`Resume_GaetanFRANCOIS_PM_FR.pdf` est la version française du CV de référence. **Choisir la langue sur celle de l'annonce, pas sur le pays** : un éditeur français qui publie en français (360Learning, Side, Inqom, RISE, Follow) attend un CV français, alors que Camunda, Constructor, Pennylane et les republications Jobgether se traitent en anglais.

### Lacune à connaître
Sur un poste produit **orienté développeurs** (SDK, API, instrumentation de tracking, attribution, outillage dev), Gaëtan n'a pas d'expérience ; c'est la seule concession honnête à faire en lettre de motivation. Ne jamais écrire qu'il n'a pas d'expérience produit, ce serait faux.

---

## Recherche UX/UI (onglet dédié "Offres UX") — ajoutée le 10/09/2026

**À inclure systématiquement dans chaque relance**, au même titre que SIRH, CSM, IA, PM et USA.

Gaëtan **était responsable UX** chez WallOfTraders.com en plus de Product Manager : il concevait les maquettes et les parcours utilisateur, animait une boucle de tests utilisateurs informels avec la communauté de traders, et veillait à la cohérence visuelle/ergonomique de la plateforme. Depuis 2025, il vibe-code aussi deux produits en solo avec Claude Code (Lifaia.com, assistant santé personnel ; ArchiKK.com, outils IA pour architectes), du wireframe au produit en ligne — un vrai différenciant sur les postes qui demandent de prototyper et shipper vite. Voir le CV dédié plus bas.

**Critère numéro un : le remote**, même logique que pour PM. Prioriser les postes 100% remote, puis remote EMEA ou remote depuis la France.

### Postes ciblés
- UX Designer / UI Designer / Product Designer, confirmé ou lead
- UX Lead / UX Manager / Responsable UX
- UX Researcher
- Postes qui demandent explicitement de structurer une démarche UX ou un Design System dans une équipe produit existante (correspond bien à l'expérience de mise en place solo chez WallOfTraders.com)

### CV à envoyer
`Resume_GaetanFRANCOIS_UXLead.pdf` : CV visuel FR dédié, dérivé du template PM. Sous-titre et profil (volontairement courts) mettent en avant le rôle réel de responsable UX chez WallOfTraders.com, sidebar Compétences avec la conception UX et **Claude Code (vibe coding)** en tête, et une entrée d'expérience 2025 sur Lifaia.com/ArchiKK.com. Voir le détail dans le tableau des fichiers du projet.

### Lacune à connaître
Gaëtan n'a pas de formation design formelle ni d'expérience en environnement produit d'équipe structurée avec des designers dédiés ; son expérience UX est celle d'un fondateur solo qui a dû tout faire, pas celle d'un praticien issu d'une école de design. C'est une concession honnête à faire en lettre de motivation sur les postes qui demandent explicitement une expertise design pure (motion, branding, recherche qualitative poussée), mais ne s'applique pas aux postes orientés produit/ergonomie où le profil est un vrai atout.

## Recherche SEO/GEO (onglet dédié "Offres SEO") — ajoutée le 11/09/2026

**À inclure systématiquement dans chaque relance**, au même titre que SIRH, CSM, IA, PM, UX et USA.

Gaëtan a piloté le SEO de WallOfTraders.com (cocons sémantiques, campagnes paid social, mesure de l'acquisition) en plus de son rôle Product Manager/UX. C'est une compétence réelle et démontrable, pas une extrapolation gratuite : à faire valoir sur les postes de responsable acquisition organique chez tout éditeur SaaS ou toute entreprise avec un site à fort trafic.

**Extension GEO/AEO (demande de Gaëtan du 11/09/2026) :** le GEO (Generative Engine Optimization) et l'AEO (Answer Engine Optimization) — l'optimisation de la visibilité d'un contenu dans les réponses des moteurs IA (ChatGPT, Perplexity, AI Overviews Google) plutôt que dans les résultats de recherche classiques — sont des extensions naturelles du SEO, en forte croissance depuis 2025-2026. Gaëtan n'a pas d'expérience GEO démontrable spécifiquement (discipline trop récente pour que quiconque en ait beaucoup), mais son expérience SEO plus sa pratique quotidienne de l'IA générative (vibe coding, usage des LLM) en font un profil crédible sur les postes hybrides SEO/GEO qui commencent à apparaître.

### Postes ciblés (intitulés extrapolés à partir de l'expérience réelle SEO de WallOfTraders.com)

- Responsable SEO / SEO Manager / SEO Lead / Head of SEO
- SEO Strategist / SEO Specialist / Consultant SEO
- GEO Manager / GEO Specialist / Generative Engine Optimization Manager
- AEO Specialist / Answer Engine Optimization
- Consultant SEO/GEO (positionnement hybride, le plus porteur actuellement)
- Growth Manager à forte composante SEO (à ne pas confondre avec un Growth Manager pur paid/product qui n'a pas ce volet)

### Routage automatique
Mots-clés testés dans `add_offre.py` (`SEO_KEYWORDS`, fonction `_is_seo()`, frontières de mot systématiques pour éviter les faux positifs type "Geography") : `SEO`, `GEO`, `Search Engine Optimization`, `Generative Engine Optimization`, `Référencement Naturel`, `Référencement SEO`, `Responsable SEO`, `SEO Manager`, `SEO Lead`, `SEO Strategist`, `SEO Specialist`, `Head of SEO`, `Growth SEO`, `SEO/GEO`, `GEO/SEO`, `AEO`, `Answer Engine Optimization`. Routage testé après UX et avant le repli SIRH dans l'ordre de priorité (USA > IA > CSM > PM > UX > SEO > SIRH par défaut) ; le filtre télétravail reste prioritaire sur tout, comme pour les autres onglets métier.

### CV à envoyer
`Resume_GaetanFRANCOIS_SEO.pdf` : CV visuel FR dédié, créé le 12/09/2026 (voir le détail dans le tableau des fichiers du projet). Pas encore de version EN ; à créer si une offre SEO/GEO rédigée en anglais le justifie.

### Lacune à connaître
Gaëtan n'a pas d'expérience SEO en environnement agence ou en équipe SEO structurée avec des outils spécialisés poussés (Screaming Frog, SEMrush/Ahrefs en profondeur, netlinking à grande échelle) ; son expérience est celle d'un fondateur solo qui gérait le SEO parmi d'autres responsabilités produit. Sur le GEO/AEO spécifiquement, aucune expérience formelle à ce jour, discipline trop récente. Concession honnête à faire en lettre de motivation sur les postes qui demandent explicitement une expertise SEO technique poussée ou une expérience GEO déjà démontrée.

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

### CV et prétentions
Utiliser les CV EN habituels selon le métier (CSM générique, SIRH EN, PM EN/Platform EN, Ashby EN pour implémentation). Une fois de premières offres USA trouvées, consulter Glassdoor/levels.fyi sur l'intitulé exact pour calibrer la colonne Prétention en USD ; ne pas extrapoler de chiffres avant d'avoir des données réelles sur des postes comparables.

### Priorité renforcée pour les offres HRIS/SIRH/SAP qui tombent hors de "Offres SIRH" (règle posée le 11/09/2026)

**Une offre HRIS/SIRH/SAP HCM/SuccessFactors qui atterrit dans un onglet autre que "Offres SIRH" (typiquement "Offres USA", via le routage automatique qui teste USA avant le repli SIRH) est un signal fort et doit systématiquement recevoir la priorité ⭐⭐⭐⭐⭐**, en haut de l'onglet. Rappel du contexte : Gaëtan a 14 ans d'expertise SAP HR/SuccessFactors, un profil déjà rare sur le marché français ; le croisement de cette expertise avec une offre internationale (USA, remote worldwide/EMEA) est exactement le genre d'opportunité différenciante qu'il ne veut pas rater, même si elle finit dans un onglet différent de celui où on la chercherait naturellement (Offres SIRH). Appliquer cette priorité par défaut lors de l'ajout, indépendamment de l'évaluation habituelle par fit/salaire.

À ce jour (11/09/2026), aucune offre HRIS n'est encore tombée dans "Offres USA" (0 sur 59 lignes) ; les offres HRIS actuellement en base sont toutes localisées en France, UK, Portugal ou Allemagne et restent donc dans "Offres SIRH". Cette règle s'appliquera dès qu'une telle offre apparaîtra.

**Même règle appliquée à "Offres CH-NL" (posée le 22/09/2026) :** le marché suisse en particulier est riche en SAP HCM/SuccessFactors (banques, pharma, horlogerie à Zurich/Genève/Bâle) ; une offre HRIS/SIRH/SAP qui atterrit dans "Offres CH-NL" plutôt que dans "Offres SIRH" doit recevoir la même priorité ⭐⭐⭐⭐⭐ par défaut.

## Recherche Suisse / Pays-Bas (onglet dédié "Offres CH-NL") — ajoutée le 22/09/2026

**À inclure systématiquement dans chaque relance**, au même titre que SIRH, CSM, IA, PM et USA. Demande de Gaëtan le 22/09/2026 : on lui a signalé qu'il y avait des offres intéressantes en Suisse et aux Pays-Bas. Cet onglet capte les offres d'**entreprises basées en Suisse ou aux Pays-Bas**, tous métiers confondus (CSM, SIRH/HRIS, PM, UX, SEO, IA/formation), du moment qu'elles sont ouvertes au télétravail total depuis la France. **Gaëtan n'est pas ouvert à la relocalisation ni au présentiel/hybride en Suisse ou aux Pays-Bas** (confirmé le 22/09/2026, même logique stricte que pour l'onglet USA) : une offre CH/NL non 100% télétravail part dans `NoRemote`, jamais dans `Offres CH-NL`.

### Critère de filtrage : le remote ouvert à la France, pas le remote local CH/NL

**Le point le plus important de cette recherche, identique au piège déjà documenté dans la section « Recherche HRIS internationale hors USA ».** Une offre suisse ou néerlandaise marquée « Remote » n'est pas automatiquement candidatable : beaucoup de postes remote en Suisse ou aux Pays-Bas exigent d'être **résident du pays ou d'y avoir une autorisation de travail** (payroll et cotisations sociales locales, surtout marqué en Suisse hors UE/AELE). Gaëtan est basé en France, sans autorisation de travail suisse ni néerlandaise.

Ne retenir que les offres explicitement ouvertes à l'international : mentions **« Remote - Worldwide »**, **« Remote - Anywhere »**, **« Remote - EMEA »**, **« Remote - Europe »**, **« Remote (International) »**, ou une entreprise déjà connue comme employeur multi-pays (souvent via une EOR type Deel/Remote.com/Oyster en arrière-plan, ou un éditeur SaaS EU qui recrute nommément "France" en plus de "Suisse"/"Pays-Bas"). Écarter (ou envoyer vers `NoRemote` avec une note) toute offre marquée **« Remote (Switzerland only) »**, **« Remote - Netherlands only »**, **« Must be based in Switzerland/the Netherlands »**, **« Swiss work permit required »** sans mention d'ouverture internationale.

En cas de doute sur une offre par ailleurs excellente, la garder avec priorité réduite et une note explicite (« éligibilité internationale à confirmer ») plutôt que de la perdre.

### Exception SIRH/SAP Suisse : présentiel/hybride accepté (posée le 22/09/2026)

**Le filtre remote strict ci-dessus ne s'applique pas aux missions SIRH/SAP en Suisse.** Gaëtan a confirmé le 22/09/2026, après un premier passage qui n'avait rien remonté d'exploitable en remote pur sur ce métier, qu'il voulait élargir spécifiquement les missions **SAP HCM/SuccessFactors/HRIS en Suisse** (Zurich, Genève, Bâle...) au présentiel et à l'hybride, même logique que l'onglet "Pays Basque" : le marché SAP suisse (banques, pharma, horlogerie) est trop important au regard de ses 14 ans d'expertise SAP pour l'écarter uniquement parce que la mission n'est pas 100% télétravail, et les TJM suisses sont nettement supérieurs aux fourchettes FR.

**Portée de l'exception, à respecter strictement :**
- **Suisse uniquement, pas les Pays-Bas** (le marché néerlandais n'a pas ce même poids SAP, l'exception ne les concerne pas).
- **SIRH/SAP uniquement** (HRIS, SAP HCM, SuccessFactors, Payroll, HR Access...), pas les autres métiers (CSM, PM, UX, SEO restent soumis au remote strict même en Suisse).
- Techniquement : marquer `RemoteExempt=True` dans le dict passé à `ajouter_offres()` (voir `add_offre.py`), en plus de `Onglet='Offres CH-NL'`. **Ne jamais déduire ce marqueur automatiquement du titre ou de la localisation** : contrairement au reste du dispositif, ce n'est pas un motif de routage détecté par regex mais une décision qu'il faut poser explicitement offre par offre, pour ne jamais faire fuiter l'exception vers un autre métier ou un autre pays par accident.
- Ces offres continuent d'atterrir dans **"Offres CH-NL"** (pas un onglet séparé), avec le champ Remote qui reflète honnêtement la réalité (« Hybride 2j/sem », « Présentiel », etc.) plutôt qu'une valeur qui laisserait croire à du télétravail confirmé.

### Postes ciblés
Mêmes familles que le reste du dispositif : CSM/Senior CSM, Technical Account Manager/Solutions Engineer/Solutions Consultant, Implementation Consultant/Onboarding Manager/Professional Services, HRIS/SIRH/SAP HCM/SuccessFactors Consultant (marché suisse très SAP, nombreuses banques et industries pharma/horlogerie à Zurich/Genève/Bâle qui tournent sur SAP HCM), Product Manager, UX/Product Designer, SEO/GEO, Formateur IA.

## Recherche HRIS internationale hors USA (Canada, UK, Australie, APAC) — ajoutée le 08/09/2026, révisée le 08/09/2026 après premier test

**Verdict du premier test (08/09/2026) : rendement nul, 0 offre retenue sur ~15 éditeurs testés avec un board exploitable.** Ne pas en faire un cluster systématique à chaque relance ; un passage ponctuel (une fois par mois environ) suffit, en se concentrant sur les deux sources ci-dessous qui bougent. Le reste de cette section documente la méthode pour ce passage ponctuel.

**Piège structurel confirmé, distinct de celui des offres USA** : contrairement aux éditeurs SaaS US qui utilisent souvent des tags "Remote-Worldwide/Anywhere/EMEA", les éditeurs HRIS canadiens/britanniques/australiens/APAC testés recrutent presque tous **par entité légale locale, pays par pays** (UK, Canada, Australie, Roumanie, Malaisie, Philippines, Vietnam comme centres de coûts distincts, jamais "n'importe où"). Le mot "Remote" dans un titre signifie ici presque toujours "remote au sein du pays d'ancrage", jamais un remote international. Sur ce premier passage, c'est systématique plutôt qu'occasionnel (contrairement aux offres USA où on trouve régulièrement des exceptions).

**Deux sources à repasser ponctuellement (bougent dans le temps), le reste n'a rien donné :**
- **API Employment Hero** (a racheté Humi/Canada et KeyPay-YouPay/Australie, gère les 3 marques sur un ATS unique) : `https://services.employmenthero.com/ats/api/v1/career_page/organisations/employmenthero/jobs?page_index=N` (pagination par `page_index`, pas `page`). 62 postes le 08/09, tous ancrés pays unique (GB/AU/CA/NZ/MY/PH/VN/RO), mais le volume justifie un contrôle périodique.
- **Access Group (UK)** sur Workday CXS : `theaccessgroup.wd103.myworkdayjobs.com/Access_Group_External_Careers`, 150 postes actifs le 08/09, tous UK-résident de fait (déplacements réguliers Londres/Loughborough exigés même sur les fiches "Remote").

Sources testées et confirmées sans board exploitable ou sans remote international, à ne pas retester avant plusieurs mois : Wagepoint (Teamtailor, Canada-only strict), League Inc (Greenhouse `leagueinc`, Canada/US/UK ancrés), Dayforce/Ceridian (aucune mention France), IRIS Software Group (Ashby `irissoftwaregroup`, 59 postes UK/Ireland/US/Romania), Zellis, Breathe HR, Personio (office-first confirmé, 3j/semaine), Sage HR, Deputy (Lever `deputy`, UK/US/AU ancrés), Darwinbox/PeopleStrong/Mekari/Talenox/HReasily (recrutement local uniquement), Humi/PandaPay/Knit People/Collage HR/Rise People (pas de board ou aucune offre), ELMO Software/Ento/HROnboard/CIPHR/MHR (pas de board exploitable trouvé).

### Critère de filtrage, identique à celui de l'onglet USA

**Même règle stricte que pour Offres USA : le remote doit être ouvert à la France, pas seulement au pays d'origine de l'entreprise.** Une offre "Remote across Canada", "Remote (Australia only)" ou "Remote - UK residents only" est à écarter (ou router en `NoRemote` avec une note), même si l'éditeur est par ailleurs un excellent fit métier. Ne retenir que "Remote - Worldwide/Anywhere/EMEA/Europe/International", ou une entreprise déjà connue comme employeur multi-pays via EOR.

**Routage** : pas de nouvel onglet dédié. Ces offres suivent le routage standard d'`add_offre.py` (SIRH/CSM/IA/PM selon le titre, NoRemote si le remote n'est pas ouvert à la France) — la nationalité canadienne/britannique/australienne/APAC de l'entreprise n'est pas en soi un critère de routage, contrairement au marqueur USA qui, lui, a son propre onglet.

### Postes ciblés
Mêmes familles que le reste du dispositif : HRIS Manager/Consultant, CSM/Senior CSM, Implementation Consultant, Solutions Engineer/TAM, Product Manager HRIS, Data Migration Lead.

---

## Recherche grosses entreprises du Sud-Ouest (onglet dédié "Pays Basque") — ajoutée le 27/08/2026

**À inclure systématiquement dans chaque relance**, au même titre que SIRH, CSM, IA, PM et USA. Demande de Gaëtan le 27/08/2026 : cibler les grosses entreprises du Sud-Ouest situées à **1h15 de route maximum de Biarritz** (donc jusqu'au bassin de Pau/Lacq et Mont-de-Marsan), tous métiers confondus parmi ceux ciblés par son profil (CSM, SIRH/SAP, PM, Formateur IA, gestion de compte, avant-vente technique...).

### Règle de routage : cet onglet échappe volontairement au filtre télétravail

**Point le plus important de cette recherche, à ne jamais oublier.** Le reste du dispositif (`add_offre.py`) envoie systématiquement dans `NoRemote` toute offre qui exclut le télétravail total (hybride, partiel, présentiel). **Cette règle ne s'applique pas à l'onglet "Pays Basque"** : ces offres sont pertinentes précisément parce qu'elles sont locales et à distance de trajet raisonnable, pas malgré leur caractère présentiel. Une offre chez TotalEnergies à Pau en présentiel reste dans "Pays Basque", elle ne part jamais dans NoRemote.

Techniquement : marquer `'Onglet': 'Pays Basque'` dans le dict passé à `ajouter_offres()`. Ce marqueur est vérifié en priorité absolue, avant même le filtre télétravail (voir `add_offre.py`, section "Ajout" de `ajouter_offres()`). L'onglet a été créé manuellement par Gaëtan dans le tableur le 27/08/2026 avec les mêmes colonnes que les autres onglets métier.

### Postes ciblés dans cet onglet
Mêmes familles que le reste du dispositif : Customer Success / Account Manager, Chef de projet SIRH / SAP HR / SAP HCM / SuccessFactors, Product Manager / Product Owner, Formateur IA / Consultant IA générative, Solutions Engineer / Technical Account Manager, Implementation Consultant, mais aussi plus largement tout poste de gestion de projet, gestion de compte, transformation digitale ou IT compatible avec le profil, vu qu'il s'agit d'un vivier local restreint (pas la peine d'être aussi strict sur l'intitulé que pour le reste du tableur).

### Extension Bordeaux et périphérie — ajoutée le 17/09/2026

**À inclure systématiquement dans chaque relance**, en plus des entreprises du bassin Pau/Lacq/Bayonne/Mont-de-Marsan listées plus haut. Demande de Gaëtan : Bordeaux est trop loin pour un présentiel régulier (hors du rayon d'1h15 de Biarritz qui justifie le reste de l'onglet), donc **ces offres ne sont retenues dans "Pays Basque" que si elles autorisent explicitement 3 jours ou plus de télétravail par semaine** (hybride 3j+/semaine, ou plus). C'est l'inverse de la règle pour le reste de l'onglet, qui elle ignore volontairement le critère télétravail.

**Critère de filtrage propre à ce sous-périmètre, à ne pas confondre avec le reste de l'onglet :**
- Retenir : mentions explicites "3 jours de télétravail/semaine", "2 jours sur site / 3 jours remote", "télétravail majoritaire", "full remote", "100% remote", ou toute formulation qui confirme sans ambiguïté 3 jours ou plus de remote par semaine.
- Écarter (ne pas ajouter, ni dans Pays Basque ni ailleurs) : hybride 1 ou 2 jours de télétravail/semaine, présentiel, ou télétravail non précisé dans le texte de l'offre. Contrairement à la règle générale des onglets métier (télétravail non renseigné = on garde), ici l'information manquante ne suffit pas : il faut une confirmation positive du nombre de jours avant d'ajouter, parce que la seule justification de inclure du Bordelais est ce volume de remote.
- Zone géographique : Bordeaux intra-muros et périphérie proche (Mérignac, Pessac, Talence, Bègles, Bruges, Le Bouscat, Villenave-d'Ornon, Bordeaux Métropole au sens large).

Techniquement : ces offres portent aussi le marqueur `Onglet: 'Pays Basque'` dans le dict transmis à `ajouter_offres()` (comme le reste de l'onglet), donc `add_offre.py` n'a pas besoin d'être modifié. Le filtre des 3j+ télétravail se fait en amont, à la lecture du texte de chaque offre, avant même de la soumettre à `ajouter_offres()` — il n'existe pas de champ structuré pour le nombre de jours de télétravail dans les sources habituelles, donc ce tri reste manuel/qualitatif à chaque relance.

**Où chercher** : mêmes familles de sources que le reste du dispositif (API France Travail avec filtre localisation Bordeaux/33, HelloWork page métier+ville Bordeaux, free-work.com, mission-freelances.fr, welcometothejungle.com, boards ATS Ashby/Lever/Greenhouse), plus les grandes entreprises et scale-ups bordelaises à contacter directement le cas échéant (à enrichir au fil des relances, pas de liste figée pour l'instant).

---

## Règles de gestion du tableur offres_emploi.xlsx

### ⚠️ RÈGLE ABSOLUE — un lien partagé par plusieurs offres différentes est presque toujours un lien générique, jamais une vraie coïncidence (posée le 21/08/2026)

**Une vraie page d'offre individuelle ne peut jamais correspondre à deux postes différents.** Si la colonne Lien contient la même URL sur deux lignes dont le Poste et/ou l'Entreprise diffèrent réellement, ce lien est presque toujours une page de recherche/catégorie/listing collée par erreur à la place du lien individuel, notamment :
- Pages de recherche **Indeed** (`fr.indeed.com/q-<mots-clés>-emplois.html`)
- Pages catégorie **LinkedIn** (`fr.linkedin.com/jobs/<mot-clé>-emplois...`) — sources de *radar* uniquement (voir plus bas), jamais un Lien final
- Pages catégorie **free-work.com** de la forme `/fr/tech-it/jobs/<mot-clé>` (à ne pas confondre avec les pages individuelles `/fr/tech-it/job-mission/<catégorie>/<slug>`, qui sont légitimes)
- La page listing **mission-freelances.fr/missions/** (sans slug individuel)

**Avant chaque relance ou chaque nouvel ajout, vérifier qu'aucun lien n'est partagé par deux offres au Poste/Entreprise différents.** Méthode : regrouper toutes les lignes de tous les onglets par valeur de colonne Lien, et pour chaque lien partagé par plus d'une ligne, comparer Poste et Entreprise après normalisation des mentions d'anonymisation (« N/C », « n.c. », « client anonymisé »...). Si au moins deux lignes ont une Entreprise clairement différente pour le même Lien, c'est le bug : retrouver l'URL individuelle réelle (nouvelle recherche ciblée sur le titre + l'entreprise), et si elle est introuvable (poste probablement pourvu depuis), **ne jamais réutiliser le lien générique** : vider la cellule Lien et documenter la raison dans Fit / Notes plutôt que de laisser un lien trompeur.

Cas à part : un lien partagé par des lignes au Poste et à l'Entreprise quasi identiques (juste une reformulation du même intitulé) n'est pas ce bug-là mais un doublon de ligne classique (la même offre ajoutée deux fois) — cas moins grave, à nettoyer en supprimant la ligne redondante plutôt qu'en cherchant un nouveau lien.

**Audits faits les 21/08 et 01/09/2026 : les onglets actifs sont entièrement propres.** Il reste un reliquat de liens génériques partagés dans `NoRemote` et `Fait` uniquement (offres déjà écartées ou traitées, priorité faible), à reprendre au fil de l'eau plutôt qu'en une passe dédiée.

Astuces trouvées pendant ces audits, à réutiliser :
- Un lien LinkedIn qui redirige vers `...?trk=expired_jd_redirect` est une preuve fiable qu'une offre est fermée (`curl -s -o /dev/null -w "%{url_effective}" -L <url>` pour le détecter sans navigateur).
- Le flux RSS carrière `career.<entreprise>.com/services/rss/job/?keywords=<mot-clé>` fonctionne très bien sur les sites SuccessFactors (Nexans, Eramet, Syensqo...) pour retrouver l'URL individuelle exacte sans passer par une recherche JS.
- L'**API Workday CXS** (`<tenant>.wdX.myworkdayjobs.com/wday/cxs/<tenant>/<site>/job/<path>`) confirme fiablement titre et statut d'un poste (fonctionne pour Strada, L-Acoustics) ; certains tenants la bloquent systématiquement (403 sur toute combinaison, cas de Valeo) — dans ce cas se contenter d'un fetch HTML 200 + titre correspondant, sans garantie à 100 %.
- Une redirection interne vers la page listing générique du site carrière (ex. `career.groupeetam.com` → 410 Gone, `talents.mc2i.fr` → redirection vers `/nos-offres`) est un signal de fermeture aussi fiable qu'un lien LinkedIn expiré.
- **Correctif à une note antérieure** : `mission-freelances.fr/missions/` n'est **pas** trop JS pour être scrapée comme indiqué précédemment — un simple `curl` avec un User-Agent navigateur retourne tous les liens individuels en clair dans le HTML source. Idem pour `free-work.com/fr/companies/<slug>/jobs`, qui liste en clair toutes les missions ouvertes d'une entreprise donnée : c'est la méthode la plus fiable pour retrouver un lien individuel free-work quand on connaît le nom du client, à privilégier sur le décodage `data-obf` qui reste réservé à freelance-informatique.fr.

### Déduplication contre l'onglet Fait — désormais automatique dans add_offre.py (corrigé le 21/08/2026)

`_liens_existants(wb)` scanne les 6 onglets (y compris Fait) au début de `ajouter_offres()`, et toute offre dont le Lien existe déjà nulle part dans le classeur est ignorée silencieusement (message `= [doublon ignoré]` en mode verbose) plutôt qu'ajoutée une seconde fois. **Ce garde-fou est automatique et ne dépend plus de la rigueur manuelle d'une session** : tant que l'insertion passe par `add_offre.ajouter_offres()`, un lien déjà connu, actif, NoRemote ou déjà classé Fait, ne peut plus être réinséré. Continuer à utiliser cette fonction (plutôt que d'écrire des scripts ponctuels qui manipulent le classeur directement) pour bénéficier de ce contrôle.

### Dédoublonnage rétroactif — `dedoublonnage_20260902.py`

Ce garde-fou ne nettoie pas rétroactivement les doublons accumulés par des relances antérieures (un même lien individuel dupliqué sur plusieurs lignes décrivant la même offre, distinct du bug des liens génériques ci-dessus). Le script `dedoublonnage_20260902.py` est réutilisable tel quel (idempotent, il rescanne à chaque exécution) et vaut la peine d'être relancé après toute session qui aurait inséré des offres sans passer par `add_offre.ajouter_offres()`. Il réutilise `_capture_cell` / `_ecrire_onglet` d'`add_offre.py`, donc les couleurs de la colonne Priorité et le tri statut+priorité sont préservés. Règle de conservation : **Fait > NoRemote > onglet métier** ; les champs manquants de la ligne conservée sont complétés depuis les lignes supprimées (entreprise nommée qui remplace un « N/C », notes les plus longues, priorité la plus haute).

**Deux pièges de comparaison à réutiliser dans tout futur dédoublonnage :**
- La colonne Entreprise porte tantôt l'employeur, tantôt la **plateforme** d'où vient l'annonce (« WorkDispo » vs « Celad », « n.c. (via Michael Page) » vs « Cabinet conseil »). Retirer les mentions entre parenthèses et les noms de plateformes avant de comparer, sinon le doublon passe inaperçu.
- Le même poste est saisi tantôt en français tantôt en anglais, ce qui casse toute comparaison d'intitulés. Quand l'employeur nommé concorde, il fait foi ; la comparaison d'intitulés ne sert qu'en dernier recours, sur les offres à client anonymisé.

**Deux pièges de fond rencontrés lors du nettoyage du 02/09, à connaître :** l'API WTTJ peut donner un poste `archived` **et** `partial` alors que la ligne d'un onglet métier le disait remote (l'API prime, garder la ligne NoRemote) ; et le titre d'un résultat WebSearch/slug peut pointer vers une offre sans rapport une fois la fiche ouverte (toujours vérifier que le nom du poste sur la page correspond bien à celui du tableur avant de trancher un doublon). Cas normal à ne pas « corriger » : le lien Arago HRIS Project Manager est présent à la fois dans `En process` et dans `Fait`, cohérent avec le statut de zone de travail manuelle d'`En process`.

### Statut "Expiré" = déplacement automatique vers Fait (règle posée le 03/09/2026)

**Dès qu'une offre a le Statut mis à `Expiré` ou `Expirée` (lien vérifié mort lors d'un contrôle de vivacité), elle doit rejoindre l'onglet `Fait`, exactement comme une ligne marquée `x` en colonne Fait.** Avant cette date, la convention était de laisser l'offre dans son onglet métier avec Statut=`Expiré`, simplement triée en bas (rang `STATUS_ORDER` le plus bas) — Gaëtan a demandé le 03/09/2026 de changer cette convention : un lien mort n'a plus sa place dans un onglet actif, il doit être archivé comme une offre traitée.

**Implémenté directement dans `add_offre.py`** : `_archiver_faits()` archive désormais vers Fait toute ligne dont `Fait=='x'` **OU** dont `Statut` (normalisé en minuscules) est dans `EXPIRE_STATUSES = {'expiré', 'expirée'}`. C'est automatique à chaque appel de `ajouter_offres()`, y compris avec une liste d'offres vide (`ajouter_offres([], verbose=True)` sert de commande de purge à la demande).

**Procédure pour un contrôle de vivacité de liens (WTTJ, HelloWork, freelance-informatique.fr ou autre) :** marquer Statut=`Expiré` sur les lignes mortes avec une note dans Fit/Notes expliquant comment la mort a été constatée (utile pour Fait, qui garde l'historique), puis appeler `add_offre.ajouter_offres([], verbose=True)` une fois toutes les lignes marquées : l'archivage vers Fait et le retri des onglets sources se font en un seul passage. Ne jamais faire ce déplacement à la main avec `openpyxl` directement, la fonction gère déjà la préservation des styles/couleurs et l'ordre.

**Fait n'est pas concerné par cette règle** : un Statut `Expiré` déjà présent dans Fait (l'offre y est déjà) ne déclenche rien de plus, et un contrôle de vivacité qui confirme la mort d'un lien déjà dans Fait ne doit **pas** changer son Statut existant (Postulé/Refusé/Pourvu...), qui reflète une action déjà prise par Gaëtan indépendamment de la vivacité ultérieure de l'annonce — voir la note du 03/09/2026 dans « Notes diverses ».

### Filtre télétravail (règle prioritaire, posée le 14/08/2026, révisée le 18/08/2026)

**`NoRemote` ne reçoit que les offres qui excluent explicitement le télétravail total.** Ce filtre s'applique **avant** le routage par métier.

Valeurs qui partent dans `NoRemote` :
- **Hybride et partiel** sous toutes leurs formes (`Hybride`, `Partiel`, `Hybride 2j/sem`, `Partiel (3j/sem)`...). Décision explicite de Gaëtan le 14/08/2026 : le télétravail partiel ne suffit pas, et il l'a reconfirmée le 18/08.
- **Présentiel**, `Sur site` et `Non`.

Valeurs qui **restent** dans les onglets métier :
- Le télétravail confirmé : `Oui` et ses variantes entre parenthèses, `Full remote`, `Remote`, `Remote-first`, `Remote Europe`, `100% remote`, `Télétravail total`, `yes`, `En ligne`.
- **L'information manquante**, depuis la révision du 18/08/2026 : cellule vide, `n.p.`, `nc`, `N/C`, `Non précisé`, `À vérifier`, `À clarifier`, `À confirmer`, `Non confirmé`. Une offre dont le télétravail n'est pas renseigné n'est plus écartée ; elle reste dans son onglet métier, à charge de clarifier au moment de candidater.

Un marqueur d'hybride l'emporte sur la présence du mot « remote » : `Hybride (3j remote + 2j sur site)` part dans `NoRemote`.

La fonction `accepte_remote()` d'`add_offre.py` implémente cette règle et le routage est automatique.

- **Neuf onglets d'offres** : `Offres SIRH`, `Offres CSM`, `Offres IA`, `Offres PM`, `Offres UX` (ajouté le 10/09/2026), `Offres SEO` (ajouté le 11/09/2026), `Offres USA` (ajouté le 22/08/2026), `Offres CH-NL` (ajouté le 22/09/2026), `NoRemote`, plus `Fait`. (L'onglet `Légende` a été supprimé le 14/08/2026 ; ne pas le recréer. L'onglet `En process` est une zone de travail manuelle de Gaëtan pour une négociation en cours, hors dispositif `add_offre.py` : ne jamais l'automatiser ni la vider.) Le routage est automatique dans `add_offre.py` : **USA d'abord** (dès qu'une offre vient d'une entreprise basée aux USA — marqueur explicite `Onglet='Offres USA'` dans le dict, ou détection sur la Localisation), **puis CH-NL** (même logique pour la Suisse/Pays-Bas, marqueur explicite `Onglet='Offres CH-NL'` ou détection sur la Localisation), puis IA, puis CSM, puis PM, puis UX, puis SEO, sinon SIRH. Une offre Product Manager ou UX/UI dont l'intitulé porte aussi un marqueur SIRH ou SAP (« Product Owner HRIS », « UX Designer SuccessFactors ») reste dans `Offres SIRH` ; le métier SIRH prime sur le titre. Le filtre télétravail (`NoRemote`) reste prioritaire sur tout, y compris sur USA et CH-NL : une offre non ouverte au remote international part dans `NoRemote`, pas dans l'onglet pays.
- **Ne jamais supprimer une ligne** du tableau, même si une offre semble expirée ou hors profil — changer le statut à la place.
- **Toujours trier par priorité décroissante** (⭐⭐⭐⭐⭐ en premier) après chaque ajout de nouvelles offres. Préserver les styles de couleur des cellules lors du tri.
- **Appliquer la couleur de fond** à la colonne Priorité pour chaque nouvelle ligne ajoutée : rouge (⭐⭐⭐⭐⭐), orange (⭐⭐⭐⭐), jaune/or (⭐⭐⭐), vert (⭐⭐), gris (⭐).

### Colonne Statut à la création d'une offre (règle posée le 09/09/2026, révisée le même jour)

**Une offre pas encore traitée ne porte ni "Nouveau" ni "À postuler" dans la colonne Statut : elle porte une date, au format ISO `YYYY-MM-DD`.** Priorité à la date de publication de l'annonce (`Date publiée`) quand elle est connue ; à défaut, la date à laquelle l'offre a été ajoutée au tableur (`Date trouvée`). Ce n'est qu'une fois l'offre traitée (candidature envoyée, refus, poste pourvu, lien mort...) que le Statut redevient un mot-clé classique (`Postulé`, `Refusé`, `Expiré`...).

Cette règle a remplacé le même jour une première version qui demandait de mettre systématiquement "À postuler" : Gaëtan a précisé vouloir une date à la place, plus informative qu'un simple mot-clé. Un reliquat de lignes anciennes n'a ni `Date publiée` ni `Date trouvée` renseignée et a été laissé inchangé plutôt que de leur inventer une date ; à reprendre au fil de l'eau si une de ces offres redevient pertinente, pas à corriger en masse avec une date arbitraire.

Techniquement, cette convention ne casse rien dans `add_offre.py` : `STATUS_ORDER` ne reconnaît que `Postulé`/`Refusé`/`Expiré`/`Expirée`, tout le reste (dates y compris) tombe dans le rang par défaut `STATUS_DEFAUT`, donc le tri se comporte exactement comme avant.

---

