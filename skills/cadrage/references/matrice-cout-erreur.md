# Matrice coût d'erreur et niveau d'autonomie : [nom du projet]

Destinataire : ... | Date : ...

Pourquoi ce document : les SLO (1.5), les risques (1.6), les garde-fous (3.7) et la frontière de confiance (3.11)
dépendent de ce que coûte une erreur et de qui la subit. Un système qui « agit » là où une erreur est grave,
sans contrôle humain, est un bloquant de revue.

## 1. Types d'erreur

| Type d'erreur | Exemple concret dans ce projet | Qui la subit | Coût unitaire (temps, argent, juridique, confiance) | Fréquence tolérable | Comment on la détecte | Comment on la répare |
|---|---|---|---|---|---|---|
| Faux positif (le système signale à tort) | | | | | | |
| Faux négatif (le système rate) | | | | | | |
| Sortie plausible mais fausse (hallucination, extraction erronée) | | | | | | |
| Refus ou absence de réponse à tort | | | | | | |
| Indisponibilité ou latence excessive | | | | | | |
| Action non voulue (agent, écriture, envoi) | | | | | | |

**Erreur la plus grave** : ... Coût : ... C'est elle qui fixe le niveau d'autonomie.

## 2. Niveau d'autonomie du MVP

| Niveau | Définition | Choisi |
|---|---|---|
| Assiste | Le système fournit une information, l'humain décide et agit | |
| Recommande | Le système propose une décision, l'humain valide avant tout effet | |
| Agit sous supervision | Le système agit, l'humain contrôle a posteriori avec possibilité d'annuler | |
| Autonome | Le système agit sans contrôle humain systématique | |

Justification du niveau choisi au regard de l'erreur la plus grave : ...
Conditions pour monter d'un niveau plus tard (chiffrées) : ...

## 3. Conséquences à reporter

- SLO (1.5) : quelle erreur mérite un SLO avec conséquence automatique.
- Risques (1.6) : l'erreur la plus grave devient un risque avec signal d'alerte.
- Spécifications (2.1) : chaque story a un critère d'acceptation sur le cas d'erreur correspondant.
- Design (3.7, 3.11) : garde-fous et points de contrôle humain là où le niveau d'autonomie l'exige.
