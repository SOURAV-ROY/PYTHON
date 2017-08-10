'''
Created on Jun 18, 2017

@author: SOURAV
'''
from PYTHON.First import Saarc
Country = input("Enter the name of the country : ")

if Country in Saarc:
    print(Country, "is a member of SAARC")
else:
    print(Country, "is not a member of SAARC")
    print(" Program terminated ")
    