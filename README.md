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

<div class='tableauPlaceholder' id='viz1724461586949' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Po&#47;PopulationDensityProject&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='PopulationDensityProject&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Po&#47;PopulationDensityProject&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1724461586949');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='650px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='650px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='977px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>


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
