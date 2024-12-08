import json

from bs4 import BeautifulSoup as bs
from oklch import RGB
from requests import get


def format_oklch(color):
    color = str(color)
    colors = color[:-1].split("(")[1].split(",")
    l, c, h = [float(color) for color in colors]
    l = round(l * 100, 2)
    c = round(c, 3)
    h = round(h)
    return f"oklch({l}% {c} {h})"


def convert_rgb_to_oklch(color):
    liste = color.split("rgb(")[1].split(")")[0].split(" ")
    r, g, b = [int(x) for x in liste]
    oklch = RGB(r, g, b).to_OKLCH()
    return format_oklch(oklch)


url = "https://tailwindcss.com/docs/background-color"
response = get(url)
html = response.content
soup = bs(html, "lxml")

table = soup.find("table", attrs={"class": "w-full text-left border-collapse"}).find(
    "tbody"
)
table_text = (
    table.text.replace("background-color", "").replace("bg-", "").replace(";", "")
)
liste = table_text.split("\n")[5:]
liste = [x for x in liste if x]
dictio = {}
for x in liste:
    name, value = x.split(": ")
    color_name, color_number = name.split("-")
    dictio.setdefault(color_name, {})
    dictio[color_name].setdefault(color_number, convert_rgb_to_oklch(value))
