#!/usr/bin/env python3

import pandas as pd
import sys

histogram = pd.read_csv('output_latency.tmp', delim_whitespace=True, header=None)
histogram.columns = ['latency', 'n']

cumsum = histogram.n.cumsum()
percentiles = cumsum / cumsum[len(cumsum) - 1]

quantiles = [0.25, 0.5, 0.9, 0.99, 0.999]

q_indices = percentiles.searchsorted(quantiles)
q_latencies = pd.Series(histogram.latency[q_indices].values, index=quantiles)
print(q_latencies)
