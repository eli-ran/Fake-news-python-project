# This is a sample Python script.
import pandas as pd

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.




print('Hello world')
print('goodbye world ;( ')
print('do you work now?')

liar = pd.read_csv('liar_dataset/train.tsv', sep='\t', header=None, usecols = [0, 1 , 2])
liar.columns =['id', 'label', 'statement']

print(liar)




