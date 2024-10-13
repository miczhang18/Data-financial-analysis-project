import pandas as pd
import numpy as np
from numpy.linalg import inv


class Investment:

    def __init__(self, df):
        self.__df = df
        self.types = list(self.__df.columns)
        self.mean = df.mean(numeric_only=False)

    def __repr__(self):
        # show the data analyzed today
        rep = f'Raw returns on 6 industries in the U.S. from August 1963 to December1999.\n{self.__df}'
        return rep

    def mean(self):
        return self.mean

    def industry_name(self):
        # present all the industrial classification
        return list(self.types)

    def mvp(self):
        # this is a function which helps us get the ratio of every stock in this portfolio.
        covariance = self.__df.cov(numeric_only=False)
        array_initial = covariance.to_numpy()
        array_nd = np.linalg.inv(array_initial)
        array_mvp = ([1, 1, 1, 1, 1, 1])
        minimum_portfolio = np.matmul(array_nd, array_mvp)
        sum_mvp = np.matmul(minimum_portfolio, array_mvp)
        percent_mvp = np.divide(minimum_portfolio, sum_mvp)
        return percent_mvp


if __name__ == '__main__':

    df0 = pd.read_excel("data.xlsx")
    df1 = df0.iloc[:437, 1:]
    df_data = Investment(df1)
    df_industry = df_data.industry_name
    print(df_data)
    stock_mean = df_data.mean
    print(f'The mean returns of those stocks is \n{stock_mean}')
    percent = df_data.mvp()
    print(f'Ration of stock in portfolio is\n {percent}')
    assert np.matmul(stock_mean, percent) == 0.01198421078927915  # Confirm the final result
    print('"+" means buy in, "-" means sell out \n')
    print("Expected return of this portfolio is:")
    print("{0:.3%}".format(np.matmul(stock_mean, percent)))

