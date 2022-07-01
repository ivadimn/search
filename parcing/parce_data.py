from pprint import pprint
from bs4 import BeautifulSoup
import re


def parce() -> None:
    with open("blank/index.html", "r") as f:
        text = f.read()
    soup = BeautifulSoup(text, "lxml")

    #title = soup.title
    #print(title)
    #print(title.text)

    #h1 = soup.find("h1")
    #print(h1)

    user_name = soup.find("div", {"class": "user__name", "id": "aaa"}).find("span")
    print(user_name.text)

    all_user_info = soup.find("div", {"class": "user__info"}).find_all("span")

    for item in all_user_info:
        print(item.text)

    all_a = soup.find_all("a")
    for item in all_a:
        item_text = item.text
        href = item.get("href")
        print("{0} - {1}".format(item_text, href))

    #post_div = soup.find(class_ = "post__text").find_parent()
    #print(post_div)

    #post_div = soup.find(class_="post__text").find_parent("div", class_= "user__post")
    #pprint(post_div)

    #post_divs = soup.find(class_="post__text").find_parents("div", class_="user__post")
    #pprint(post_divs)

    #next_e = soup.find(class_ = "post__title").next_element.next_element
    #print(next_e)

    next_e = soup.find(class_="post__title").find_next()
    #print(next_e)

    next_sib = soup.find(class_="post__title").find_next_sibling()
    #print(next_sib)

    prev_sib = soup.find(class_="post__date").find_previous_sibling()
    #print(prev_sib)

    post_title = soup.find(class_="post__date")\
        .find_previous_sibling().find_next().text
    #print(post_title)

    all_a = soup.find(class_ = "some__links").find_all("a")
    for item in all_a:
        href_attr = item.get("href")
        data_attr = item.get("data-attr")
        print("{0} {1}".format(href_attr, data_attr))

    find_by_text = soup.find("a", text=re.compile("Clothes"))
    print(find_by_text)

    find_all_clothes = soup.find_all(text=re.compile("[Cc]lothes"))
    print(find_all_clothes)