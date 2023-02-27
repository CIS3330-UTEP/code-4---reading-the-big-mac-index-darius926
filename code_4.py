import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df= pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    query = f"(iso_a3 == '{country_code.upper()}' and date >= {year}-01-01 and date <= {year}-12-31)"
    result_df = df.query(query)
    result = round(result_df, input,2)

def get_big_mac_price_by_country(country_code):
    query= f"(iso_a3 == '{KOR.upper()}')
    result_df = df.query(query)
    result=(round(krw_df ['dollar_price'].mean(),2))


def get_the_cheapest_big_mac_price_by_year(year):
    query = f"(date >= {2008}-01-01 and date <= {2008}-12-31)"
    result_df = df.query(query)
    result = round(result_df, input,2)
    min_idx= (MYR_df ['dollar_price'].idxmin())

def get_the_most_expensive_big_mac_price_by_year(year):
    query = f"(date >= {2003}-01-01 and date <= {2003}-12-31)"
    result_df = df.query(query)
    result = round(result_df, input,2)
    max_idx= (CHF_df ['dollar_price'].idxmax())

if __name__ == "__main__":
    pass 

