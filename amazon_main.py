import scrap
# from convert_json import MakeJson
from make_html import MakeHtml


# projectName = input("Enter project name: ")
# fileName = input("Enter JSON file name: ")
# url = input("Enter url to parse: ")
# div_id = input("Enter div id: ")

projectName = "Amazongift_man"
fileName = projectName + ".html"
url = "https://www.amazon.ca/gcx/Gifts-for-Men/gfhz/?categoryId=adult-male"
div_id = "gcx-gf-section-0"

ele_list = scrap.scrap_url(url, div_id)
# # for i in range(20):
# #     for j in range(4):
# print(ele_list[19][3])
# MakeJson(projectName, ele_list, fileName)
MakeHtml(projectName, fileName, ele_list)
