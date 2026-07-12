# Scripts pour le brief HR Path
## Ce que tu dois pouvoir dire quasi tel quel

---

## 1. Ton discours SF Employee Central (2 min)

À servir si Laurent Tarnat te demande "Racontez-moi ce que vous avez fait sur EC" ou "Comment vous positionnez-vous sur SuccessFactors ?".

> "Employee Central chez L'Oréal, c'était le socle du projet OneProfile. On a migré la donnée maître SAP HR de 40 pays vers SF EC en plusieurs vagues, sur une architecture position management stricte, très différente du couple PA/OM SAP classique. Le vrai enjeu se jouait au niveau fonctionnel bien plus qu'au niveau technique : redéfinir ce qui restait dans le core global, ce qui pouvait rester local, et cadrer la reprise depuis un existant SAP HR qui portait 15 ans d'historique.
>
> Mon rôle couvrait le cadrage des règles de gestion pays par pays, la rédaction des specs fonctionnelles, la coordination avec l'intégrateur sur les MDF et les Business Rules, la reprise de données, et la recette avec les key users RH.
>
> Sur EC en projet international, ce qui compte vraiment, c'est trois choses. Un : la maîtrise du modèle organisationnel, donc position, job classification, cost center, department, division, et la cohérence entre ces objets. Deux : la solidité du plan de reprise, parce qu'un employment mal repris bloque toute la chaîne aval sur la paye, les temps ou le talent. Trois : la gouvernance sur les évolutions post go-live, sur qui décide de faire évoluer un event reason ou un workflow, et sur comment on absorbe les demandes des pays sans exploser le core global."

Pourquoi ça marche : tu montres que tu maîtrises le vocabulaire (position management, MDF, Business Rules, event reason, workflow, employment, foundation objects), que tu comprends la logique projet (core vs local, reprise, gouvernance), et que ton discours est structuré. Un DRH ne comprendra pas tout le vocabulaire technique, mais un HRIS Manager oui, et c'est lui que tu dois convaincre.

---

## 2. Questions typiques d'un DRH ou HRIS Manager sur EC et tes réponses

### "Quelle est la différence fondamentale entre SAP HR et SuccessFactors EC ?"

> "SAP HR est structuré autour de l'infotype et du couple PA/OM. C'est une logique historisée par matricule et par infotype, très solide en gestion administrative locale. EC est structuré autour de la position et du modèle MDF, qui est un metadata framework configurable. Ça change deux choses concrètes. Un : on peut faire évoluer la structure de donnée sans passer par ABAP, ce qui rend l'outil plus vivant côté RH. Deux : le référentiel devient position-centric, donc il faut redéfinir la gouvernance des positions, qui les crée, qui les modifie. Beaucoup de projets EC échouent sur ce point-là, pas sur la migration technique."

### "Sur quel périmètre EC êtes-vous à l'aise ?"

> "Core HR : personal information, employment information, job information, compensation information. Gestion organisationnelle : positions, foundation objects. Workflows et Business Rules côté cadrage fonctionnel. Reprise de données depuis SAP HR. Intégrations descendantes vers la paye et vers un outil de gestion des temps. Sur le paramétrage technique fin, MDF custom et code XML des templates, je m'appuie sur l'intégrateur ; c'est mon rôle de porter le besoin métier et de recetter, pas de coder les templates."

### "Quels sont les pièges que vous avez vus sur une migration SAP HR → EC ?"

> "Trois pièges récurrents. Le premier : sous-estimer le nettoyage de la donnée source. On croit qu'on peut reprendre l'infotype 0001 tel quel, on découvre en run que 20% des positions n'ont pas de titulaire ou que les cost centers ne matchent plus le référentiel financier. Le deuxième : vouloir répliquer la logique SAP HR dans EC. On finit avec des MDF custom pour reproduire des infotypes, on perd tout le bénéfice du standard. Le troisième : négliger la gouvernance post go-live, notamment la gestion des demandes pays. Sans un DPO ou un HRIS Manager qui arbitre, le core dérive en six mois."

### "Comment gérez-vous les demandes de customisation pays ?"

> "Grille simple : est-ce que le besoin est réel, est-ce qu'il est légal ou réglementaire, est-ce qu'il peut être couvert par le standard SF avec un paramétrage local, sinon est-ce qu'on documente comme dérogation temporaire. Chaque customisation a un coût de TMA et un coût de rollout futur, donc chaque demande passe devant un comité d'arbitrage avec la DRH corporate. C'est comme ça qu'on faisait sur L'Oréal, et c'est ce qui a permis de tenir 40 pays sur un core relativement stable."

---

## 3. Ta posture de challenger face à l'intégrateur

### Le principe (à dire tel quel au brief)

> "Ma posture face à un intégrateur repose sur une conviction simple. L'intégrateur connaît son produit mieux que moi ; moi je connais l'usage long terme et le métier client mieux que lui. Le rôle de l'AMOA, c'est de faire tenir cet écart, pas de créer du conflit. Je challenge sur les choix qui vont créer de la dette dans deux ou trois ans, pas sur ceux qui me plaisent moins esthétiquement. Et je le fais toujours par question, jamais par affirmation."

### L'exemple concret L'Oréal (à sortir dès qu'on te demande un cas)

> "Un exemple concret. Sur OneProfile, l'intégrateur proposait de gérer une population très spécifique en Chine, les contrats saisonniers liés à la période promotionnelle, via un MDF custom avec un workflow parallèle. Techniquement ça tenait la route. Ma question à l'atelier de cadrage a été simple : est-ce qu'on va pouvoir maintenir ce MDF custom dans deux ans quand on rebasculera sur le standard SF, et qui portera la formation des paies chinoises quand elles auront un objet qui n'existe nulle part ailleurs. On a fini par retenir une solution standard avec une Business Rule d'event derivation. Moins élégante côté intégrateur, plus robuste côté client. C'est ce type d'arbitrage qui fait la valeur de l'AMOA."

Adaptation : si tu veux un autre exemple, cite le RFP externalisation TMA que tu as piloté et gagné. Tu as géré la posture inverse, tu sais comment un intégrateur pense et se protège.

### Les 5 questions que tu poses systématiquement

Sers-les si on te demande "concrètement, comment vous challengez ?" :

> "Cinq questions reviennent en permanence dans mes ateliers. Un : est-ce que ce choix nous contraint dans deux ou trois ans en TMA ou en rollout pays. Deux : est-ce standard SF ou custom, et si custom, qui le maintient et à quel coût. Trois : quel est l'impact sur la downstream chain, paye, temps, talent. Quatre : est-ce que le business owner en face a bien compris ce qu'on lui demande de valider. Cinq : si on change d'intégrateur dans cinq ans, est-ce qu'on arrive à désassembler cette solution. Une réponse floue sur une de ces cinq questions, c'est le signal qu'il faut creuser."

### Comment tu formules un désaccord (sans agresser)

Trois règles à énoncer si on t'interroge sur la méthode :

> "Trois règles que je m'impose. Toujours par question, jamais par affirmation ; ça laisse à l'intégrateur la place de se réajuster sans perdre la face. Toujours devant les stakeholders métier, pas en réunion technique isolée avec l'intégrateur, parce que l'arbitrage doit être visible. Toujours avec une alternative crédible en poche, ou au moins avec une question précise sur ce qui remplace, sinon c'est du blocage stérile."

### Trois phrases-types que tu utilises en atelier (à mémoriser)

Utilisables en entretien pour montrer que ta posture est incarnée :

> "Je comprends la logique proposée. Est-ce qu'on peut regarder ensemble ce que ça implique sur la TMA dans six mois ?"
>
> "OK sur le principe. J'ai une alternative à comparer avec la vôtre, ça permettra à la DRH d'arbitrer en connaissance de cause."
>
> "Ce que vous proposez tient techniquement. Sur le maintien en TMA et le rollout pays, comment on l'organise ?"

---

## 4. Si Laurent Tarnat te demande "Comment ça se passe avec l'intégrateur si vous êtes en désaccord fort ?"

> "Je remonte l'arbitrage à la DRH ou au HRIS Manager avec les deux options documentées, avantages et coûts long terme de chacune. Je ne bloque jamais un livrable, je documente le désaccord et je laisse la décision au business owner. Mon expérience, c'est que les vrais points durs sont rares ; la plupart du temps l'intégrateur ajuste dès qu'il voit qu'on a fait le boulot de comparaison sérieusement. Sur L'Oréal, en dix ans, j'ai dû monter deux fois seulement au niveau du sponsor projet. Les deux fois, ma position a été retenue, parce qu'elle était étayée."

Cette phrase te positionne senior : tu ne dramatises pas les conflits, tu ne fuis pas non plus, tu as une méthode.

---

## À retenir avant le brief

- Le vocabulaire clé SF EC : position management, MDF, Business Rules, workflow, event reason, event derivation, foundation objects, employment, job classification.
- Ton exemple canon : le MDF custom Chine remplacé par une Business Rule standard.
- Ta posture résumée en une phrase : "Toujours par question, toujours devant témoins, toujours avec une alternative."
- Ne jamais dire "je ne suis pas d'accord avec l'intégrateur" ; dis "j'ai posé une question sur X et on a retenu une alternative."
