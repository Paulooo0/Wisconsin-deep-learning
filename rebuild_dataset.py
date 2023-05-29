import pandas as pd
import numpy as np

def main():
    def get_data(path):
        df = pd.read_csv(path)
        return df

    path = 'C:/Users/paulo/Data/dataset/cancer_wisconsin.csv'
    transformed_df = get_data(path)

    to_drop = transformed_df.columns[transformed_df.isna().all()]
    transformed_df = transformed_df.drop(to_drop, axis=1)

    # Transform strings to numerical data, seen in data analysis
    for i in  range(len(transformed_df)):
        if transformed_df.loc[i, 'diagnosis'] == "B":
            transformed_df.loc[i, 'diagnosis'] = 0
        if transformed_df.loc[i, 'diagnosis'] == "M":
            transformed_df.loc[i, 'diagnosis'] = 1
    
    # Logarithmic transformation for the columns also seen in data analysis
    for i in range(len(transformed_df)):
        transformed_df.loc[i, 'area_mean'] = np.log(transformed_df.loc[i, 'area_mean'])
        transformed_df.loc[i, 'compactness_mean'] = np.log(transformed_df.loc[i, 'compactness_mean'])*-1
        transformed_df.loc[i, 'concavity_mean'] = np.log(transformed_df.loc[i, 'concavity_mean'])*-1
        transformed_df.loc[i, 'concave points_mean'] = np.log(transformed_df.loc[i, 'concave points_mean'])*-1
        transformed_df.loc[i, 'compactness_se'] = np.log(transformed_df.loc[i, 'compactness_se'])*-1
        transformed_df.loc[i, 'concavity_se'] = np.log(transformed_df.loc[i, 'concavity_se'])*-1
        transformed_df.loc[i, 'symmetry_se'] = np.log(transformed_df.loc[i, 'symmetry_se'])*-1
        transformed_df.loc[i, 'area_worst'] = np.log(transformed_df.loc[i, 'area_worst'])

    print(transformed_df.head(5))

    # Write a new dataset with transformed values
    file = open('dataset/rebuilded_cancer_wisconsin.csv', 'w')   
    file.write(transformed_df.to_csv(index=False))
    file.close()

    
if __name__ in '__main__':
    main()
