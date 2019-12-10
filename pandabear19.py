#!/usr/bin/python3
import pandas as pd
import matplotlib.pyplot as plt


def main():
    ciscocsv = pd.read_csv("ciscodata.csv")
    ciscojson = pd.read_json("ciscodata.json")
    ciscodf = pd.concat([ciscocsv, ciscojson], ignore_index=True, sort=False)


if __name__ == "__main__":
    main()
