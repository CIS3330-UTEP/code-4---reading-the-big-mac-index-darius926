import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df= pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    query = f"(iso_a3 == '{country_code.upper()}' and date >= {year}-01-01 and date <= {year}-12-31)"
    result_df = df.query(query)
    result = round(result_df, input,2)

def get_big_mac_price_by_country(country_code):
    pass querey= f"(iso_a3 == '{KOR}')
    print(mean_df in {year} in ('dollar_price')
    round(input,2)

def get_the_cheapest_big_mac_price_by_year(year):
    pass year=(2008)
    "country_name(country_code): $dollar_price" ()

def get_the_most_expensive_big_mac_price_by_year(year):
    pass year=(2008)
    "country_name(country_code): $dollar_price" ()

if __name__ == "__main__":
    pass 

