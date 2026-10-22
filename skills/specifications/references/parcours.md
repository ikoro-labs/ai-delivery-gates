# Parcours utilisateur bout-en-bout : [nom du projet]

Destinataire : ... | Date : ...

Un diagramme par cas d'usage du MVP (donc en général un seul). Le chemin nominal et, pour chaque dépendance
(modèle, donnée, service tiers, humain qui valide), le chemin d'échec : ce que l'utilisateur voit, ce que le
système fait, ce qui est tracé.

```mermaid
flowchart TD
    A[Entrée utilisateur] --> B{Validation des entrées}
    B -- invalide --> B1[Message d'erreur explicite, événement tracé]
    B -- valide --> C[Appel du modèle]
    C -- timeout ou erreur --> C1[Fallback : règle simple ou cache, incident tracé]
    C -- ok --> D{Confiance suffisante ?}
    D -- non --> D1[Réponse prudente, demande de validation humaine]
    D -- oui --> E[Résultat affiché avec version du modèle]
    E --> F[Signal utilisateur capté : clic, correction, rejet]
```

## Points de contrôle humain
Où l'humain valide, selon le niveau d'autonomie choisi en 1.3 bis : ...

## Ce que voit l'utilisateur quand ça échoue
| Panne | Message ou comportement visible | Délai | Tracé où |
|---|---|---|---|

## Stories révélées par le parcours
Liste des stories manquantes découvertes en dessinant le parcours, à ajouter au backlog ou aux non-goals.
