from django.test import TestCase

from transit.models import Company
from transit.models import UserProfile
from django.contrib.auth.models import User


from django.conf import settings
# Create your tests here.

class CompanyTestCase(TestCase):
    def test_name_locale(self):

        company = Company.objects.create(name='The blue sea', name_km='សមុទ្រខៀវ', name_zh_hans='蓝色的大海')
        company.save()

        json_i18n = {'name_km': 'សមុទ្រខៀវ', 'name_zh_hans': '蓝色的大海'}
        self.assertEqual(settings.LANGUAGE_CODE, 'en')
        self.assertEqual(company.i18n, json_i18n)
        
        self.assertEqual(company.name, 'The blue sea')
        self.assertEqual(company.name_en, 'The blue sea')

        self.assertEqual(company.name_km, 'សមុទ្រខៀវ')
        self.assertEqual(company.name_zh_hans, '蓝色的大海')
        self.assertEqual(company.name_vi, None)


class UserTestCase(TestCase):
    def test_create_user_profile_when_create_user(self):
        user = User.objects.create(username='joeann', password='cienfuegos')
        self.assertEqual(user.username, 'joeann')
        self.assertIsNotNone(user.id)
        self.assertEqual(user.user_profile.profile_pic.url, '/uploads/default-pic.png')
        

