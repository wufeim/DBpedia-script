#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename : clean_city.py
# @Date : 2020-01-26
# @Author : Wufei Ma

import os
import sys

import json

import numpy as np
import pandas as pd

import utils
from parseRules import *


def intersection(l1, l2):
    return [x for x in l1 if x in l2]


if __name__ == '__main__':

    save_dir = os.path.join('json_city')
    json_files = [x for x in os.listdir(save_dir) if x.endswith('.json')]
    print(
        'Found {:d} JSON file(s) from {:s}.'.format(len(json_files), save_dir))

    keys = None
    keys_count = {}
    for file in json_files:
        with open(os.path.join(save_dir, file), 'r') as f:
            raw = f.read()
        attr = json.loads(raw.strip())
        for k in attr.keys():
            if k in keys_count.keys():
                keys_count[k] += 1
            else:
                keys_count[k] = 1
        if keys is None:
            keys = list(attr.keys())
        else:
            keys = intersection(keys, list(attr.keys()))
    print('Found {:d} shared keys:'.format(len(keys)))
    print(keys)
    print('Full keys list:')
    sorted_keys = [k for k, v in
                   sorted(keys_count.items(), key=lambda item: item[1],
                          reverse=True)]
    for k in sorted_keys:
        print(k, keys_count[k])

    keys = [
        'name',
        # 'areaCode',
        # 'type',
        # 'timeZone',
        'areaTotal',
        'areaLand',
        'areaWater',
        'populationTotal',
        'populationDensity',
        'popPlaceByArea',
        'elevation',
        # 'governmentType'
    ]
    df = pd.DataFrame(columns=keys)
    for file in json_files:
        with open(os.path.join(save_dir, file), 'r') as f:
            raw = f.read()
        attr = json.loads(raw.strip())
        info = {
            'name': file[:-5],
            # 'areaCode': parse_areaCode(attr['dbo:areaCode'] if 'dbo:areaCode' in attr else None),
            # 'type': parse_cityType(attr['dbo:type'] if 'dbo:type' in attr else None),
            # 'timeZone': parse_timezone(attr['dbo:timeZone'] if 'dbo:timeZone' in attr else None),
            'areaTotal': parse_cityAreaTotal(attr['dbo:areaTotal'] if 'dbo:areaTotal' in attr else None),
            'areaLand': parse_cityAreaLand(attr['dbo:areaLand'] if 'dbo:areaLand' in attr else None),
            'areaWater': parse_cityAreaWater(attr['dbo:areaWater'] if 'dbo:areaWater' in attr else None),
            'populationTotal': parse_cityPopulation(attr['dbo:populationTotal'] if 'dbo:populationTotal' in attr else None),
            'populationDensity': parse_cityPopulationDensity(attr['dbo:populationDensity'] if 'dbo:populationDensity' in attr else None),
            'popPlaceByArea': parse_cityPopPlaceByArea(attr['dbo:PopulatedPlace/areaTotal'] if 'dbo:PopulatedPlace/areaTotal' in attr else None),
            'elevation': parse_cityElevation(attr['dbo:elevation'] if 'dbo:elevation' in attr else None),
            # 'governmentType': parse_cityGovernment(attr['dbo:governmentType'] if 'dbo:governmentType' in attr else None),
        }
        df = df.append(info, ignore_index=True)
    print(df.head())
    df.to_csv('city.csv')
