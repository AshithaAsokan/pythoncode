from django.test import TestCase

def concate_string(str1,str2):
    return str1+str2

class TestDemo(TestCase):
    def test_concate(self):
        self.assertEqual(concate_string('hello','how are you?'),'hellohow are you?')