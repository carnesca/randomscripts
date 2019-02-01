import pandas as pd
from nltk.corpus import stopwords
stop = stopwords.words('english')

#adds these words to list of stopwords
stop.extend(["still", "going", "like", "i", "the", "would", "get"])

# reads CSV file and puts data into a dataframe
may_mentions = pd.read_csv("may_mentions.csv")

#Deletes all words in the data found in stopwords list
may_mentions["text_wo_stopwords"] = may_mentions["Text"].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))

#splits up each row of text and generates list of 50 most frequently occuring words
most_freq = pd.Series(' '.join(may_mentions["text_wo_stopwords"]).lower().split()).value_counts()[:50]

#Puts output of line 13 into dateframe with titles and prints the dataframe in terminal
most_freq.rename_axis("Top Words").reset_index(name = "Num. of times found")

#Creates CSV file for output for further analysis
"""
most_freq.to_csv("most_freq_may_mentions.csv", sep=',', encoding='utf-8')
"""
