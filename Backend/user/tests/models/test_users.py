from django.test import TestCase
from Backend.user.models.profiles import Photographer
from django.contrib.auth.models import User

class PhotographerModelTest(TestCase):
    def setUp(self):        
        self.user = User.objects.create_user(username='photographeruser', password='testpassword')
    
    def test_photographer_creation(self):
        photographer = Photographer.objects.create(
            user=self.user,
            type_user='Photographer',
            name_photographer='John Doe',
            name_company='Doe Photography',
            phone='1234567890'
        )
        
        self.assertEqual(photographer.name_photographer, 'John Doe')
        self.assertEqual(photographer.name_company, 'Doe Photography')
        self.assertEqual(photographer.phone, '1234567890')
        self.assertEqual(photographer.user.username, 'photographeruser')
        self.assertEqual(photographer.type_user, 'Photographer')

    def test_photographer_str(self):
        photographer = Photographer.objects.create(
            user=self.user,
            type_user='Photographer',
            name_photographer='John Doe',
            name_company='Doe Photography',
            phone='1234567890'
        )
        
        self.assertEqual(str(photographer), 'photographeruser - Photographer')

    def test_photographer_user_relation(self):
       
        photographer = Photographer.objects.create(
            user=self.user,
            type_user='Photographer',
            name_photographer='John Doe',
            name_company='Doe Photography',
            phone='1234567890'
        )
        
        self.assertEqual(photographer.user, self.user)