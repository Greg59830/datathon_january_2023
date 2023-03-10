# -*- coding: utf-8 -*-
"""Projet3_authors_csv2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-LkLSXEtg_O-p157WMYPBT0JdVvY4PIZ
"""

import pandas as pd
import numpy as np
import re

from google.colab import drive
drive.mount('/content/drive')

link = "/content/drive/MyDrive/2209-Data/Projets/Projet3/ACMG/Greg/Full_author_name_audrey.csv"
df_author2_split = pd.read_csv(link,sep=",")

#supprimer unnamed 0
df_author2_split=df_author2_split.drop(columns=['Unnamed: 0'])

df_author2_split=df_author2_split.rename(columns={"0": "Author_Name"})

# on va séparer ce qu'il y a avant et après le /split/
df_author2_split['Author'] = df_author2_split['Full_author_name'].apply(lambda mytext : re.split('/split/',mytext)[0].title() )

#chercher les mails
test = df_author2_split.iloc[0,1]
mails = re.findall("\S+@\S+",test)[0].strip('.')
print(mails)

def check_mail(text):
  try :
    #return re.findall("\S+@[\w\.]+",text)[0].strip('.')
    return re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',text)[0]
  except :
    return ''

df_author2_split['email']  = df_author2_split.Full_author_name.apply(check_mail)



# supprimer colonne full author name
df_author2_split=df_author2_split.drop(columns=['Full_author_name'])

print(df_author2_split.head().to_markdown())

# ok on a plus ques les authors normés et les mail
df_author2_split.to_csv('/content/drive/MyDrive/2209-Data/Projets/Projet3/ACMG/Greg/authors_mail.csv', index=False)