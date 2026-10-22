---
name: projet-ia
description: >
  Orchestrateur du playbook projet IA, phases 0 à 3 (spike, cadrage, spécifications, system design).
  Utiliser ce skill dès que l'utilisateur démarre, cadre, spécifie ou conçoit un projet IA, ML, GenAI, RAG
  ou agentique, ou demande où en est un projet suivi par le playbook : « je démarre un projet IA »,
  « nouveau projet », « cadrage », « spike », « go/no-go », « où en est le projet », « phase suivante »,
  « clore la phase », « passe en taille S », « start an AI project », « scoping », « kickoff ».
  Déclencher aussi quand l'utilisateur parle d'architecture, de choix de modèle, de RAG ou d'agents pour un
  projet qui n'a pas encore de fichier docs/projet/etat.md : le cadrage passe avant la technique.
metadata:
  version: "0.1.0"
---

# Orchestrateur projet IA

## Rôle

Tenir la roadmap des phases 0 à 3 et empêcher de sauter une étape. Le playbook repose sur une règle simple :
chaque phase produit un livrable, chaque livrable passe une revue, et rien ne se code avant la fin de la
phase 1 (le hook `garde-code` du plugin le fait respecter). La raison est documentée dans
`references/playbook.md` : la plupart des projets IA échouent sur les données et le cadrage, pas sur le modèle.

## Démarrage d'une session

1. Chercher `docs/projet/etat.md` à la racine du projet.
   - S'il existe : le lire, résumer en trois lignes (phase courante, livrables, points ouverts) et reprendre là.
   - Sinon : poser les questions d'initialisation (nom du projet, profil, domaine métier, destinataire principal
     des documents ; sponsor, décideur du go/no-go et owner prod si profil production ou plateforme) puis créer
     le fichier à partir de `references/etat-projet.md`.
2. Lire `references/profils-tailles.md`, fixer la taille de chaque phase, l'écrire dans l'état. Pour le profil
   plateforme, appliquer les substitutions listées.
3. Lire la section de `references/playbook.md` qui correspond à la phase courante (phases 0 à 3). Les phases 4 à
   10 y figurent pour le contexte et les points de sortie, elles sont hors périmètre de ce plugin.

## Boucle de phase

Pour chaque phase, dans l'ordre 0, 1, 2, 3 :

1. Invoquer le skill de phase : `spike`, `cadrage`, `specifications`, `system-design`. Il mène l'entretien avec
   l'utilisateur et écrit les livrables sous `docs/projet/0N-<phase>/`.
2. Quand le skill de phase confirme que ses critères de sortie sont remplis, invoquer `revue-de-phase`.
3. Appliquer le verdict de la revue :
   - tous les bloquants levés, chaque majeur levé ou accepté avec motif daté : phase close, ajouter N à
     `phases_closes` dans l'état ;
   - sinon : retour au skill de phase sur les points restants, puis nouveau passage de revue.
4. Mettre à jour l'état après chaque étape : livrables, revues, décisions, journal daté.

Ne jamais invoquer un skill de phase N+1 tant que N n'est pas dans `phases_closes`. Si l'utilisateur insiste,
expliquer ce qui bloque et proposer la voie prévue (lever le point, ou accepter un majeur avec motif).

## Points de sortie, hérités du playbook

- Phase 0 : timebox atteinte sans critère atteint, on ne prolonge pas ; on reformule ou on arrête. Vérifier que
  le code du spike a été jeté avant de clore.
- Phase 1 : pas d'échantillon réel extrait, pas de Go. Critères d'arrêt non datés ou non chiffrés, pas de Go.
- Phase 3 : coûts estimés au-dessus du budget SLO, retour en 1.5 (revoir le budget) ou en 2.6 (réduire le
  périmètre). Pas de passage en force.
- Anti tunnel : signaler quand la phase 3 dure plus longtemps que le spike plus une semaine, et quand rien ne
  tourne, même mal, deux semaines après le Go.

## Règles permanentes

- Ne jamais remplir un livrable avec des chiffres inventés. Une case inconnue reste « à vérifier » avec le nom
  de la personne ou de la source qui peut y répondre. Un livrable plein de valeurs plausibles mais fausses est
  pire qu'un livrable troué : il passe la revue et échoue en production.
- Chaque document porte un destinataire nommé dans son en-tête, même si c'est l'utilisateur dans six mois.
- Passer une phase en taille S exige un motif d'une ligne dans l'état : « cette phase ne change aucune décision
  parce que ... ». Sauter une phase n'est pas une option.
- Les décisions prises en cours de route (choix écartés, majeurs acceptés, changements de périmètre) sont
  consignées dans la section Décisions de l'état, avec la date. C'est la matière des ADR et des revues.

## Requêtes courantes

- « Où en est le projet » : résumer l'état sans relire tout le playbook.
- « Saute la phase 2 » : refuser ; proposer la taille S avec motif.
- « Désactive la garde-code » : écrire `garde_code: off` dans l'état et une ligne datée dans le journal avec le
  motif donné par l'utilisateur. Rappeler que la garde se réactive en remettant `on`.
- « Challenge-moi » ou « relis ça » sur un livrable existant : invoquer `revue-de-phase` directement.
