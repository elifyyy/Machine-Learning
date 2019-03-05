import xml.etree.ElementTree as ET
import os

directory = os.path.join("en","truth.txt")
file = open(directory , "r")

actual_results = []
for line in file:
    temp_arr = line.split(":::")
    actual_results.append(temp_arr)

root_arr = []
for i in range(0,len(actual_results)):
    sample_name = os.path.join("en",actual_results[i][0]+".xml")
    tree = ET.parse(sample_name)
    root = tree.getroot()
    root_arr.append(root)

number_of_tweets =(len(root[0]))

all_users_tweets = []
for j in range (0,len(root_arr)):
    temp = []
    for x in range(0,number_of_tweets):
        temp.append(root_arr[j][0][x].text)
    all_users_tweets.append(temp)
