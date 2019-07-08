'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

def getAveragePolaritySubjectivity(sentiments):
    totalPolarity = 0
    totalSubjectivity = 0
    for sentiment in sentiments:
        totalPolarity += sentiment.polarity
        totalSubjectivity += sentiment.subjectivity
    return (totalPolarity/len(sentiments), totalSubjectivity/len(sentiments))

allSentiments = []
#Get the JSON data
tweetFile = open("../u2.1/tweets_small.json", "r")
tweetData = json.load(tweetFile)
for tweet in tweetData:
    '''
    The polarity score is a float within the range [-1.0, 1.0].
    The subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective.
    '''
    text = tweet['text']
    blob = TextBlob(text)
    allSentiments.append(blob.sentiment)
tweetFile.close()

averages = getAveragePolaritySubjectivity(allSentiments)
print(f'Average polarity: {averages[0]}')
print(f'Average subjectivity: {averages[1]}')
