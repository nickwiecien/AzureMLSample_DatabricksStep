from azureml.core import Run
import pandas as pd 
import os
import argparse

# Parse input arguments
parser = argparse.ArgumentParser("Databricks Test - Step Three")

args, _ = parser.parse_known_args()

# Get current run
current_run = Run.get_context()

# Get associated AML workspace
ws = current_run.experiment.workspace

# Connect to default blob datastore
ds = ws.get_default_datastore()

for f in os.listdir('./output_data'):
    print(f)

output_df = pd.read_csv(f'./output_data/output.csv')
print(output_df)