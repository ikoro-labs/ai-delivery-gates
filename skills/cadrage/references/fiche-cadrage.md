# Fiche de cadrage : [nom du projet]

Phase 1 du playbook, points 1.0 à 1.9. **Une page. Quarante-cinq minutes en profil perso.**
Date : ... | Profil : spike / perso / production / plateforme | Domaine : ...

**Destinataire** : ... | **Sponsor** : ... | **Décideur go/no-go** : ... | **Owner prod** : ...
(En perso : destinataire = moi dans six mois, les trois autres « sans objet ».)

---

## 1. Problème (1.1 à 1.3)

**Qui souffre, de quoi, à quelle fréquence, à quel coût (temps, argent, frustration)** : ...

**Pourquoi l'IA plutôt qu'une règle métier, du SQL ou une heuristique** : ... (ce qui a été essayé ou écarté, avec son résultat)
**Pourquoi pas l'existant** : outil déjà en place, solution du marché, changement de process. Ce qu'on a regardé et pourquoi ça ne suffit pas.
Si la réponse tient en une heuristique ou un outil existant, le faire, et s'arrêter là.

**Utilisateur cible et cas d'usage unique du MVP** : ...
**Où ça s'insère** : dans quel workflow, à quel moment, ce que l'utilisateur arrête de faire, comment on mesure l'usage réel.

**Coût d'erreur et niveau d'autonomie (1.3 bis)** : erreur la plus grave : ... | niveau : assiste / recommande / agit sous supervision / autonome. Détail dans `matrice-cout-erreur.md`.

**(Profil perso) Ce que ce projet doit prouver de moi en entretien** : ...

---

## 2. Métriques et SLO (1.4 et 1.5)

**La différence.** Une métrique décrit, un SLO engage. Une métrique se lit, on la commente à la revue mensuelle. Un SLO a un seuil et une conséquence automatique quand il est franchi : alerte, blocage de release, rollback, coupure de fonctionnalité. Un seuil sans conséquence écrite est une métrique déguisée en engagement.

Chaque ligne a une valeur cible **et** une méthode de mesure. Une métrique sans méthode de mesure est une intention.

| Nature | Catégorie | Nom | Cible ou seuil | Comment je la mesure | Conséquence si franchi | Aujourd'hui |
|---|---|---|---|---|---|---|
| Métrique | Produit | ex. taux de clic sur les items recommandés | ... | ... | sans objet | ... |
| Métrique | Produit | ex. part de sessions avec au moins une interaction | ... | ... | sans objet | ... |
| Métrique | Modèle | ex. recall@50, NDCG@10 | ... | jeu d'évaluation figé, daté (eval-seed) | sans objet | ... |
| **SLO** | Modèle | perf minimale sur golden set | ... | en CI, à chaque release | release bloquée | ... |
| **SLO** | Système | latence p95 de bout en bout | ... | mesurée sous charge, pas en local | alerte + fallback | ... |
| **SLO** | Système | disponibilité | ... | ... | alerte, post-mortem sous 48h | ... |
| Métrique | Coût | coût pour mille requêtes | ... | ... | sans objet | ... |
| **SLO** | Coût | budget mensuel maximum | ... | suivi quotidien | alerte à 80%, coupure à 100% | ... |

Règle : trois à cinq SLO maximum. Au-delà, aucun n'est respecté et plus personne ne regarde les alertes. Tout le reste est une métrique.

**Baseline de référence** : contre quoi le gain sera jugé (règle simple, popularité, modèle existant, ce que fait l'utilisateur aujourd'hui).

---

## 3. Risques (1.6)

En profil perso : trois lignes maximum. En profil production : registre complet dans `registre-risques.md`, les trois premiers ici.

| Risque | Probabilité | Impact | Mitigation | Signal d'alerte |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

Catégories à balayer : privacy et données personnelles, biais, coût qui dérape, dépendance à un tiers, réglementaire.
**Checkpoint réglementaire** : rempli dans `checkpoint-reglementaire.md` le AAAA-MM-JJ / sans objet parce que ...

---

## 4. Faisabilité data (1.7)

**Point de mort réel des projets perso.** Cette section ne se remplit pas de mémoire.

- Source exacte et mode d'accès : ...
- Volume et profondeur d'historique : ...
- Fraîcheur et fréquence de mise à jour : ...
- Qualité observée : manquants, doublons, biais de collecte, fuites potentielles : ...
- Droits d'usage et licence : ...
- **Preuve d'accès** : échantillon réel extrait le [date], chemin ou lien : ...
- **Jeu d'éval amorcé** : N cas réels annotés le [date], chemin : `eval-seed/`, annotés par ..., avec quelle consigne.

Sans échantillon réel extrait, la case n'est pas cochée et le projet ne démarre pas. Sans cas annotés, les métriques modèle de la section 2 sont des intentions.

---

## 5. Go / No-Go (1.8)

Décision : **GO / NO-GO**, le [date], par [décideur].
Motif en deux lignes : ...
Ce que je ne sais pas encore et que j'accepte de découvrir en route : ...

---

## 6. Critères d'arrêt (1.9)

Écrits maintenant, avant tout attachement au projet. Falsifiables et datés.

| Date de vérification | Condition de poursuite (chiffrée) | Décision si non atteinte |
|---|---|---|
| ... | ... | pivot / arrêt |
| ... | ... | pivot / arrêt |

Formulations interdites : « si ça ne marche pas », « si les retours sont mauvais », « si je n'ai plus le temps ».
Une condition de poursuite se vérifie avec un chiffre observable par quelqu'un d'autre que moi.

---

## Contrôle final avant de passer en phase 2

- [ ] Un échantillon réel de données a été extrait
- [ ] 20 à 50 cas réels annotés existent dans `eval-seed/`
- [ ] Chaque métrique a une méthode de mesure
- [ ] Une baseline de référence est nommée
- [ ] Le coût d'erreur et le niveau d'autonomie sont écrits et cohérents avec les SLO
- [ ] Le checkpoint réglementaire est rempli ou « sans objet » motivé
- [ ] Les critères d'arrêt sont datés et chiffrés
- [ ] Destinataire, sponsor et décideur sont nommés
- [ ] Cette fiche tient sur une page
