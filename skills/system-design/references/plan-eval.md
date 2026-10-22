# Plan d'évaluation : [nom du projet]

Destinataire : ... | Date : ...

Pourquoi ce document : sans jeu d'évaluation figé, chaque changement de prompt, de modèle ou de données est un
pari. Le golden set amorcé en phase 1 (eval-seed) devient ici un actif versionné.

## Golden set
| Rubrique | Valeur |
|---|---|
| Origine | eval-seed de la phase 1 + ... |
| Taille | N cas. Justification : régression minimale à détecter ..., donc N suffisant parce que ... |
| Couverture | par type de cas, par gravité, par source ; cas rares critiques sur-représentés volontairement |
| Annotation | qui, consigne, accord inter-annotateurs si plusieurs |
| Figé le | AAAA-MM-JJ, version v1, chemin, hash ou tag |
| Règle d'évolution | on ajoute, on ne modifie pas un cas existant sans nouvelle version ; jamais utilisé pour l'entraînement |

## Métriques
| Niveau | Métrique | Seuil bloquant en CI | Seuil d'alerte | Fréquence |
|---|---|---|---|---|
| Offline, modèle | | | | à chaque release |
| Offline, GenAI | pertinence, faithfulness, refus corrects, format | | | à chaque changement de prompt ou de modèle |
| Online, produit | métrique produit de la fiche §2 | sans objet | | hebdomadaire |

## Juge LLM (si utilisé)
- Consigne du juge versionnée.
- Calibration : taux d'accord avec des labels humains sur N cas, mesuré le ..., seuil minimal ...
- Biais connus du juge (longueur, position, auto-préférence) et parades.
- Le juge n'est jamais le même modèle que celui évalué sans justification écrite.

## Évaluations adverses (GenAI)
| Attaque | Cas de test | Comportement attendu | En CI |
|---|---|---|---|
| Injection directe | | | |
| Injection indirecte via contenu récupéré | | | |
| Exfiltration de données | | | |
| Appel de tool abusif | | | |
| Boucle d'agent | | | |

## Rejouabilité
Commande unique pour rejouer l'évaluation sur une version donnée du modèle et du golden set.
