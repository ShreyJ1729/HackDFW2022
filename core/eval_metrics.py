import pandas as pd

pop = pd.read_csv("./output/hotspots-amiW=1-tamiW=1-sens=75.csv")
pop=pop.reset_index()
def findPop(block_id):
    for index,row in pop.iterrows():
        print(pop.index.row)
        #if block_id == :
          #  print(pop[index+3][row])
findPop(481130190462)
def evalMetric(block_id):
results = pd.read_csv("./output/routes.csv")
results = results.blockId
safety = []
carbon = []
impact = []
def populateEvalMetrics(block_id):
    global safety, carbon, impact
    safety_score = 67
    carbon_footprint = pop[pop['blkgrp']==bl]
    print(carbon_footprint)
    carbon_footprint = carbon_footprint * 0.01 / 3
    safety.append(safety_score)
    carbon.append(carbon_footprint)
     impact = impact.append(pop.population.values[block_id])

    
for entry in results:
   populateEvalMetrics(entry)
results['Safety'] = safety
results['Carbon'] = carbon
results['Impact'] = impact 
    

