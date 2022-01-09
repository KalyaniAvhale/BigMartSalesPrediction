'''
# Script will params.yaml file configurations and
# load data from datasource

author : Kalyani Avhale
modefied_version : 0.0.1

'''
import os,sys
import yaml
import pandas as pd 
import argparse
import logging

#logging module
log_file_path = os.path.join("src","load_data_stage.log")

def get_logger(file_name=log_file_path):
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(file_name,mode='w')
    fh.setFormatter(formatter)
    logger.addHandler(fh)   
    return logger
    


#read params.yaml file
def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

#read data from datasource
def get_data(config_path):
    config = read_params(config_path)
    train_data_path = config['data_source']['data_source_train']
    test_data_path = config['data_source']['data_source_test']
    train = pd.read_csv(train_data_path, sep=",", encoding="utf-8")
    test = pd.read_csv(test_data_path, sep=",", encoding="utf-8")
    get_logger().info("Data Fetched from source successfully !")
    return train,test

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args = args.parse_args()
    get_data(config_path=parsed_args.config)