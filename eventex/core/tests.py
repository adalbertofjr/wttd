from django.test import TestCase

class TestHome(TestCase):
    def test_get_200(self):
        response = self.client.get("/")
        self.assertEqual(200, response.status_code)

    
    def test_should_use_template_index_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')
