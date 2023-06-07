import check50 # import the check50 module
import check50.py
import re
import os

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
    """File exists""" # this is what you will see when running check50
    check50.exists("Assignment_2.py") # the actual check
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases1():
    """Program prints correct output 1"""
    
    actual = check50.run("python3 Assignment_2.py").stdout(timeout=20)
    
    expected = "The shape of the original DataFrame is:\s*\(9999, 11\)"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the shape of the original DataFrame."
        raise check50.Missing("Correct results",'your output',help=help)
