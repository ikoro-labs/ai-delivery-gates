# Exigences non fonctionnelles : [nom du projet]

Destinataire : ... | Date : ...

Chaque exigence a une cible mesurable et une méthode de vérification. Une exigence sans méthode est un vœu.
Les SLO sont copiés de la fiche de cadrage (section 2). Les contraintes certaines du checkpoint réglementaire
deviennent des exigences ici.

| Domaine | Exigence | Cible | Vérifiée comment et quand | Origine (SLO 1.5, checkpoint, coût d'erreur) |
|---|---|---|---|---|
| Performance | latence p95 bout-en-bout | | test de charge avant release | SLO |
| Disponibilité | | | | SLO |
| Coût | budget mensuel, coût par mille requêtes, coût max par session | | suivi quotidien | SLO |
| Qualité modèle | perf minimale sur golden set | | CI, bloquant | SLO |
| Sécurité | authentification, scopes minimaux, secrets hors repo | | revue + scan en CI | |
| Sécurité GenAI | contenu récupéré traité comme non fiable, privilèges des tools, limite d'actions par session | | suite adverse en CI | coût d'erreur |
| Privacy | pas de PII dans les logs ni dans les prompts non nécessaires, suppression sur demande | | revue des logs, test de suppression | checkpoint |
| Conformité | obligations identifiées au checkpoint (documentation, supervision humaine, information des personnes) | | | checkpoint |
| Observabilité | tracing des requêtes, coût par requête, version du modèle dans chaque réponse | | vérifié en staging | |
| Reproductibilité | run rejouable en une commande, environnement figé | | | |
