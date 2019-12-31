from django.test import TestCase

# Create your tests here.

from .cleaningTelNum import remove_spaces_from_tel, remove_plus_from_tel, remove_country_code, place_zero_at_first


class RemoveSpacesFromTel(TestCase):
    
    def test_remove_spaces_from_tel_one_space_at_start(self):
        result = remove_spaces_from_tel(" 073123123")
        self.assertEqual(result, ("073123123"))

    def test_remove_spaces_from_tel_two_spaces_at_start(self):
        result = remove_spaces_from_tel("  073123123")
        self.assertEqual(result, ("073123123a"))

    def test_remove_spaces_from_tel_more_spaces(self):
        result = remove_spaces_from_tel("  073 123 123")
        self.assertEqual(result, ("073123123"))

class RemovePlusFromTel(TestCase):

    def test_remove_first_plus(self):
        result = remove_plus_from_tel("+073123123")
        self.assertEqual(result, ("073123123"))

class RemoveCountryCodeSE(TestCase):

    def test_remove_country_code_se_46(self):
        result = remove_country_code("4673123123", "SE")
        self.assertEqual(result, ("73123123"))

    def test_remove_country_code_se_046(self):
        result = remove_country_code("04673123123", "SE")
        self.assertEqual(result, ("73123123"))

    def test_remove_country_code_se_0046(self):
        result = remove_country_code("004673123123", "SE")
        self.assertEqual(result, ("73123123"))

    def test_remove_country_code_se_346(self):
        result = remove_country_code("34673123123", "SE")
        self.assertEqual(result, ("73123123"))

    def test_remove_country_code_se_00(self):
        result = remove_country_code("0073123123", "SE")
        self.assertEqual(result, ("73123123"))


class RemoveCountryCodeFI(TestCase):

    def test_remove_country_code_fi_58(self):
        result = remove_country_code("5873123123", "FI")
        self.assertEqual(result, ("73123123"))

    def test_remove_country_code_fi_058(self):
        result = remove_country_code("05873123123", "FI")
        self.assertEqual(result, ("73123123"))

    def test_remove_country_code_fi_0058(self):
        result = remove_country_code("005873123123", "FI")
        self.assertEqual(result, ("73123123"))

    def test_remove_country_code_fi_358(self):
        result = remove_country_code("35873123123", "FI")
        self.assertEqual(result, ("73123123"))

    def test_remove_country_code_fi_00(self):
        result = remove_country_code("0073123123", "FI")
        self.assertEqual(result, ("73123123"))


class PlaceZeroAtFirst(TestCase):

    def test_place_zero(self):
            result = place_zero_at_first("73123123")
            self.assertEqual(result, ("073123123"))

    def test_dont_place_zero(self):
            result = place_zero_at_first("073123123")
            self.assertEqual(result, ("073123123"))
