import pandas as pd
import requests

class HTS:

    default_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
    }

    url_default = 'https://stackexchange.com/leagues/1/alltime/stackoverflow'

    # =========================================================================
    def __init__(self, url = None, headers = default_header):
        self.__url = url
        self.__headers = headers
        self.__data = None

    def __str__(self):
        return "URL='%s':table_count=%s" % (self.url, self.table_count)

    # =========================================================================
    @property
    def url(self):
        """ URL to be parsed """
        return self.__url

    @url.setter
    def url(self, the_url):
        self.__url = the_url

    @property
    def data(self):
        return self.__data

    @property
    def table_count(self):
        return len(self.__data)

    # =========================================================================
    def load(self):
        r = requests.get(self.__url, self.__headers)
        self.__data = pd.read_html(r.text)

    def get_table_content(self, table_index):
        if (table_index >= 1) and (table_index <= self.table_count):
            return self.__data[table_index -1]
        else:
            raise ValueError("Index must a positive Int between 1 and table_count.")

    def get_table_content_as_csv(self, table_index, with_index=False):
       raw_data = self.get_table_content(table_index)
       return raw_data.to_csv(with_index)
