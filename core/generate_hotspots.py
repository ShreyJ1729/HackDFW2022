import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def generate_hotspot_csv(input_filename, columns_of_interest, AMI_WEIGHT=1, T_AMI_WEIGHT=1, HOTSPOT_SENSITIVITY=75, save_image=False, save_csv=False):

    df = pd.read_csv(input_filename)

    # drop na columns
    print("df size before dropping N/A: ", len(df))
    df.dropna(axis='index', how='any', subset=columns_of_interest, inplace=True)
    print("df size after dropping N/A: ", len(df))

    # only get block groups in dallas-fort worth-arlington area
    df = df[df['cbsa'].str.contains("Dallas-Fort Worth-Arlington")]
    print("df size after filtering DFW: ", len(df))

    # calculate annual median income
    df['ami'] = df.apply(lambda row: row.t_cost_ami * 100/row.t_ami, axis=1)

    # normalize ami + transport as a percent of ami, generate heatmap
    ami = np.array(1/df.ami)
    t_ami = np.array(df.t_ami)

    ami_norm = (ami-ami.mean())/ami.std()
    t_ami_norm = (t_ami-t_ami.mean())/t_ami.std()

    # poverty score calculation + normalization + clipping
    pScore = ami**AMI_WEIGHT*t_ami**T_AMI_WEIGHT
    pScoreNorm = 0.05+1/2.5 * (pScore-pScore.mean())/(pScore.std())
    pScoreNormClip = np.clip(pScoreNorm, -1, 1)
    # pScoreNormClip = pScoreNorm

    threshold = np.percentile(pScoreNormClip, HOTSPOT_SENSITIVITY)
    exceed_threshold_indices = pScoreNormClip > threshold
    df = df.assign(poverty_score=pScoreNormClip)
    df = df.assign(hotspot=exceed_threshold_indices)
    print(sum(exceed_threshold_indices), " hotspots identified")

    if save_image:
        plt.title("Histogram of Poverty Score (Normalized + Clipped)")
        plt.xlabel("Poverty Score")
        plt.ylabel("Count")
        plt.hist(pScoreNormClip, bins=100)
        plt.savefig(f"./output/pscore-hist-amiW={AMI_WEIGHT}-tamiW={T_AMI_WEIGHT}-sens={HOTSPOT_SENSITIVITY}.png")
    
    if save_csv:
        df.to_csv(f"./output/hotspots-amiW={AMI_WEIGHT}-tamiW={T_AMI_WEIGHT}-sens={HOTSPOT_SENSITIVITY}.csv")
    
    return df    

if __name__=="__main__":
    print(generate_hotspot_csv(input_filename="./data/htaindex_data_blkgrps_48.csv",
    columns_of_interest=['blkgrp', 'cbsa', 'population', 't_cost_ami', 't_ami', 'h_cost'],
    AMI_WEIGHT=1,
    T_AMI_WEIGHT=1,
    HOTSPOT_SENSITIVITY = 75,
    save_image=True,
    save_csv=True))