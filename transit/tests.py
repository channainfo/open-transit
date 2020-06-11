from django.test import TestCase

from transit.models import Company
from django.conf import settings
# Create your tests here.

class CompanyTestCase(TestCase):
    def test_name_locale(self):

        company = Company.objects.create(name='The blue sea', name_kh='សមុទ្រខៀវ', name_zh='蓝色的大海')
        company.save()

        json_i18n = {'name_kh': 'សមុទ្រខៀវ', 'name_zh': '蓝色的大海'}
        self.assertEqual(settings.LANGUAGE_CODE, 'en')
        self.assertEqual(company.i18n, json_i18n)
        
        self.assertEqual(company.name, 'The blue sea')
        self.assertEqual(company.name_en, 'The blue sea')

        self.assertEqual(company.name_kh, 'សមុទ្រខៀវ')
        self.assertEqual(company.name_zh, '蓝色的大海')
        self.assertEqual(company.name_fr, None)
