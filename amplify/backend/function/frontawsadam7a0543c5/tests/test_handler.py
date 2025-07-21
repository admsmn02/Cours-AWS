import json
import pytest
import sys
import os

# Ajouter le répertoire src au chemin Python pour pouvoir importer la fonction
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from index import handler


class TestLambdaHandler:
    """Tests pour la fonction Lambda handler"""
    
    def test_handler_returns_correct_status_code(self):
        """Test que le handler retourne le bon code de statut"""
        # Arrange
        event = {}
        context = {}
        
        # Act
        response = handler(event, context)
        
        # Assert
        assert response['statusCode'] == 200
        assert 'headers' in response
        assert 'body' in response
    
    def test_handler_returns_correct_headers(self):
        """Test que le handler retourne les bons headers CORS"""
        # Arrange
        event = {}
        context = {}
        
        # Act
        response = handler(event, context)
        
        # Assert
        headers = response['headers']
        assert headers['Access-Control-Allow-Headers'] == '*'
        assert headers['Access-Control-Allow-Origin'] == '*'
        assert headers['Access-Control-Allow-Methods'] == 'OPTIONS,POST,GET'
    
    def test_handler_returns_valid_json_body(self):
        """Test que le handler retourne un body JSON valide"""
        # Arrange
        event = {}
        context = {}
        
        # Act
        response = handler(event, context)
        
        # Assert
        body = response['body']
        # Vérifier que c'est un JSON valide
        parsed_body = json.loads(body)
        assert parsed_body == 'Hello from your new Amplify Python lambda!'
    
    def test_handler_with_different_event_data(self):
        """Test que le handler fonctionne avec différents types d'événements"""
        # Arrange
        event = {
            'httpMethod': 'GET',
            'path': '/test',
            'queryStringParameters': {'param1': 'value1'}
        }
        context = {}
        
        # Act
        response = handler(event, context)
        
        # Assert
        assert response['statusCode'] == 200
        assert 'body' in response
        body = json.loads(response['body'])
        assert body == 'Hello from your new Amplify Python lambda!'
    
    def test_handler_with_post_data(self):
        """Test que le handler fonctionne avec des données POST"""
        # Arrange
        event = {
            'httpMethod': 'POST',
            'body': json.dumps({'test': 'data'}),
            'headers': {'Content-Type': 'application/json'}
        }
        context = {}
        
        # Act
        response = handler(event, context)
        
        # Assert
        assert response['statusCode'] == 200
        headers = response['headers']
        assert 'Access-Control-Allow-Origin' in headers
        body = json.loads(response['body'])
        assert body == 'Hello from your new Amplify Python lambda!'
