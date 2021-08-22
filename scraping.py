import requests  # p/ fz as req
from bs4 import BeautifulSoup  # p/ manipular o HTML
from colored import fg, bg, attr

url = 'https://shdo.wordpress.com/online/tabela-de-cores-rgb/'
response = requests.get(url)

html = BeautifulSoup(response.text, 'html.parser')

tr = []
for topic in html.select('.entry-content table tbody .fixedfont'):
    tr.append(topic.text)

tup = [(tr[x], tr[x+1], tr[x+2]) for x in range(0, len(tr), 3)]

reset = attr('reset')
font_color = fg('black')

for color, rgb, hexa in tup:
    bg_color = bg(hexa)
    color_bg = font_color + bg_color
    print(color_bg, f'Cor: {color} | RGB: {rgb} | Hexadecimal: {hexa}', reset)
