# Template de user story

À utiliser en phase 2.1 du playbook. Maximum 8 stories pour un MVP.

---

## Template

**US-XX : [titre court, un verbe et un objet]**

> En tant que **[rôle précis, pas "utilisateur"]**
> je veux **[capacité observable]**
> afin de **[bénéfice, le pourquoi]**

**Critères d'acceptation**

- Étant donné [contexte de départ], quand [action], alors [résultat observable]
- Étant donné [cas limite], quand [action], alors [comportement attendu]
- Étant donné [cas d'erreur], quand [action], alors [message ou fallback]

**Hors périmètre de cette story** : [ce qu'on ne fait pas ici, pour éviter le glissement]

**Notes** : dépendances, question ouverte, décision renvoyée en ADR.

---

## Exemple rempli (chaîne reco et RAG)

**US-03 : Voir des produits similaires sur une fiche produit**

> En tant que **visiteur consultant une fiche produit**
> je veux **voir une liste de produits proches de celui que je regarde**
> afin de **trouver une meilleure option sans relancer une recherche**

**Critères d'acceptation**

- Étant donné une fiche produit valide, quand la page se charge, alors 10 recommandations s'affichent en moins de 200 ms au p95
- Étant donné un produit sans historique d'interactions, quand la page se charge, alors le fallback catalogue s'applique et la liste n'est jamais vide
- Étant donné une panne du service de ranking, quand la page se charge, alors les résultats de retrieval bruts sont servis et l'incident est tracé
- Étant donné une liste servie, quand un clic a lieu, alors l'événement est enregistré avec l'identifiant de version du modèle

**Hors périmètre** : personnalisation par utilisateur connecté, tests A/B, réordonnancement temps réel.

---

## Les 6 tests d'une bonne story (INVEST)

| Critère | Question |
|---|---|
| Indépendante | Peut-elle être livrée sans attendre une autre story ? |
| Négociable | Décrit-elle un besoin, pas une implémentation imposée ? |
| Valeur | Quelqu'un remarquerait-il sa livraison ? |
| Estimable | Sait-on à peu près combien de travail elle représente ? |
| Small | Tient-elle dans un seul cycle de livraison ? |
| Testable | Peut-on écrire un test qui échoue avant et passe après ? |

---

## Ce qui n'est pas une user story

- Une décision d'architecture ("je veux une base vectorielle") → ADR, phase 3.3
- Une exigence non fonctionnelle transverse (latence globale, sécurité, budget) → NFR, phase 2.5
- Une tâche technique sans bénéficiaire ("mettre en place la CI") → tâche du backlog
- Un epic déguisé ("je veux un moteur de recommandation") → à découper

---

## Cas des projets sans utilisateur final

**Plateforme ou librairie** : le rôle devient le développeur intégrateur.

> En tant que **développeur intégrant le moteur de capabilities**
> je veux **déclarer une capability retrieval en moins de dix lignes**
> afin de **brancher un nouveau backend sans modifier le cœur**

Les critères d'acceptation portent alors sur le contrat public, les messages d'erreur, et la compatibilité ascendante.

**Projet perso ou portfolio** : garder le format, ajouter une ligne "ce que cette story prouve en entretien". Une story qui ne sert ni un utilisateur ni une preuve n'a pas de raison d'être dans le MVP.
