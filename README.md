# Countries By Population Density Project


This project uses Airflow to scrape and clean data from Wikipedia. The clean data is then pushed to Azure Data lake for processing. Tableau is the used to visualize the data.


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

It's good to reflect on what you learned throughout the process of building this project. Here you might discuss what you would have done differently if you had more time/money/data. Did you end up choosing the right tools or would you try something else next time?

## Contact

Please feel free to contact me if you have any questions at: LinkedIn, Twitter
