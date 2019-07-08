'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud

# return set of words that have neutral sentiment
def getNeutralWords(wordSet):
    neutral = []
    for word in wordSet:
        blob = TextBlob(word)
        if blob.sentiment.polarity == 0:
            neutral.append(word)
    return neutral

# return set of words that have positive sentiment
def getPositveWords(wordSet):
    positive = []
    for word in wordSet:
        blob = TextBlob(word)
        if blob.sentiment.polarity > 0:
            positive.append(word)
    return positive

# return set of words that have positive sentiment
def getNegativeWords(wordSet):
    negative = []
    for word in wordSet:
        blob = TextBlob(word)
        if blob.sentiment.polarity < 0:
            negative.append(word)
    return negative

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

def graphScatterplot(sentiments, figure_num):
    plt.figure(1)
    np.random.seed(19680801)

    N = len(sentiments)
    x = getPolarityArray(sentiments)
    y = getSubjectivityArray(sentiments)
    colors = np.random.rand(N)
    area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    plt.show()

def generateWordCloud(text, title, figure_num):
    # Create and generate a word cloud image:
    # lower max_font_size, change the maximum number of word and lighten the background:
    wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)
    plt.figure(figure_num)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.title(title)
    plt.axis("off")
    plt.show()

def loadJSON():
    allTweetText = ''
    allSentiments = []
    tweetFile = open("../u2.1/tweets_small.json", "r")
    tweetData = json.load(tweetFile)
    for tweet in tweetData:
        '''
        The polarity score is a float within the range [-1.0, 1.0].
        The subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective.
        '''
        text = tweet['text']
        allTweetText += text + ' '
        blob = TextBlob(text)
        allSentiments.append(blob.sentiment)
    tweetFile.close()
    return (allTweetText, allSentiments)
# array containing all Sentiment objects
tupleObj = loadJSON()
allSentiments = tupleObj[1]
allTweetText = tupleObj[0]
filteredWords = []
filteredNoDuplicates = set()
print(allTweetText)

# print average polarities and subjectivities
averages = getAveragePolaritySubjectivity(allSentiments)
print(f'Average polarity: {averages[0]}')
print(f'Average subjectivity: {averages[1]}')
print('')

graphScatterplot(allSentiments, 1)
# graph polarity histogram
polarities = getPolarityArray(allSentiments)

graphHistogram(polarities, -1, 1, 'Polarity Values', 'Number of tweets', 'Histogram of Polarity', 2)

# graph subjectivity histogram
subjectivities = getSubjectivityArray(allSentiments)

graphHistogram(subjectivities, 0, 1, 'Subjectivity Values', 'Number of tweets', 'Histogram of Subjectivity', 3)

tweetBlob = TextBlob(allTweetText)
for word in tweetBlob.word_counts:
    if len(word) < 3:
        continue
    elif not word.isalpha():
        continue
    elif word in ['and', 'about', 'the', 'http']:
        continue
    else:
        filteredWords.append(word)
        filteredNoDuplicates.add(word)

input = ' '.join(filteredWords)
generateWordCloud(input, 'Tweets', 4)

neutralWords = getNeutralWords(filteredNoDuplicates)
positiveWords = getPositveWords(filteredNoDuplicates)
negativeWords = getNegativeWords(filteredNoDuplicates)

generateWordCloud(' '.join(neutralWords), 'Neutral Words', 5)
generateWordCloud(' '.join(positiveWords), 'Positive Words', 6)
generateWordCloud(' '.join(negativeWords), 'Negative Words', 7)
