import pandas as pd

def get_data(path):
    return pd.read_csv(path)

def main():
    path = 'dataset/cancer_wisconsin.csv'
    transformed_df = get_data(path)

    to_drop = transformed_df.columns[transformed_df.isna().all()]
    transformed_df = transformed_df.drop(to_drop, axis=1)
    transformed_df = transformed_df.drop(['id'], axis=1)

    for i in  range(len(transformed_df)):
        if transformed_df.loc[i, 'diagnosis'] == "B":
            transformed_df.loc[i, 'diagnosis'] = 0
        if transformed_df.loc[i, 'diagnosis'] == "M":
            transformed_df.loc[i, 'diagnosis'] = 1

    print(transformed_df.head(5))

    file = open('dataset/rebuilded_cancer_wisconsin.csv', 'w')   
    file.write(transformed_df.to_csv(index=False))
    file.close()

    
if __name__ in '__main__':
    main()
