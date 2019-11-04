from django.test import TestCase

# Create your tests here.

from .cleaningTelNum import remove_spaces_from_tel, remove_plus_from_tel


class RemoveSpacesFromTel(TestCase):
    
    def test_remove_spaces_from_tel_one_space_at_start(self):
        result = remove_spaces_from_tel(" 073123123")
        self.assertEqual(result, ("073123123"))

    def test_remove_spaces_from_tel_two_spaces_at_start(self):
        result = remove_spaces_from_tel("  073123123")
        self.assertEqual(result, ("073123123"))

    def test_remove_spaces_from_tel_more_spaces(self):
        result = remove_spaces_from_tel("  073 123 123")
        self.assertEqual(result, ("073123123"))

class RemovePlusFromTel(TestCase):

    def test_remove_first_plus(self):
        result = remove_plus_from_tel("+073123123")
        self.assertEqual(result, ("073123123"))
