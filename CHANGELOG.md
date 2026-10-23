# Changelog

Format inspiré de Keep a Changelog. Versions selon SemVer ; la version de référence est celle de
`.claude-plugin/plugin.json`.

## [Non publié]

### Ajouté
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
