# Checklists transverses (à passer en clôture de phase 3)

## Privacy et sécurité (systématique)
- [ ] Chiffrement at-rest et in-transit
- [ ] Scopes OAuth minimaux
- [ ] Suppression des données sur demande
- [ ] Pas de PII dans les logs ni dans les prompts LLM non nécessaires
- [ ] Cadre réglementaire vérifié (checkpoint de phase 1 reporté en NFR)
- [ ] Le contenu récupéré (documents, pages, outputs d'outils) est traité comme une entrée non fiable

## Coûts GenAI
- [ ] Limite de coût par session et par utilisateur
- [ ] Caching des réponses et des embeddings
- [ ] Modèle le plus petit qui fait le job (routage petit/gros modèle)
- [ ] Suivi du coût par requête prévu dans le monitoring

## Anti toy-project
- [ ] De vrais utilisateurs identifiés et un plan pour les atteindre
- [ ] Des données réelles (APIs, production), pas seulement Kaggle
- [ ] Des SLO chiffrés et mesurés (latence, dispo, budget)
- [ ] Un journal d'incidents prévu
- [ ] Des chiffres à raconter : « j'ai amélioré X de Y% », « réduit le coût de Z »

## Anti tunnel de documentation
- [ ] Chaque document produit a un destinataire nommé
- [ ] Le ratio heures de code sur heures de document reste au-dessus de 3 pour 1 (projeté)
- [ ] La phase 3 n'a pas duré plus longtemps que le spike plus une semaine
- [ ] Quelque chose tournera, même mal, avant la fin de la deuxième semaine après le Go

## Definition of Done (reprise pour les phases suivantes)
- [ ] Testée (unit + intégration)
- [ ] Monitorée (métrique + alerte si critique)
- [ ] Documentée (README ou ADR)
- [ ] Déployée et vérifiée en prod
