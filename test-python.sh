#!/bin/bash

# Script pour exécuter les tests Python de la fonction Lambda
echo "🐍 Exécution des tests Python pour la fonction Lambda..."

# Aller dans le répertoire de la fonction
cd amplify/backend/function/frontawsadam7a0543c5

# Vérifier si Python 3.13 est disponible
if command -v python3.13 &> /dev/null; then
    PYTHON_CMD="python3.13"
elif command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
else
    echo "❌ Python 3 n'est pas installé"
    exit 1
fi

echo "📦 Installation des dépendances de test..."
$PYTHON_CMD -m pip install pytest pytest-cov pytest-mock

echo "🧪 Exécution des tests..."
$PYTHON_CMD -m pytest tests/ -v --tb=short

# Retourner au répertoire racine
cd ../../../..

echo "✅ Tests Python terminés"
