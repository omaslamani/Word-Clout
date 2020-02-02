# importing all the libraries required for this WordCloud generator
import numpy as np
import pandas as pd
from os import path
from PIL import Image
import matplotlib.pyplot as plt
import wordcloud


DataFrame = pd.read_csv("SampleCSV.csv")
DataFrame.head()
DataFrame[["name", "fruit", "number"]].head()
fruit = DataFrame.groupby("name")
fruit.describe().head()
fruit.mean().sort_values(by="number", ascending=False).head()
text = DataFrame.fruit[2]
print(text)
mask = np.array(Image.open("AmyKlobuchar.png"))
mask


imageColors = wordcloud.ImageColorGenerator(mask)

AK = wordcloud.WordCloud(background_color="white", mask=mask, contour_color='firebrick', contour_width=3,max_words=1000000)
AK.generate(text)
AK.to_file("AmyKlobuchar.png")

plt.imshow(AK, interpolation='bilinear')
plt.axis("off")
plt.show()