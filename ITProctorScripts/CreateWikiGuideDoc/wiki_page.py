from bs4 import BeautifulSoup


class Wiki_Page:
    # Need to be inside a requests.Session() to use these
    def __init__(self, response_object):
        self.response_object = response_object

    def print_header(self):
        soup = BeautifulSoup(self.response_object.text, "html.parser")
        div = soup.find('div', attrs={"class": "wiki_headingtitle"})
        return div.prettify()

    def print_content(self):
        soup = BeautifulSoup(self.response_object.text, "html.parser")
        div = soup.find('div', attrs={"class": "text_to_html"})
        return div.prettify()
