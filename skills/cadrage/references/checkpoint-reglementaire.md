# Checkpoint réglementaire : [nom du projet]

Destinataire : ... | Rempli le : ... | Par : ...

Objectif : savoir avant le Go quelles règles s'imposent au système, pas les découvrir en revue de sécurité ou
devant un client. Pour chaque ligne : réponse, source datée (texte officiel, doc fournisseur, avis juridique
interne), statut. Une ligne sans source est « non vérifié ». L'expert métier et le Lead Tech contrôlent ce
fichier en revue.

Les textes et leurs échéances évoluent. Vérifier la version en vigueur sur une source officielle (EUR-Lex,
Légifrance, CNIL, Commission européenne) au moment du cadrage plutôt que de se fier à la mémoire.

| # | Question | Réponse | Source (URL, date) | Statut (ok / à traiter / non vérifié / sans objet) |
|---|---|---|---|---|
| 1 | Données personnelles traitées ? Lesquelles, pour quelle finalité, sur quelle base légale (RGPD) ? | | | |
| 2 | Données sensibles (santé, biométrie, opinions, infractions) ? Si oui, régime spécifique ? | | | |
| 3 | Une AIPD (analyse d'impact relative à la protection des données) est-elle requise ? Qui la porte ? | | | |
| 4 | Minimisation : quelles données on n'ingère pas, durée de conservation, suppression sur demande ? | | | |
| 5 | AI Act (règlement UE 2024/1689) : le cas d'usage relève-t-il d'une pratique interdite, d'un système à haut risque, d'une obligation de transparence, ou d'aucune catégorie ? Sur quel critère ? | | | |
| 6 | AI Act : quelles obligations en découlent (documentation, supervision humaine, journalisation, information des personnes) et à quelle échéance (vérifier la date en vigueur) ? | | | |
| 7 | Hébergement et résidence des données : où sont traitées les données (région), transferts hors UE, clauses contractuelles ? | | | |
| 8 | Fournisseur de modèle : conditions d'usage, utilisation des données pour l'entraînement du fournisseur, SLA, politique de changement de version, réversibilité ? | | | |
| 9 | Licences : données (droits d'usage), modèles et poids (licence, restrictions commerciales), librairies ? | | | |
| 10 | Propriété et responsabilité des sorties : qui est responsable d'une décision prise sur une sortie du système ? Validation humaine imposée par le domaine ? | | | |
| 11 | Secrets d'affaires et confidentialité : que contiennent les prompts et les logs, qui y accède ? | | | |
| 12 | Règles sectorielles (santé, finance, assurance, marchés publics, construction, ...) : lesquelles s'appliquent ? | | | |
| 13 | Traçabilité et archivage : quelles sorties doivent être conservées, combien de temps, sous quelle forme ? | | | |

## Sortie du checkpoint

- Risques identifiés reportés dans `registre-risques.md` avec propriétaire.
- Contraintes certaines reportées dans la NFR (phase 2, 2.5) : ce ne sont plus des risques, ce sont des exigences.
- Si une ligne est « à traiter » et bloque le Go (exemple : base légale absente), le dire dans la décision 1.8.
