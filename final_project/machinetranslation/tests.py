import unittest
from translator import englishtofrench, frenchtoenglish

class TestEnglishtofrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishtofrench('Hello'),'Bonjour') 
            # test when Hello is given as input the translation is Bonjour
        self.assertEqual(englishtofrench(None),"Nothing to translate / Rien à traduire") 
            # test when input is null. Must return the message nothing to translate
        self.assertEqual(englishtofrench(''),"Nothing to translate / Rien à traduire") 
            # test when input is empty. Must return the message nothing to translate
        self.assertNotEqual(englishtofrench('Hello'),'Hello')
            # test when sending English text is given as input the translation is NOT returning English

class Testfrenchtoenglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchtoenglish('Bonjour'), 'Hello') 
            # test when Bonjour is given as input the translation is Hello.
        self.assertEqual(frenchtoenglish(None),"Nothing to translate / Rien à traduire") 
            # test when input is null. Must return the message nothing to translate
        self.assertEqual(frenchtoenglish(''),"Nothing to translate / Rien à traduire") 
            # test when input is empty. Must return the message nothing to translate
        self.assertNotEqual(englishtofrench('Bonjour'),'Bonjour')
            # test when sending French text is given as input the translation is NOT returning French

unittest.main()
