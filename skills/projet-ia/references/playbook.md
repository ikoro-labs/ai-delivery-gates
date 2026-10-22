# Playbook Projet IA v2 - Framework réutilisable (ML / DL / GenAI / Plateforme)

> Document de référence à dupliquer au démarrage de chaque projet IA.
> Principe : chaque phase produit un livrable concret. Ne pas passer à la phase suivante sans le livrable de sortie.
> **Règle v2 : aucun document sans destinataire nommé, même si c'est moi dans six mois.**

---

## Comment utiliser ce playbook

### 1. Choisir le profil de projet

| Profil                       | Description                                                     | Phases actives                           |
| ---------------------------- | --------------------------------------------------------------- | ---------------------------------------- |
| **Spike**                    | Lever une incertitude technique en quelques jours               | 0 uniquement                             |
| **Projet perso / portfolio** | Système étroit, utilisateurs réels ou réalistes, sert de preuve | 0 à 10 en taille S/M                     |
| **Système de production**    | Utilisateurs réels, engagement de service, équipe               | 0 à 10 en taille L                       |
| **Plateforme / librairie**   | Le consommateur est un développeur, pas un utilisateur final    | 0 à 10 avec les substitutions ci-dessous |

### 2. Choisir la taille

Chaque phase se décline en trois tailles. **S** : quelques lignes dans un seul fichier. **M** : un document par phase. **L** : le livrable complet tel que décrit.

Par défaut, un projet perso tourne en S sur les phases 2, 3, 8, et en M ou L sur 4, 5, 7, 9. La profondeur va dans le système, pas dans la documentation qui le décrit.

### 3. Substitutions pour le profil Plateforme / librairie

| À remplacer                | Par                                                                                  |
| -------------------------- | ------------------------------------------------------------------------------------ |
| 1.3 Persona + user journey | Consommateurs de l'API : qui appelle, depuis quel contexte, avec quelles contraintes |
| 2.1 User stories           | Cas d'usage d'intégration, du "hello world" au cas avancé                            |
| 2.3 Spéc API               | Contrats publics, politique de versionnement, compatibilité ascendante, dépréciation |
| 6.6 Front minimal          | Expérience développeur : quickstart en moins de 10 minutes, exemples exécutables     |
| 10.1 README                | Documentation de référence + guide de contribution + politique d'extension           |

---

## Phase 0 - Spike (nouveau)
**Objectif** : lever la plus grosse incertitude technique avant d'investir. Timeboxé.

| # | Tâche | Livrable |
|---|---|---|
| 0.1 | Formuler l'incertitude en une question binaire ("est-ce que X est atteignable avec Y ?") | Une phrase écrite |
| 0.2 | Fixer la timebox (1 à 3 jours) et le critère de réussite chiffré | Timebox + seuil |
| 0.3 | Coder jetable, sans tests, sans propreté, sur données réelles ou échantillon | Résultat mesuré |
| 0.4 | Verdict : viable, non viable, ou incertitude déplacée | Note de 10 lignes |
| 0.5 | **Jeter le code du spike** | Dépôt vierge pour la phase 6 |

**Anti-pattern** : laisser un spike devenir la base du projet. Le code de spike n'a ni tests ni structure, et il définira toute l'architecture par inertie.

**Point de sortie** : si le critère de 0.2 n'est pas atteint à la fin de la timebox, on ne prolonge pas. On reformule le problème ou on arrête.

---

## Phase 1 - Cadrage
**Objectif** : valider que le problème mérite d'être résolu et que l'IA est la bonne approche.

| #   | Tâche                                                                                                      | Livrable                                  |
| --- | ---------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| 1.1 | Définir le problème : qui souffre, de quoi, à quelle fréquence                                             | One-pager problème                        |
| 1.2 | Vérifier que l'IA est nécessaire (vs règles métier / SQL / heuristique)                                    | Justification écrite                      |
| 1.3 | Définir les utilisateurs cibles et le cas d'usage unique du MVP                                            | Persona + user journey                    |
| 1.4 | Fixer les success metrics : produit (usage, rétention) ET techniques (perf modèle, latence, coût)          | Tableau de métriques chiffrées            |
| 1.5 | Fixer les SLOs : latence p95, disponibilité, budget mensuel max                                            | SLOs documentés                           |
| 1.6 | Analyse des risques : privacy, biais, coût, dépendances tierces, réglementaire                             | Registre des risques + mitigations        |
| 1.7 | Valider la faisabilité data : les données existent-elles, sont-elles accessibles, en quel volume/qualité ? | Preuve d'accès (échantillon réel extrait) |
| 1.8 | Go/No-Go                                                                                                   | Décision documentée                       |
| 1.9 | **Écrire les critères d'arrêt du projet** : à quelle date, sur quel chiffre, on arrête ou on pivote        | Critères datés et chiffrés                |

**Anti-pattern** : commencer à coder avant 1.7. Sans données accessibles, pas de projet.

**Sur 1.9** : un critère d'arrêt doit être falsifiable et daté. "Si les retours ne sont pas bons" n'en est pas un. "Si au 30/09 moins de 2 utilisateurs ont fait passer leurs propres données et déclarent qu'ils l'utiliseraient" en est un. On l'écrit avant de s'attacher au projet, jamais après.

### Variante : profil projet perso / portfolio

| #         | En profil perso                                                                                                                                                                       |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.1 à 1.3 | Trois lignes. Si je ne sais pas dire qui utiliserait ça, je construis une démo, pas un système                                                                                        |
| 1.4       | Ajouter une ligne : **quelle question d'entretien ce projet répond**                                                                                                                  |
| 1.5       | SLO auto-imposés mais réels (p95, coût pour mille requêtes). Ce sont les chiffres que je défendrai, donc ils sont mesurés, pas déclarés                                               |
| 1.6       | Réduit à trois risques maximum. Pas de volet réglementaire                                                                                                                            |
| 1.7       | **Point de mort réel des projets perso.** La plupart échouent sur les données, pas sur le modèle. Jeu de données réel avec de vraies interactions, identifié avant d'écrire une ligne |
| 1.8       | Décision solo, deux lignes                                                                                                                                                            |
| 1.9       | Garde tout son sens : un projet perso sans condition d'arrêt devient un zombie qu'on traîne deux ans                                                                                  |

Ce qui saute : registre de risques complet, volet réglementaire, validation par des parties prenantes.

---

## Phase 2 - Spécifications
**Objectif** : figer le QUOI avant le COMMENT.

| #   | Tâche                                                        | Livrable          |
| --- | ------------------------------------------------------------ | ----------------- |
| 2.1 | User stories du MVP (max 8) avec critères d'acceptation      | Backlog priorisé  |
| 2.2 | Spéc fonctionnelle : parcours utilisateur bout-en-bout       | Diagramme de flux |
| 2.3 | Spéc API : endpoints, schémas (pydantic), erreurs            | Contrat OpenAPI   |
| 2.4 | Spéc data : schémas, data contracts, rétention, suppression  | Schéma versionné  |
| 2.5 | Spéc non-fonctionnelle : sécurité, privacy, conformité, SLOs | Section NFR       |
| 2.6 | Définir ce qui est HORS scope (aussi important que le scope) | Liste "non-goals" |

---

## Phase 3 - ML System Design
**Objectif** : concevoir le système complet avant d'entraîner quoi que ce soit.

| #    | Tâche                                                                                                                                  | Livrable              |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| 3.1  | Diagramme d'architecture global : ingestion → features → training → serving → monitoring → feedback                                    | Diagramme             |
| 3.2  | Formuler chaque problème ML : type de tâche, input/output, métrique d'optimisation vs métrique métier                                  | Fiche par modèle      |
| 3.3  | Choix d'architecture documentés avec trade-offs (3 lignes de justification minimum par choix)                                          | ADRs                  |
| 3.4  | Design features : online vs offline, fraîcheur, feature store ou pas                                                                   | Spéc features         |
| 3.5  | Design training : déclencheurs de retraining, validation avant promotion, rollback                                                     | Pipeline dessiné      |
| 3.6  | Design serving : batch vs temps réel, caching, fallback si modèle indisponible                                                         | Spéc serving          |
| 3.7  | (GenAI) Design agents : graphe d'états, tools, gestion d'erreurs, limites de coût/session, garde-fous                                  | Spéc agents           |
| 3.8  | (GenAI) Design RAG : chunking, embedding, retrieval, re-ranking, évaluation faithfulness                                               | Spéc RAG              |
| 3.9  | Design évaluation : golden sets figés, métriques offline/online, évals GenAI (LLM-as-judge)                                            | Plan d'éval           |
| 3.10 | Estimation de coûts par composant vs budget SLO                                                                                        | Tableau de coûts      |
| 3.11 | **Frontière de confiance** : d'où viennent les entrées non fiables, où sont les points de contrôle, quels privilèges portent les tools | Schéma des frontières |

**Anti-pattern** : choisir la techno avant le problème ("je veux utiliser LangGraph" → non : "quel problème, quelle solution minimale").

---

## Phase 4 - Data
**Objectif** : pipeline de données fiable avant toute modélisation.

| # | Tâche | Livrable |
|---|---|---|
| 4.1 | Ingestion : connecteurs, gestion OAuth/quotas, idempotence | Pipeline d'ingestion |
| 4.2 | Validation : data contracts en CI (pandera / great_expectations) | Contrats actifs |
| 4.3 | Stockage par zones : raw / processed / curated | Structure S3 + DB |
| 4.4 | EDA : distributions, manquants, fuites de données potentielles | Notebook + synthèse |
| 4.5 | Feature engineering versionné et testé | Code features + tests |
| 4.6 | (Si labeling) Process d'annotation + contrôle qualité inter-annotateurs | Guidelines + dataset labellisé |
| 4.7 | **Versionnement des jeux de données et lineage** : quel dataset a produit quel modèle, avec quel code | Snapshots identifiés |

**Point de sortie** : si à la fin de la phase 4 la qualité des données rend la cible de 1.4 inatteignable, on revient en phase 1. Continuer en espérant que le modèle compense est l'erreur la plus coûteuse du cycle.

---

## Phase 5 - Modélisation
**Objectif** : itérer vite, mesurer tout, baseline d'abord.

| # | Tâche | Livrable |
|---|---|---|
| 5.1 | **Baseline simple d'abord** (règle, régression, RandomForest) | Score de référence |
| 5.2 | Tracking systématique dès le run 1 (MLflow ou équivalent) | Expériences tracées |
| 5.3 | Itérations modèles : chaque itération battant la précédente est documentée (quoi, pourquoi, gain) | Log d'itérations |
| 5.4 | Validation rigoureuse : split temporel si time series, pas de fuite train/test | Protocole écrit |
| 5.5 | (GenAI) Itération prompts/contexte versionnée et évaluée sur golden set | Prompts versionnés + scores |
| 5.6 | Sélection finale : gain vs baseline chiffré, coût d'inférence acceptable | Modèle en registry |
| 5.7 | **Reproductibilité** : seeds, environnement figé, commande unique pour rejouer le meilleur run | Run rejouable |
| 5.8 | **Budget de calcul** : coût et durée d'entraînement plafonnés, décidés avant de lancer | Plafond écrit |

**Anti-pattern** : partir sur du DL/LLM sans baseline. Le gain doit être prouvé, pas supposé.

**Point de sortie** : si après trois itérations documentées le gain sur la baseline reste sous le seuil de 1.4, on arrête la modélisation et on livre la baseline. Une baseline en production bat un modèle sophistiqué jamais déployé.

---

## Phase 6 - Développement
**Objectif** : code de qualité production dès le départ.

| # | Tâche | Livrable |
|---|---|---|
| 6.1 | Structure repo claire (api/, ml/, agents/, infra/, front/) + pre-commit (lint, typing) | Repo initialisé |
| 6.2 | IaC dès le départ (Terraform/CDK), environnements dev/prod séparés | Infra versionnée |
| 6.3 | Backend API : auth, endpoints métier, health checks, gestion d'erreurs structurée | API fonctionnelle |
| 6.4 | Intégration serving modèles dans l'API (avec timeout + fallback) | Endpoints ML |
| 6.5 | (GenAI) Orchestration agents + tools + mémoire | Agents fonctionnels |
| 6.6 | Front minimal centré sur le parcours MVP | UI utilisable |
| 6.7 | Gestion des secrets (Secrets Manager, jamais en clair) | Zéro secret dans le repo |

---

## Phase 7 - Tests
**Objectif** : confiance pour déployer sans peur.

| # | Tâche | Livrable |
|---|---|---|
| 7.1 | Tests unitaires sur la logique cœur (~80%) | CI verte |
| 7.2 | Tests d'intégration API + DB + auth | Suite d'intégration |
| 7.3 | Tests data : contrats en CI, schéma tiers cassé détecté | Alertes data |
| 7.4 | Tests modèles : perf minimale sur golden set en CI (bloquant si régression) | Gate qualité modèle |
| 7.5 | (GenAI) Suite d'évals à chaque changement de prompt/modèle : pertinence, faithfulness, refus corrects | Gate qualité GenAI |
| 7.6 | Tests de charge : p95 vs SLO | Rapport de charge |
| 7.7 | Tests E2E du parcours critique | Suite E2E |
| 7.8 | **(GenAI) Tests adverses** : injection de prompt directe et indirecte via contenu récupéré, exfiltration de données, appel d'outil abusif, boucle infinie d'agent | Suite adverse en CI |

---

## Phase 8 - Déploiement
**Objectif** : livrer souvent, sans casse.

| # | Tâche | Livrable |
|---|---|---|
| 8.1 | CI : lint + tests + build + scan sécurité | Pipeline CI |
| 8.2 | CD : auto en dev, approbation manuelle en prod | Pipeline CD |
| 8.3 | Stratégie release modèles : shadow / canary, rollback en un clic | Procédure testée |
| 8.4 | Runbook de déploiement : migrations, feature flags, plan de rollback | Checklist |
| 8.5 | Déploiement progressif : staging → validation → prod | Prod en ligne |

---

## Phase 9 - Monitoring & Exploitation
**Objectif** : savoir ce qui se passe, réagir vite, apprendre de chaque incident.

| #   | Tâche                                                                                                         | Livrable            |
| --- | ------------------------------------------------------------------------------------------------------------- | ------------------- |
| 9.1 | Dashboards : (1) SLOs produit, (2) santé modèles (drift, perf), (3) LLM/agents (latence, coût, erreurs tools) | Dashboards en ligne |
| 9.2 | Tracing GenAI (Langfuse ou équiv.) : sessions, coûts, conversations à problème                                | Tracing actif       |
| 9.3 | Détection de drift (features + prédictions) avec rapport périodique                                           | Rapports drift      |
| 9.4 | Alerting : SLO dépassé, drift, budget à 80%                                                                   | Alertes → Slack     |
| 9.5 | Journal d'incidents : post-mortem sous 48h (contexte, cause racine, fix, prévention)                          | Post-mortems        |
| 9.6 | Boucle de feedback : signaux utilisateurs → dataset d'amélioration → retraining                               | Boucle active       |
| 9.7 | Revue mensuelle : coûts, optimisations, tendances                                                             | Compte-rendu        |

**Point de sortie** : à la revue mensuelle, si l'usage réel reste sous le seuil de 1.4 pendant deux mois consécutifs, appliquer les critères d'arrêt de 1.9. Maintenir un système que personne n'utilise coûte plus cher que de l'éteindre.

---

## Phase 10 - Capitalisation
**Objectif** : transformer le projet en actif (portfolio, connaissance, réutilisation).

| # | Tâche | Livrable |
|---|---|---|
| 10.1 | README complet : architecture, choix, limitations, chiffres réels | Doc |
| 10.2 | Article technique : trade-offs et résultats mesurés | Publication |
| 10.3 | Post-mortems publiés (anonymisés) | 2-3 posts |
| 10.4 | Rétrospective : ce qui marche → mettre à jour CE playbook | Playbook v+1 |
| 10.5 | **Fiche entretien** : problème, contraintes, mon rôle précis, 3 arbitrages, chiffres, ce que je referais autrement | Une page par projet |

---

## Checklists transverses

### Checklist "anti toy-project"
- [ ] De vrais utilisateurs identifiés et un plan pour les atteindre
- [ ] Des données réelles (APIs, production), pas seulement Kaggle
- [ ] Des SLOs chiffrés et mesurés (latence, dispo, budget)
- [ ] Un journal d'incidents vivant
- [ ] Des chiffres à raconter : "j'ai amélioré X de Y%", "réduit le coût de Z"

### Checklist "anti tunnel de documentation" (nouveau)
- [ ] Chaque document produit a un destinataire nommé
- [ ] Le ratio heures de code sur heures de document reste au-dessus de 3 pour 1
- [ ] La phase 3 n'a pas duré plus longtemps que la phase 0 et la phase 4 réunies
- [ ] Quelque chose tourne, même mal, avant la fin de la deuxième semaine

### Checklist privacy/sécurité (systématique)
- [ ] Chiffrement at-rest et in-transit
- [ ] Scopes OAuth minimaux
- [ ] Suppression des données sur demande
- [ ] Pas de PII dans les logs ni dans les prompts LLM non nécessaires
- [ ] Vérifier le cadre réglementaire (santé, finance = zones sensibles)
- [ ] Le contenu récupéré (documents, pages, outputs d'outils) est traité comme une entrée non fiable

### Checklist coûts GenAI
- [ ] Limite de coût par session/utilisateur
- [ ] Caching des réponses/embeddings
- [ ] Modèle le plus petit qui fait le job (router petit/gros modèle)
- [ ] Suivi coût par requête dans le monitoring

### Definition of Done (toute feature)
- [ ] Testée (unit + intégration)
- [ ] Monitorée (métrique + alerte si critique)
- [ ] Documentée (README ou ADR)
- [ ] Déployée et vérifiée en prod

---

## Principes directeurs
1. **Baseline d'abord** - prouver le gain avant de complexifier.
2. **Chaque phase livre quelque chose d'utilisé** - pas de tunnel.
3. **Mesurer > supposer** - chaque décision d'architecture appuyée par un chiffre.
4. **Les trade-offs documentés sont de l'or** (ADRs) - c'est la matière des entretiens et des revues.
5. **Le monitoring n'est pas une phase finale** - il commence avec le premier déploiement.
6. **Réduire le scope, augmenter la profondeur** - un système étroit et abouti > une plateforme large et creuse.
7. **Écrire la condition d'arrêt avant de s'attacher** - un projet sans point de sortie ne s'arrête jamais.
8. **Le playbook sert le projet, pas l'inverse** - si une phase ne change aucune décision, elle passe en taille S.
