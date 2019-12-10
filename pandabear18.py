#!/usr/bin/python3
import pandas as pd
import matplotlib.pyplot as plt


def main():
    ciscocsv = pd.read_csv("ciscodata.csv")
    ciscojson = pd.read_json("ciscodata.json")
    print(ciscocsv.head())
    print(ciscojson.head())

    ciscodf = pd.concat([ciscocsv,ciscojson])
    print(ciscodf)

if __name__ == "__main__":
    main()
