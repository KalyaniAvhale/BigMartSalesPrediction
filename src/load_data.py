'''
# Script will read data from source and 
# save it to data/raw for further processing

author : Kalyani Avhale
modefied_version : 0.0.1

'''
import os
import pandas as pd 
import argparse
from get_data import read_params, get_data, get_logger


#load and save data from source to data/raw dir
def load_and_save(config_path):
    config = read_params(config_path)
    train , test = get_data(config_path)

    raw_train_path = config["load_data"]["raw_train_csv"]
    raw_test_path = config["load_data"]["raw__test_csv"]

    train.to_csv(raw_train_path, sep=",", index=False)
    test.to_csv(raw_test_path, sep=",", index= False)
    get_logger().info("Data loaded and saved Successfully to : ")
    get_logger().info("Train : "+raw_train_path)
    

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args = args.parse_args()
    load_and_save(config_path=parsed_args.config)