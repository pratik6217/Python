# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_p_0NxTH7fXR6rfWOfQi7djkEH6mDsZ8
"""

class Pratik:
  def __init__(self,name):
    self.name=name
    print(name)
    
  def __str__(self):
    return("Hi my name is {}".format(self.name))
  def print_name(self):
    return "My name is {name}".format(name=self.name)

'''help(Pratik)
obj1=Pratik("Pratik")
obj2=Pratik("Mehak")
obj3=Pratik("Ananya")
print(obj1)
print(obj2)
print(obj3)'''

print(obj1.print_name())
print(obj2.print_name())
print(obj3.print_name())

from google.colab import drive
drive.mount('/content/drive')

import datetime
date_time=(datetime.datetime.now())
print(date_time.time())
print(date_time.date())
print(date_time.year)

import os
os.system("bash")

import pandas
names=["Pratik","Mehak","Ananya","Madhu"]
sur_names=["Mishra","Makhijja","Panday","Singh"]
age=[19,19,23,19]
gender=["Male","Female","Female","Female"]
dict_1={"Names":names,"Surnames":sur_names,"Age":age,"Gender":gender,"Mode":"1"}
df=pandas.DataFrame({"Names":names,"Surnames":sur_names,"Age":age,"Gender":gender,"Mode":1})

'''for key, value in dict_1.items():
  if "Pratik" in value or "1" in value:
    print(dict_1[key])'''

print(df)

python --version