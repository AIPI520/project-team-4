[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/YhqNqk94)


# Project README: Data Processing & Model Selection

## Overview

This project involves data processing and model selection for a weather-related dataset. The aim is to clean and transform the data, explore feature relevance, and ultimately select an appropriate model for prediction.

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

#### 1. Iterative Statistical Removal

   a. **Numeric Features:**
      - Used Pearson correlation between float/int features and the target variable.
      - Applied Chi-Square for object features with the target.
      - Dropped features not rejecting the null hypothesis.

   b. **Correlation Between Features:**
      - Checked for high correlation (above 0.9) to identify potential multicollinearity.
      - Removed features with high correlation to reduce redundancy.

#### 2. Grouping Features

   a. **Similarity-Based Grouping:**
      - Grouped features based on name similarity.
      - Found correlations within each group and selected the feature with the highest correlation with the target.

#### Conclusion

- Despite applying various statistical methods, around 400 features remained.
- The dataset was still too large for efficient modeling.

## Model Selection

### Random Forest

- Chose Random Forest as the modeling algorithm.
- Further steps involve fine-tuning hyperparameters and evaluating model performance.
