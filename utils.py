#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename : utils.py
# @Date : 2020-01-16
# @Author : Wufei Ma

import requests
from bs4 import BeautifulSoup

import json


class DBpediaSpider(object):

    def __init__(self, db_url):
        self.db_url = db_url

    def get_attributes(self):
        ret = requests.get(self.db_url)
        soup = BeautifulSoup(ret.content, 'html.parser')
        # print(soup.prettify())
        table = soup.find_all("table", {"class": "description table table-striped"})
        if len(table) == 0:
            raise ValueError("Description table not found.")
        else:
            table = table[0]

        entries = table.find_all("tr")

        attr_table = dict()
        for entry in entries:
            attr, value = self.parse_entry(entry)
            if attr is None or value is None:
                continue
            attr_table[attr] = value

        return attr_table

    def parse_entry(self, entry):
        tds = entry.find_all("td")
        if len(tds) == 0:
            return None, None

        # Get attribute name and value
        attr = tds[0].a.get_text().strip()
        value_entries = tds[1].find_all("li")

        special_cases = [
            'dbo:abstract',
            'rdfs:comment',
            'rdfs:label'
        ]

        if attr in special_cases:
            value = tds[1].find("span",
                                {"property": attr,
                                 "xml:lang": "en"})
            if value is not None:
                value = value.get_text().strip()
        else:
            value = [self.parse_attr_value(x) for x in value_entries]

        return attr, value

    def parse_attr_value(self, li):
        smalls = [x.get_text().strip() for x in li.find_all("small")]
        if '(xsd:integer)' in smalls:
            li.small.decompose()
            return int(li.get_text().strip())
        elif '(xsd:float)' in smalls:
            li.small.decompose()
            return float(li.get_text().strip())
        return li.get_text().strip()


if __name__ == '__main__':

    example_url_rpi = 'http://dbpedia.org/page/Rensselaer_Polytechnic_Institute'
    json_file = 'example_rpi.json'

    spider = DBpediaSpider(example_url_rpi)
    attrs = spider.get_attributes()

    # Save attr to file
    s = json.dumps(attrs, indent=4)
    with open(json_file, 'w') as f:
        f.write(s)
