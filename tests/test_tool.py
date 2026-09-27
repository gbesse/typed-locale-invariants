import copy
import json
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tool import check
DATA = json.loads((Path(__file__).resolve().parents[1]/'examples/decisions.json').read_text())

class LocaleTests(unittest.TestCase):
    def test_detects_flip_and_drift(self):
        result = check(DATA)
        self.assertFalse(result['ok'])
        self.assertEqual(len(result['findings']), 2)

    def test_stable_variants_pass(self):
        data = copy.deepcopy(DATA)
        data['groups'][0]['variants'][2]['choice'] = 'refund'
        data['groups'][0]['variants'][2]['probability'] = 0.87
        self.assertTrue(check(data)['ok'])

    def test_missing_locale_rejected(self):
        data = copy.deepcopy(DATA)
        data['groups'][0]['variants'].pop()
        with self.assertRaises(ValueError):
            check(data)
