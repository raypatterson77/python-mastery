#!/usr/bin/env python

import tracemalloc
import csv

with open('Data/ctabus.csv') as f:
    tracemalloc.start()
    data = f.read()
    print(len(data))
    print(tracemalloc.get_traced_memory())
    tracemalloc.stop()

with open('Data/ctabus.csv') as f:
    tracemalloc.start()
    lines = f.readlines()
    print(len(lines))
    print(tracemalloc.get_traced_memory())
    tracemalloc.stop()

def read_rides_as_tuples(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records 

if __name__ == '__main__':
    tracemalloc.start()
    rows = read_rides_as_tuples('Data/ctabus.csv')
    print('mem use: curent %d, peak %d' % tracemalloc.get_traced_memory())