import requests
import json
import os

# list of api endpoints
urls = [
    "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/tps00203?format=JSON&time=2023&geo=BE&geo=BG&geo=CZ&geo=DK&geo=DE&geo=EE&geo=IE&geo=EL&geo=ES&geo=FR&geo=HR&geo=IT&geo=CY&geo=LV&geo=LT&geo=LU&geo=HU&geo=MT&geo=NL&geo=AT&geo=PL&geo=PT&geo=RO&geo=SI&geo=SK&geo=FI&geo=SE&geo=IS&geo=LI&geo=NO&unit=THS_PER&lang=en",
    "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/tps00172?format=JSON&time=2023-Q4&geo=BE&geo=BG&geo=CZ&geo=DK&geo=DE&geo=EE&geo=IE&geo=EL&geo=ES&geo=FR&geo=HR&geo=IT&geo=CY&geo=LV&geo=LT&geo=LU&geo=HU&geo=MT&geo=NL&geo=AT&geo=PL&geo=PT&geo=RO&geo=SI&geo=SK&geo=FI&geo=SE&geo=IS&geo=LI&geo=NO&s_adj=NSA&nace_r2=B-S&sizeclas=TOTAL&indic_em=JOBVAC&lang=en",
    "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/tps00001?format=JSON&time=2023&geo=BE&geo=BG&geo=CZ&geo=DK&geo=DE&geo=EE&geo=IE&geo=EL&geo=ES&geo=FR&geo=HR&geo=IT&geo=CY&geo=LV&geo=LT&geo=LU&geo=HU&geo=MT&geo=NL&geo=AT&geo=PL&geo=PT&geo=RO&geo=SI&geo=SK&geo=FI&geo=SE&geo=IS&geo=LI&geo=NO&lang=en",
]


def fetch_save_json(url, filename):
    try:
        # make get request to api
        response = requests.get(url)
        # check if request is successful
        if response.status_code == 200:
            try:
                # parse json data
                data = response.json()
                if isinstance(data, (dict, list)):
                    # save json to file
                    with open(filename, "w") as json_file:
                        json.dump(data, json_file, indent=4)
                        print(f"successfully saved data from {url} to {filename}")
                else:
                    print(f"unexpected data type prom {url}: {type(data)}")
            except ValueError as e:
                print(f"failed to parse from {url}: {e}")
        else:
            print(f"failed to retrieve data from {url}: {response.status_code}")
    except requests.RequestException as e:
        print(f"error occurred while fetching data from {url}: {e}")


# ensure the directory for saving files exists
os.makedirs("json_data", exist_ok=True)

for i, url in enumerate(urls):
    filename = os.path.join("json_data", f"data_{i + 1}.json")
    fetch_save_json(url, filename)
