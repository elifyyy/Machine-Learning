import ParseXML as x
import nltk
import numpy as np
from sklearn import preprocessing

tech_file = open("tech_words.txt",'r') #words taken from http://www.rhymezone.com (words related to technology)

tech_word = []
for line in tech_file :
    if len(line) > 3 :
        tech_word.append(line.strip().lower())

personal_file = open("personal_words.txt",'r')#words taken from http://www.rhymezone.com (words related to friend)

personal_word = []
for line in personal_file :
    if len(line) > 3 :
        personal_word.append(line.strip().lower())


samples = []
for i in range (0,len(x.all_users_tweets)): #iterate over all sample data
    sample_i = np.array([[0 , 0 , 0, 0]]) #num_of_pronouns, num_of_det_prepos ,num_of_tech_words ,num_of_personal_words
    number_of_pronoun = 0
    number_of_det_prepos = 0
    number_of_tech_words = 0
    number_of_personal_words = 0
    for j in range (0,len(x.all_users_tweets[i])):
        text = nltk.tokenize.word_tokenize(x.all_users_tweets[i][j])
        temp = nltk.pos_tag(text)
        for elem in temp:
            if elem[1] == 'DT' or elem[1] == 'IN':
                number_of_det_prepos = number_of_det_prepos + 1
            elif elem[1] == 'PRP' or elem[1] == 'PRP$' or elem[1] == 'WP' or  elem[1] ==  'WP$':
                number_of_pronoun = number_of_pronoun + 1
            elif elem[0].lower() in tech_word :
               number_of_tech_words = number_of_tech_words + 1
            elif elem[0].lower() in personal_word :
               number_of_personal_words = number_of_personal_words + 1
    sample_i[0][0] = number_of_pronoun
    sample_i[0][1] = number_of_det_prepos
    sample_i[0][2] = number_of_tech_words
    sample_i[0][3] = number_of_personal_words
    samples.append(sample_i)

real_classes = [] #1 for female,0 for male
for i in range(0,len(x.actual_results)):
    if(x.actual_results[i][1]== "female"):
        real_classes.append(1)
    else:
        real_classes.append(0)

samples = np.array(samples)
nsamples, nx, ny = samples.shape
samples = samples.reshape((nsamples,nx*ny))
real_classes = np.array(real_classes)
samples = preprocessing.scale(samples)

print(samples)