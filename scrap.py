from selenium import webdriver


def scrap_url(url, div_id):
    driver = webdriver.Chrome()

    driver.get(url)

    id_found = driver.find_element_by_id(div_id)

    elements = id_found.find_elements_by_css_selector("*")
    attr_list = get_elements(elements)
    driver.close()

    return attr_list


def get_elements(elements):

    attr_list = []
    x = ' '
    for ele in elements:

        title = ele.get_attribute("title")
        href = ele.get_attribute("href")
        image = ele.get_attribute("src")
        price = ele.get_attribute("innerText")

        if title:
            if len(title) >= 80:
                title = title[0:79] + "..."
            elif len(title) < 80:
                for i in range(80 - len(title)):
                    title = title + x
            attr_tuple = ()
            attr_tuple = attr_tuple + (title,)
            attr_tuple = attr_tuple + (price,)
        else:
            pass
        if href:
            link = href
            # href_tag = "<a href=" + link + ">"
            attr_tuple = attr_tuple + (link,)
        else:
            pass
        if image:
            # image_tag = href_tag + "<img src=" + image + ">" + "</a>"
            attr_tuple = attr_tuple + (image,)
            attr_list.append(attr_tuple)

        else:
            pass


    return attr_list
