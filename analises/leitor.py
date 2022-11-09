import pandas as pd
from PyPDF2 import PdfReader
import re

reader = PdfReader(r"D:\visualcode\data_analistyc\files\Enel.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

values = re.findall(r'\d+,\d+', text)
faturamento = re.findall(r'^([a-z].*?[\d+,\d+])$', text, flags=re.I)
print(values)
# print(faturamento)