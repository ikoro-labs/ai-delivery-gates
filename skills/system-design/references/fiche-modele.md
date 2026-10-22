# Fiche modèle : [nom du problème ML]

Destinataire : ... | Date : ...

| Rubrique | Contenu |
|---|---|
| Problème métier servi | story ou SLO de référence |
| Type de tâche | classification, ranking, extraction, génération, régression, retrieval, ... |
| Entrées | schéma, provenance, fraîcheur, ce qui est connu au moment de la prédiction |
| Sorties | schéma, format, confiance ou score, ce que fait le consommateur avec |
| Métrique d'optimisation | ce que le modèle maximise (loss, métrique offline) |
| Métrique métier | ce que le produit mesure (fiche de cadrage §2), et pourquoi les deux peuvent diverger |
| Baseline | règle, heuristique, modèle simple ; score actuel sur le jeu d'éval |
| Seuil de gain | gain minimal sur la baseline pour justifier le modèle (phase 1, 1.4) |
| Données d'entraînement | source, volume, période, biais connus, fuites exclues |
| Contraintes | latence, coût par inférence, taille, explicabilité, supervision humaine |
| Niveau d'autonomie | assiste / recommande / agit sous supervision / autonome (matrice 1.3 bis) |
| Risques spécifiques | drift, biais, dépendance fournisseur |

Un modèle par fiche. Un système qui nécessite trois fiches a trois problèmes ML, et donc trois baselines.
