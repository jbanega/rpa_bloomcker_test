import datetime
import os
import pandas as pd
import requests
from pathlib import Path


def get_covid19_data(api_url):
    # Retrieve information from API as json to pandas dataframe
    r = requests.get(api_url)
    data = r.json()
    df = pd.DataFrame.from_dict(data)
    
    # Filtering information
    covid19_df = df[["country", "confirmed", "recovered", "deaths", "critical"]].set_index("country")
    return covid19_df


def generate_csv_report(covid19_df):
    print("Generating CVS Report...", "\n")
    
    # Setting csv file name
    date = str(datetime.datetime.now()).split()[0]
    BASE_DIR = Path(__file__).resolve().parent
    csv_file = os.path.join(BASE_DIR, "reports", "covid19_" + date +".csv")

    # Exporting dataframe to csv
    covid19_df.to_csv(csv_file)

    print(f"CSV report has been generated.\nSee the file {csv_file}")
    exit()