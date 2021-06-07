from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
df = pd.read_csv('Book.csv')
font = ImageFont.truetype('arial.ttf',45)
for index,j in df.iterrows():
    img = Image.open('ideathon.jpeg')
    draw = ImageDraw.Draw(img)
    draw.text(xy=(492,380),anchor="md",text='{}'.format(j['name']),fill=(0,0,0),font=font)
    img.save('certificates/{}.pdf'.format(j['name']))