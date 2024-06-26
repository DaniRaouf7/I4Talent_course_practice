from i4talent_practice import pandas

def read_data(datapath: str) -> pd.DataFrame:
    return pd.read_csv(datapath)


def drop_irrelevant_column(df: pd.DataFrame, cols_list: list[str]) -> pd.DataFrame:
    return df.drop(columns=cols_list)


def get_final_dataframe(datapath: str) -> pd.DataFrame:
    return(read_data(datapath)
           .pipe(drop_irrelevant_column, ['Name', 'PassengerId'])
          )