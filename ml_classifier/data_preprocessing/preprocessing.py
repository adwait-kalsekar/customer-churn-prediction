import pandas as pd
import joblib

def load_model_data():
    model_1 = joblib.load("ml_classifier/trained_model/final_model_1.pkl")
    model_2 = joblib.load("ml_classifier/trained_model/final_model_2.pkl")
    (score_1, score_2) = joblib.load("ml_classifier/trained_model/get_scores.pkl")
    col_names = joblib.load("ml_classifier/trained_model/col_names.pkl")

    return model_1, model_2, score_1, score_2, col_names

def convert_to_int(df, column_names):
    for column_name in column_names:
        df[column_name] = df[column_name].astype(str).astype(int)
    return df

# def dummy_data(df_object_type):
#     print("Objects inside func: ", df_object_type)
#     df_object_dummies =  pd.get_dummies(df_object_type, drop_first=True)
#     print("Dummies: ", df_object_dummies)
#     return df_object_dummies

def encode_data(df, column_names):
    
    # df_object_type = df[["Geography", "Gender"]]
    # print("Objects outside func: ", df_object_type)

    # df_numeric_type = df.drop(["Geography", "Gender"], axis=1)

    # df_object_dummies = dummy_data(df_object_type)
    

    # encoded_df = pd.concat([df_numeric_type, df_object_dummies], axis=1)

    if df['Geography'][0] == 'Germany':
        df['Geography_Germany'] = 1
        df['Geography_Spain'] = 0
    elif df['Geography'][0] == 'France':
        df['Geography_Germany'] = 0
        df['Geography_Spain'] = 0
    elif df['Geography'][0] == 'Spain':
        df['Geography_Germany'] = 0
        df['Geography_Spain'] = 1
    else:
        raise Exception("Error in Geography Column")

    if df['Gender'][0] == 'Male':
        df['Gender_Male'] = 1
    elif df['Gender'][0] == 'Female':
        df['Gender_Male'] = 0
    else:
        raise Exception("Error in Gender Column")
    
    
    df = df.drop(["Gender", "Geography"], axis=1)

    df.reindex(columns=column_names)
    print(df)
    print(df.iloc[:,2])
    df = df.iloc[:,[1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    print(df)

    encoded_df = convert_to_int(df, column_names)

    return encoded_df