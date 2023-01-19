# -*- coding: utf-8 -*-
"""companysearch.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18U8gEcGCdbKm9inVBsV7c165XY4YpOCo
"""

import pandas as pd
import numpy as np
import re

from google.colab import drive
drive.mount('/content/drive')

link = "/content/drive/MyDrive/2209-Data/Projets/Projet3/ACMG/Greg/new_article.csv"
company_search = pd.read_csv(link,sep=",")

print(company_search.head(100).to_markdown())

contact_filter=company_search[company_search["Author_contact"] != 'university']  #filtrer au mximmumn pour les value count

#15902 données dans author_contact, on va supprimer les nan
contact_filter.dropna(inplace = True)
print(contact_filter.info())

print(contact_filter.head(50).to_markdown())

print(contact_filter.info())

contact_filter.to_csv('/content/drive/MyDrive/2209-Data/Projets/Projet3/ACMG/contact_filter.csv', index=False)