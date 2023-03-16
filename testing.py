import csv
import pandas as pd

actualfile = "actual_branch_sliding.csv"
predictionfile = "prediction_branch_sliding.csv"

actualreader = csv.reader(actualfile,)