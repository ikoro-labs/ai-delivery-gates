# Design RAG : [nom du projet]

Destinataire : ... | Date : ...

| Rubrique | Choix | Justification chiffrée (ADR si non trivial) |
|---|---|---|
| Corpus | sources, volume, formats, fraîcheur, droits | |
| Prétraitement | extraction (PDF, tableaux, images), nettoyage, métadonnées conservées | |
| Chunking | stratégie, taille, recouvrement, respect de la structure (sections, tableaux) | |
| Embeddings | modèle, dimension, coût, langue, multilingue | |
| Index | type, filtres par métadonnées, mise à jour (incrémentale, rebuild), suppression d'un document | |
| Retrieval | top-k, hybride (lexical + vectoriel), filtres | |
| Re-ranking | oui/non, modèle, coût ajouté, gain mesuré | |
| Génération | modèle, contexte maximal, citations obligatoires, comportement sans résultat pertinent | |
| Fraîcheur | délai entre mise à jour d'une source et visibilité dans les réponses | |

## Évaluation spécifique (reportée dans plan-eval.md)
- Retrieval : recall@k et précision sur le golden set de questions avec passages attendus.
- Faithfulness : la réponse est-elle soutenue par les passages fournis (juge calibré) ?
- Refus corrects : questions hors corpus, le système dit qu'il ne sait pas.
- Injection indirecte : documents du corpus contenant des instructions, le système ne les suit pas.

## Entrées non fiables
Tout document du corpus est une entrée non fiable (frontière de confiance 3.11).
