# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 20:25:27 2018

@author: michi
"""

def set_input(text):
    return input(text)

def set_annual_salary():
    annual_salary = int(set_input("Enter your annual salary: "))
    return annual_salary

def set_portion_saved():
    portion_saved = float(set_input("The portion of salary to be saved: "))
    return portion_saved

def set_total_cost():
    total_cost = int(set_input("Enter the cost of your dream home: "))
    return total_cost

def set_semi_annual_raise():
    semi_annual_raise = float(set_input\
                              ("Enter the semi-annual raise, as a decimal: "))
    return semi_annual_raise

def set_portion_down_payment():
    return 0.25

def set_current_savings():
    return 0.0

def set_r():
    return 0.04

def set_down_payment(inputs):
    down_payment = inputs['total_cost']*inputs['portion_down_payment']
    return down_payment

def set_monthly_saved(inputs):
    monthly_saved = inputs['annual_salary']*inputs['portion_saved'] / 12
    return monthly_saved

def months_to_save(input_vars):
    inputs = input_vars
    current_savings = inputs['current_savings']
    r = inputs['r']
    
    month = 0
    down_payment = set_down_payment(inputs)

    while current_savings < down_payment:
        if month % 6 == 0 and month > 1:
            inputs['annual_salary'] = inputs['annual_salary'] + inputs\
            ['annual_salary']*inputs['semi_annual_raise']
            
        monthly_saved = set_monthly_saved(inputs)
        monthly_savings = current_savings*r/12 + monthly_saved
        current_savings += monthly_savings
        month += 1
        
    return month

if __name__ == '__main__':
    inputs = {
            'annual_salary': set_annual_salary(),
            'portion_saved': set_portion_saved(),
            'total_cost': set_total_cost(),
            'semi_annual_raise': set_semi_annual_raise(),
            'portion_down_payment': set_portion_down_payment(),
            'current_savings': set_current_savings(),
            'r': set_r()
            }
    months_req = months_to_save(inputs)
    print("Number of months: {}".format(months_req))