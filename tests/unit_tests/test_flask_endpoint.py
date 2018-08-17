"""Test the flask endpoints with local data."""

import unittest
import json

import src.flask_endpoint as rest_api


class TestFlaskMethods(unittest.TestCase):
    """Test the flask endpoints with local data."""

    def setUp(self):
        """Create a api client."""
        rest_api.app.testing = True
        self.client = rest_api.app.test_client()
        assert len(rest_api.list_routes()) == 6

    def test_health_checks(self):
        """Test the liveness and readiness probes."""
        self.assertEqual(self.client.get('/api/v1/liveness').status, '200 OK')
        self.assertEqual(self.client.get(
            '/api/v1/readiness').status, '200 OK')

    def test_root_path(self):
        """Test the root path."""
        self.assertEqual(self.client.get('/').status, '200 OK')

    def test_model_details(self):
        """Test model details endpoint."""
        self.assertEqual(self.client.get(
            '/api/v1/model_details').status, '200 OK')

    def test_companion_recommendations(self):
        """Test companion recommendations endpoint."""
        data = [{"ecosystem": "maven",
                 "package_list": ["org.apache.commons:commons-lang3"]
                 }]
        self.assertEqual(self.client.post(
            '/api/v1/companion_recommendation',
            data=json.dumps(data),
            headers={'content-type': 'application/json'}).status, '200 OK')


if __name__ == '__main__':
    unittest.main()
