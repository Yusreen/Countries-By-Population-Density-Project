# Countries By Population Density Project


This project uses Airflow to scrape and clean data from Wikipedia. The clean data is then pushed to Azure Data lake for processing. Tableau is the used to visualize the data.

View the interactive Tableau dashboard here: <https://public.tableau.com/app/profile/yusreen.shah/viz/PopulationDensityProject/Dashboard1>


## Overview

The goal of this project was to understand the role of docker and Airflow in Data Engineering.
Libraries like BeautifulSoup as well as Geocoder are used to extract data as well as use the extracted data to locate each country.

## System Architecture
![image](https://github.com/user-attachments/assets/cf115ff1-8932-4fa6-936a-4125d4edac48)



### Data Visualization

The dashboard is as follows:
![image](https://github.com/user-attachments/assets/cad0cbbf-3900-4c63-b8af-6440e0fffbd7)



## Requirements
- Python 3.9 (minimum)
- Docker
- PostgreSQL
- Apache Airflow 2.6 (minimum)

## Getting Started

1. Clone the repository.
   ```bash
   git clone https://github.com/Yusreen/CountriesByPopulationDensityProject.git
   ```

2. Install Python dependencies.
   ```bash
   pip install -r requirements.txt
   ```
   
## Running the Code With Docker

1. Start your services on Docker with
   ```bash
   docker compose up -d
   ``` 
2. Trigger the DAG on the Airflow UI.

## How It Works
1. Fetches data from Wikipedia.
2. Cleans the data.
3. Transforms the data.
4. Pushes the data to Azure Data Lake.
## Lessons Learned

1. I learnt how to read the html using Developer Tools and fetch the correct table using BeautifulSoup.
   ![image](https://github.com/user-attachments/assets/611c35de-a0eb-4047-8a13-e9ab3e19ad78)

2. I learnt how to use geocoder to get the correct location of the country/territory.
   ![image](https://github.com/user-attachments/assets/c5bb2c09-bd30-4537-b457-9f560c7ff93d)

3. I learnt how to correctly use dags in Airflow as well as familiarize myself with the UI.
4. I learnt how to use Tableau for effective storytelling.




## References

This project was inspired by: https://github.com/airscholar/FootballDataEngineering
