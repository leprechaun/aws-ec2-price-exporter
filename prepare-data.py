#!/usr/bin/env python3

from prometheus_client import CollectorRegistry, Gauge, write_to_textfile
import csv

registry = CollectorRegistry()
g = Gauge('aws_ec2_instance_price', 'price of individual instance types in a region', ['region', 'instance_type'], registry=registry)

regions = ["ap-southeast-1"]

for region in regions:
    with open('data/' + region + '.csv') as csvfile:
      spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
      for row in spamreader:
        if row[1] == "API Name":
          continue

        price = row[30].split(" ")[0].lstrip("$")

        if price == "unavailable":
          continue

        row = {
          "region": region,
          "instance_type": row[1],
          "price": float(price)
        }

        g.labels( region=row['region'], instance_type=row['instance_type']).set(row['price'])


write_to_textfile('metrics', registry)
