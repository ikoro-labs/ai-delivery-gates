# Consolidation des constats

## 1. Contrôle du format
Vérifier chaque constat contre `format-constat.md`. Renvoyer à l'agent (ou reformuler en le signalant) tout
constat sans section, sans question ou sans preuve attendue. Vérifier qu'un agent sans bloquant a produit sa
vérification de grille.

## 2. Dédoublonnage
Même section et même question : fusionner, conserver la sévérité la plus haute, noter les agents concernés.
Une convergence (deux ou trois agents sur le même point) est un signal fort : la traiter en priorité et le dire.

## 3. Classement
Bloquants, puis majeurs, puis mineurs. À sévérité égale, les convergences d'abord, puis l'ordre des sections du
livrable.

## 4. Présentation à l'utilisateur

```markdown
## Revue de phase N, passage P, AAAA-MM-JJ

| Id | Sévérité | Section | Question à trancher | Preuve attendue | Agents |
|---|---|---|---|---|---|

### Raisons numéro un d'échec
- Lead Tech : ...
- Product Owner : ...
- Expert métier : ...

### Pré-mortem consolidé (phases 1 et 3)
voir pre-mortem.md
```

Puis, pour chaque bloquant et majeur, demander la réponse de l'utilisateur. Trois issues possibles :
- **levé** : preuve fournie, livrable mis à jour (vérifier que la mise à jour est faite, pas promise) ;
- **accepté** (majeurs seulement) : motif daté, écrit dans l'état et dans le livrable ;
- **non fondé** : l'utilisateur montre que l'agent a mal lu ; motif écrit, constat clos.

Ne jamais clore un constat sur une promesse (« je le ferai en phase 4 ») sans la transformer en non-goal daté,
en risque, ou en majeur accepté.

## 5. Second passage
Relancer uniquement les agents concernés par les points restants, avec le livrable mis à jour et les réponses.
Deux passages maximum ; ensuite, liste des points ouverts à l'utilisateur, « décision humaine requise », phase
non close.

## 6. Trace
Ligne dans la table Revues de l'état ; majeurs acceptés aussi dans la table Décisions.
