from django.test import TestCase

# Create your tests here.

from .cleaningTelNum import remove_first_space_from_tel


class CleaningTelNumber(TestCase):
    
    def test_remove_first_space_from_tel(self):
        result = remove_first_space_from_tel(" 073123123")
        self.assertEqual(result, ("073123123"))

    def test_remove_first_space_from_tel(self):
        result = remove_first_space_from_tel("  073123123")
        self.assertEqual(result, ("073123123"))

    def test_remove_first_space_from_tel(self):
        result = remove_first_space_from_tel("  073 123 123")
        self.assertEqual(result, ("073123123"))