#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename : clean.py
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

    save_dir = os.path.join('json')
    json_files = [x for x in os.listdir(save_dir) if x.endswith('.json')]
    print('Found {:d} JSON file(s) from {:s}.'.format(len(json_files), save_dir))

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
    sorted_keys = [k for k, v in sorted(keys_count.items(), key=lambda item: item[1], reverse=True)]
    for k in sorted_keys:
        print(k, keys_count[k])

    # Prepare city info
    city_df = pd.read_csv(os.path.join('city.csv'), index_col=0)
    print(city_df.head())
    city_list = list(city_df['name'])

    print(city_df.loc[city_df['name'] == 'Seattle']['areaTotal'].values[0])

    # Create dataframe with shared keys.
    keys = [
        'name',
        'endowment',
        'geoPoint',
        'state',
        'city',
        'type',
        'campus',
        'facultySize',
        'numOfPostGrad',
        'numOfUnderGrad',
        'numOfStudents',
        'arwuW',
        'qsW',
        'forbes',
        'thesW',
        'usnwrNu',
        'usnwrW',
        'wamoNu',
        'city_areaTotal',
        'city_areaLand',
        'city_areaWater',
        'city_populationTotal',
        'city_populationDensity',
        'city_popPlaceByArea',
        'city_elevation'
    ]
    df = pd.DataFrame(columns=keys)
    for file in json_files:
        with open(os.path.join(save_dir, file), 'r') as f:
            raw = f.read()
        attr = json.loads(raw.strip())
        city = parse_city(attr['dbo:city'] if 'dbo:city' in attr else None)
        info = {
            'name': file[:-5],
            'endowment': parse_endowment(attr['dbo:endowment']),
            'numOfPostGrad': parse_numPostGrad(attr['dbo:numberOfPostgraduateStudents']),
            'numOfUnderGrad': parse_numUnderGrad(attr['dbo:numberOfUndergraduateStudents']),
            'geoPoint': parse_geoPoint(attr['georss:point']),
            'city': parse_city(attr['dbo:city'] if 'dbo:city' in attr else None),
            'type': parse_type(attr['dbo:type'] if 'dbo:type' in attr else None),
            'numOfStudents': parse_numStudents(attr['dbo:numberOfStudents'] if 'dbo:numberOfStudents' in attr else None),
            'arwuW': parse_arwuw(attr['dbp:arwuW'] if 'dbp:arwuW' in attr else None),
            'qsW': parse_qsw(attr['dbp:qsW'] if 'dbp:qsW' in attr else None),
            'state': parse_state(attr['dbo:state'] if 'dbo:state' in attr else None),
            'forbes': parse_forbes(attr['dbp:forbes'] if 'dbp:forbes' in attr else None),
            'thesW': parse_thesw(attr['dbp:thesW'] if 'dbp:thesW' in attr else None),
            'usnwrNu': parse_usnwrnu(attr['dbp:usnwrNu'] if 'dbp:usnwrNu' in attr else None),
            'usnwrW': parse_usnwrw(attr['dbp:usnwrW'] if 'dbp:usnwrW' in attr else None),
            'wamoNu': parse_wamonu(attr['dbp:wamoNu'] if 'dbp:wamoNu' in attr else None),
            'facultySize': parse_facultySize(attr['dbo:facultySize'] if 'dbo:facultySize' in attr else None),
            'campus': parse_campus(attr['dbo:campus'] if 'dbo:campus' in attr else None),
            'city_areaTotal': city_df.loc[city_df['name'] == city]['areaTotal'].values[0] if city in city_list else -1.0,
            'city_areaLand': city_df.loc[city_df['name'] == city]['areaLand'].values[0] if city in city_list else -1.0,
            'city_areaWater': city_df.loc[city_df['name'] == city]['areaWater'].values[0] if city in city_list else -1.0,
            'city_populationTotal': city_df.loc[city_df['name'] == city]['populationTotal'].values[0] if city in city_list else -1,
            'city_populationDensity': city_df.loc[city_df['name'] == city]['populationDensity'].values[0] if city in city_list else -1.0,
            'city_popPlaceByArea': city_df.loc[city_df['name'] == city]['popPlaceByArea'].values[0] if city in city_list else -1.0,
            'city_elevation': city_df.loc[city_df['name'] == city]['elevation'].values[0] if city in city_list else -1.0
        }
        df = df.append(info, ignore_index=True)
    print(df.head())
    df.to_csv('college.csv')
