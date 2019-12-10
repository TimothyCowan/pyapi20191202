#!/usr/bin/python3
import pandas as pd
import matplotlib.pyplot as plt


def main():
    excel_file = 'datasets/movies.xls'
    movies = pd.read_excel(excel_file)
    # print(movies.head())
    movies_sheet1 = pd.read_excel(excel_file, sheet_name=0, index_col=0)
    # print(movies_sheet1.head())
    movies_sheet2 = pd.read_excel(excel_file, sheet_name=1, index_col=0)
    # print(movies_sheet2.head())
    movies_sheet3 = pd.read_excel(excel_file, sheet_name=2, index_col=0)
    # print(movies_sheet3.head())

    movies = pd.concat([movies_sheet1, movies_sheet2, movies_sheet3])
    print(movies.shape)

    sorted_by_gross = movies.sort_values(["Gross Earnings"], ascending=False)
    print(sorted_by_gross.head(10))

    sorted_by_gross['Gross Earnings'].head(10).plot(kind='barh')
    plt.savefig('stackbar.png')


if __name__ == "__main__":
    main()
