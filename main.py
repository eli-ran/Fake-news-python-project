# This is a sample Python script.
import pandas as pd
from matplotlib import pyplot as plt

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


liar = pd.read_csv('liar_dataset/train.tsv', sep='\t', header=None, usecols = [0, 1 , 2, 4])
liar.columns =['id', 'label', 'statement', 'speaker']
#liar.columns =['id', 'label', 'statement', 'subject', 'speaker', 'jib_title', 'state', 'party', 'subject', 'bt-count', 'ht-count', 'mt-count', 'pof-count', 'context']

plot_size = plt.rcParams["figure.figsize"]
print(plot_size[0])
print(plot_size[1])

plot_size[0] = 8
plot_size[1] = 6
plt.rcParams["figure.figsize"] = plot_size

#liar.speaker.value_counts().plot(kind='pie', autopct='%1.0f%%')

speakerCount = liar.speaker.value_counts()
speakerCountDF = speakerCount.to_frame().reset_index()
speakerCountDF.columns = ['name','count']
#print(labels)
fig1, ax1 = plt.subplots()
ax1.pie(speakerCount[0:10], labels = speakerCountDF.name[0:10],autopct='%1.1f%%', startangle=90)
#ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

#print(speakerCount)
# create a new dataset, deleting the unnecessary columns
