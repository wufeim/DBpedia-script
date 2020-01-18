#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename : main.py
# @Date : 2020-01-18
# @Author : Wufei Ma

import os
import sys

import json

import utils


if __name__ == '__main__':

    with open('college_list_urls.json', 'r') as f:
        raw = f.read()

    college_list = json.loads(raw.strip())

    output_dir = 'json'
    for c in college_list:
        spider = utils.DBpediaSpider(c['url'])
        try:
            attr = spider.get_attributes()
        except ValueError as e:
            print('Cannot retrieve attributes from {:s}: {}'
                  .format(c['name'], e))
        s = json.dumps(attr, indent=4)
        filename = os.path.join(output_dir, c['name']+'.json')
        with open(filename, 'w') as f:
            f.write(s)
        print('Saved attributes for {:s} in {:s}'.format(c['name'], filename))
