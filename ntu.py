'''
Author: Amit Chakraborty
Project: NTU Faculty Profile Scraper
Profile URL: https://github.com/amitchakraborty123
E-mail: mr.amitc55@gmail.com
'''

import time
import pandas as pd
import requests
import os


def get_data():
    print('==================== Getting Data Fro NTU ====================')
    url = 'https://www.ntu.edu.sg/research/faculty-directory/GetAcademicProfiles/?searchFaculty=&interests=all&page'
    i = 0
    while True:
        i += 1
        print(f'>>>>>>>>>>>>> Page: {i}')
        response = requests.get(f'{url}={i}')
        if response.status_code == 200:
            data = response.json()
            items = data.get("items", [])
            if len(items) < 1:
                break
            for item in items:
                if not item:
                    continue
                data = {
                    "Title": item.get("title"),
                    "Url": item.get("url"),
                    "Tag": item.get("tag"),
                    "Description": item.get("description"),
                    "Email": item.get("email"),
                    "Interests": item.get("interests"),
                    "Appointments": item.get("appointments"),
                    "Profilepictureurl": item.get("profilepictureurl"),
                }
                df = pd.DataFrame([data])
                df.to_csv('Data.csv', mode='a', header=not os.path.exists('Data.csv'), encoding='utf-8-sig', index=False)
            time.sleep(1)
        else:
            print(f"[WARNING] Failed to fetch page {i}: {response.status_code}")
    print("All Data Scraped Successfully.....")



if __name__ == '__main__':
    get_data()
