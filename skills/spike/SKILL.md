---
name: spike
description: >
  Phase 0 du playbook projet IA : lever la plus grosse incertitude technique en timebox, sur données réelles,
  avec du code jetable. Utiliser dès que l'utilisateur parle de spike, de POC jetable, de prototype rapide,
  de « est-ce que X est faisable avec Y », « on teste vite », « feasibility check », ou quand l'orchestrateur
  projet-ia lance la phase 0.
metadata:
  version: "0.1.0"
---

# Phase 0 : spike

## Pourquoi cette phase existe

Un spike achète de l'information, pas du code. On y lève la plus grosse incertitude technique avant d'investir
dans le cadrage et le design. Le danger documenté dans le playbook : laisser le spike devenir la base du
projet. Son code n'a ni tests ni structure, et il définira toute l'architecture par inertie.

## Entretien, dans l'ordre

1. **0.1 La question binaire.** Demander à l'utilisateur de formuler l'incertitude en une phrase répondant par
   oui ou non : « est-ce que X est atteignable avec Y ? ». Refuser les formulations ouvertes (« explorer »,
   « voir ce que ça donne »). Si deux incertitudes émergent, prendre la plus risquée et noter l'autre.
2. **0.2 Timebox et critère.** Un à trois jours. Le critère de réussite est un chiffre fixé maintenant (ex. recall
   supérieur à 0,7 sur 200 cas réels, latence sous 2 s sur 50 requêtes). Un critère fixé après les résultats
   n'est pas un critère.
3. **0.3 Données.** Réelles ou échantillon réel. Noter la source et le chemin. Une donnée synthétique produit un
   verdict sur la donnée synthétique, pas sur le projet.
4. **0.4 Code.** Dans `spike/` à la racine du projet (le hook garde-code l'autorise). Pas de tests, pas de
   structure, pas de revue de code.
5. **0.5 Verdict.** Viable, non viable, ou incertitude déplacée (dans ce cas, écrire la nouvelle question).
   Note de dix lignes maximum selon `references/note-spike.md`.

## Livrable

`docs/projet/00-spike/note-spike.md`, rempli depuis `references/note-spike.md`. Destinataire nommé en en-tête.

## Critères de sortie

- Question binaire, timebox et critère chiffré écrits avant la première ligne de code (horodatés).
- Résultat mesuré sur données réelles, avec la commande ou le notebook qui l'a produit.
- Verdict écrit.
- Code jeté : proposer `git rm -r spike/` ou une archive hors du dépôt. Ce qui survit au spike, c'est la note et
  le résultat, jamais le code. Si l'utilisateur veut garder le code « pour s'en inspirer », l'archiver hors
  repo et le dire dans la note.

## Point de sortie

Timebox atteinte sans critère atteint : ne pas prolonger. Reformuler la question ou arrêter. Un spike prolongé
est un projet qui a commencé sans cadrage.

## Ensuite

Signaler à l'orchestrateur que les critères de sortie sont remplis. La revue de phase 0 est allégée : le
Lead Tech passe sa grille complète, le Product Owner et l'Expert métier répondent chacun à une seule question.
