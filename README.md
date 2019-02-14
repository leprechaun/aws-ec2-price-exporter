# AWS EC2 Price Exporter

## Problem statement

I'm already using [banzaicloud/aws-spot-price-exporter](banzaicloud/https://github.com/banzaicloud/spot-price-exporter) but I always want to have a metric for normal instances.

Thing is, the prices pretty much never change, so, no need to run code. We're reading CSV in this repo, courtesy of https://www.ec2instances.info, and writing a file with metrics, that we're going to server over nginx.

"Exporter" is a big word here. But it works.
