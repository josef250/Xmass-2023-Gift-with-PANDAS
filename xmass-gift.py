# Xmass Gift Boxes

import pandas as pd

gifts = {"InBox": ["Shoes", "Phone", "Laptop"],
         "Width": [10, 8, 25],
         "Height": [5, 4, 12]}
# creating data frame for my dictionary

data = pd.DataFrame(gifts)

area = []
# width * Height

for i in range(len(data)):
    area_cal = data["Width"][i] * data["Height"][i]
    area.append(area_cal)

data["Box Area"] = area
data.to_csv("Xmass-gifts.xls", sep="\t")
