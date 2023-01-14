from django.test import TestCase
from models import *
# Create your tests here.
#TestCase class
class MenuTest(TestCase):
    def test_get_item(self):
        item = menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")