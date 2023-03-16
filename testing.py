import pandas as pd

actualfile = "actual_branch_sliding.csv"
predictionfile = "prediction_branch_sliding.csv"

actualreader = pd.read_csv(actualfile, usecols = ['ROLL NO.','CURRENT BRANCH','ALLOTTED BRANCH'])
predreader = pd.read_csv(predictionfile, usecols = ['ROLL NO.','CURRENT BRANCH','ALLOTTED BRANCH'])

c_result = actualreader[~actualreader.apply(tuple,1).isin(predreader.apply(tuple,1))]
print(c_result)          
            
            
