import json
import os

import youtube_dl
from tqdm import tqdm

with open("ads.json", "r") as file:
    js = file.read()
    datas = json.loads(js)

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC

# options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# driver = webdriver.Chrome(options=options, executable_path='chromedriver.exe')

def download_subs(url, path, lang="en"):
    SAVE_PATH = '/'.join(os.getcwd().split('/')[:3]) + '/scripts'
    opts = {
        "skip_download": True,
        "writesubtitles": f"{path}.vtt",
        "subtitlelangs": lang,
        'outtmpl': SAVE_PATH + "/" + path
    }

    with youtube_dl.YoutubeDL(opts) as yt:
        yt.download([url])

ids_check = {}
links_check = {}

for data in datas:
    for info in data["data"]:
        ids_check.update({info["link_id"]: 0})
        links_check.update({info["href"]: 0})

for i in tqdm(range(len(datas))):
    data = datas[i]
    for info in data["data"]:
        link = info["href"]
        id = info["link_id"]
        if links_check[link] == 0:
            links_check[link] = 1
            ids_check[id] = 1
            try:
                download_subs(link, str(id))
            except:
                pass

