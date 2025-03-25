import pandas as pd
def row_correlation(df, top_n=10):
    copy=df.copy()
    drop=copy['Team/Year']
    copy=copy.drop('drop',axis=1)
    target_row=copy.loc[int(input())]
    correlations=copy.apply(lambda row: row.corr(target_row), axis=1)
    copy['Team/Year']=drop
    top10=correlations.abs().nlargest(top_n)
    return correlations.loc[top10.index]