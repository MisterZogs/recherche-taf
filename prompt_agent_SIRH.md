# Prompt – Agent de recherche d'emploi SIRH / CSM / Formateur IA

Copier-coller ce prompt dans Claude Code (ou tout autre assistant IA avec accès aux outils).

---

## Prompt

```
Je cherche un emploi en France, 100% remote de préférence, CDI ou mission freelance.
Mes trois cibles principales sont :
1. Consultant SIRH / SAP HCM / SAP SuccessFactors / Chef de projet SIRH / AMOA SIRH /
   Pre-sales HR Tech / Group HRIS Manager
2. Customer Success Manager Senior (SaaS B2B, enterprise, français + anglais)
3. Formateur IA générative / Consultant conduite du changement IA / IA x SIRH

Crée-moi un fichier Excel "offres_emploi.xlsx" qui liste les offres actuellement
disponibles, avec exactement ces 15 colonnes dans cet ordre :
Priorité | Statut | Fait | Poste | Entreprise | Source | Contrat | Localisation |
Remote | Salaire / TJM | Durée mission | Fit / Notes | Lien | CV à envoyer | Prétention

Le fichier doit avoir quatre onglets :
- "Offres SIRH" (consultants SIRH, SAP HCM/SF, chef de projet, AMOA, pre-sales RH)
- "Offres CSM" (Customer Success Manager, Account Manager, Success Consultant SaaS)
- "Offres IA" (formateur IA, consultant IA générative, conduite du changement IA, IA x SIRH)
- "Fait" (archive vide)

─────────────────────────────────────────
MISE EN FORME
─────────────────────────────────────────
La colonne Priorité utilise des étoiles (⭐ à ⭐⭐⭐⭐⭐) avec ces couleurs de fond :
- ⭐⭐⭐⭐⭐ → rouge  (FF0000)
- ⭐⭐⭐⭐   → orange (FF8C00)
- ⭐⭐⭐     → or     (FFD700)
- ⭐⭐       → vert   (70AD47)
- ⭐         → gris   (969696)

En-tête bleu foncé (1F3864), texte blanc, lignes alternées bleu clair (F2F7FF) / blanc.
Freeze la première ligne. Filtre automatique sur toutes les colonnes.

─────────────────────────────────────────
CRITÈRES DE NOTATION — ONGLET OFFRES SIRH
─────────────────────────────────────────
- ⭐⭐⭐⭐⭐ : full remote + SAP HCM/SuccessFactors senior + grands comptes internationaux,
  OU Group HRIS Manager, OU Directeur de Programme SIRH, OU Pre-sales/Solution Advisor SAP
- ⭐⭐⭐⭐   : cabinet SIRH spécialisé (HR Path, ACT-ON, Arago, DXC, Deloitte HR...), mission
  freelance TJM affiché et télétravail partiel, chef de projet SIRH senior remote
- ⭐⭐⭐     : consultant SIRH confirmé hybride IDF, AMOA SIRH, Workday/SF/SAP sans TJM affiché
- ⭐⭐       : CDI présentiel obligatoire, SIRH non-SAP junior
- ⭐         : junior/stage, CDD court, hors profil

─────────────────────────────────────────
CRITÈRES DE NOTATION — ONGLET OFFRES CSM
─────────────────────────────────────────
- ⭐⭐⭐⭐⭐ : full remote + profil senior + français requis + plateforme SaaS enterprise, OU
  poste au croisement CSM + HRIS/RH (ex : Deel, Remote.com, Oyster, Workday)
- ⭐⭐⭐⭐   : remote EU/EMEA confirmé, senior ou strategic CSM, anglais + français, scale-up
  bien financée (Ashby, Maze, Mural, n8n, HackerOne...)
- ⭐⭐⭐     : remote partiel ou EMEA sans filtre géo FR, CSM mid-market bon fit
- ⭐⭐       : salaire en dessous du marché senior (<60K€) ou présentiel
- ⭐         : junior, stage, hors profil

─────────────────────────────────────────
CRITÈRES DE NOTATION — ONGLET OFFRES IA
─────────────────────────────────────────
- ⭐⭐⭐⭐⭐ : full remote + formateur IA générative ou change manager IA + grands groupes,
  OU croisement IA x SIRH / IA x RH (déploiement IA dans HRIS, programme transformation IA RH)
- ⭐⭐⭐⭐   : freelance formateur IA générative télétravail, PMO programme IA, consultant
  conduite du changement IA remote ou hybride IDF
- ⭐⭐⭐     : formateur IA présentiel province, consultant IA partiel, mission courte
- ⭐⭐       : profil data science pur (Python, RAG, MLOps) ou junior IA
- ⭐         : hors profil (dev LLM, ingénieur ML)

Trie les offres par priorité décroissante au sein de chaque onglet. Statut par défaut :
"À postuler".

─────────────────────────────────────────
ROUTING DES OFFRES ENTRE ONGLETS
─────────────────────────────────────────
- "Offres IA" : si le titre contient Formateur IA, Formation IA, IA générative,
  Intelligence Artificielle, AI Trainer, GenAI, LLM, Prompt, Change Manager IA,
  Conduite du changement IA, IA x SIRH, IA x RH
- "Offres CSM" : si le titre contient Customer Success, CSM, Success Manager,
  Account Manager (SaaS)
- "Offres SIRH" : tout le reste (SIRH, SAP, HRIS, Chef de projet, AMOA, pre-sales RH)

─────────────────────────────────────────
SITES À SCRAPER — OFFRES SIRH / SAP
─────────────────────────────────────────
Boards spécialisés SAP / SIRH :
- eursap.eu/sap-jobs/
- free-work.com/fr/tech-it/jobs/sap-hcm
- free-work.com/fr/tech-it/jobs/sap-successfactors
- free-work.com/fr/tech-it/job-mission/administrateur-applicatif-erp-crm-sirh/
- free-work.com/fr/tech-it/job-mission/consultant-moa-amoa/
- freelance-informatique.fr/missions/sirh
- freelance-informatique.fr/missions/sap-hr
- whitehallresources.com
- movementgroup.uk
- opusresourcing.com

Cabinets SIRH — pages carrière :
- jobs.hr-path.com/jobs
- lehibou.com (via free-work.com/fr/companies/lehibou/jobs)
- careers.soprasteria.fr/
- jobs.eviden.com/?search=SAP+HR
- www.zalaris.com/careers/
- www.expleo.com/fr/carrieres/nos-offres/
- apply.deloitte.com/careers/SearchJobs/?3_56_3=300060
- careers.ey.com/ey/search/?q=SIRH+SAP&locationsearch=France

LinkedIn (méthode catégorie — fetch direct, ne pas chercher par texte) :
- fr.linkedin.com/jobs/successfactors-emplois-région-de-paris-france
- fr.linkedin.com/jobs/hris-emplois
- fr.linkedin.com/jobs/consultant-sirh-emplois
- fr.linkedin.com/jobs/sap-hcm-emplois

Boards généralistes France :
- apec.fr (recherche "consultant SIRH SAP SuccessFactors")
- hellowork.com/fr-fr/emplois/consultant-sirh.html
- welcometothejungle.com (recherche "consultant SIRH", "SAP SuccessFactors")

WebSearch à lancer :
- "consultant SAP SuccessFactors freelance France remote 2026"
- "chef de projet SIRH senior remote CDI France 2026"
- "AMOA SIRH SAP SuccessFactors mission freelance 2026"
- site:jobs.ashbyhq.com HRIS OR SIRH remote 2026

─────────────────────────────────────────
SITES À SCRAPER — OFFRES CSM
─────────────────────────────────────────
ATS directs (WebSearch) :
- WebSearch : site:jobs.ashbyhq.com "customer success" EMEA remote "french"
- WebSearch : site:jobs.lever.co "customer success manager" remote France 2026
- WebSearch : site:boards.greenhouse.io "customer success" remote France 2026

Boards remote monde :
- app.welcometothejungle.com/jobs?remoteOnly=true&query=customer+success+manager
- remoteok.com/remote-customer-success-jobs (WebSearch si bloqué)
- euremotejobs.com (WebSearch : "customer success manager" EMEA remote 2026 site:euremotejobs.com)
- himalayas.app/jobs/customer-success
- remotive.com/remote-jobs/customer-service

Boards VC portfolio (WebSearch) :
- WebSearch : site:jobs.a16z.com "customer success" remote
- WebSearch : site:careers.balderton.com "customer success"

Boards FR + généralistes :
- welcometothejungle.com (recherche "customer success manager" remote)
- apec.fr (recherche "customer success manager")
- fr.linkedin.com/jobs/customer-success-manager-emplois-france

Éditeurs HRIS (poste CSM / Implementation) :
- jobs.ashbyhq.com/deel (Deel CSM)
- workday.wd5.myworkdayjobs.com/Workday
- WebSearch : "Oyster HR customer success manager EMEA 2026"
- WebSearch : "Remote.com customer success manager EMEA 2026"

─────────────────────────────────────────
SITES À SCRAPER — OFFRES FORMATEUR IA / CONSULTANT IA
─────────────────────────────────────────
- free-work.com/fr/tech-it/jobs/ia
- free-work.com/fr/tech-it/jobs/ia-generative
- free-work.com/fr/tech-it/job-mission/assistant-chef-de-projet/ (filtre IA)
- free-work.com/fr/tech-it/job-mission/consultant/ (filtre IA)
- mission-freelances.fr/missions/
- welcometothejungle.com (recherche "formateur IA", "consultant IA générative")
- WebSearch : "formateur IA freelance mission remote France 2026"
- WebSearch : "consultant IA générative conduite du changement freelance France 2026"
- WebSearch : "IA x SIRH consultant formateur France 2026"
- WebSearch : "change manager IA générative freelance remote France 2026"
- ai-jobs.net (recherche "customer success" ou "change manager")

Pour chaque offre, remplis : titre exact du poste, entreprise, source du site,
type de contrat (CDI/Freelance/Mission), ville, remote (Oui/Partiel/Non), salaire
ou TJM si affiché, durée si mission freelance, une courte note de contexte, et le lien
direct vers l'offre. Vise 40 à 60 offres par onglet.

─────────────────────────────────────────
COLONNE "CV À ENVOYER" — ADAPTATION DU CV
─────────────────────────────────────────
Si je te fournis mon CV (en HTML, Word, PDF ou texte), pour chaque offre tu dois :
1. Analyser les mots-clés et exigences de l'offre.
2. Créer une version adaptée qui met en avant les expériences et compétences les plus
   pertinentes (sans inventer d'éléments absents du CV — seulement réorganiser,
   reformuler et mettre en valeur).
3. Sauvegarder sous : CV_[Prénom][NOM]_[NomEntreprise].html (+ PDF si possible).
4. Écrire ce nom dans la colonne "CV à envoyer" de la ligne concernée.

Ne pas adapter le CV pour les offres ⭐ ou ⭐⭐ sauf demande. Commencer par ⭐⭐⭐⭐⭐ et ⭐⭐⭐⭐.

─────────────────────────────────────────
COLONNE "PRÉTENTION"
─────────────────────────────────────────
Pré-remplis avec une fourchette cible selon le type de poste :

SIRH :
- CDI Consultant SIRH confirmé : 55-70K€
- CDI Consultant SIRH senior / Chef de projet (7+ ans) : 70-85K€
- CDI Group HRIS Manager / Directeur de Programme : 90-110K€
- CDI Pre-sales / Solution Advisor SAP : 95-115K€
- Freelance / Mission SIRH senior : 650-750€/j
- Freelance / Mission Chef de projet SIRH : 600-700€/j

CSM :
- CDI CSM Senior / Account Manager : 80-95K€
- CDI CSM Enterprise grand compte : 90-110K€
- CDI Pre-sales / Solution Consultant HR Tech : 95-115K€

Formateur IA / Consultant IA :
- Mission freelance formateur IA : 600-800€/j
- CDI Change Manager IA / Responsable transformation IA : 70-90K€
- Mission PMO programme IA : 650-750€/j

Je pourrai ajuster ces valeurs manuellement au cas par cas.

─────────────────────────────────────────
WORKFLOW — COMMENT UTILISER LE FICHIER
─────────────────────────────────────────
Colonne "Statut" — valeurs possibles :
  À postuler | Postulé | En cours | Refusé | Expiré | Hors profil

Colonne "Fait" — pour archiver une offre :
  Écrire "x" dans cette cellule. Lors de la prochaine mise à jour, toutes les lignes
  marquées "x" sont automatiquement déplacées vers l'onglet "Fait".

─────────────────────────────────────────
MISE À JOUR ULTÉRIEURE
─────────────────────────────────────────
Pour relancer une recherche et ajouter de nouvelles offres au fichier existant, dire :
"Relance une recherche d'offres SIRH, CSM et Formateur IA sur tous les sites et ajoute
les nouvelles trouvées dans offres_emploi.xlsx. Avant d'ajouter, déplace les lignes
marquées 'x' dans la colonne Fait vers l'onglet Fait. Ne supprime jamais une ligne
existante. Trie chaque onglet par priorité décroissante."

─────────────────────────────────────────
GÉNÉRATION DU FICHIER
─────────────────────────────────────────
Génère le fichier avec Python (bibliothèque openpyxl) et exécute le script directement.
```

---

## Notes pour l'utilisation

- **Adapter le ranking** : précise ta spécialité (SAP HCM Payroll, SuccessFactors EC,
  conduite du changement, migration de données...) ou tes contraintes (uniquement
  freelance, uniquement remote, uniquement France) pour que l'IA affine les ⭐.

- **Donner son CV** : idéalement en HTML ou texte brut pour faciliter l'adaptation.
  Un PDF est lisible mais moins éditable.

- **TJM / salaires de référence France 2026 :**

  SIRH / SAP :
  - Consultant SIRH junior (0-3 ans) : 400-550€/j | 40-55K€ CDI
  - Consultant SIRH confirmé (3-7 ans) : 550-700€/j | 55-70K€ CDI
  - Consultant SAP HCM/SF senior (7+ ans) : 650-800€/j | 70-85K€ CDI
  - Chef de projet SIRH senior : 650-750€/j | 70-85K€ CDI
  - Directeur de Programme SIRH : 750-950€/j | 90-110K€ CDI
  - Pre-sales / Solution Advisor SAP : 95-115K€ CDI

  CSM :
  - CSM Senior / Account Manager : 80-95K€ CDI
  - CSM Enterprise / Strategic : 90-115K€ CDI

  Formateur IA / Consultant IA :
  - Formateur IA générative freelance : 600-800€/j
  - Change Manager IA CDI : 70-90K€
  - PMO programme IA freelance : 650-750€/j
