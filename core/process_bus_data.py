import pandas as pd
import requests
import json

def main():
    df = pd.read_csv("./data/city-of-dallas-texas-dart-bus-stops/city-of-dallas-texas-dart-bus-stops.csv")

    def get_url_req(lat, lon):
        return f"https://geo.fcc.gov/api/census/area?lat={lat}&lon={lon}&censusYear=2020&format=json"


    index2block = [[] for i in range(len(df))]
    for i, row in enumerate(tqdm(df.iterrows(), total=len(df))):
        url = get_url_req(row[1].shape_Y, row[1].shape_X)
        res = requests.get(url)
        res = json.loads(res.text)
        blocks = [i['block_fips'] for i in res['results']]
        for block in blocks:
            index2block[i].append(block)

    print(index2block, file=open("./output/dart-bus-blockgroups.txt", "w+"))

# if __name__=="__main__":
    # main()