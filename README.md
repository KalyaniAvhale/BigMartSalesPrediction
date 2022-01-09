# Sales Prediction for Big Mart Outlets

### Use Case : 
The data scientists at BigMart have collected 2013 sales data for 1559 products across 10 stores in different cities. Also, certain attributes of each product and store have been defined. The aim is to build a predictive model and predict the sales of each product at a particular outlet.

Using this model, BigMart will try to understand the properties of products and outlets which play a key role in increasing sales.

## Dataset 
import Kaggle dataset from Kaggle platform

```
 import kaggle
 !kaggle datasets download -d brijbhushannanda1979/bigmart-sales-data
```
After this setup your vscode with virtual env and create directory structure with script [template.py](BigMartSalesPrediction/template.py)

Then setup git and dvc with below commands :

```
git init
dvc init
dvc add data/data_given
git add .
git commit -m "Project structure created"
```
Create git repository in github and follow the commands displayed for pushing existing project 

- params.yaml : Create a file to track parameters and hyperparameters associated with the ML experiments

- dvc.yaml : Define Pipeline stages and to reproduce complete or partial pipeline execute below command 

```
dvc repro 
```  

## Stage 1 : Load and Save Data 

- get_data.py : Script will fetch the data from datasource(here data is manually stored under data/data_given dir)

- load_data.py : Script will load and save the dataset files under data/raw dir for further processing 


