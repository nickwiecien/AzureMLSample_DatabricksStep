from azureml.core import Run
import pandas as pd 
import os
import argparse
from datetime import datetime

# Parse input arguments
parser = argparse.ArgumentParser("Databricks Test - Step One")
parser.add_argument('--input_data', dest='input_data', required=True)
parser.add_argument('--output_data', dest='output_data', required=True)

args, _ = parser.parse_known_args()
input_data = args.input_data
output_data = args.output_data

# Get current run
current_run = Run.get_context()

# Get associated AML workspace
ws = current_run.experiment.workspace

# Connect to default blob datastore
ds = ws.get_default_datastore()

kv = ws.get_default_keyvault()

# Create datasets if not exists
os.makedirs(input_data, exist_ok=True)
os.makedirs(output_data, exist_ok=True)

timestamp = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')

df = pd.DataFrame([{"A": timestamp}])
df.to_csv(os.path.join(input_data, 'input.csv'), index=False)
