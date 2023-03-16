import csv
import pandas as pd

actualfile = "actual_branch_sliding.csv"
predictionfile = "prediction_branch_sliding.csv"

actualreader = pd.read_csv(actualfile, usecols = ['ROLL NO.','CURRENT BRANCH','ALLOTTED BRANCH'])
predreader = pd.read_csv(predictionfile, usecols = ['ROLL NO.','CURRENT BRANCH','ALLOTTED BRANCH'])

with open('data_diff.csv', 'w') as outFile:    
    for row in actualreader:
        if row not in predreader:
            outFile.write(row)
            
            