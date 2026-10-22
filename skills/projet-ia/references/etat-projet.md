# Format du fichier d'état : docs/projet/etat.md

Un seul fichier, lu par l'orchestrateur, par les skills de phase, par les agents de revue et par le hook
`garde-code`. L'en-tête est volontairement simple (une clé par ligne) pour rester lisible par un script.

```markdown
---
nom: <nom du projet>
profil: spike | perso | production | plateforme
domaine: <slug du fichier de domaine, ex. batiment-controle-technique>
destinataire_principal: <qui lit les livrables>
sponsor: <qui porte le projet, ou "sans objet" en perso>
decideur_go_nogo: <qui tranche en 1.8>
owner_prod: <qui portera le système en production, ou "à définir">
tailles: 0=S 1=L 2=L 3=L
phase_courante: 0
phases_closes: []
garde_code: on
---

# État du projet <nom>

## Livrables
| Phase | Livrable | Chemin | Statut (à faire / en cours / complet / revu) |
|---|---|---|---|

## Revues
| Date | Phase | Passage | Bloquants restants | Majeurs acceptés (motif) | Verdict |
|---|---|---|---|---|---|

## Décisions
| Date | Décision | Référence (ADR, revue, constat) |
|---|---|---|

## Critères d'arrêt (copie de 1.9, mise à jour si révisés)
| Date de vérification | Condition de poursuite chiffrée | Décision si non atteinte |
|---|---|---|

## Journal
- AAAA-MM-JJ : <événement, décision, motif>
```

Règles :
- `phases_closes` est une liste entre crochets, ex. `[0, 1]`. Le hook `garde-code` cherche la valeur `1` dedans.
- `garde_code: off` désactive le hook ; chaque passage à `off` est daté et motivé dans le journal.
- Un majeur accepté apparaît deux fois : dans la ligne de revue et dans la table Décisions.
- Le journal est chronologique, une ligne par événement, pas de prose.
