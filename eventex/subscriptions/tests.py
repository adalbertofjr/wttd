from django.test import TestCase


class SubscribeTest(TestCase):
    def test_get(self):
        """Get /inscricao/ must return status code 200"""
        resp = self.client.get('/inscricao/')
        self.assertEqual(200, resp.status_code)