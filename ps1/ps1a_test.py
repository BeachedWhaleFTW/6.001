# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 19:10:32 2018

@author: michi
"""

from unittest.mock import patch
from unittest import TestCase
import ps1a


@contextmanager
def mock_set_input(mock):
    original_set_input = ps1a.set_input
    ps1a.set_input = lambda _: mock
    yield
    ps1a.set_input = original_set_input

class Ps1a_Test(TestCase):

    def test_set_annual_salary(self):
        with mock_set_input('120000'):
            self.assertEqual(ps1a.set_annual_salary(), 120000)
    
    def test_set_portion_saved(self):
        with mock_set_input('0.10'):
            self.assertEqual(ps1a.set_portion_saved(), 0.10)
        
    def test_set_total_cost(self):
        with mock_set_input('1000000'):
            self.assertEqual(ps1a.set_total_cost(), 1000000)
        
    def test_set_portion_down_payment(self):
        self.assertEqual(ps1a.set_portion_down_payment(), 0.25)
    
    def test_set_current_savings(self):
        self.assertEqual(ps1a.set_current_savings(), 0.0)
        
    def test_set_r(self):
        self.assertEqual(ps1a.set_r(), 0.04)
    
        
    def test_set_down_payment(self):
        inputs = {
                'total_cost': 1000000,
                'portion_down_payment': 0.25
                }
        self.assertEqual(ps1a.set_down_payment(inputs), 250000)
        
        inputs = {
                'total_cost': 500000,
                'portion_down_payment': 0.25
                }
        self.assertEqual(ps1a.set_down_payment(inputs), 125000)
        
    def test_set_monthly_saved(self):
        inputs = {
                'annual_salary': 120000,
                'portion_saved': 0.10
                }
        self.assertEqual(ps1a.set_monthly_saved(inputs), 12000 / 12)
        
        inputs = {
                'annual_salary': 80000,
                'portion_saved': 0.10
                }
        self.assertEqual(ps1a.set_monthly_saved(inputs), 8000 / 12)
        
    def test_months_to_save(self):
        inputs = {
                'annual_salary': 120000,
                'portion_saved': 0.10,
                'total_cost': 1000000,
                'portion_down_payment': 0.25,
                'current_savings': 0.0,
                'r': 0.04
                }
        self.assertEqual(ps1a.months_to_save(inputs), 183)
        
        inputs = {
                'annual_salary': 80000,
                'portion_saved': 0.15,
                'total_cost': 500000,
                'portion_down_payment': 0.25,
                'current_savings': 0.0,
                'r': 0.04
                }
        self.assertEqual(ps1a.months_to_save(inputs), 105)
        
#execution of test methods     
test = Ps1a_Test()
method_names = [
        'test_set_annual_salary',
        'test_set_portion_saved',
        'test_set_total_cost',
        'test_set_portion_down_payment',
        'test_set_current_savings',
        'test_set_r',
        'test_set_down_payment',
        'test_set_monthly_saved',
        'test_months_to_save'
        ] #probably a better way to retrieve these
for method in method_names:
    getattr(test, method)() #calls method