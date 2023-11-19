import pandas as pd
import math
from difflib import SequenceMatcher

import warnings
warnings.filterwarnings('ignore')

class FeatureBuilder:

    """
    This function filters the best features from the dataframe.
    It groups similar features together and selects the best feature from each group.
    The best feature is the one that has the highest correlation with the target variable.
    
    Parameters:
    df (DataFrame): The input dataframe
    
    Returns:
    X_train (DataFrame): The training data
    X_test (DataFrame): The test data
    y_train (Series): The target variable for the training data
    y_test (Series): The target variable for the test data
    selected_feats (list): The list of selected features
    """
    @staticmethod
    def filter_best_features(df):
        train_df_total = df.loc[df['SimStartDate'] < '2018-11-01']
        test_df_total = df.loc[df['SimStartDate'] >= '2018-11-01']

        X_train_SimStartDate = train_df_total['SimStartDate']
        X_test_SimStartDate = test_df_total['SimStartDate']

        train_df_total = FeatureBuilder._convert_date_columns(train_df_total)
        test_df_total = FeatureBuilder._convert_date_columns(test_df_total)
        df = FeatureBuilder._convert_date_columns(df)

        groups = FeatureBuilder._group_features(df.columns.unique().tolist())
        selected_features = [FeatureBuilder._get_best_feature_from_group(group, df) for group in groups]

        train_df = train_df_total[selected_features]
        test_df = test_df_total[selected_features]

        # Use all data after Nov 1, 2018 (15 storms) as test set
        # test_df = df[selected_features].loc[(df['SimStartDate_year'] > 2018) | 
        #                                      ((df['SimStartDate_year'] == 2018) & (df['SimStartDate_month'] > 11)) |
        #                                      ((df['SimStartDate_year'] == 2018) & (df['SimStartDate_month'] == 11) & (df['SimStartDate_day'] >= 1))]
       
        # train_df = df[selected_features].loc[(df['SimStartDate_year'] < 2018) | 
        #                                       ((df['SimStartDate_year'] == 2018) & (df['SimStartDate_month'] < 11)) |
        #                                       ((df['SimStartDate_year'] == 2018) & (df['SimStartDate_month'] == 11) & (df['SimStartDate_day'] < 1))]        

        X_train = train_df.drop(['outage_count'], axis=1)
        y_train = train_df['outage_count']

        X_test = test_df.drop(['outage_count'], axis=1)
        y_test = test_df['outage_count']

        return X_train, X_test, y_train, y_test, selected_features, X_train_SimStartDate, X_test_SimStartDate

    @staticmethod
    def remove_one_value_features(df):
        one_value_features_list = []
        for column in df.columns:
            if df[column].nunique() == 1:
                one_value_features_list.append(column)

        df.drop(one_value_features_list, axis=1, inplace=True)
        return df

    """
    This function groups similar features together.
    Similarity is calculated as a % using the SequenceMatcher from difflib.
    """
    @staticmethod
    def _group_features(features, similarity_threshold=80):
        groups = []
        used_indices = set()

        for i, f1 in enumerate(features):
            if i in used_indices:
                continue

            # This will be a new group
            current_group = [f1]
            used_indices.add(i)

            for j, f2 in enumerate(features):
                if j in used_indices or i == j:
                    continue

                # Calculate similarity
                similarity = SequenceMatcher(None, f1, f2).ratio() * 100
                if similarity > similarity_threshold:
                    current_group.append(f2)
                    used_indices.add(j)
            
            groups.append(current_group)

        return groups

    """
    This function selects the best feature from a group using the correlation with the target variable.
    """
    @staticmethod
    def _get_best_feature_from_group(group, df):
        if len(group) > 1:
            highest_corr = -math.inf
            for feat in group:
                corr = abs(df['outage_count'].corr(df[feat]))
                if(math.isnan(corr)):
                    corr = 0
                if corr > highest_corr:
                    highest_corr = corr
                    selected_feature = feat

            if highest_corr == 0:
                print('Selected feature: ', selected_feature, ' with correlation: ', highest_corr)
           
            return selected_feature
        else:
            print('Selected feature: ', group[0])
            return group[0]
        
    @staticmethod
    def _convert_date_columns(df):
        datetime_features = list(df.select_dtypes(include = "datetime64[ns, UTC]").columns)
        for i in datetime_features:
            df[i+"_year"] = df[i].dt.year
            df[i+"_month"] = df[i].dt.month
            df[i+"_day"] = df[i].dt.day
            df[i+"_hour"] = df[i].dt.hour
            
        df.drop(columns = datetime_features, inplace = True)

        return df
