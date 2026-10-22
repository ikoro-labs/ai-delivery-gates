# Spécification data : [nom du projet]

Destinataire : ... | Date : ...

## Sources
| Source | Propriétaire | Mode d'accès | Fréquence | Volume | Schéma versionné où |
|---|---|---|---|---|---|

## Schémas
Pour chaque table ou flux : champ, type, unité, référentiel ou nomenclature, nullable, PII (oui/non), exemple réel.

| Champ | Type | Unité ou référentiel | Nullable | PII | Exemple |
|---|---|---|---|---|---|

## Data contracts
| Contrat | Entre qui et qui | Règles vérifiées (schéma, plages, fraîcheur, volume) | Outil (pandera, great_expectations, autre) | Que se passe-t-il en cas de rupture |
|---|---|---|---|---|

## Rétention et suppression
| Donnée | Durée de conservation | Motif (légal, métier) | Suppression sur demande : procédure et délai | Anonymisation ou pseudonymisation |
|---|---|---|---|---|

## Lineage
Quel dataset (snapshot identifié) a produit quel modèle, avec quel code (commit). Où c'est enregistré.

## Fuites potentielles
Champs qui contiennent la cible ou une information postérieure à la prédiction. Comment ils sont exclus.
