---
name: revue-de-phase
description: >
  Gate de fin de phase du playbook projet IA : lance en parallèle les agents lead-tech, product-owner et
  expert-metier sur les livrables d'une phase (spike, cadrage, spécifications, system design), consolide
  leurs constats classés bloquant / majeur / mineur, mène le pré-mortem et rend le verdict de clôture.
  Utiliser quand l'utilisateur demande une revue, un challenge, une relecture critique d'un cadrage, d'une
  spec, d'un ADR ou d'un design IA : « challenge-moi », « qu'est-ce que j'ai raté », « relis ça », « on peut
  clore la phase ? », « review this spec », ou quand l'orchestrateur projet-ia termine une phase.
metadata:
  version: "0.1.0"
---

# Revue de phase

## Pourquoi cette gate existe

L'auteur d'un document ne voit plus ses trous. Trois lecteurs avec des angles différents et des grilles
écrites en voient davantage, à condition qu'ils ne se lisent pas entre eux et qu'ils soient tenus à un format
qui interdit la complaisance. La gate ne juge pas la qualité de la prose : elle cherche ce qui fera échouer
le projet et le transforme en questions auxquelles l'utilisateur peut répondre.

## 1. Préparer le paquet

Rassembler, sans rien reformuler :
- la phase revue et sa taille (depuis `docs/projet/etat.md`), le profil, le domaine ;
- les chemins des livrables de la phase ;
- l'état du projet complet ;
- les critères de sortie de la phase (section « Critères de sortie » du skill de phase) ;
- le fichier de domaine : `references/domaines/<domaine>.md`. S'il n'existe pas, joindre
  `references/domaines/_template.md` et le signaler à l'expert métier ;
- `references/format-constat.md`, à transmettre intégralement à chaque agent.

Si l'utilisateur demande une revue hors orchestrateur (« challenge ce document »), déduire la phase du
contenu, le dire, et procéder de la même façon sans fichier d'état s'il n'y en a pas.

## 2. Lancer les trois agents

Lancer `ai-delivery-gates:lead-tech`, `ai-delivery-gates:product-owner` et `ai-delivery-gates:expert-metier` en parallèle, dans le
même tour, avec le même paquet. Chaque agent reçoit son angle, pas les constats des autres : l'indépendance est
ce qui fait apparaître les convergences.

Phase 0 : l'agent lead-tech passe sa grille complète ; product-owner et expert-metier reçoivent une seule
question chacun (« l'incertitude levée est-elle l'hypothèse la plus risquée du projet ? » et « l'échantillon
testé est-il représentatif des cas du terrain ? ») et répondent en un constat maximum.

Phases 1 et 3 : demander explicitement le pré-mortem (trois scénarios par agent).

## 3. Consolider

Suivre `references/consolidation.md` : contrôle du format, dédoublonnage, classement, convergences, puis
présentation à l'utilisateur. Un constat qui ne respecte pas le format (pas de section visée, pas de question,
pas de preuve attendue) est renvoyé à l'agent ou reformulé, jamais présenté tel quel.

## 4. Pré-mortem (phases 1 et 3)

Suivre `references/pre-mortem.md`. Chaque scénario finit en risque, en critère d'arrêt, en réponse écrite ou en
acceptation datée. Sans pré-mortem traité, la phase n'est pas close.

## 5. Verdict et clôture

Règle de clôture, fixée par l'utilisateur à la conception du plugin :
- tous les bloquants sont levés (preuve fournie et livrable mis à jour), ou clos « non fondé » avec motif si
  l'utilisateur montre que l'agent a mal lu ;
- chaque majeur est levé ou accepté avec un motif daté, écrit dans l'état (ligne de revue et table Décisions)
  et dans le livrable ;
- les mineurs sont consignés, jamais bloquants.

Passages : le second passage ne relance que les agents concernés, sur les points restants, avec les réponses
de l'utilisateur. Au-delà de deux passages, remettre la liste des points ouverts à l'utilisateur avec la mention
« décision humaine requise » et ne pas clore : la revue n'est pas là pour boucler.

Écrire dans `docs/projet/etat.md` : date, phase, numéro de passage, bloquants restants, majeurs acceptés avec
motif, verdict. Rendre la main à l'orchestrateur.
