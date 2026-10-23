# AI Delivery Gates (plugin Claude Code)

Roadmap, livrables et gate de revue pour les phases 0 à 3 d'un projet IA : spike, cadrage, spécifications,
system design. Le plugin encode le playbook v2 et ses templates, ajoute six checkpoints (parties prenantes,
alternatives et existant, matrice coût d'erreur et niveau d'autonomie, checkpoint réglementaire, jeu d'éval
amorcé dès la phase 1, adoption) et fait relire chaque livrable par trois agents indépendants.

## Composants

| Composant | Nom | Rôle |
|---|---|---|
| Skill | `projet-ia` | Orchestrateur : état du projet, profil et taille, boucle de phase, points de sortie |
| Skill | `spike` | Phase 0 : question binaire, timebox, résultat mesuré, code jeté |
| Skill | `cadrage` | Phase 1 : fiche de cadrage, one-pager, risques, checkpoint réglementaire, matrice coût d'erreur, go/no-go, critères d'arrêt |
| Skill | `specifications` | Phase 2 : stories, non-goals, parcours, spec API, spec data, NFR |
| Skill | `system-design` | Phase 3 : fiches modèle, architecture, ADR, agents et RAG, plan d'éval, coûts, frontière de confiance |
| Skill | `revue-de-phase` | Gate : lance les trois agents, consolide, pré-mortem, verdict |
| Agent | `lead-tech` | Faisabilité, architecture, coûts, sécurité, évaluabilité |
| Agent | `product-owner` | Valeur, utilisateurs, métriques, périmètre, adoption |
| Agent | `expert-metier` | Réalisme terrain, vocabulaire, réglementation du domaine (fichier `skills/revue-de-phase/references/domaines/`) |
| Hook | `garde-code` | PreToolUse : bloque l'écriture de code applicatif tant que la phase 1 n'est pas close |

## Installation

Le dépôt est aussi un marketplace Claude Code (`.claude-plugin/marketplace.json`) :

```
/plugin marketplace add ikoro-labs/ai-delivery-gates
/plugin install ai-delivery-gates@ikoro-labs
```

En local, depuis un clone :

```bash
claude plugin validate ./ai-delivery-gates     # vérifie manifeste et structure
claude --plugin-dir ./ai-delivery-gates     # charge le plugin pour la session
```

Prérequis du hook : `uv` dans le PATH (le hook lance `uv run --no-project --quiet python`, ce qui évite l'absence de `python3` sous Windows). Si `uv` est absent, la commande échoue en erreur non bloquante et la garde est inactive : vérifier avec `/hooks` et un essai d'écriture refusé.

## Utilisation

- Démarrer : « je démarre un projet IA ... » ou `/ai-delivery-gates:projet-ia`. L'orchestrateur crée
  `docs/projet/etat.md` et lance la phase 0.
- Chaque phase écrit ses livrables sous `docs/projet/0N-<phase>/` par entretien ; rien n'est inventé, les cases
  inconnues restent « à vérifier ».
- Clore une phase : « on peut clore la phase ? » lance la revue. Clôture quand tous les bloquants sont levés et
  chaque majeur levé ou accepté avec motif daté.
- Revue à la demande sur n'importe quel document : « challenge-moi sur ce cadrage ».

## Fichier d'état

`docs/projet/etat.md`, format dans `skills/projet-ia/references/etat-projet.md`. L'en-tête porte
`phases_closes` et `garde_code`, lus par le hook.

## Garde-code

Tant que `1` n'est pas dans `phases_closes`, toute écriture hors `docs/`, `spike/`, `.claude/` et fichiers `.md`
ou `.txt` est refusée avec le motif. Désactivation : `garde_code: off` dans l'état, avec une ligne datée dans le
journal. Le hook ne fait rien dans un projet sans `docs/projet/etat.md`.

## Personnalisation

- Domaines : un fichier par domaine récurrent dans `skills/revue-de-phase/references/domaines/`. Le fichier
  `batiment-controle-technique.md` est une amorce dont les lignes « à vérifier » doivent être contrôlées.
  Copier `_template.md` pour un nouveau domaine. Les fichiers de domaine autres que `_template.md` et
  `batiment-controle-technique.md` sont ignorés par git : ils restent locaux, car ils portent souvent du contexte
  d'organisation ou de projet. L'expert métier propose en fin de revue les lignes à ajouter.
- Modèle des agents : `model: inherit` par défaut ; passer `opus` dans le frontmatter de chaque agent pour
  forcer le modèle le plus puissant en revue.
- Accès web des agents : retirer `WebSearch` et `WebFetch` de la liste `tools` pour un agent hors ligne.
- Règle de clôture et nombre de passages : `skills/revue-de-phase/SKILL.md`, section 5.

## Limites de la v1

- Non testé sur un projet réel : à itérer sur deux ou trois cas.
- Le fichier de domaine bâtiment est une amorce, pas une référence vérifiée.
- Le hook couvre les tools Write, Edit, MultiEdit et NotebookEdit ; une écriture par Bash n'est pas interceptée.

## Licence

MIT, voir [LICENSE](LICENSE).
