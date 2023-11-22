[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/YhqNqk94)


# Project README: Data Processing & Model Selection

## Overview

This project involves data processing and model selection for a weather-related dataset. The aim is to clean and transform the data, explore feature relevance, and ultimately select an appropriate model for prediction of number of outages caused by every storm in every location (grid cell).

## Running the Project
To run the project you only need to run the makefile in the root directory of the project (this will install the requirements and run the pipeline):
```
make all
```

## Project Structure
```bash
.
├── Makefile
├── Notes
├── README.md
├── data
│   └── outage_data.parquet
├── notebooks
│   ├── 20_features.ipynb
│   ├── EDA_starter.ipynb
│   ├── feature_Corr_selection.ipynb
│   ├── feature_reducer.ipynb
│   ├── feature_seleciton_JL.ipynb
│   ├── features_2kto3k.ipynb
│   ├── pickle_files
│   │   ├── drop_cols_correlation_09.pkl
│   │   ├── drop_list.pkl
│   │   ├── drop_list_anova_cat.pkl
│   │   ├── drop_list_group.pkl
│   │   └── pearson_stat_drop_cols.pkl
│   └── rf_analyser.ipynb
├── project_requirements.md
├── requirements.txt
├── src
│   ├── __pycache__
│   │   ├── data_loader.cpython-39.pyc
│   │   ├── feature_builder.cpython-39.pyc
│   │   ├── model_builder.cpython-39.pyc
│   │   └── model_trainer.cpython-39.pyc
│   ├── data_loader.py
│   ├── feature_builder.py
│   ├── main.py
│   ├── model_builder.py
│   └── model_trainer.py
└── tree.md
```
During experimentation we used the `notebooks` folder to store all the notebooks we used to explore the data and test different approaches. 

The `src` folder contains all the code that is used in the pipeline. The `data` folder contains the data we used for the project.

- `main.py`: Contains the entry point of the pipeline.
- `data_loader.py`: Exposes a method to load the data from parquet file, perform label encoding, and return the data as a pandas dataframe.
- `feature_builder.py`: Here is the core of feature selection and splitting the data into the train and test sets based on the SimStartDate column.
- `model_builder.py`: This script was mainly used during experimentation and encapsulates the logic of instantiating and the models.
- `model_trainer.py`: In this script are the methods to train the instantiated model, make predictions and evaluate the model.



## Data Processing

### Cleaning & Transformations

1. **Initial Exploration**
   - Used `.info()` to identify data types: 3 objects, 5 datetimes & rest float/int
   - Observed there are no null values
   - Identified features with only one unique value.

2. **Data Type Conversion**
   - Converted object types to appropriate encodings.
   - Transformed datetimes into separate columns for day, month, year, and hour.

3. **Handling Features with One Value**
   - Identified features with only one value for most instances (e.g., "HOURLY_WET_SNOW_ACCUM_RATE m/h-filtered_8-min_min").
   - Removed features with limited variability.

### Manual Feature Understanding (First Attempt)

1. **Dividing Data for Manual Understanding**
   - Attempted to split data into parts for manual feature analysis by individuals.
   - Each person responsible for finding correlations and understanding feature meanings.

2. **Challenges and Conclusion**
   - Faced challenges due to the large volume of data.
   - Many features measured the same weather conditions using different metrics.
   - Decided it was impractical to manually analyze all features individually.

### Baseline Model

- Ran Lasso regression with all features.
- Obtained a sparse set of features but with high RMSE.

### Statistical Methods for Feature Selection (Second Attempt)

   a. **Numeric Features:**
      - Used Pearson correlation between float/int features and the target variable.
      - Applied Chi-Square for object features with the target.
      - Dropped features not rejecting the null hypothesis.

   b. **Correlation Between Features:**
      - Checked for high correlation (above 0.9) to identify potential multicollinearity.
      - Removed features with high correlation to reduce redundancy.

#### Conclusion

- Despite applying various statistical methods, around 400 features remained.
- The dataset was still too large for efficient modeling.

### Similarity-Based Feature Grouping (third and final attempt)

- Grouped features based on name similarity.
- Found correlations within each group and selected the feature with the highest correlation with the target.
- Remove remaining features with correlation below 0.1 against the target variable.

## Model Selection

### Experimentation findings
Since we were not satisfyed with the MAPE values that the different models we tried were giving us, we thought that this could be due to unbalance between types of storms (since different features may be associated withteach type), so we analyzed the possibility of using different models for each type of storm, however we found out that on the test set we only have data for 1 type of storm.

### Model choice: Random Forest

- We chose Random Forest Regressor as the modeling algorithm.
- Given the size of the dataset and the number of feature we were not able to run automatic hyperparameters fine-tuning (we tried GridSearchCV and RandomSearchCV).