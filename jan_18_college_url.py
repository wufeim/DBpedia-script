#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename : jan_18_college_url.py
# @Date : 2020-01-18
# @Author : Wufei Ma

import os
import sys

import json


if __name__ == '__main__':

    with open('college_list.txt', 'r') as f:
        raw = f.read()

    colleges = raw.strip().split('\n')
    print(colleges)

    college_list = [{"name": x, "url": "http://"} for x in colleges]
    s = json.dumps(college_list, indent=4)

    with open('college_list_urls.json', 'w') as f:
        f.write(s)
