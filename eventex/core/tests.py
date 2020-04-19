from django.test import TestCase

class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get("/")


    def test_get_200(self):
        """GET / must return status code 200 """
        self.assertEqual(200, self.response.status_code)

    
    def test_should_use_template_index_html(self):
        """GET / must use template index.html """
        self.assertTemplateUsed(self.response, 'index.html')
