#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename : parseRules.py
# @Date : 2020-01-26
# @Author : Wufei Ma

import os
import sys

import numpy as np
import pandas as pd


def parse_endowment(x):
    x = x[0]
    val, power = x.split('E')
    return int(float(val) * np.power(10, int(power)))


def parse_numPostGrad(x):
    return int(x[0])


def parse_numUnderGrad(x):
    return int(x[0])


def parse_geoPoint(x):
    return tuple(map(float, x[0].split()))


def parse_city(x):
    if x is None:
        return ''
    else:
        return x[0].split(':')[1]


def parse_type(x):
    if x is None:
        return ''
    else:
        return x[0].split(':')[1]


def parse_numStudents(x):
    if x is None:
        return -1
    else:
        return int(x[0])


def parse_arwuw(x):
    if x is None:
        return -1
    else:
        return int(x[0])


def parse_qsw(x):
    if x is None:
        return -1
    else:
        return int(x[0])


def parse_state(x):
    if x is None:
        return ''
    else:
        return x[0].split(':')[1]


def parse_forbes(x):
    if x is None:
        return -1
    else:
        return int(x[0])


def parse_thesw(x):
    return int(x[0]) if x is not None else -1


def parse_usnwrnu(x):
    return int(x[0]) if x is not None else -1


def parse_usnwrw(x):
    return int(x[0]) if x is not None else -1


def parse_wamonu(x):
    return int(x[0]) if x is not None else -1


def parse_facultySize(x):
    return int(x[0]) if x is not None else -1


def parse_campus(x):
    return x if x is not None else ''


def parse_areaCode(x):
    return x[0] if x is not None else ''


def parse_cityType(x):
    return x[0].split(':')[1] if x is not None else ''


def parse_timezone(x):
    return x[0].split(':')[1] if x is not None else ''


def parse_cityAreaTotal(x):
    return float(x[0].split()[0]) if x is not None else -1.0


def parse_cityAreaLand(x):
    return float(x[0].split()[0]) if x is not None else -1.0


def parse_cityAreaWater(x):
    return float(x[0].split()[0]) if x is not None else -1.0


def parse_cityPopulation(x):
    return int(x[0]) if x is not None else -1


def parse_cityPopulationDensity(x):
    return float(x[0].split()[0]) if x is not None else -1.0


def parse_cityPopPlaceByArea(x):
    return float(x[0]) if x is not None else -1.0


def parse_cityElevation(x):
    return float(x[0].split()[0]) if x is not None else -1.0


def parse_cityGovernment(x):
    return x[0].split(':')[1] if x is not None else ''


if __name__ == '__main__':

    print(['1.002E9'], parse_endowment(['1.002E9']))
    print([19000], parse_numPostGrad([19000]))
    print([48000], parse_numUnderGrad([48000]))
    print(['40.501666666666665 -74.44805555555556'], parse_geoPoint(['40.501666666666665 -74.44805555555556']))
    print(["dbr:Boston"], parse_city(["dbr:Boston"]))
    print(["dbr:Private_university"], parse_type(["dbr:Private_university"]))
    print([32551], parse_numStudents([32551]))
    print(["dbr:Massachusetts"], parse_state(["dbr:Massachusetts"]))
