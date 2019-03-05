import numpy as np
from sklearn import preprocessing

file = open('53727641925datVersion2.txt', 'r') #file size was too large, beacause of memory issue, i only took some of the data.

samples = []

for line in file:
    token_arr = line.split(" ")
    index=0
    length = len(token_arr)
    while index < length:
        if bool(token_arr[index].strip())==False: # means empty string
            del token_arr[index]
        else:
            index = index + 1
        length = len(token_arr)

    samples.append(token_arr)

samples = np.array(samples[1:])


#find average of each col (same features of each sample) to not reported data
average_of_each_col_arr = []
for i in range (len(samples[0])):
    average = 0
    num_of_reported_data = 1
    for j in range(len(samples)):
        try:
            average = average + int(samples[j][i]) # itarete over same ith features for all samples
            num_of_reported_data = num_of_reported_data + 1
        except:
            pass # means it is not reported data
    average = average / num_of_reported_data
    average_of_each_col_arr.append(average)
                       

#replace averages instead of *'s
for i in range (len(samples)):
    for j in range (len(samples[i])):
        if('*' in samples[i][j]):
            samples[i][j] = average_of_each_col_arr[j]

#for SKC col
#CLR -> 1 , SCT ->2, BKN->3, OVC->4 OBS->5 POB->6
for i in range (len(samples)):
    if samples[i][7]== 'CLR':
        samples[i][7] = 1
    if samples[i][7]== 'SCT':
        samples[i][7] = 2
    if samples[i][7]== 'BKN':
        samples[i][7] = 3
    if samples[i][7]== 'OVC':
        samples[i][7] = 4
    if samples[i][7]== 'OBS':
        samples[i][7] = 5
    if samples[i][7]== 'POB':
        samples[i][7] = 6

#cast to float
for i in range (len(samples)):
    for j in range (len(samples[i])):
        samples[i][j] = float (samples[i][j])


samples = preprocessing.scale(samples) # scaling features








