import json
import pandas as pd
from geopy import Nominatim
from geopy.exc import GeocoderTimedOut
from datetime import datetime

def get_wikipedia_page(url):
    import requests

    print("Getting wikipedia page ...", url)
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        return response.text
    except requests.RequestException as e:
        print(f"An error occured: {e}")

def get_wikipedia_data(html):
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find_all("table", {"class": "wikitable"})[0]

    table_rows = table.find_all('tr')
    
    table_rows = table.find_all('tr')
    return table_rows

def extract_wikipedia_data (**kwargs):
    url = kwargs['url']
    html = get_wikipedia_page(url)
    rows = get_wikipedia_data(html)

    data = []

    for i in range(1, len(rows)):
        tds= rows[i].find_all('td')
        values ={
            'Rank':i,
            'Location':tds[0].text.replace(',',''),
            'Population_per_square_area':tds[1].text.replace(',',''),
            'Population':tds[3].text.replace(',',''),
            'Land_area':tds[4].text.replace(',',''),
        }
        data.append(values)
    print("The rows are {r}", len(rows))

   #data_df = pd.DataFrame(data)
    #data_df[['Country', 'Territory']] = data_df['Location'].str.extract(r'^(.*?)(?:\s*\((.*?)\))?$')
    # Insert the Country and Territory columns right after the location column
    #data_df.insert(data_df.columns.get_loc('Location') + 1, 'Country', data_df.pop('Country'))
    #data_df.insert(data_df.columns.get_loc('Location') + 2, 'Territory',data_df.pop('Territory'))
    #data_df.to_csv('data/extracted_data.csv',index=False)

    json_rows = json.dumps(data)
    kwargs['ti'].xcom_push(key='rows', value=json_rows)

    return "OK"

import geocoder

def get_lat_long(country, territory=None):
    location = geocoder.arcgis(f'{territory}, {country}') if territory else country

    if location.ok:
        return location.latlng

    return None
    

def transform_wikipedia_data(**kwargs):
    data = kwargs['ti'].xcom_pull(key='rows', task_ids='extract_data_from_wikipedia')

    data = json.loads(data)

    population_df = pd.DataFrame(data)
    population_df[['Territory', 'Country']] = population_df['Location'].str.extract(r'^(.*?)(?:\s*\((.*?)\))?$')
    
    population_df['Population_per_square_area'] = population_df['Population_per_square_area'].astype(float)
    population_df['Population'] = population_df['Population'].astype(float)
    population_df['Land_area'] = population_df['Land_area'].astype(float)
    population_df['Latitude'], population_df['Longitude'] = zip(*population_df.apply(lambda x: get_lat_long(x['Country'], x['Territory']), axis=1))
    
    kwargs['ti'].xcom_push(key='rows', value=population_df.to_json())
    return "OK"


def write_wikipedia_data(**kwargs):
    data = kwargs['ti'].xcom_pull(key='rows', task_ids='transform_wikipedia_data')

    data = json.loads(data)

    df_output= pd.DataFrame(data)

    file_name = ('population_cleaned_' + str(datetime.now().date())
                 + "_" + str(datetime.now().time()).replace(":", "_") + '.csv')
    
    
    #df_output.to_csv('data/' + file_name, index=False)
    df_output.to_csv('abfs://populationdataengineering@populationyussa.dfs.core.windows.net/data/' + file_name,
                storage_options={
                    'account_key': ''
                }, index=False)