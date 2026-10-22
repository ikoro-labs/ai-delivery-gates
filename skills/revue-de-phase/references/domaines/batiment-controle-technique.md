# Domaine : bâtiment et contrôle technique de la construction (France)

Destinataire : agent expert-metier | Créé le : 2026-10-21 | Mis à jour le : 2026-10-21

Amorce à valider et compléter par un expert du domaine. Les lignes marquées « à vérifier » n'ont pas été contrôlées contre une
source officielle au moment de l'écriture : l'expert métier doit les vérifier (web, source datée) avant de s'en
servir en revue, ou les traiter comme non vérifiées.

## Vocabulaire et référentiels
| Terme | Définition opérationnelle | Pièges d'emploi |
|---|---|---|
| MOA (maître d'ouvrage) | Celui pour qui l'ouvrage est construit, il décide et paie | Ne pas confondre avec MOE |
| MOE (maître d'œuvre) | Conçoit et dirige l'exécution (architecte, BET) | |
| Contrôleur technique / bureau de contrôle | Donne des avis sur la solidité et la sécurité des ouvrages, indépendant de la MOE et des entreprises | Un avis n'est pas une réception ni une validation de conception |
| Mission de contrôle technique (L, S, PS, HAND, etc.) | Périmètres normalisés de contrôle (solidité, sécurité des personnes, parasismique, accessibilité) | Codes et périmètres : à vérifier (norme NF P 03-100, à confirmer) |
| RICT / RFCT | Rapport initial / rapport final de contrôle technique | À vérifier |
| Avis (favorable, défavorable, suspendu) | Position formelle du contrôleur sur un document ou un ouvrage | « Suspendu » n'est pas « défavorable » : il attend des pièces |
| Réserve | Défaut constaté à la réception, à lever par l'entreprise | Ne pas confondre avec un avis défavorable |
| OPR | Opérations préalables à la réception | |
| PV de réception, levée de réserves | Actes juridiques qui déclenchent garanties et paiements | |
| DOE, DIUO | Dossier des ouvrages exécutés, dossier d'intervention ultérieure sur l'ouvrage | |
| CCTP, DCE, lot | Cahier des clauses techniques particulières, dossier de consultation, découpage par corps d'état | Les données sont souvent organisées par lot |
| ERP, IGH | Établissement recevant du public, immeuble de grande hauteur : régimes de sécurité spécifiques | |
| DTU, Eurocodes, RE2020 | Règles de l'art, normes de calcul, réglementation environnementale | Vérifier la version applicable à la date du projet (RT2012 vs RE2020) |
| Diagnostics immobiliers (DPE, amiante, plomb, termites) | Documents réglementaires distincts du contrôle technique | Ne pas mélanger les régimes |

## Textes, normes et obligations qui s'imposent à un système IA dans ce domaine
| Texte ou norme | Ce qu'il impose | Source (URL) | Vérifié le |
|---|---|---|---|
| Code de la construction et de l'habitation (CCH) | Cadre du contrôle technique, cas où il est obligatoire, agrément des contrôleurs | Légifrance | à vérifier |
| Loi n° 78-12 du 4 janvier 1978 (loi Spinetta) | Responsabilité et assurance construction (garantie décennale), rôle du contrôleur technique | Légifrance | à vérifier |
| Agrément des contrôleurs techniques | Le contrôleur engage sa responsabilité : un avis produit par un système IA ne peut pas être émis sans validation par une personne habilitée | | à vérifier |
| Normes de mission (NF P 03-100 ou équivalent) | Périmètre des missions, contenu des rapports | AFNOR | à vérifier |
| RGPD | Données des occupants, des salariés sur chantier, photos avec personnes | CNIL | à vérifier |
| AI Act | Vérifier si un cas d'usage touche la sécurité des personnes ou des infrastructures critiques (possible haut risque) | EUR-Lex | à vérifier |

## Données du terrain
| Source | Où elle vit | Qualité réelle observée | Biais de collecte connus |
|---|---|---|---|
| Rapports et avis de contrôle | PDF, outils métier, GED | Rédaction humaine, styles variables, structure par lot pas toujours explicite | Dépend du rédacteur et de l'agence ; sous-déclaration possible ; vocabulaire interne |
| Plans, CCTP, DCE | PDF, DWG, BIM (IFC) | Extraction difficile (tableaux, plans) | Versions multiples, la dernière n'est pas toujours identifiée |
| Photos de chantier | Mobile, GED | Métadonnées incomplètes | Personnes visibles (RGPD) |
| Référentiels (nomenclatures de lots, codes d'avis) | Outils internes | Hétérogènes entre agences | |

## Cas limites fréquents et cas rares critiques
- Fréquents : réhabilitation vs neuf (règles différentes), avis suspendus en attente de pièces, modifications en cours de chantier, documents en plusieurs versions.
- Rares mais coûteux : ouvrages atypiques (structure, ERP de grande capacité), erreur sur un avis touchant la solidité ou la sécurité des personnes.

## Qui fait quoi
Le contrôleur technique (personne habilitée) émet et signe l'avis ; l'ingénieur ou le responsable d'affaire
prépare ; la MOA reçoit. Validation humaine obligatoire pour tout avis ou toute conclusion engageant la
responsabilité : un système IA assiste ou recommande, il n'émet pas (matrice 1.3 bis).

## Erreurs classiques des projets IA dans ce domaine
- Extraire des avis de PDF sans conserver la structure par lot et par document de référence.
- Confondre réserve, avis défavorable et avis suspendu dans les labels.
- Ignorer la version du référentiel applicable (RT2012 vs RE2020, version des DTU).
- Entraîner ou évaluer sur les rapports d'une seule agence et généraliser.
- Oublier les personnes visibles sur les photos de chantier.

## Questions que l'expert pose systématiquement
- Qui signe la sortie du système, et qu'est-ce qui l'engage ?
- Le golden set contient-il des cas de solidité et de sécurité des personnes en proportion suffisante ?
- Les données viennent-elles de plusieurs agences et de plusieurs rédacteurs ?
- Quel référentiel (date, version) s'applique aux ouvrages du jeu de données ?
