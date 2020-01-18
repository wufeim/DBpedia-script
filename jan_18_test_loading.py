#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename : jan_18_test_loading.py
# @Date : 2020-01-18
# @Author : Wufei Ma

import json

if __name__ == '__main__':

    with open('example_rpi.json', 'r') as f:
        raw = f.read()

    attr = json.loads(raw.strip())

    print(attr.keys())
    print(attr['dbo:wikiPageID'])
    print(attr['dbp:academicStaff'])
    print(attr['dbo:president'])
