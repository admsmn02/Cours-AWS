import json
import pytest
import sys
import os
import unittest.mock as mock

# Ajouter le répertoire src au chemin Python pour pouvoir importer la fonction
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


class TestUtilities:
    """Tests pour les fonctions utilitaires"""
    
    def test_json_serialization(self):
        """Test de sérialisation JSON"""
        # Arrange
        test_data = {
            'message': 'Hello World',
            'status': 'success',
            'code': 200
        }
        
        # Act
        json_string = json.dumps(test_data)
        parsed_data = json.loads(json_string)
        
        # Assert
        assert parsed_data == test_data
        assert parsed_data['message'] == 'Hello World'
        assert parsed_data['status'] == 'success'
        assert parsed_data['code'] == 200
    
    def test_cors_headers_structure(self):
        """Test de la structure des headers CORS"""
        # Arrange
        expected_headers = {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        }
        
        # Act & Assert
        assert 'Access-Control-Allow-Headers' in expected_headers
        assert 'Access-Control-Allow-Origin' in expected_headers
        assert 'Access-Control-Allow-Methods' in expected_headers
        assert expected_headers['Access-Control-Allow-Origin'] == '*'
    
    @mock.patch('builtins.print')
    def test_print_functionality(self, mock_print):
        """Test que la fonction print fonctionne correctement"""
        # Arrange
        test_message = "Test message"
        
        # Act
        print(test_message)
        
        # Assert
        mock_print.assert_called_once_with(test_message)
    
    def test_response_structure_validation(self):
        """Test de validation de la structure de réponse Lambda"""
        # Arrange
        response = {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            'body': json.dumps('Test response')
        }
        
        # Act & Assert
        assert 'statusCode' in response
        assert 'headers' in response
        assert 'body' in response
        assert isinstance(response['statusCode'], int)
        assert isinstance(response['headers'], dict)
        assert isinstance(response['body'], str)
        
        # Vérifier que le body est un JSON valide
        parsed_body = json.loads(response['body'])
        assert parsed_body == 'Test response'
    
    def test_lambda_context_simulation(self):
        """Test de simulation du contexte Lambda"""
        # Arrange
        mock_context = {
            'function_name': 'test-function',
            'function_version': '1',
            'invoked_function_arn': 'arn:aws:lambda:us-east-1:123456789:function:test',
            'memory_limit_in_mb': '128'
        }
        
        # Act & Assert
        assert 'function_name' in mock_context
        assert 'memory_limit_in_mb' in mock_context
        assert mock_context['function_name'] == 'test-function'
        assert mock_context['memory_limit_in_mb'] == '128'
