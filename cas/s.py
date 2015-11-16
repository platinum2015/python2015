# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import os 

import xlrd
from xml.dom import minidom
from xml.dom.minidom import parse, parseString
from datetime import  date

f = 'DataMasking_ObjectListing.xlsx'
directory = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(directory,f)
today = date.today()

pd.read_excel(filename)