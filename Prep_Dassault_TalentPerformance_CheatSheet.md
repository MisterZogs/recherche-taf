# Cheat sheet — SF Talent & Performance
## Ce que tu dois savoir pour tenir l'entretien Dassault

---

## Le vocabulaire SF, sans jargon

Dans SAP SuccessFactors, "Talent" n'est pas un module unique ; c'est une **suite de modules** greffés sur Employee Central (la donnée maître). Les cinq briques historiques :

- **Performance & Goals** (PMGM) — évaluation annuelle, objectifs, calibration
- **Succession & Development** — plans de succession, hauts potentiels, 9-box
- **Career Development Planning (CDP)** — parcours de carrière, mobilité interne
- **Learning (LMS)** — formation, catalogue, certifications
- **Compensation** — augmentations, primes, bonus (souvent à part)

Quand Dassault dit "Talent et Performance", ils visent surtout **Performance & Goals + Succession & Development**, parfois avec CDP. Learning et Compensation sont souvent des chantiers séparés.

Tout tourne autour d'un principe : **la donnée employé est dans EC**, les modules Talent lisent EC et écrivent leurs propres objets (formulaires, plans, nominations).

---

## Performance & Goals — ce qu'il fait

Deux volets, deux formulaires :

### Goal Management (GM)
Gestion des objectifs individuels. Le manager et le collaborateur définissent les objectifs de l'année, alignés sur les objectifs de l'entreprise (**goal cascading** : objectif corporate → BU → équipe → individu). Suivi en cours d'année.

Vocabulaire :
- **Goal Plan** = le formulaire d'objectifs de l'année
- **Cascading goals** = objectifs déversés du top vers le bas
- **SMART goals** = spécifiques, mesurables, atteignables, réalistes, temporels (Dassault l'utilisera à coup sûr)
- **Continuous Performance Management (CPM)** = check-ins réguliers manager/collaborateur en cours d'année, remplace peu à peu l'entretien annuel unique

### Performance Management (PM)
Le cycle d'évaluation annuel ou semestriel. Un formulaire de review qui contient : les objectifs (récupérés de GM), les compétences, l'auto-évaluation, l'évaluation manager, la note finale.

Vocabulaire :
- **Performance form** ou **PM form** = le formulaire de review
- **Route map** = le workflow du formulaire (self → manager → 2nd level → HR → completed). C'est ça que l'AMOA spécifie.
- **Rating scale** = échelle de notation (1-5, ou libellés)
- **Section** = bloc du formulaire (objectifs, compétences, commentaires)

### Calibration
Sujet politique. Une fois toutes les reviews faites, les managers se réunissent (physiquement ou dans l'outil) pour **calibrer** les notes : s'assurer qu'un "3" dans une équipe = un "3" dans une autre. On peut ajuster les notes finales à ce moment.

Vocabulaire :
- **Calibration session** = la réunion de calibration
- **9-box grid** = matrice 3×3 performance (X) × potentiel (Y) utilisée en calibration et succession
- **Rating distribution** = la courbe cible des notes (ex : 10% "outstanding", 70% "meets", 20% "below")
- **Bias reduction** = argument massue de SF pour vendre le module

### 360 Degree Reviews
Feedback à 360° (pairs, N-1, N+1, clients internes). Fonctionnalité additionnelle à PM.

---

## Succession & Development — ce qu'il fait

### Succession
Identifier qui remplace qui. Les postes-clés (positions critiques) ont des **successeurs nommés** avec un niveau de préparation (ready now / ready in 1-2 years / ready in 3-5 years).

Vocabulaire :
- **Nomination** = désignation d'un successeur sur une position
- **Talent pool** = vivier (ex : "futurs directeurs de site")
- **Position tile** = vue par position pour voir les successeurs
- **Talent Review form** = formulaire annuel Talent Review, souvent conjoint à PM
- **Org chart de succession** = vue graphique des successions
- **Talent Card** = fiche synthétique employé (perf, potentiel, mobilité, aspiration)

### 9-box (à retenir absolument)
Matrice 3×3 croisant :
- **Performance** (axe X) : basse / moyenne / haute
- **Potentiel** (axe Y) : bas / moyen / haut

Case en haut à droite (perf + potentiel élevés) = "**high potentials / stars**", à protéger et développer. Case en bas à gauche = "**underperformers**", plan d'action ou sortie. On utilise le 9-box en calibration ET en Talent Review.

### Development Plan
Le plan de développement individuel : compétences à acquérir, formations à suivre, mobilités souhaitées. Se lie à Learning (formations) et Career Development (parcours).

---

## Ce que Dassault peut te demander concrètement

**"Comment structureriez-vous un formulaire de performance ?"**

Route map = self-eval → manager eval → skip-level review → HR final → complete. Sections : objectifs (importés GM), compétences (competency library), commentaires libres, note globale. Attention au **weighting** entre objectifs et compétences (ex : 70/30). Rating scale à définir avec la DRH — souvent 4 ou 5 niveaux, avec ou sans "meets expectations" au centre.

**"Comment gérez-vous la calibration ?"**

Session de calibration animée par un facilitateur (souvent RH), avec les managers d'une même population. On projette le 9-box, on discute les cas limites, on ajuste. Sortie : notes finales validées. Le rôle du HRIS/AMOA = paramétrer la session (population, critères, note visible ou pas au manager avant), garantir la traçabilité des ajustements.

**"Un successeur ready now qui refuse la mobilité, vous faites quoi ?"**

C'est une question métier, pas outil. Réponse : le sujet remonte au HRBP et à la DRH, le processus Talent Review sert justement à mettre ces cas en visibilité. L'outil documente ; l'humain arbitre.

**"Comment articulez-vous Performance et Succession ?"**

Le **Talent Card** aggrège la perf (venant de PM), le potentiel (rating dédié) et la mobilité (aspiration + mobilité géo). Le 9-box lit ces deux dimensions. En calibration Talent, on ajuste les positions dans le 9-box, ce qui alimente les nominations et les talent pools.

**"Quelle intégration avec Employee Central ?"**

EC pousse : job info, position, manager, équipe. Les modules Talent lisent EC pour peupler les formulaires et les rôles (self, manager). Toute évolution job/position dans EC se répercute sur les workflows Talent (**event derivation** dans EC déclenche les recalculs).

---

## Ce que tu DIS en entretien (posture)

Tu es **AMOA fonctionnel**, pas paramétreur. Ton rôle sur Talent & Performance :

- Cadrer le besoin métier avec la DRH : quels cycles, quelle population, quelle rating scale, quels formulaires
- Spécifier les route maps, les sections, les liens EC → PM → Succession
- Recetter la solution livrée par l'intégrateur
- Challenger l'intégrateur quand ses choix vont créer de la dette (ex : rating scale non standard réutilisée sur d'autres cycles, calibration paramétrée trop rigide)
- Former les key users et les managers pilotes
- Documenter les règles de gestion

**Ce que tu ne fais pas** (et tu le dis) : configurer les XML des templates, écrire les Business Rules, développer les intégrations. Tu challenges celui qui le fait.

---

## Ce qu'il ne faut PAS dire

- "Je maîtrise le paramétrage Performance & Goals" — ils testeront
- "J'ai piloté un cycle Talent Review complet" — sauf si c'est vrai
- "Les Business Rules côté MDF Talent, je connais bien" — trop précis, tu vas te griller
- Confondre **rating** (note) et **weight** (pondération)
- Confondre **calibration** et **9-box** — la calibration est le processus, le 9-box est un outil de visualisation
- Confondre **Succession** (préparer un remplaçant sur une position) et **Career Development** (parcours de carrière individuel choisi par l'employé)

---

## Ta phrase d'ancrage si on te pousse sur T&P

> "Sur L'Oréal mon scope principal était Core HR EC, Payroll et gestion des temps. J'ai croisé Talent & Performance côté donnée maître — EC alimente PM et Succession — et côté articulation avec la DRH sur les cycles annuels. Sur le paramétrage fin des templates PM, des cycles de calibration ou des talent pools, je m'appuie sur l'intégrateur et je porte le besoin métier. Ma valeur ajoutée est de faire tenir le fonctionnel et de challenger les choix de l'intégrateur, pas de coder les templates."

C'est net, honnête, et ça positionne exactement ton rôle AMOA.

---

## À réviser 15 min avant l'entretien

Cinq mots à savoir replacer sans hésiter :
1. **Route map** (workflow du formulaire PM)
2. **Cascading goals** (déversement d'objectifs)
3. **Calibration session** (réunion d'ajustement des notes)
4. **9-box** (matrice perf × potentiel)
5. **Talent pool** (vivier de successeurs)

Si tu places ces cinq-là correctement, tu passes pour crédible sans avoir à rentrer dans le paramétrage.
