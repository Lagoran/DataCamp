# Import pandas as pd
file = '../_datasets/log_file.txt'
import pandas as pd
import numpy as np

col1 = []

col2 = []

col3 = []

with open(file) as f:
    txt = f.readlines()

print(txt,txt[0],txt[1])

print(txt[0].split(']')[0].strip('['))
print(txt[0].split(' ')[1])
print(txt[0].split(' ')[2])
# print(txt[0].split(']')[0].strip('['))

for line in txt:

    ss=line.split(' ',2)

    s=line.split(']')[0].strip('[')

    # dt = datetime.strptime(s1, dtfmt)

    col1.append(s)

    s1=line.split(' ')[1].strip()

    col2.append(s1)

    if len(line) > (len(s)+len(s1)):

        col3.append(ss[2].strip('\n'))

    else:

        col3.append(np.nan)

df = pd.DataFrame([col1, col2, col3])

df = df.T

df.columns=['ID','Event_name', 'Message']

# Assign the filename: file

# Read the file into a DataFrame: df
#df = pd.read_csv(file)

# View the head of the DataFrame
print(df.head())