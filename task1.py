import requests
import pdfminer.high_level
from lxml import html

embassy_link = requests.get('http://www.germania.diplo.de/Vertretung/russland/ru/02-mosk/1-visa/3-merkblaetter/nationale-visa/0-nationale-visa.html#topic23')
parsed_embassy_link = html.fromstring(embassy_link.text)
all_links = parsed_embassy_link.xpath('//a/@href')
for i in all_links:
    if '1entschiedenevisumantraege.pdf' in i:
        link_to_list = 'http://www.germania.diplo.de' + i
r = requests.get(link_to_list)
with open('res.pdf', 'wb') as res:
    res.write(r.content)
with open('res.pdf', 'rb') as doc:
    with open('res.txt', 'wb') as docTxt:
        pdfminer.high_level.extract_text_to_fp(doc, docTxt)
with open('res.txt', 'r') as docTxt1:
    l = docTxt1.read()
    if '3607376' in l:
        print("You did great!")
    else:
        print("Not today, babe :(")