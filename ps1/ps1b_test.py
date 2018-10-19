# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 20:25:42 2018

@author: michi
"""

from unittest import TestCase
import ps1b


@contextmanager
def mock_set_input(mock):
    original_set_input = ps1b.set_input
    ps1b.set_input = lambda _: mock
    yield
    ps1b.set_input = original_set_input

class Ps1b_Test(TestCase):

    def test_set_annual_salary(self):
        with mock_set_input('120000'):
            self.assertEqual(ps1b.set_annual_salary(), 120000)
    
    def test_set_portion_saved(self):
        with mock_set_input('0.10'):
            self.assertEqual(ps1b.set_portion_saved(), 0.10)
        
    def test_set_total_cost(self):
        with mock_set_input('1000000'):
            self.assertEqual(ps1b.set_total_cost(), 1000000)
        
    def test_set_portion_down_payment(self):
        self.assertEqual(ps1b.set_portion_down_payment(), 0.25)
        
    def test_set_semi_annual_raise(self):
        with mock_set_input('0.03'):
            self.assertEqual(ps1b.set_semi_annual_raise(), 0.03)
    
    def test_set_current_savings(self):
        self.assertEqual(ps1b.set_current_savings(), 0.0)
        
    def test_set_r(self):
        self.assertEqual(ps1b.set_r(), 0.04)
        
    def test_months_to_save(self):
        #test case 1:
        inputs = {
                'annual_salary': 120000,
                'portion_saved': 0.05,
                'total_cost': 500000,
                'semi_annual_raise': 0.03,
                'portion_down_payment': 0.25,
                'current_savings': 0.0,
                'r': 0.04
                }
        self.assertEqual(ps1b.months_to_save(inputs), 142)
        #test case 2:
        inputs = {
                'annual_salary': 80000,
                'portion_saved': 0.1,
                'total_cost': 800000,
                'semi_annual_raise': 0.03,
                'portion_down_payment': 0.25,
                'current_savings': 0.0,
                'r': 0.04
                }
        self.assertEqual(ps1b.months_to_save(inputs), 159)
        #test case 3:
        inputs = {
                'annual_salary': 75000,
                'portion_saved': 0.05,
                'total_cost': 1500000,
                'semi_annual_raise': 0.05,
                'portion_down_payment': 0.25,
                'current_savings': 0.0,
                'r': 0.04
                }
        self.assertEqual(ps1b.months_to_save(inputs), 261)
        
#execution of test methods     
test = Ps1b_Test()
method_names = [
        'test_set_annual_salary',
        'test_set_portion_saved',
        'test_set_total_cost',
        'test_set_semi_annual_raise',
        'test_set_portion_down_payment',
        'test_set_current_savings',
        'test_set_r',
        'test_months_to_save'
        ] #probably a better way to retrieve these
for method in method_names:
    getattr(test, method)() #calls method