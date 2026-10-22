# Estimation de coûts : [nom du projet]

Destinataire : ... | Date : ... | Budget SLO mensuel (fiche §2) : ...

Chaque prix a une source et une date : les prix des fournisseurs de modèles changent souvent. Un prix sans
source est « non vérifié ». Les volumes viennent de la fiche de cadrage (utilisateurs, fréquence) ou du spike.

| Composant | Unité | Volume mensuel prévu (source) | Prix unitaire (source, date) | Coût mensuel | Variabilité (ce qui peut le doubler) |
|---|---|---|---|---|---|
| Inférence modèle principal | 1000 requêtes | | | | |
| Modèle de secours ou routage petit/gros | | | | | |
| Embeddings et index | | | | | |
| Stockage (raw, processed, curated) | | | | | |
| Compute training ou fine-tuning | | | | | |
| Tracing, monitoring | | | | | |
| Humain dans la boucle (annotation, validation) | heures | | | | |
| **Total** | | | | | |

Coût pour mille requêtes : ...
Total mensuel vs budget SLO : ... Marge : ... %

## Leviers si dépassement
Caching, modèle plus petit avec routage, limite de coût par session, réduction du périmètre (non-goals).
Un dépassement sans levier chiffré renvoie en phase 1 (budget) ou en phase 2 (périmètre).
