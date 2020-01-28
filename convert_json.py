import json

import os
# #Read JSON data into the datastore variable
#
#
# #Use the new datastore datastructure
# print datastore["office"]["parking"]["style"]

class MakeJson:
    projectName = ''
    elementsList = ''
    fileName = ''

    def __init__(self, projectName, elementsList, fileName):
        MakeJson.projectName = projectName
        MakeJson.elementsList = elementsList
        MakeJson.fileName = fileName
        self.create_dir()
        self.create_file()

    @staticmethod
    def create_dir():
        if not os.path.exists(MakeJson.projectName):
            print("Creating directory" + MakeJson.projectName)
            os.makedirs(MakeJson.projectName)

    @staticmethod
    def create_file():
        k = 0
        with open('AmazonMan.json', 'r') as file:
            jsonStore = json.load(file)
            for i in range(4):
                for j in range(0, 20, 4):

                    jsonStore['content'][0]['elements'][i]['elements'][j]['settings'][
                        'html'] = MakeJson.elementsList[k][2]
                    k += 1
            k = 0
            for i in range(4):
                for j in range(1, 20, 4):
                    jsonStore['content'][0]['elements'][i]['elements'][j]['settings'][
                        'editor'] = MakeJson.elementsList[k][0]
                    k += 1
            k = 0
            for i in range(4):
                for j in range(2, 20, 4):
                    jsonStore['content'][0]['elements'][i]['elements'][j]['settings']['editor'] = MakeJson.elementsList[k][1]
                    k += 1
            k=0
            for i in range(4):
                for j in range(3, 20, 4):
                    jsonStore['content'][0]['elements'][i]['elements'][j]['settings']['link'][
                        'url'] = MakeJson.elementsList[k][3]
                    k += 1

            with open("AmazonMan.json", "w") as jsonFile:
                json.dump(jsonStore, jsonFile)




    # if filename:
    #     with open(filename, 'r') as f:
    #         datastore = json.load(f)
    # json_str = json.dumps(attr_list);
    # file_path = os.path.join(project_name, filename)
    #
    # if not os.path.isfile(file_path):
    #     write_file(file_path, json_str)