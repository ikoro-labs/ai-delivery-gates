# Spécification API : [nom du projet]

Destinataire : ... | Date : ... | Version de l'API : v1

## Principes
- Contrat d'abord : le schéma (pydantic ou OpenAPI) est la source de vérité, le code le suit.
- Toute écriture est idempotente ou porte une clé d'idempotence.
- Toute réponse ML porte l'identifiant de version du modèle et un identifiant de requête pour le tracing.
- Un timeout et un fallback sont définis pour chaque endpoint qui appelle un modèle.

## Endpoints
| Méthode | Chemin | Rôle | Auth | Entrée (schéma) | Sortie (schéma) | Timeout | Fallback |
|---|---|---|---|---|---|---|---|

## Schémas
```python
from pydantic import BaseModel, Field

class ExempleRequete(BaseModel):
    texte: str = Field(min_length=1, max_length=5000)

class ExempleReponse(BaseModel):
    resultat: str
    version_modele: str
    id_requete: str
```

## Modèle d'erreur
| Code HTTP | Code applicatif | Quand | Corps | Action attendue du client |
|---|---|---|---|---|
| 400 | | entrée invalide | | corriger |
| 401 / 403 | | auth | | |
| 422 | | contrainte métier | | |
| 429 | | quota ou budget atteint | | réessayer après |
| 503 | | modèle indisponible, fallback appliqué ou non | | |

## Versionnement et dépréciation
Politique (préfixe de chemin, en-tête), durée de support d'une version, procédure de dépréciation.
Profil plateforme : compatibilité ascendante garantie sur ..., changements cassants uniquement en version majeure.

## Limites
Débit par client, taille maximale des entrées, coût maximal par requête ou par session.
