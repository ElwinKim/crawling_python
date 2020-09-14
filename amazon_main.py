import scrap
from convert_json import MakeJson
from make_html import MakeHtml

projectName = "Amazongift_man1"
fileName = projectName + ".html"
url = "https://www.amazon.ca/gcx/Gifts-for-Men/gfhz/?categoryId=adult-male"
div_id = "gcx-gf-section-0"

# To save scrapped data from scrap.py file
ele_list = scrap.scrap_url(url, div_id)

# Send parameters to make HTML file with collected data 
MakeHtml(projectName, fileName, ele_list)

# Send parameters to convert Json file with collected data 
MakeJson(projectName, fileName, ele_list)