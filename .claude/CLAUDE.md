# ai-delivery-gates

Ce dépôt est le plugin Claude Code `ai-delivery-gates`. Il est distribué par la marketplace
`ikoro-labs`, que sert le dépôt `ikoro-labs/forge` en épinglant chaque version publiée.

- **Essayer un changement dans une vraie session** : `claude --plugin-dir <ce dépôt>`, lancé depuis
  un projet jetable.
- **Les règles** : [`docs/contribuer.md`](../docs/contribuer.md) pour le contenu, les tests, les
  branches, les commits et la publication.
- **Vérifier avant toute PR** :

  ```sh
  uv run --no-project --quiet python -m unittest discover -s tests
  claude plugin validate .
  ```
