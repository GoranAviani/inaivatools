from django.test import TestCase

# Create your tests here.


# calling a test: ./manage.py test apirelay.tests

from apirelay.dataProcessing import check_country_code

class APIrelayTestCase(TestCase):

    def test_SE_country_code(self):
        result = check_country_code("SE")
        self.assertEqual(result, "existing_country")

    def test_YU_country_code(self):
        result = check_country_code("YU")
        self.assertEqual(result, "non_existing_country")