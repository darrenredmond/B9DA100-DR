# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 19:42:39 2018

@author: 99993
"""

import unittest
from spellcheck import SpellChecker
class TestSpellChecker(unittest.TestCase):

    def setUp(self):
        self.spellChecker = SpellChecker()
        self.spellChecker.load_words('spell.words')

    def test_spell_checker(self):
        self.assertTrue(len(self.spellChecker.words) > 50000)
        self.assertTrue(self.spellChecker.check_word('zygotic'))
        self.assertFalse(self.spellChecker.check_word('zogotic'))
        self.assertEqual([{'line': 1, 'pos': 9, 'word': 'mistasdas'}],
                self.spellChecker.check_words('zygotic mistasdas elementary'))
        self.assertEqual([],
                self.spellChecker.check_words('our first correct sentence'))
        self.assertEqual(0,
                len(self.spellChecker.check_words('Our first correct sentence.')))
        self.assertEqual([{'line': 1, 'pos': 9, 'word': 'mistasdas'}, {'line': 1, 'pos': 19, 'word': 'spelllleeeing'}],
                self.spellChecker.check_words('zygotic mistasdas spelllleeeing elementary'))
        self.assertEqual(2,
                len(self.spellChecker.check_words('zygotic mistasdas spelllleeeing elementary')))
        #self.assertEqual(0, len(self.spellChecker.check_document('spell.words')))
        self.assertEqual([{'line': 2, 'pos': 8, 'word': 'larn'}, 
                          {'line': 2, 'pos': 13, 'word': 'huw'}, 
                          {'line': 2, 'pos': 26, 'word': 'wurdz'}],
                self.spellChecker.check_document('darren.txt'))
        self.assertEqual({'darren.txt': [{'line': 2, 'pos': 8, 'word': 'larn'}, 
                          {'line': 2, 'pos': 13, 'word': 'huw'}, 
                          {'line': 2, 'pos': 26, 'word': 'wurdz'}]},
                self.spellChecker.check_directory('*.txt'))

if __name__ == '__main__':
    unittest.main()
