# Journal des versions

Une entrée par version publiée du plugin `ai-delivery-gates`, la plus récente en haut. Chaque
version porte le tag `ai-delivery-gates--v<X.Y.Z>` sur ce dépôt ; sa version est celle de
`.claude-plugin/plugin.json`, et nulle part ailleurs. Les tags `v0.2.0` à `v0.2.3` sont antérieurs
à cette règle et ne changent pas.

## [0.2.4] - 2026-10-23

Le plugin prend l'identité visuelle d'ikoro-labs, et son dépôt s'aligne sur celui de forge : même
plan de README, même journal, mêmes tags, une CI et des tests. Le contenu des skills, des agents et
du hook ne change pas.

### Identité
- Nouvelle icône `.claude-plugin/icon.png`, export de sa source `docs/logo.svg` : le portique de la
  revue sur le chemin des phases, aux couleurs d'ikoro-labs.
- Bannière `docs/banniere.png` (source `docs/banniere.svg`), en tête du README et pour l'aperçu
  social du dépôt.

### Dépôt
- README au plan de celui de forge : comment ça marche, ce que le plugin apporte, prérequis,
  installer, configurer, limites connues, aller plus loin.
- `.claude/CLAUDE.md` (hors du plugin chargé), `docs/contribuer.md` (contenu, tests, branches, commits, publication) et modèle de PR.
- Les versions se taguent désormais `ai-delivery-gates--v<X.Y.Z>`, comme celles de forge.
- Manifeste : champ `homepage`.

### Tests
- `tests/test_garde_code.py` : le refus tant que la phase 1 est ouverte, les chemins toujours
  autorisés, la levée de la garde, un chemin hors du projet, une entrée illisible.
- `tests/test_plugin_content.py` : aucun nom de projet ni de personne, pas de tiret cadratin, la
  version dans `plugin.json` seulement, le journal ouvert sur cette version, l'icône, la licence.
- CI GitHub Actions : la suite sous Linux et sous Windows, et `claude plugin validate .`.

## [0.2.3] - 2026-10-23

### Supprimé
- Adresse e-mail de l'auteur dans le manifeste, et nom de personne dans le fichier de domaine
  `batiment-controle-technique.md`.

## [0.2.2] - 2026-10-23

### Modifié
- Distribution par le catalogue `ikoro-labs` (dépôt `ikoro-labs/forge`) : installation par
  `/plugin marketplace add ikoro-labs/forge` puis `/plugin install ai-delivery-gates@ikoro-labs`.

### Supprimé
- Manifeste `.claude-plugin/marketplace.json` : le dépôt ne déclare plus son propre catalogue.

## [0.2.1] - 2026-10-23

### Ajouté
- Licence MIT (`LICENSE`, champ `license` du manifeste).
- Icône du plugin `.claude-plugin/icon.png` (1024 × 1024).
- Manifeste de marketplace `.claude-plugin/marketplace.json` : installation par
  `/plugin marketplace add ikoro-labs/ai-delivery-gates` puis `/plugin install ai-delivery-gates@ikoro-labs`.

## [0.2.0] - 2026-10-22

### Modifié
- Plugin renommé `playbook-ia` en `ai-delivery-gates` : les commandes deviennent `/ai-delivery-gates:<skill>`
  et les agents `ai-delivery-gates:<agent>` (changement incompatible avec les sessions qui chargeaient `playbook-ia`).
- Manifeste : auteur `ikoro-labs`, champ `repository` ajouté.

### Ajouté
- Les fichiers de domaine propres à une organisation ou un projet sont ignorés par git (seuls `_template.md` et
  `batiment-controle-technique.md` sont versionnés).

## [0.1.1] - 2026-10-22

### Modifié
- Hook garde-code : lancé via `uv run --no-project --quiet python` au lieu de `python3`, absent par défaut sous
  Windows (la garde était alors inactive sans alerte).
- README : prérequis du hook passé de `python3` à `uv`, procédure de vérification ajoutée.

### Retiré
- README : section « Cas de test suggérés ».

## [0.1.0]

### Ajouté
- Version initiale : skills `projet-ia`, `spike`, `cadrage`, `specifications`, `system-design`,
  `revue-de-phase` ; agents `lead-tech`, `product-owner`, `expert-metier` ; hook `garde-code`.
