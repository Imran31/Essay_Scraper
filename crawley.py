from bs4 import BeautifulSoup
import requests
from fpdf import FPDF,HTMLMixin

class MyFPDF(FPDF, HTMLMixin):
    pass
url = 'http://www.paulgraham.com/articles.html'
soup = BeautifulSoup(requests.get(url).text,"lxml")
essay_links = soup.find_all('a')
j = 1

def make_new_pdf(content,file_name):
    pdf = MyFPDF()
    pdf.add_page()
    pdf.set_font('Times','', 14)
    pdf.write(7,content)
    pdf.output(file_name, 'F')

for i in range(4,len(essay_links) - 4):
    link = BeautifulSoup(requests.get("http://www.paulgraham.com/" + str(essay_links[i]['href'])).text,"lxml")
    data = link.find_all('tr')
    make_new_pdf((data[0].get_text().encode('utf-8')), str(essay_links[i].get_text()))
    j += 1
    print(j)
