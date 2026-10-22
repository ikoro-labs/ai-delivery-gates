# Frontière de confiance : [nom du projet]

Destinataire : ... | Date : ...

Principe : tout ce qui n'est pas écrit par l'équipe est une entrée non fiable, y compris les documents de
l'entreprise récupérés par un RAG, les pages web, les sorties des tools et les messages des utilisateurs.
Une entrée non fiable peut contenir des instructions ; le système ne doit jamais les exécuter comme si elles
venaient du code.

## Schéma
```mermaid
flowchart LR
    subgraph NF[Zone non fiable]
        U[Utilisateur]
        D[Documents récupérés]
        W[Web, APIs tierces]
        TO[Sorties des tools]
    end
    subgraph C[Points de contrôle]
        V1[Validation des entrées]
        V2[Isolation instructions / données]
        V3[Autorisation par tool]
        V4[Validation des sorties]
    end
    subgraph F[Zone de confiance]
        O[Orchestrateur]
        T[Tools à privilège minimal]
        S[(Données sensibles)]
    end
    U --> V1 --> O
    D --> V2 --> O
    W --> V2
    TO --> V2
    O --> V3 --> T
    T --> V4 --> U
    S -.accès contrôlé.-> T
```

## Inventaire
| Source d'entrée | Fiable ? | Peut contenir des instructions ? | Point de contrôle | Ce qui est fait en cas de contenu suspect |
|---|---|---|---|---|

| Tool | Privilèges (lecture, écriture, envoi, paiement) | Données accessibles | Confirmation humaine | Journalisé |
|---|---|---|---|---|

| Donnée sensible | Où elle vit | Qui y accède | Dans les prompts ? (non sauf nécessité écrite) | Dans les logs ? (non) |
|---|---|---|---|---|

## Checklist (inspirée de l'OWASP Top 10 for LLM Applications, vérifier la version en vigueur)
- [ ] Injection de prompt directe : entrées utilisateur validées, consignes système non modifiables par l'entrée.
- [ ] Injection indirecte : contenu récupéré isolé, jamais interprété comme instruction.
- [ ] Excès d'autonomie : chaque tool a le privilège minimal, les actions irréversibles exigent une confirmation.
- [ ] Fuite d'informations sensibles : PII et secrets hors prompts et hors logs sauf nécessité écrite.
- [ ] Chaîne d'approvisionnement : modèles, poids, datasets et dépendances avec provenance et licence vérifiées.
- [ ] Sorties : validées avant exécution (code, requêtes, liens) et avant affichage.
- [ ] Déni de service et coût : limites par session et par utilisateur.
- [ ] Journalisation : chaque action de tool est tracée avec l'identifiant de session.
