import re
from pdfminer.high_level import extract_pages ,extract_text
import pandas as pd
import dataframe_image as dfi
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
#df = pd.DataFrame(data)
#dfi.export(df, 'df_styled.png')
#print(df)

#extract pdf

for page_layout in extract_pages("input.pdf"):
  for element in page_layout:
    print(element)