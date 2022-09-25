# def checkLimeable(block_number, longitude, latitude, LIME_LAT= 0.005, LIME_LONG = 0.003):
#     #use gmaps api to find center of block and run checkLimeable on those coordinates
#     noLimes = 0
#     noBuses = 0
#     listArr = [[type_station, block_id, stop_id]]
#     closest_stop_id = findClosestStation(longitude, latitude)
#     for longi in bus_df.shape_X.values:
#         if (longitude + LIME_LONG >= longi or longitude - LIME_LONG <= longi):
#             latitude = bus.df.shape_Y.values[longi]
#             if(latitude + LIME_LAT >= lat or latitude - LIME_LONG <= lat):
#                     listArr.append(["Lime", block_number,closest_stop_id])
#                     noLimes+=1
#         else: 
#             listArr.append(["Bus", block_number, closest_stop_id])
#             noBuses+=1

import pandas as pd
import math
import numpy as np 

blockgroups = open("./output/dart-bus-blockgroups.txt", "r").read()
blockgroups = eval(blockgroups)
bus_df = pd.read_csv("./data/city-of-dallas-texas-dart-bus-stops/city-of-dallas-texas-dart-bus-stops.csv")
hotspot_df = pd.read_csv("./output/hotspots-amiW=1-tamiW=1-sens=75.csv")
pop = pd.read_csv("./data/htaindex_data_blkgrps_48.csv")
pop = pop.population

P_THRESHOLD = 90

def check_pScore(block):
    poverty_arr = np.array(hotspot_df.poverty_score)
    threshold = np.percentile(poverty_arr, P_THRESHOLD)
    row = hotspot_df[hotspot_df['blkgrp']==block]
    if row.iloc[0].poverty_score > threshold:
        checkLimeablewithTract(block, )

def checkLimeablewithTract(block):
    tract_hotspot = str(block)[5:]
    block_group = str(block)[-5:]
    for i in range(len(blockgroups)):
        blocks = blockgroups[i]
        for block in blocks:
            tract_bus = block[5:-3]
            if tract_bus==tract_hotspot:
                return True
    return False

def distance(lat1, lat2, long1, long2):
    return math.sqrt((lat1-lat2)**2+(long1-long2)**2)
                    
                    
def findClosestStation(longitude, latitude):
    mindist = distance(latitude, bus_df.iloc[0].shape_Y, longitude, bus_df.iloc[0].shape_X)
    min_stopid = bus_df.iloc[0].stop_id
    
    for i in range(len(bus_df)):
        dist = distance(latitude, bus_df.iloc[i].shape_Y, longitude, bus_df.iloc[i].shape_X)
        if dist<mindist:
            mindist = dist
            min_stopid = bus_df.iloc[i].stop_id
    return min_stopid

def create_routes(blockgroups, bus_df, hotspot_df, pop, P_THRESHOLD=90):
    routes = [["type", "blockId", "stopId"]]
    for i in range(len(blockgroups)):
        blockarr = blockgroups[i]
        # print(blockarr)
        for block in blockarr:
            block = int(block[:-3])
            if (block in hotspot_df.blkgrp.values):
                check_pScore(block)
            else:
                if checkLimeablewithTract(block, ):
                    # add lime bus
                    routes.append(["lime-bus", block, bus_df.iloc[i].stop_id])
                else:
                    # bus rerouting
                    routes.append(["bus", block])
    return routes

routes = create_routes(blockgroups, bus_df, hotspot_df, pop)

print(len(routes))
with open("./output/routes.csv", "w+") as f:
    for i in range(len(routes)):
        f.write(",".join(map(str, routes[i])).lstrip("[").rstrip("]"))
        f.write("\n")

