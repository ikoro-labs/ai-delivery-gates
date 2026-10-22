# Registre des risques : [nom du projet]

Destinataire : ... | Mis à jour le : ...

Un risque est un événement incertain avec un effet sur les objectifs du cadrage (métriques, SLO, budget, délai,
conformité). Ce qui est certain n'est pas un risque, c'est une contrainte : elle va dans la fiche ou la NFR.

Échelles : probabilité faible / moyenne / forte ; impact faible / moyen / fort / bloquant.
Un risque fort × fort sans mitigation écrite est un bloquant de revue.

| Id | Catégorie | Risque (événement, cause, effet) | Probabilité | Impact | Mitigation | Signal d'alerte (observable, mesuré) | Propriétaire |
|---|---|---|---|---|---|---|---|
| R1 | privacy | ... | ... | ... | ... | ... | ... |

## Catégories à balayer systématiquement

- Privacy et données personnelles : PII dans les données, dans les prompts, dans les logs ; droits des personnes.
- Biais : population sous-représentée dans les données, proxy discriminant, biais de collecte (qui a produit la donnée, dans quel but).
- Coût : volume réel supérieur au prévu, prix fournisseur, boucles d'agents, réentraînements.
- Dépendance à un tiers : fournisseur de modèle, API externe, changement de version, quota, arrêt du service, réversibilité.
- Réglementaire : voir `checkpoint-reglementaire.md`, reporter ici les risques identifiés.
- Données : accès retiré, schéma source qui change, qualité qui se dégrade, fuite cible dans les features.
- Adoption : résistance des utilisateurs, double saisie, perte de confiance après une erreur visible.
- Sécurité : injection de prompt directe ou indirecte, exfiltration via tools, abus de privilèges.

## Règles

- Le signal d'alerte est quelque chose qu'on mesure déjà ou qu'on s'engage à mesurer (dashboard, alerte). « On s'en rendra compte » n'est pas un signal.
- Chaque risque a un propriétaire nommé (en perso : moi).
- Les risques acceptés sans mitigation sont marqués « accepté le AAAA-MM-JJ par ... ».
