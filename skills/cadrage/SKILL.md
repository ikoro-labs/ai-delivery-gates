---
name: cadrage
description: >
  Phase 1 du playbook projet IA : fiche de cadrage sur une page, one-pager pour le destinataire, registre de
  risques, checkpoint réglementaire, faisabilité data avec échantillon réel, go/no-go et critères d'arrêt.
  Utiliser quand l'utilisateur cadre un projet IA, ML ou GenAI, parle de problème à résoudre, de métriques,
  de SLO, de faisabilité data, de go/no-go, de « pourquoi l'IA », de risques, de budget, de « scoping »,
  de « problem statement », ou quand l'orchestrateur projet-ia lance la phase 1.
metadata:
  version: "0.1.0"
---

# Phase 1 : cadrage

## Pourquoi cette phase existe

Valider que le problème mérite d'être résolu et que l'IA est la bonne approche. Tout ce qui suit (spec, design,
données, modèle) dépend des chiffres fixés ici : métriques, SLO, budget, critères d'arrêt. Un cadrage mou
produit un projet qui ne peut ni réussir ni s'arrêter.

## Méthode

Remplir la fiche par entretien, section par section, dans l'ordre ci-dessous. Poser les questions du template,
noter les réponses, refuser ce qui n'est pas chiffré ou pas vérifiable. Ne jamais compléter une case avec une
valeur plausible : écrire « à vérifier : <qui ou quelle source> ». Quand une réponse tient en une heuristique
(1.2), le dire et proposer d'arrêter là : c'est un succès du cadrage, pas un échec.

Taille : lire la taille de la phase dans l'état. En S ou M (profil perso), appliquer la variante perso de
`profils-tailles.md` (orchestrateur) : trois lignes pour 1.1 à 1.3, trois risques maximum, décision solo.

## Entretien, dans l'ordre

| Étape | Question centrale | Référence |
|---|---|---|
| 1.0 Parties prenantes | Qui lit, qui sponsorise, qui tranche le go/no-go, qui portera en prod | en-tête de `references/fiche-cadrage.md` |
| 1.1 Problème | Qui souffre, de quoi, à quelle fréquence, à quel coût | fiche §1 |
| 1.2 Pourquoi l'IA | Quelle règle, quel SQL, quelle heuristique a été essayée ou écartée, avec quel résultat ; quel outil existant, quel achat, quel changement de process ferait le travail | fiche §1 |
| 1.3 Utilisateur et cas d'usage | Persona nommé, cas d'usage unique du MVP, où le système s'insère dans le workflow, ce que l'utilisateur arrête de faire, comment on mesure l'usage réel | fiche §1 |
| 1.3 bis Coût d'erreur et autonomie | Que coûte chaque type d'erreur, qui le subit, niveau d'autonomie choisi | `references/matrice-cout-erreur.md` |
| 1.4 Métriques | Produit et modèle, cible, méthode de mesure, baseline de référence | fiche §2 |
| 1.5 SLO | Trois à cinq, avec seuil, mesure hors poste local et conséquence automatique | fiche §2 |
| 1.6 Risques | Registre, puis checkpoint réglementaire | `references/registre-risques.md`, `references/checkpoint-reglementaire.md` |
| 1.7 Faisabilité data | Source, accès, volume, fraîcheur, qualité, droits, échantillon réel extrait, jeu d'éval amorcé | fiche §4 |
| 1.8 Go/No-Go | Décision datée, motif en deux lignes, inconnues acceptées | fiche §5 |
| 1.9 Critères d'arrêt | Dates, conditions chiffrées observables par un tiers, décision | fiche §6 |

Pourquoi cet ordre : le coût d'erreur (1.3 bis) conditionne les SLO (1.5), les risques (1.6) et les garde-fous
du design ; le jeu d'éval amorcé (1.7) rend les métriques modèle (1.4) mesurables au lieu de déclaratives.

## Règles de rédaction

- Une métrique a une méthode de mesure, sinon c'est une intention. Un SLO a un seuil et une conséquence
  automatique, sinon c'est une métrique déguisée.
- Trois à cinq SLO maximum. Au-delà, personne ne regarde les alertes.
- Formulations interdites pour les critères d'arrêt : « si ça ne marche pas », « si les retours sont mauvais »,
  « si je n'ai plus le temps ». Une condition de poursuite se vérifie avec un chiffre qu'un tiers peut observer.
- La fiche tient sur une page. Les détails (registre complet, checkpoint, matrice) vivent dans leurs fichiers.
- Le one-pager est écrit pour le destinataire nommé, sans jargon, sans solution dans la section Problème.

## Livrables (dossier `docs/projet/01-cadrage/`)

| Fichier | Depuis | Taille |
|---|---|---|
| `fiche-cadrage.md` | `references/fiche-cadrage.md` | M et L |
| `one-pager.md` | `references/one-pager.md` | M et L (en S, remplace la fiche) |
| `registre-risques.md` | `references/registre-risques.md` | L (en perso, trois lignes dans la fiche) |
| `checkpoint-reglementaire.md` | `references/checkpoint-reglementaire.md` | L, et dès que des données personnelles réelles sont traitées |
| `matrice-cout-erreur.md` | `references/matrice-cout-erreur.md` | M et L |
| `eval-seed/README.md` | liste des 20 à 50 cas annotés, origine, chemin, date | toutes tailles |

## Critères de sortie

- Un échantillon réel de données a été extrait : chemin vérifiable, date, volume.
- 20 à 50 cas réels annotés existent (le jeu d'éval amorcé), même grossièrement.
- Chaque métrique a une méthode de mesure ; chaque SLO a seuil, mesure et conséquence.
- Une baseline de référence est nommée.
- Le checkpoint réglementaire est rempli ou explicitement « sans objet » avec motif.
- Les critères d'arrêt sont datés et chiffrés.
- La décision go/no-go est écrite, datée, avec ses inconnues acceptées.
- La fiche tient sur une page.

## Ensuite

Signaler à l'orchestrateur que les critères de sortie sont remplis. La revue de phase 1 inclut le pré-mortem.
La phase 1 close est ce qui lève le hook garde-code.
