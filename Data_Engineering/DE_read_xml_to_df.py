# import the BeautifulSoup and pandas
from bs4 import BeautifulSoup
import pandas as pd

# open the data.xml file and load into Beautiful Soup
with open("data.xml") as fp:
    soup = BeautifulSoup(fp, "lxml") # lxml is the Parser type

# build an empty dictionary. 
# Use the destination tag(tag_name_3 in this case) as the keys
xml_dict = {'key_a':[]
            , 'key_b':[]
            , 'key_c':[]
            , 'key_d':[]}

for record in soup.find_all(tag_name_1):
    # use the find_all method to get all fields in each record
    for record in record.find_all(tag_name_2):
        xml_dict[record[tag_name_3]].append(record.text)

#convert the dict to pandas dataframe
df_xml = pd.DataFrame.from_dict(xml_dict)
