import csv
import json
import pandas as pd

file = r'D:\DSI\DATA\DSIdb\KTB_Finish\1-9813038675\2561.01-2561.05_finish.csv'
json_file = r"D:\DSI\DATA\DSIdb\KTB_Finish\1-9813038675\longplianfile.json"

print((pd.read_csv(file)).head())
