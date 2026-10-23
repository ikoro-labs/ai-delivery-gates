# Contribuer et publier

Pour qui modifie le plugin lui-même. Ces règles valent pour le contenu du plugin, pour `tests/` et
pour la documentation ; [`.claude/CLAUDE.md`](../.claude/CLAUDE.md) les résume pour une session Claude Code.

## Le contenu

- **Il reste générique** : un skill, un agent ou une référence ne cite ni un nom de personne, ni un
  nom de projet, ni un chemin propre à un projet. Un test le garde. Le contexte d'une organisation
  va dans un fichier de domaine local, ignoré par git.
- **Il n'invente rien** : une information inconnue reste « à vérifier », et une ligne non contrôlée
  contre une source le dit.
- **Le hook** est en Python de la bibliothèque standard, lancé par
  `uv run --no-project --quiet python`, sous Linux comme sous Windows, à partir de Python 3.10.
  Aucun `python3` cité : sous Windows, c'est un alias du Microsoft Store. Son échec sort à 0 et ne
  bloque jamais la session ; seul un refus motivé bloque une écriture.
- **La prose** est en français, sans tiret cadratin. Une phrase dit ce qui est, éprouvé ou non.

## Les tests

Chaque comportement ajouté ou changé du hook ou du contenu a son test dans `tests/`. La suite ne
demande que la bibliothèque standard et tourne sous Linux et sous Windows :

```sh
uv run --no-project --quiet python -m unittest discover -s tests
claude plugin validate .
```

Un test n'écrit que dans un dossier temporaire, jamais dans le vrai `~/.claude`.

## Branches, commits et PR

- Une branche par changement, depuis `main` : `feat/<slug>`, `fix/<slug>`, `docs/<slug>`,
  `test/<slug>` ou `chore/<slug>`, le slug en français, en minuscules et avec des tirets.
- Jamais de commit direct sur `main` : tout passe par une PR, que la CI doit rendre verte.
- Conventional Commits, en français : `<type>(<zone>): <ce qui change>`, la zone étant celle du
  plugin touchée (`cadrage`, `revue-de-phase`, `hooks`, `release`...). Le corps dit pourquoi.
- Le corps d'une PR suit `.github/pull_request_template.md`.

## Publier une version

1. Changer `version` dans `.claude-plugin/plugin.json`, et nulle part ailleurs.
2. Ouvrir l'entrée correspondante en tête de `CHANGELOG.md`.
3. Vérifier (voir [Les tests](#les-tests)), puis fusionner sur `main`.
4. Poser et pousser le tag annoté `ai-delivery-gates--v<X.Y.Z>`, deux tirets, comme les tags de
   forge. Un tag ne se déplace ni ne se supprime une fois poussé. Les tags `v0.2.0` à `v0.2.3`
   sont antérieurs à cette règle et ne changent pas.
5. Une PR sur `ikoro-labs/forge` fait pointer l'entrée `ai-delivery-gates` de
   `.claude-plugin/marketplace.json` sur le nouveau tag : c'est elle qui publie la version.

## Le dépôt

```text
.claude-plugin/plugin.json      le manifeste, seul endroit qui porte la version
.claude-plugin/icon.png         l'icône du plugin, l'export de docs/logo.svg
skills/                         projet-ia, spike, cadrage, specifications, system-design,
                                revue-de-phase, chacun avec ses références
agents/                         lead-tech, product-owner, expert-metier
hooks/                          hooks.json et scripts/garde_code.py
tests/                          tests du hook et du contenu
README.md                       la page d'accueil : ce que fait le plugin, l'installer, où lire la suite
docs/contribuer.md              cette page
docs/architecture.excalidraw    le schéma du README, sa source éditable
docs/architecture.svg           son export, que le README affiche
docs/logo.svg                   le logo, sa source
docs/banniere.svg               la bannière du README et de l'aperçu GitHub, sa source
CHANGELOG.md                    une entrée par version publiée
.claude/CLAUDE.md               le résumé de ces règles pour une session Claude Code
.github/                        la CI (tests sous Linux et Windows, validation) et le modèle de PR
```

## Le schéma, le logo et la bannière

Le schéma du `README.md` a sa source dans `docs/architecture.excalidraw`, à ouvrir dans Excalidraw ;
`docs/architecture.svg` en est l'export, police comprise, refait à chaque changement de la source.

Le logo a sa source dans `docs/logo.svg`. Son export en PNG de 1024 px, `.claude-plugin/icon.png`,
est l'icône du plugin, et se refait à chaque changement de la source :

```sh
uv run --no-project --quiet --with cairosvg python -c "import cairosvg; cairosvg.svg2png(url='docs/logo.svg', write_to='.claude-plugin/icon.png', output_width=1024, output_height=1024)"
```

La bannière, `docs/banniere.png` (1280 × 640), s'exporte de même depuis `docs/banniere.svg`, avec
`output_width=1280, output_height=640`. Son texte demande la police JetBrains Mono installée sur le
poste. C'est aussi l'aperçu social du dépôt, à téléverser à la main dans **Settings → General →
Social preview**.

Ces exports demandent la bibliothèque système cairo : `libcairo2` sous Linux ; sous Windows, une
installation qui la fournit (GTK, MSYS2). Ils n'ont été essayés que sous Linux.
