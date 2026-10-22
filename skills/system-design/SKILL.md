---
name: system-design
description: >
  Phase 3 du playbook projet IA : concevoir le système complet avant d'entraîner ou de prompter quoi que ce
  soit. Architecture, fiche par modèle, ADR avec trade-offs chiffrés, features, training, serving, design
  agents et RAG, plan d'évaluation avec golden set, estimation de coûts, frontière de confiance. Utiliser
  quand l'utilisateur parle d'architecture, de choix de modèle ou de techno, d'ADR, de RAG, d'agents, de
  golden set, d'évaluation, de LLM-as-judge, de coûts d'inférence, de garde-fous, de prompt injection,
  de « system design », ou quand l'orchestrateur projet-ia lance la phase 3.
metadata:
  version: "0.1.0"
---

# Phase 3 : ML system design

## Pourquoi cette phase existe

Concevoir le système entier (ingestion, features, training, serving, monitoring, feedback) avant d'écrire la
première ligne de modélisation. Anti-pattern nommé dans le playbook : choisir la techno avant le problème
(« je veux utiliser LangGraph »). Quand l'utilisateur arrive avec une techno choisie, repartir de la fiche
modèle (3.2) et traiter la techno comme une option d'ADR parmi d'autres.

Vérifier que les phases 1 et 2 sont dans `phases_closes`. Sinon, renvoyer à l'orchestrateur.

## Entretien, dans l'ordre

| Étape | Ce qu'on produit | Référence |
|---|---|---|
| 3.2 Fiches modèle | Une fiche par problème ML : type de tâche, entrées et sorties, métrique d'optimisation vs métrique métier, baseline | `references/fiche-modele.md` |
| 3.1 Architecture | Diagramme mermaid ingestion → features → training → serving → monitoring → feedback | `references/architecture.md` |
| 3.3 ADR | Un ADR par choix non trivial, options chiffrées, existant ou achat toujours évalué | `references/adr.md` |
| 3.4 Features | Online vs offline, fraîcheur, feature store ou pas | section dans `architecture.md` |
| 3.5 Training | Déclencheurs de réentraînement, validation avant promotion, rollback | section dans `architecture.md` |
| 3.6 Serving | Batch vs temps réel, caching, timeout, fallback si modèle indisponible | section dans `architecture.md` |
| 3.7 Agents (GenAI) | Graphe d'états, tools et privilèges, erreurs, limites par session, garde-fous | `references/design-agents.md` |
| 3.8 RAG (GenAI) | Chunking, embedding, retrieval, re-ranking, fraîcheur de l'index, faithfulness | `references/design-rag.md` |
| 3.9 Évaluation | Golden set figé depuis le jeu d'éval amorcé en phase 1, métriques offline et online, juge calibré, seuils en CI, evals adverses | `references/plan-eval.md` |
| 3.10 Coûts | Par composant, prix sourcé et daté, total mensuel vs budget SLO | `references/couts.md` |
| 3.11 Frontière de confiance | Entrées non fiables, points de contrôle, privilèges des tools, données sensibles | `references/frontiere-confiance.md` |

Clôture : passer les checklists de `references/checklists.md` (privacy et sécurité, coûts GenAI, anti toy-project,
anti tunnel).

Taille S (profil perso) : un seul fichier `system-design.md` avec fiche modèle, diagramme, deux ou trois ADR
courts, plan d'éval et coûts. Les sections 3.7 et 3.8 seulement si GenAI.

## Règles de rédaction

- Pas d'ADR sans au moins deux options et un chiffre par option (coût, latence, effort, maturité). L'option
  « existant, achat ou ne rien construire » figure toujours, même écartée.
- Chaque composant du diagramme répond à une story ou à un SLO. Un composant « au cas où » est un non-goal
  qui n'a pas été écrit.
- Le golden set est figé, daté, versionné, et sa taille est justifiée par rapport à la régression qu'on veut
  détecter. Un juge LLM est calibré contre des labels humains avec un taux d'accord mesuré.
- Les coûts utilisent des prix sourcés et datés (doc fournisseur, URL). Un total au-dessus du budget SLO
  renvoie en phase 1 ou 2, pas à un « on optimisera plus tard ».
- Les entrées non fiables (documents récupérés, outputs de tools, contenu utilisateur) sont listées et chaque
  tool a un privilège minimal écrit.
- Reproductibilité et observabilité se décident ici : seeds, environnement figé, tracing, coût par requête,
  version du modèle dans chaque réponse.

## Livrables (dossier `docs/projet/03-system-design/`)

| Fichier | Depuis |
|---|---|
| `fiches-modele.md` | `references/fiche-modele.md` |
| `architecture.md` | `references/architecture.md` (diagramme, features, training, serving) |
| `adr/ADR-001-<slug>.md` ... | `references/adr.md` |
| `design-agents.md` (GenAI) | `references/design-agents.md` |
| `design-rag.md` (GenAI) | `references/design-rag.md` |
| `plan-eval.md` | `references/plan-eval.md` |
| `couts.md` | `references/couts.md` |
| `frontiere-confiance.md` | `references/frontiere-confiance.md` |

## Critères de sortie

- Chaque problème ML a sa fiche avec baseline et les deux métriques distinguées.
- Chaque choix non trivial a un ADR avec options chiffrées.
- Fallback défini pour chaque appel de modèle ; rollback défini pour chaque promotion de modèle.
- Golden set figé, daté, versionné ; seuils bloquants en CI écrits ; evals adverses listées (GenAI).
- Total des coûts sous le budget SLO, avec sources datées.
- Frontière de confiance dessinée, privilèges des tools écrits.
- Checklists transverses passées.

## Ensuite

Signaler à l'orchestrateur que les critères de sortie sont remplis. La revue de phase 3 inclut le pré-mortem.
