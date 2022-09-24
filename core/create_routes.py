from argparse import BooleanOptionalAction
import pandas as pd
import numpy as np 

blockgroups = open("./output/dart-bus-blockgroups.txt", "r").read()
blockgroups = eval(blockgroups)
bus_df = pd.read_csv("./data/city-of-dallas-texas-dart-bus-stops/city-of-dallas-texas-dart-bus-stops.csv")
hotspot_df = pd.read_csv("./output/hotspots-amiW=1-tamiW=1-sens=75.csv")

P_THRESHOLD = 90

def check_pScore(block):
    poverty_arr = np.array(hotspot_df.poverty_score)
    threshold = np.percentile(poverty_arr, P_THRESHOLD)
    hotspot_df[hotspot_df['block']==block]
    pass

def checkLimeable():
    pass

for blockarr in blockgroups:
    # print(blockarr)
    for block in blockarr:
        block = int(block[:-3])
        if (block in hotspot_df.blkgrp.values):
            check_pScore(block)
        else:
            checkLimeable()