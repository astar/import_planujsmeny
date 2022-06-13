#!/usr/bin/env python3

import pandas as pd
from dateutil.parser import  parse
import sys

fn = sys.argv[1]
data = pd.read_html(fn)[0].iloc[:-2]
data.columns = data.columns.get_level_values(1)
data.dropna(subset=['Směna'], inplace=True)
data['Směna'] = data['Směna'].str.replace(', Saunamistři, Saunamistr', '')
data = data.iloc[:,:2]
data['Subject'] = 'Smena maximus'
data['Start Date'] = data['Datum'].str.split(' ').str[1].str[:-1].apply(parse)
data['Start Time'] = data['Směna']
data['End Time'] = data['Směna']
data['Start Time'], data['End Time'] = zip(*data['Směna'].str.split('-'))
data["All Day Event"] = False
data["Location"] = "Maximus Resort, Hrázní 327/4a, 635 00 Brno-Kníničky, Czechia"
data["Description"] = None
data = data.iloc[:,2:]
data.to_csv(f"{fn.rsplit('.', 1)[0]}.csv", index=False, header=True)