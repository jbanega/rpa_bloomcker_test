from utils import (get_covid19_data, generate_csv_report)


def main():
    program_title = "REPORT GENERATOR OF COVID-19 WORLDWIDE SITUATION"
    api_url = "https://covid19-api.com/country/all?format=json"
    print(program_title.center(75, "*"))
    print("Source: ", api_url, "\n")

    covid19_df = get_covid19_data(api_url)
    generate_csv_report(covid19_df)


if __name__ == "__main__":
    main()