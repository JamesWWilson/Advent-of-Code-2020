
# 12-06-2020

# https://adventofcode.com/2020/day/6

import pandas as pd 
import numpy as np 

# Read each line of the file into a format suitable for a matrix 
merged_sublist = []
custom_forms = []
with open('input.txt','r') as f:
    for line in f:
        # if line is not blank
        if(len(line.split())!=0):
            #print(1)
            cf = line.split()
            # integrate into sublist
            #for i in zip(pp, merged_sublist):
            for i in cf:
                merged_sublist.append(i)
        # if line is blank
        if(len(line.split())==0):
            #print(0)
            # append sublist to custom_forms
            for i in merged_sublist:
                custom_forms.append(merged_sublist)
            # clear sublist object 
            merged_sublist = []

print(custom_forms)

cf_data = pd.DataFrame(custom_forms)
cf_data.drop_duplicates(inplace=True)
cf_data.reset_index(inplace=True)
cf_data.head(20)

# count individuals 

# combined fields 
cf_data["combined_fields"] = cf_data[0].fillna('') + cf_data[1].fillna('') + cf_data[2].fillna('')  + cf_data[3].fillna('') + cf_data[4].fillna('') 
# subset to just combined field 
cf_data["combined_fields"] 


# sort each row
# count unique number of characters 
cf_data

len(set(cf_data["combined_fields"]))


cf_data["combined_fields"].str.cat()


