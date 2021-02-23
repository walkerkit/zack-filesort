import pandas as pd
from os import walk

_, _, filenames = next(walk("C:/"))

dataFrames = []
for file in filenames:
    df = pd.read_csv('C:/' + file, header=None, delim_whitespace=True)
    dataFrames.append(df)
print(dataFrames)

data = []
for frame in dataFrames:
    data.append(getInfo(frame))


def getInfo:

    return (range, spread)
