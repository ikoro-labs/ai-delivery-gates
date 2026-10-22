# Profils et tailles (phases 0 à 3)

Choisir le profil au démarrage, puis la taille de chaque phase. Écrire les deux dans `docs/projet/etat.md`.

## Profils

| Profil | Description | Phases actives dans ce plugin |
|---|---|---|
| Spike | Lever une incertitude technique en quelques jours | 0 uniquement |
| Projet perso / portfolio | Système étroit, utilisateurs réels ou réalistes, sert de preuve | 0 à 3 en S/M |
| Système de production | Utilisateurs réels, engagement de service, équipe | 0 à 3 en L |
| Plateforme / librairie | Le consommateur est un développeur, pas un utilisateur final | 0 à 3 avec substitutions |

## Tailles

- **S** : quelques lignes dans un seul fichier.
- **M** : un document par phase.
- **L** : le livrable complet tel que décrit dans le playbook.

Tailles par défaut :

| Profil | Phase 0 | Phase 1 | Phase 2 | Phase 3 |
|---|---|---|---|---|
| Perso | S (note de 10 lignes) | M (fiche une page) | S | S |
| Production | S (note de 10 lignes) | L | L | L |
| Plateforme | S | L | L avec substitutions | L |

La profondeur va dans le système, pas dans la documentation qui le décrit. Passer une phase en S par rapport au
défaut exige un motif écrit dans l'état : « cette phase ne change aucune décision parce que ... ».

## Substitutions pour le profil Plateforme / librairie

| À remplacer | Par |
|---|---|
| 1.3 Persona + user journey | Consommateurs de l'API : qui appelle, depuis quel contexte, avec quelles contraintes |
| 2.1 User stories | Cas d'usage d'intégration, du « hello world » au cas avancé |
| 2.3 Spéc API | Contrats publics, politique de versionnement, compatibilité ascendante, dépréciation |

Les substitutions 6.6 et 10.1 du playbook concernent des phases hors périmètre.

## Variante profil perso en phase 1

| # | En profil perso |
|---|---|
| 1.1 à 1.3 | Trois lignes. Si on ne sait pas dire qui utiliserait ça, on construit une démo, pas un système |
| 1.4 | Ajouter une ligne : quelle question d'entretien ce projet répond |
| 1.5 | SLO auto-imposés mais réels (p95, coût pour mille requêtes), mesurés, pas déclarés |
| 1.6 | Trois risques maximum. Pas de volet réglementaire |
| 1.7 | Point de mort réel des projets perso : jeu de données réel identifié avant d'écrire une ligne |
| 1.8 | Décision solo, deux lignes |
| 1.9 | Garde tout son sens : un projet perso sans condition d'arrêt devient un zombie |

Ce qui saute en perso : registre de risques complet, volet réglementaire, validation par des parties prenantes.
Le checkpoint réglementaire reste obligatoire dès que des données personnelles réelles sont traitées, même en perso.
