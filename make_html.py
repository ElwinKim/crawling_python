from selenium import webdriver
from bs4 import BeautifulSoup
import os
import time

class MakeHtml:
    project_name = ''
    file_name = ''
    elements_list = ''

    def __init__(self, project_name, file_name, elements_list):
        MakeHtml.project_name = project_name
        MakeHtml.file_name = file_name
        MakeHtml.elements_list = elements_list

        self.update_html()


    @staticmethod
    def update_html():
        
        with open(MakeHtml.file_name) as file:
            html_parse = file.read()
        soup = BeautifulSoup(html_parse, 'html.parser')
        k = 0
        title = soup.find_all(class_="title")
        for t in title:
            t.string = MakeHtml.elements_list[k][0]
            k += 1

        k = 0
        for a in soup.find_all(class_ = "image_link"):
            a['href'] = MakeHtml.elements_list[k][2]
            k += 1

        k = 0
        for a in soup.find_all(class_ = "button_link"):
            a['href'] = MakeHtml.elements_list[k][2]
            k += 1

        k = 0
        price = soup.find_all(class_="dollar")
        for p in price:
            p.string = MakeHtml.elements_list[k][1]
            k += 1

        k = 0
        for img in soup.find_all('img'):
            img['src'] = MakeHtml.elements_list[k][3]
            k += 1

        k = 0
        price = soup.find_all(class_="dollar")
        for p in price:
            p.string = MakeHtml.elements_list[k][1]
            k += 1
            

    # save the file again
        if not os.path.isfile(MakeHtml.project_name+".html"):
            with open(MakeHtml.project_name+".html", "w") as outf:
                outf.write(str(soup))
        else:
            with open(MakeHtml.project_name+".html", "w") as outf:
                outf.write(str(soup))
        





    # @staticmethod
    # def make_html():
    #     with open(MakeHtml.file_name, "w") as file:
    #         file.write()






    # if filename:
    #     with open(filename, 'r') as f:
    #         datastore = json.load(f)
    # json_str = json.dumps(attr_list);
    # file_path = os.path.join(project_name, filename)
    #
    # if not os.path.isfile(file_path):
    #     write_file(file_path, json_str)