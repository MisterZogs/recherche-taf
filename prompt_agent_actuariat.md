# Prompt – Agent de recherche d'emploi actuariat

Copier-coller ce prompt dans Claude Code (ou tout autre assistant IA avec accès aux outils).

---

## Prompt

```
Je cherche un emploi d'actuaire en France. Je préfère le remote, et je suis ouvert
aux CDI et aux missions freelance. Peu importe le niveau d'expérience requis.

Crée-moi un fichier Excel "offres_actuariat.xlsx" qui liste les offres actuellement
disponibles, avec exactement ces 15 colonnes dans cet ordre :
Priorité | Statut | Fait | Poste | Entreprise | Source | Contrat | Localisation |
Remote | Salaire / TJM | Durée mission | Fit / Notes | Lien | CV à envoyer | Prétention

Le fichier doit avoir deux onglets : "Offres Actuariat" (les offres) et "Fait" (archive vide).

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
CRITÈRES DE NOTATION
─────────────────────────────────────────
- ⭐⭐⭐⭐⭐ : full remote confirmé, OU grand employeur de référence (SCOR, Aon, Allianz,
  AXA, Crédit Agricole, Société Générale, Swiss Re) avec cabinet actuariat pur-player
- ⭐⭐⭐⭐   : cabinet conseil spécialisé actuariat (Actuelia, Sia, CORRELIUM, FINAX...),
  Big 4 (Deloitte/KPMG/PwC), ou freelance avec TJM affiché et télétravail partiel
- ⭐⭐⭐     : assureur/mutuelle mid-range en IDF avec hybride, ou mission freelance Paris
- ⭐⭐       : présentiel obligatoire ou province sans remote confirmé
- ⭐         : junior/stage, CDD court, ou hors profil actuarial pur

Trie les offres par priorité décroissante. Statut par défaut : "À postuler".

─────────────────────────────────────────
SITES À SCRAPER
─────────────────────────────────────────
Sites spécialisés actuariat :
- theactuaryjobs.com/jobs/france/
- actuarylist.com/countries/france
- babyloneconsulting.fr/categorie-missions/actuariat/
- actuelia.fr
- freelance-informatique.fr (recherche "actuaire")

Sites génériques France :
- linkedin.com (recherche "actuaire emplois France")
- indeed.fr (recherche "actuaire France")
- welcometothejungle.com (recherche "actuaire")
- hellowork.com/fr-fr/emplois/actuaire.html
- free-work.com/fr/tech-it/autre/job-mission/actuaire-1
- glassdoor.fr (recherche "actuaire France")

Cabinets recrutement spécialisés assurance/actuariat :
- Taylor Made Recrutement, Morgan Philips, Fed Finance, LHH, FINAX Consulting

Pour chaque offre, remplis : titre exact du poste, entreprise, source du site,
type de contrat (CDI/CDD/Freelance/Mission), ville, remote (Full remote/Hybride/
Présentiel/n.c.), salaire ou TJM si affiché, durée si mission freelance, une courte
note de contexte, et le lien direct vers l'offre.

Vise 40 à 60 offres pour avoir une bonne base.

─────────────────────────────────────────
COLONNE "CV À ENVOYER" — ADAPTATION DU CV
─────────────────────────────────────────
Si je te fournis mon CV (en HTML, Word, PDF ou texte), pour chaque offre tu dois :
1. Analyser les mots-clés et exigences de l'offre.
2. Créer une version adaptée de mon CV qui met en avant les expériences et compétences
   les plus pertinentes pour cette offre spécifique (sans inventer d'éléments absents
   du CV original — seulement réorganiser, reformuler et mettre en valeur).
3. Sauvegarder cette version sous un nom de fichier du type :
   CV_[Prénom][NOM]_[NomEntreprise].html (et générer le PDF correspondant si possible).
4. Écrire ce nom de fichier dans la colonne "CV à envoyer" de la ligne concernée.

Ne pas adapter le CV pour les offres notées ⭐ ou ⭐⭐ sauf demande explicite.
Commencer par les offres ⭐⭐⭐⭐⭐ et ⭐⭐⭐⭐.

─────────────────────────────────────────
COLONNE "PRÉTENTION"
─────────────────────────────────────────
Pré-remplis cette colonne avec une fourchette salariale cible selon le type de poste :
- CDI actuaire junior (0-3 ans) : 40-55K€
- CDI actuaire confirmé (3-7 ans) : 55-80K€
- CDI actuaire senior (7+ ans) : 80-110K€
- Freelance/Mission : 500-800€/j selon le niveau

Je pourrai ajuster ces valeurs manuellement au cas par cas.

─────────────────────────────────────────
WORKFLOW — COMMENT UTILISER LE FICHIER
─────────────────────────────────────────
Colonne "Statut" — valeurs possibles :
  À postuler | Postulé | En cours | Refusé | Expiré | Hors profil

Colonne "Fait" — pour archiver une offre :
  Écrire "x" dans cette cellule. Lors de la prochaine mise à jour du fichier,
  toutes les lignes marquées "x" seront automatiquement déplacées vers l'onglet "Fait".

─────────────────────────────────────────
MISE À JOUR ULTÉRIEURE
─────────────────────────────────────────
Pour relancer une recherche et ajouter de nouvelles offres au fichier existant, dire :
"Relance une recherche d'offres actuariat sur tous les sites et ajoute les nouvelles
trouvées dans offres_actuariat.xlsx. Avant d'ajouter, déplace les lignes marquées 'x'
dans la colonne Fait vers l'onglet Fait. Ne supprime jamais une ligne existante."

─────────────────────────────────────────
GÉNÉRATION DU FICHIER
─────────────────────────────────────────
Génère le fichier avec Python (bibliothèque openpyxl) et exécute le script directement.
```

---

## Notes pour l'utilisation

- **Adapter le ranking** : si tu as une spécialité (vie, non-vie, santé, ALM, tarification,
  provisionnement, IFRS17...) ou une préférence forte (ex : uniquement freelance, uniquement
  Paris), précise-le dans le prompt pour que l'IA affine les ⭐.

- **Donner son CV** : idéalement en HTML ou en texte brut pour que l'IA puisse le modifier
  facilement. Un PDF est lisible mais moins facilement éditable.

- **TJM marché actuariat France 2026** (pour calibrer les prétentions) :
  - Junior (0-3 ans) : 350-500€/j
  - Confirmé (3-7 ans) : 500-700€/j
  - Senior (7+ ans) : 700-950€/j
  - Spécialité rare (IFRS17, ALM, S2 interne) : jusqu'à 1000€/j
