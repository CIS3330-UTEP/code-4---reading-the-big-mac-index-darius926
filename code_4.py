import csv
import pandas as pd

filename = './big-mac-full-index.csv'
file_object=open(filename)
df= pd.read_csv(filename)
print(df.columns)

year=2003
country_code='KOR'

def get_big_mac_price_by_year(year,country_code):
    query = f"(iso_a3 == '{str(country_code).upper()}' and date >= {year}-01-01 and date <= {year}-12-31)"
    result_df = df.query(query)
    result = round(result_df['d']. mean(),2)
    print(result)
    return result
    


def get_big_mac_price_by_country(country_code):
    query= f"(iso_a3 == '{str(country_code).upper()}')"
    result_df = df.query(query)
    result=(round(result_df ['dollar_price'].mean(),2))
    print(result)
    return result


def get_the_cheapest_big_mac_price_by_year(year):
    query = f"(iso_a3 == 'KOR' and date >= {year}-01-01 and date <= {year}-12-31)"
    result_df = df.query(query)
    result = round(result_df['dollar_price'], min(),2)
    min_idx= (result_df ['dollar_price'].idxmin())
    print(result)
    return result, min_idx


def get_the_most_expensive_big_mac_price_by_year(year):
    query = f"(date >= {year}-01-01 and date <= {year}-12-31)"
    result_df = df.query(query)
    result = round(result_df['dollar_price'], max(),2)
    max_idx= (result_df ['dollar_price'].idxmax())
    print(result)
    return result, max_idx




if __name__ == "__main__":
      year=2003
      country_code='KOR'
      print(get_big_mac_price_by_country(year))
      print(get_big_mac_price_by_country(country_code))
