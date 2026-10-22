---
name: specifications
description: >
  Phase 2 du playbook projet IA : figer le QUOI avant le COMMENT. User stories du MVP avec critères
  d'acceptation, parcours bout-en-bout, spécification API, spécification data, exigences non fonctionnelles,
  non-goals. Utiliser quand l'utilisateur parle de backlog, user stories, critères d'acceptation, endpoints,
  schémas, contrat d'API, OpenAPI, pydantic, data contracts, rétention, NFR, périmètre, « ce qu'on ne fait
  pas », « product spec », ou quand l'orchestrateur projet-ia lance la phase 2.
metadata:
  version: "0.1.0"
---

# Phase 2 : spécifications

## Pourquoi cette phase existe

Figer ce que le système fait et ne fait pas avant de décider comment. Les stories donnent les critères
d'acceptation que les tests et les évals reprendront ; la spec data fixe ce qu'on a le droit de stocker ; les
non-goals protègent le périmètre quand la phase 3 voudra tout prévoir.

Vérifier d'abord que la phase 1 est dans `phases_closes` de l'état. Sinon, renvoyer à l'orchestrateur.

## Entretien, dans l'ordre

| Étape | Ce qu'on produit | Référence | Pourquoi dans cet ordre |
|---|---|---|---|
| 2.1 Stories | Huit stories maximum, format INVEST, critères d'acceptation nominal, limite, erreur | `references/user-story.md` | Tout le reste en découle |
| 2.6 Non-goals | Liste datée de ce qu'on ne fait pas, avec motif et condition de réexamen | `references/non-goals.md` | Écrits tout de suite après les stories, pendant que les idées écartées sont fraîches |
| 2.2 Parcours | Diagramme de flux bout-en-bout en mermaid, avec les chemins d'échec | `references/parcours.md` | Révèle les stories manquantes |
| 2.3 Spec API | Endpoints, schémas (pydantic ou OpenAPI), modèle d'erreur, versionnement | `references/spec-api.md` | Contrat entre front, backend et ML |
| 2.4 Spec data | Schémas, data contracts, rétention, suppression, PII | `references/spec-data.md` | Contrat entre sources et pipeline |
| 2.5 NFR | Sécurité, privacy, conformité, SLO repris de la phase 1, observabilité | `references/nfr.md` | Reprend les contraintes certaines du checkpoint réglementaire |

Profil plateforme : appliquer les substitutions (consommateurs de l'API, cas d'usage d'intégration, contrats
publics et compatibilité ascendante). Profil perso : une ligne « ce que cette story prouve en entretien » par
story ; taille S signifie un seul fichier `specifications.md` avec stories, non-goals et parcours.

## Règles de rédaction

- Une story a un rôle précis (jamais « utilisateur »), une capacité observable, un bénéfice. Chaque story a au
  moins un critère d'acceptation de cas d'erreur ou de fallback : c'est là que les systèmes IA échouent.
- Ce qui n'est pas une story : une décision d'architecture (ADR, phase 3), une exigence transverse (NFR),
  une tâche technique sans bénéficiaire (backlog), un epic déguisé (à découper).
- Les SLO de la NFR sont copiés de la fiche de cadrage, pas réinventés. Si un SLO change ici, c'est une
  décision consignée dans l'état avec motif.
- Les critères d'acceptation chiffrés (latence, taille de liste, délai) utilisent les mêmes unités et les
  mêmes percentiles que les SLO.
- Une story qui contredit un non-goal est une erreur à résoudre avant la revue.

## Livrables (dossier `docs/projet/02-specifications/`)

| Fichier | Depuis |
|---|---|
| `backlog.md` | `references/user-story.md`, stories priorisées |
| `non-goals.md` | `references/non-goals.md` |
| `parcours.md` | `references/parcours.md` |
| `spec-api.md` | `references/spec-api.md` |
| `spec-data.md` | `references/spec-data.md` |
| `nfr.md` | `references/nfr.md` |

## Critères de sortie

- Huit stories au plus, chacune testable (un test qui échoue avant et passe après est imaginable).
- La première story livrable seule apporte une valeur observable.
- Non-goals écrits, datés, cohérents avec les stories.
- Parcours avec au moins un chemin d'échec par point de dépendance (modèle, donnée, tiers).
- Spec API avec modèle d'erreur et politique de versionnement ; spec data avec rétention et suppression.
- NFR : chaque exigence a une cible mesurable et une méthode de vérification.

## Ensuite

Signaler à l'orchestrateur que les critères de sortie sont remplis, puis `revue-de-phase`.
