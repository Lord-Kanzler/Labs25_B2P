# -*- coding: utf-8 -*-
"""LABS25_BridgesToProsperity.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13_vk_ydnVkB6FriTJ3gobJIb8WKzYLiD
"""

# Imports
import pandas as pd

"""Provided Data URLs"""

# Rwandan Government Village Data
site_assessment = 'https://raw.githubusercontent.com/Lord-Kanzler/Labs25_B2P/master/Data/B2P_Rwanda_Site_Assessment_Data.csv'

# Bridges to Prosperity Rwanda Data
names_codes = 'https://raw.githubusercontent.com/Lord-Kanzler/Labs25_B2P/master/Data/Rwanda_Administrative_Levels_and_Codes_Province_through_Village.csv'

# Loading data
site_assessment = pd.read_csv(site_assessement)
print(site_assessment.shape)
site_assessment.head(20)

names_codes = pd.read_csv(names_codes)
print(names_codes.shape)
names_codes.head(20)