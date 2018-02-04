import requests
from bs4 import BeautifulSoup

from wiki_page import Wiki_Page
import doc_maker

if __name__ == "__main__":
    url_login = r"http://moodle.casb.com/login/index.php"
    #  Enter credentials here
    payload = {'username': 'YOUR_USERNAME', 'password': 'YOUR_PASSWORD'}
    url_map_page = r"http://moodle.casb.com/mod/wiki/map.php?pageid=204"
    session = requests.Session

    with requests.Session() as s:
        p = s.post(url_login, data=payload)

        # An authorised request to the map of all wiki links
        r = s.get(url_map_page)

        soup = BeautifulSoup(r.text, 'html.parser')

        # Find all the links on the map page and store them in an list
        # I know that the links I want are in the td elements on the webpage
        list_wiki_links = []
        for td in soup.find_all('td'):
            link = td.a
            if(link is not None):
                list_wiki_links.append(link.get('href'))

        # Create an Wiki_Page object for every page and store in a list
        list_wiki_page_objects = []

        total = len(list_wiki_links)
        print("There are {0} links to process".format(total))
        for wiki_link in list_wiki_links:
            r = s.get(wiki_link)
            list_wiki_page_objects.append(Wiki_Page(r))
            print(wiki_link)

    content = ""
    for wiki_object in list_wiki_page_objects:
        content += r"<hr>"
        content += wiki_object.print_header()
        content += wiki_object.print_content()

    doc_maker.maker("ITWiki", content)
