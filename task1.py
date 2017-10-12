import requests
import pdfminer.high_level

r = requests.get('http://www.germania.diplo.de/contentblob/4048654/Daten/7889181/1entschiedenevisumantraege.pdf')
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
