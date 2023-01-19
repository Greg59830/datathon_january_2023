# -*- coding: utf-8 -*-
"""population.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xS2yHNCOEJPPxGosx5ywYKajbJ6--YPA
"""

import pandas as pd
import numpy as np
import re

from google.colab import drive
drive.mount('/content/drive')

link = "/content/drive/MyDrive/2209-Data/Projets/Projet3/ACMG/data/Population.csv"
population_cleaned= pd.read_csv(link,sep=",")

population_cleaned=population_cleaned.drop(['Unnamed: 0'], axis=1)

print(population_cleaned['Population'].value_counts())

population_cleaned['Age'] = population_cleaned['Population'].apply(lambda x: 'undefined' if 'female' in x else x)# new colunm ok

population_cleaned[['Age']] = population_cleaned[['Age']] .replace(["adult"], ["19-44"])# Adult  = 19-44

population_cleaned[['Age']] = population_cleaned[['Age']] .replace(["aged"], ["65+"])# aged = 65+ in new colunm NOK

population_cleaned[['Age']] = population_cleaned[['Age']] .replace(["aged, 80 and over"], ["80+"])# aged = 80+ in new colunm NOK

population_cleaned[['Age']] = population_cleaned[['Age']] .replace(["male"], ["undefined"])# male=undefined

population_cleaned[['Age']] = population_cleaned[['Age']] .replace(["female"], ["undefined"])# female=undefined

population_cleaned[['Age']] = population_cleaned[['Age']] .replace(["middle aged"], ["45+"])# female=undefined

population_cleaned[['Age']] = population_cleaned[['Age']] .replace(["adolescent"], ["13-18"]) #adolescent= 13-18

population_cleaned[['Age']] = population_cleaned[['Age']] .replace(["child"], ["0-18"]) #adolescent= 13-18

population_cleaned[['Age']] = population_cleaned[['Age']] .replace(["young adult"], ["19-24"]) #young adult= 19-24

population_cleaned[['Age']] = population_cleaned[['Age']] .replace(["infant"], ["1-23 months"]) #infant= 1-23 months

population_cleaned[['Age']] = population_cleaned[['Age']] .replace(["child, preschool"], ["2-5"]) #child, preschool = 2-5 years

population_cleaned[['Age']] = population_cleaned[['Age']] .replace(["infant, newborn"], ["0-23 months"]) #infant,newborn = 1-23 months

population_cleaned[['Age']] = population_cleaned[['Age']] .replace(["pregnant women"], ["undefined"]) #infant,newborn = 1-23 months

print(population_cleaned.head(500).to_markdown())

population_cleaned.to_csv('/content/drive/MyDrive/2209-Data/Projets/Projet3/ACMG/CSV traités/population_cleaned.csv', index=False)

population_cleaned['sex'] = population_cleaned['Population'].apply(lambda x: 'female' if 'female' in x else x)

population_cleaned[['sex']] = population_cleaned[['sex']] .replace(["adult"], ["undefined"])# Adult  = undefined

population_cleaned[['sex']] = population_cleaned[['sex']] .replace(["aged"], ["undefined"])#  aged  = undefined

population_cleaned[['sex']] = population_cleaned[['sex']] .replace(["aged, 80 and over"], ["undefined"]) # 80+ = undefined

population_cleaned[['sex']] = population_cleaned[['sex']] .replace(["middle aged"], ["undefined"])# middleaged=undefined

population_cleaned[['sex']] = population_cleaned[['sex']] .replace(["adolescent"], ["undefined"]) #adolescent= undefined

population_cleaned[['sex']] = population_cleaned[['sex']] .replace(["child"], ["undefined"]) #adolescent= undefined

population_cleaned[['sex']] = population_cleaned[['sex']] .replace(["young adult"], ["undefined"]) #young adult= undefined

population_cleaned[['sex']] = population_cleaned[['sex']] .replace(["infant"], ["undefined"]) #infant= undefined

population_cleaned[['sex']] = population_cleaned[['sex']] .replace(["child, preschool"], ["undefined"]) #child pre school= undefined

population_cleaned[['sex']] = population_cleaned[['sex']] .replace(["infant, newborn"], ["undefined"])  #infant,newborn = undefined

population_cleaned[['sex']] = population_cleaned[['sex']] .replace(["pregnant women"], ["female"]) #pregnant women = female
