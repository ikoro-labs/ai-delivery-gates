# Format de constat (obligatoire pour les trois agents)

Un constat est une question posée à l'auteur, pas un commentaire. S'il ne pointe pas une section, s'il n'a pas de
question à trancher ou s'il n'indique pas ce qui permettrait de le clore, il n'est pas recevable.

## Sévérités

- **Bloquant** : si c'est vrai, la phase ne peut pas être close. Un critère de sortie n'est pas rempli, un
  principe du playbook est violé, ou une décision repose sur une donnée inexistante ou non vérifiée.
- **Majeur** : affaiblit fortement le projet ; une décision explicite et datée de l'auteur peut l'accepter.
- **Mineur** : amélioration ; consigné, jamais bloquant.

## Gabarit de sortie

```markdown
## Constats

### Bloquants
- [B1] Section : <section ou ligne du livrable>
  Constat : <ce qui manque ou ce qui est faux, en une ou deux phrases>
  Question à trancher : <la question précise à laquelle l'auteur doit répondre>
  Preuve attendue : <chiffre, fichier, source datée ou décision écrite qui clôt le constat>

### Majeurs
- [M1] Section : ... | Constat : ... | Question à trancher : ... | Preuve attendue : ...

### Mineurs
- [m1] Section : ... | Constat : ... | Question à trancher : ... | Preuve attendue : ...

## Vérification de la grille
(obligatoire si aucun bloquant ; sinon facultatif)
- <point de grille> : conforme parce que <élément précis du livrable>

## Raison numéro un d'échec
<une phrase>. Signal avant-coureur : <ce qu'on observera en premier>.

## Pré-mortem (phases 1 et 3 uniquement)
1. Six mois plus tard, le projet est arrêté parce que <cause>, conséquence de <décision ou absence de décision prise aujourd'hui, section visée>.
2. ...
3. ...
```

## Interdits

- « À préciser », « manque de détail », « à compléter », « ok dans l'ensemble », « semble correct », « bon travail ».
- Un constat sans section visée.
- Un constat sans question ni preuve attendue.
- Réécrire le livrable à la place de l'auteur.
- Une affirmation issue du web sans source datée : écrire « non vérifié » à la place.
