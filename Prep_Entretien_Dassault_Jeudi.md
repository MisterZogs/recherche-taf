# Entretien Dassault Systèmes — jeudi 9h
## Brief consolidé post-appel Laurent Tarnat

---

## Dassault Systèmes — chiffres clés à connaître

### Dirigeante RH — point critique

**Laurence Barthès — Executive Vice President, Chief People & Information Officer**

Elle est à la fois DRH ET DSI. Double portefeurique rare : elle a l'autorité RH et l'autorité IT dans le même périmètre. Le projet SIRH est au cœur de sa fonction. La décision sur l'architecture (cloud souverain, ECP, intégrateur) passe par elle. Si elle est dans la salle jeudi, tu sais à qui tu parles.

Autres dirigeants à connaître :
- **Pascal Daloz** — CEO (a remplacé Bernard Charlès récemment)
- **Florence Verzelen** — EVP EMEA
- **Rouven Bergmann** — CFO

### Effectifs et géographie

- ~**26 000 collaborateurs** dans le monde
- **184 sites**, **159 pays** avec clients actifs
- Répartition : **41% Europe / 32% Asie-Pacifique / 27% Amériques**
- **41% des effectifs en R&D** — culture d'ingénieurs confirmée

### Financier

- **CA 2025 : 6,24 milliards €** (+4% à taux constants)
- **82% de revenus récurrents**
- Répartition du CA : USA 47%, France 16%, reste Europe 12%, Asie 19%
- Le marché américain domine — l'anglais est la langue de travail interne

### Ce que tu places en entretien

- *"26 000 collaborateurs dans 159 pays, c'est un périmètre comparable à L'Oréal — même complexité multi-pays, mêmes enjeux core vs local."*
- *"J'ai travaillé dans un contexte similaire d'ingénieurs — L'Oréal est une entreprise de science. Le métier RH y est exigeant sur la preuve, pas sur l'intention. C'est une posture que j'ai naturellement."*

---

## Contexte confirmé

- **Format** : plusieurs interlocuteurs Dassault Systèmes + Laurent Tarnat (HR Path), jeudi 9h
- **Tu dépends de l'entité Conseil** chez HR Path (pas paramétrage, pas intégration)
- **Besoin exprimé** : expert SF senior pour migrer PeopleSoft vers SF
- **Culture client** : ingénieurs — valorisent la rigueur, les faits, les exemples concrets

### Cartographie SIRH Dassault Systèmes aujourd'hui

| Brique | Système actuel | Destination probable |
|---|---|---|
| Core HR / donnée maître | **PeopleSoft** (Oracle) | **SF Employee Central (EC)** |
| Paie | **Meta4** | À définir : meta4 maintenu + interface EC, ou remplacé par **ECP** |
| Recrutement | **Taleo** (Oracle) | Probablement SF Recruiting — à confirmer en entretien |

---

## EC vs ECP — comprendre avant d'entrer dans la salle

### Employee Central (EC)

EC est le **Core HR de SuccessFactors**. Il stocke la donnée maître employé dans le cloud :
- Personal data (nom, adresse, données personnelles)
- Employment data (contrat, statut, temps de travail)
- Job & Organisation data (position, département, cost center, manager)
- Compensation data (salaire de référence)

**EC ne calcule pas la paie.** Il la nourrit. Il pousse des événements (augmentation, départ, embauche, changement de poste) vers la paie. Actuellement chez Dassault, PeopleSoft remplit ce rôle ; Meta4 reçoit les données de PeopleSoft et calcule.

### Employee Central Payroll (ECP)

ECP est le **moteur de paie SAP hébergé dans le cloud SuccessFactors**. Techniquement, c'est l'ancien moteur SAP HR Payroll (les mêmes schémas, les mêmes clusters, la même logique de calcul) mais opéré par SAP dans son infrastructure cloud. Il se connecte directement à EC, sans interface externe à maintenir.

### La logique de Laurent Tarnat

> « Si t'as un EC, mettre un ECP. »

Le raisonnement est simple : si on migre la donnée maître vers EC, il faut connecter la paie à EC. Deux chemins :

**Option A — EC + ECP (tout SAP)**
- La donnée maître est dans EC
- ECP la lit directement, sans interface
- Un seul fournisseur, un seul contrat, une seule chaîne de mises à jour
- Avantages : cohérence, moins d'intégrations, SAP gère l'infrastructure
- Inconvénients : migration Meta4 → ECP = projet paie à part entière (schémas de paie, règles locales, tests de régression, re-formation des équipes paie)

**Option B — EC + Meta4 maintenu**
- EC devient la donnée maître
- Meta4 reste le calculateur de paie
- Il faut construire et maintenir une interface EC → Meta4 (format d'échange, fréquence, gestion des erreurs)
- Avantages : pas de migration paie, moins de risque sur les bulletins, équipes paie ne changent pas d'outil
- Inconvénients : deux systèmes à maintenir, interface à gérer, complexité lors des upgrades SF

**Ce que tu dois demander en entretien** : "Meta4 est-il dans le périmètre de ce projet, ou est-ce qu'on part sur une intégration EC vers Meta4 maintenu ?"

La réponse conditionne toute l'architecture. Si Meta4 reste, il faut commencer à penser aux flux : quelles données partent de EC vers Meta4, à quelle fréquence, dans quel format (API, fichier plat, middleware), et qui gère les erreurs.

---

## SAP for HANA vs Cloud Souverain

Laurent se demande si Dassault ira vers l'un ou l'autre. Tu dois pouvoir en parler si la question vient.

### SAP S/4HANA (pour mémoire)

S/4HANA est l'ERP SAP nouvelle génération qui tourne sur la base de données HANA (in-memory). Il contient un module RH de base, mais la stratégie SAP est claire depuis 2012 : **les RH vont dans SuccessFactors, pas dans S/4HANA**. S/4HANA et SF coexistent via intégrations (finance ↔ paie, etc.). Quand on parle de migration vers SF, S/4HANA n'est pas une alternative ; c'est un sujet parallèle (si Dassault a aussi un ERP SAP à moderniser).

### Cloud Souverain

Le cloud souverain est une infrastructure cloud qui garantit trois choses :
1. **Résidence des données en France ou dans l'UE** — les données RH ne quittent pas le territoire
2. **Opérateur non soumis au CLOUD Act américain** — une entreprise US hébergeant des données peut être contrainte de les communiquer aux autorités américaines, même si le serveur est en Europe ; un opérateur souverain coupe ce risque
3. **Certification de sécurité reconnue** — SecNumCloud (ANSSI), C5, ISO 27001 niveau renforcé

**En France, les acteurs du cloud souverain :**
- **OVHcloud** — certifié SecNumCloud
- **Bleu** (Capgemini + Microsoft) — en cours de certification, partenaire SAP pour cloud souverain France
- **S3NS** (Thales + Google) — en cours

**SAP et le cloud souverain :** SAP a signé un partenariat avec Bleu pour proposer ses solutions (BTP, SuccessFactors) sur cloud souverain français. L'offre existe mais est encore jeune ; toutes les fonctionnalités SF ne sont pas forcément disponibles en mode souverain.

### Pourquoi c'est un enjeu pour Dassault Systèmes

Dassault Systèmes est éditeur logiciel (3DEXPERIENCE), pas un OIV (Opérateur d'Importance Vitale) au sens de la loi de programmation militaire. Mais :
- Ils travaillent avec des clients défense et aéronautique qui ont des exigences de sécurité très fortes
- Leur capital intellectuel (code source, roadmap produit) justifie des politiques data très strictes
- Les données RH contiennent des informations sur des personnes habilitées ou sur des postes sensibles
- La réglementation NIS2 (transposée en France en 2024) renforce les exigences sur les opérateurs essentiels

### Avantages cloud souverain pour Dassault

- Conformité ANSSI et politiques de sécurité internes
- Protection contre le CLOUD Act US (SAP, même s'il est allemand, utilise des hyperscalers US comme AWS)
- Données RH ne quittent pas la France
- Argument réglementaire auprès de leurs clients défense

### Inconvénients cloud souverain

- Fonctionnalités SF réduites : toutes les releases SF ne sont pas disponibles en souverain au même moment
- Coût plus élevé qu'un cloud standard
- Écosystème partenaires plus restreint
- Déploiement plus complexe, délais plus longs
- Moins de retours d'expérience (marché jeune, peu de projets réalisés)
- Mises à jour moins fréquentes que SF standard

### Ce que tu peux dire si on te pose la question

> "La décision cloud souverain vs cloud standard doit être tranchée avant le design fonctionnel, pas après. Elle conditionne les modules SF disponibles, les options d'intégration avec Meta4 ou ECP, et le contrat SAP. Je recommande de clarifier dès le cadrage les exigences ANSSI et les contraintes de résidence des données. Si vous êtes soumis à des politiques groupe sur le cloud souverain, c'est un élément non-négociable à poser sur la table au démarrage."

---

## Points d'attention à mentionner en entretien

### Double saisie pendant et après la migration

Pendant la période de transition — entre le moment où SF EC est en production et celui où PeopleSoft est officiellement décommissionné — les équipes RH risquent de devoir saisir les mêmes informations dans les deux systèmes : tout mouvement (embauche, promotion, départ) saisi dans SF doit parfois être resaisi dans PeopleSoft tant que celui-ci alimente encore d'autres processus (paie Meta4, reporting legacy, badge, Active Directory...).

C'est un point d'attention majeur pour trois raisons :

1. **Charge de travail** — les RH font deux fois le travail pendant une période qui peut durer plusieurs semaines ou mois selon le planning de décommissionnement
2. **Risque de divergence** — une saisie oubliée ou différente entre les deux systèmes crée une incohérence qui peut bloquer la paie ou fausser le reporting
3. **Question de gouvernance** — pendant la cohabitation, quel système fait foi ? SF ou PeopleSoft ?

**Ce que tu peux dire en entretien :**

> "Un point d'attention que j'anticipe sur ce type de migration : la période de double saisie entre le go-live SF et le décommissionnement effectif de PeopleSoft. C'est souvent sous-estimé côté charge RH et risque de divergence. Il faut planifier très précisément cette fenêtre — idéalement la réduire au maximum — et décider dès le cadrage quel système est la donnée maître pendant cette cohabitation. Sur L'Oréal on avait imposé une règle simple : dès le go-live SF, SF est la donnée maître ; PeopleSoft est alimenté par interface en lecture seule le temps du décommissionnement, les RH ne saisissent plus dedans."

---

## À clarifier avec Laurent Tarnat AVANT l'entretien

- **"HR Path fait-il uniquement le conseil AMOA sur ce projet, ou aussi l'implémentation technique ?"** — si HR Path est aussi l'intégrateur, ta posture de "challenger" change : tu collabores avec des collègues indirects, pas avec un prestataire externe. Calibre ça avec Laurent avant d'entrer dans la salle.

---

## Ce que tu sais sur PeopleSoft

PeopleSoft est un SIRH Oracle historique, répandu dans les grandes entreprises françaises des années 2000. Sa logique est différente de SF EC ; c'est un point d'attention majeur pour la migration.

**Différences clés PeopleSoft vs SF EC :**

| Concept | PeopleSoft | SF Employee Central |
|---|---|---|
| Unité de base | **Job Code** (fonction générique) | **Position** (poste individuel) |
| Organisation | Business Unit / Department / Location | Company / BU / Division / Department / Location |
| Personnalisation | Très forte, souvent mal documentée | Configurable via MDF, mais encadrée |
| Historique | Long (parfois 20-30 ans de données) | Reprise partielle en général |
| Self-service | Variable selon les déploiements | Natif et central |

**Pièges de migration PeopleSoft → SF EC que tu peux citer :**

1. **Job Code vs Position** : PeopleSoft gère des Job Codes (ex : "Ingénieur logiciel senior") ; SF EC est position-centric (ex : "Poste #12345 — Ingénieur logiciel senior, équipe 3DEXPERIENCE Paris"). La migration implique de créer un référentiel de postes qui n'existe peut-être pas dans PeopleSoft. C'est souvent un chantier de gouvernance en soi.

2. **Mapping organisationnel** : les Business Units PeopleSoft ne se mappent pas directement sur la hiérarchie fondation SF (Company → BU → Division → Department → Location). Ce mapping doit être fait avec la DRH et la Finance — c'est du cadrage fonctionnel pur.

3. **Donnée personnalisée** : PeopleSoft est très configurable. Il peut y avoir des champs ou des tables métier customs qui n'ont aucun équivalent standard SF. Chaque champ custom = décision de migration (standard SF, MDF custom, ou abandon).

4. **Données historiques** : reprendre 15 ans d'historique PeopleSoft vers SF EC est coûteux et risqué. La reprise est souvent limitée à N-2 ou N-3 ans, avec archivage du reste. C'est une décision métier.

5. **Interface Meta4** : si Meta4 reçoit aujourd'hui des données de PeopleSoft, la question est : dans quel format, avec quelle fréquence, et qui est la donnée maître de la paie — PeopleSoft ou Meta4 ? Si les gestionnaires paie saisissent directement dans Meta4, il y a peut-être une divergence entre les deux systèmes.

---

## Questions à poser jeudi

### Gouvernance de la donnée

- "Aujourd'hui, quelle est la donnée maître employé pour la paie — PeopleSoft ou Meta4 ? Meta4 reçoit-il une interface de PeopleSoft, ou les équipes paie saisissent-elles elles-mêmes dans Meta4 ?"
- "En cas de divergence entre PeopleSoft et Meta4 sur une information employé — par exemple le salaire ou le statut de contrat — quel système fait foi ?"
- "Qui est responsable de la création des postes et des mouvements organisationnels dans PeopleSoft — la DRH corporate, les RH pays, ou la DSI ?"
- "Y a-t-il un référentiel de postes aujourd'hui dans PeopleSoft, ou travaillez-vous principalement avec des Job Codes ?"

### Qualité de la donnée et périmètre de migration

- "Avez-vous fait un audit de la donnée PeopleSoft ? Quelle est votre évaluation de sa qualité — doublons, postes sans titulaire, données obsolètes ?"
- "PeopleSoft est-il la seule source de vérité, ou y a-t-il des données RH qui vivent dans des fichiers Excel ou des outils locaux ?"
- "Quelle est la stratégie sur l'historique — reprise complète, reprise sur N-X ans, ou archivage séparé ?"
- "Y a-t-il des champs ou des fonctionnalités très spécifiques dans PeopleSoft que vous utilisez et qui n'ont pas d'équivalent standard SF ?"

### Périmètre et scope

- "Meta4 est-il dans le périmètre de ce projet, ou est-ce qu'on part sur une intégration EC vers Meta4 maintenu ?"
- "Taleo pour le recrutement — est-il remplacé en même temps que PeopleSoft, ou c'est un chantier séparé ?"
- "Combien de pays sont dans le périmètre ? Quelle est la logique de priorisation des vagues ?"
- "Y a-t-il d'autres systèmes interfacés avec PeopleSoft aujourd'hui — gestion des temps, badgeage, Active Directory, ERP finance ?"

### Cloud et hébergement

- "Est-ce que Dassault Systèmes a des exigences de résidence des données ou de cloud souverain pour son SIRH ? Êtes-vous soumis à des certifications de sécurité particulières ?"
- "La question de l'hébergement SF — cloud souverain ou cloud SAP standard — a-t-elle été tranchée ?"

### Organisation du projet

- "L'intégrateur est-il déjà retenu, ou êtes-vous encore en sélection ? Et qui est-il ?"
- "Quelle est la structure de l'équipe côté Dassault — HRIS Manager, DPO, DRH corporate, DSI ?"
- "Quel est le sponsor du projet — côté RH, côté DSI, ou les deux ?"
- "Qu'est-ce qui motive la migration maintenant — fin de maintenance PeopleSoft, décision stratégique groupe, ou les deux ?"
- "Quel est le planning cible pour le go-live de la première vague ?"

### Conduite du changement

- "Comment les équipes RH utilisent-elles PeopleSoft aujourd'hui — self-service ou tout passe par l'équipe SIRH ?"
- "Les managers ont-ils accès à PeopleSoft, ou l'outil est-il utilisé uniquement par les RH ?"
- "Y a-t-il déjà un programme de conduite du changement prévu, ou c'est dans le scope de la mission ?"

---

## Comment positionner ton expérience sur ce contexte PeopleSoft → SF

La plupart de ton expérience est SAP HR → SF EC (L'Oréal). PeopleSoft → SF EC suit la même logique fonctionnelle — c'est toujours une migration de donnée maître vers un nouveau modèle de données SF. Ce que tu dois adapter dans ton discours :

> "Mon expérience directe est SAP HR → SF EC chez L'Oréal. La migration depuis PeopleSoft suit la même logique fonctionnelle : définir le modèle organisationnel SF, faire le mapping des données source, piloter la reprise, et cadrer les règles de gestion pays. La principale différence est dans la structure de la donnée source — PeopleSoft est orienté Job Code là où SF EC est position-centric, ce qui crée un chantier de gouvernance sur la création du référentiel de postes. C'est exactement le type de sujet que j'anticipe et que je prends en charge."

---

## Chiffres clés à garder en tête (inchangés)

- 15 ans SIRH, 14 ans SAP
- 10 ans sur le compte L'Oréal mondial (Fortune 370), 40+ pays
- Go-live OneProfile (SAP HR → SF EC)
- Go-live OnePayroll (paie mondiale centralisée)
- RFP externalisation TMA piloté et gagné
- 7 ans de remote continu
- Disponible : 10 août 2026 — TJM cible : 750€ HT/j
