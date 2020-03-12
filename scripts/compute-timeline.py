#!/usr/bin/env python

import pandas as pd
from functools import reduce

def parse_csv(filename):
  return pd.read_csv(filename, parse_dates=[2], dayfirst=True)

def export_csv(frame, filename):
  with open(filename, 'w+') as f:
    return frame.to_csv(f, sep=',', encoding='utf-8')

if __name__ == '__main__':
  tests_and_confirmed = parse_csv('timeline/tests-and-confirmed.csv')
  by_situation = parse_csv('timeline/by-situation.csv')
  by_source = parse_csv('timeline/by-source.csv')
  by_region = parse_csv('timeline/by-region.csv')
  healthcare = parse_csv('timeline/healthcare-workers.csv')

  dfs = [tests_and_confirmed, by_situation, by_source, by_region, healthcare]

  totals = reduce(lambda left,right: pd.merge(left,right,on='Date'), dfs)
  print(totals)
  export_csv(totals, 'timeline/_totals.csv')

  