# Azure Machine Learning Pipeline Sample - DatabricksStep

This repo contains a sample notebook highlighting utilization of a `DatabricksStep` in an Azure Machine Learning pipeline. Here a `FileDataset` is used as both an input and output of the `DatabricksStep` (i.e., data is read from an input set and written to an output set during execution of the Databricks notebook).

Note: Details on configuring a DatabricksStep in an Azure ML pipeline along with a sample notebook can be found [here](https://learn.microsoft.com/en-us/python/api/azureml-pipeline-steps/azureml.pipeline.steps.databricks_step.databricksstep?view=azure-ml-py). 