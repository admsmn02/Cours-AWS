# Tests Python pour la fonction Lambda

Ce répertoire contient les tests pour la fonction Lambda AWS écrite en Python.

## Structure des tests

```
tests/
├── __init__.py
├── test_handler.py      # Tests pour la fonction handler principale
└── test_utilities.py    # Tests pour les fonctions utilitaires
```

## Tests implémentés

### test_handler.py

- **test_handler_returns_correct_status_code**: Vérifie que le handler retourne le code de statut 200
- **test_handler_returns_correct_headers**: Vérifie que les headers CORS sont correctement configurés
- **test_handler_returns_valid_json_body**: Vérifie que le body de la réponse est un JSON valide
- **test_handler_with_different_event_data**: Teste le handler avec différents types d'événements
- **test_handler_with_post_data**: Teste le handler avec des données POST

### test_utilities.py

- **test_json_serialization**: Teste la sérialisation/désérialisation JSON
- **test_cors_headers_structure**: Vérifie la structure des headers CORS
- **test_print_functionality**: Teste la fonction print avec des mocks
- **test_response_structure_validation**: Valide la structure de réponse Lambda
- **test_lambda_context_simulation**: Simule et teste le contexte Lambda

## Exécution des tests

### Localement

```bash
# Depuis la racine du projet
npm run test:python

# Ou directement avec pytest
cd amplify/backend/function/frontawsadam7a0543c5
python3 -m pytest tests/ -v
```

### Dans la pipeline

Les tests sont automatiquement exécutés lors du build backend dans AWS Amplify grâce à la configuration dans `amplify.yml`.

## Dépendances

- pytest
- pytest-cov (pour la couverture de code)
- pytest-mock (pour les mocks)

## Configuration

- `pytest.ini`: Configuration pytest
- `Pipfile`: Dépendances Python avec pipenv
