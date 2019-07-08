'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np

def getAveragePolaritySubjectivity(sentiments):
    totalPolarity = 0
    totalSubjectivity = 0
    for sentiment in sentiments:
        totalPolarity += sentiment.polarity
        totalSubjectivity += sentiment.subjectivity
    return (totalPolarity/len(sentiments), totalSubjectivity/len(sentiments))

def getPolarityArray(sentiments):
    polarities = []
    for sentiment in sentiments:
        polarities.append(sentiment.polarity)
    return polarities

def getSubjectivityArray(sentiments):
    subjectivities = []
    for sentiment in sentiments:
        subjectivities.append(sentiment.subjectivity)
    return subjectivities

def graphHistogram(data, minX, maxX, xLabel, yLabel, title, figure_num):
    plt.figure(figure_num)
    num_bins = 20
    n, bins, patches = plt.hist(data, num_bins, facecolor='g', alpha=0.75)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.axis([minX, maxX, 0, len(data)]) # min and max for x axis, then y axis
    plt.grid(True)
    plt.show()

def graphScatterplot(sentiments):
    plt.figure(1)
    np.random.seed(19680801)

    N = len(sentiments)
    x = getPolarityArray(sentiments)
    y = getSubjectivityArray(sentiments)
    colors = np.random.rand(N)
    area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    plt.show()
# array containing all Sentiment objects
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

# print average polarities and subjectivities
averages = getAveragePolaritySubjectivity(allSentiments)
print(f'Average polarity: {averages[0]}')
print(f'Average subjectivity: {averages[1]}')
print('')

graphScatterplot(allSentiments)
# graph polarity histogram
polarities = getPolarityArray(allSentiments)
graphHistogram(polarities, -1, 1, 'Polarity Values', 'Number of tweets', 'Histogram of Polarity', 2)

# graph subjectivity histogram
subjectivities = getSubjectivityArray(allSentiments)
graphHistogram(subjectivities, 0, 1, 'Subjectivity Values', 'Number of tweets', 'Histogram of Subjectivity', 3)
