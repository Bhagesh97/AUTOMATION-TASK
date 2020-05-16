import time

import pyautogui
from selenium import  webdriver
import urllib.request
import numpy as np
import os
import json
import glob
import pandas as pd
options = webdriver.ChromeOptions()
import csv




options = webdriver.ChromeOptions()
preferences={"download.default_directory":r"C:\Users\Developers\PycharmProjects\officework",
             "download.directory_upgrade": True,
             "safebrowsing.enabled": True
             }

options.add_experimental_option("prefs",preferences)
browser=webdriver.Chrome( executable_path=r'C:\Users\Developers\PycharmProjects\officework\Chromedriver.exe')
browser=webdriver.Chrome(options=options)

minimumWindow=False
def internet_on():
    i=0
    while True:
        try:
            urllib.request.urlopen('http://www.google.com/',timeout=20)
            return True
        except:
            print("Internet Not Working for last %s minutes" %i)
            i=i+1
            time.sleep(60)
            pass

browser.maximize_window()
if minimumWindow:

    pyautogui.move(600,3,1)
    pyautogui.drag(0,200,1,button='left')



browser.get('https://fbr.gov.pk/download-atl/132041')
# print(":testing")
pyautogui.click(407,809)
# df = pd.DataFrame()
# xlfname = '202046095128395ATL_IT.xlsx'
# xl = pd.ExcelFile(xlfname)
#
# for sheet in xl.sheet_names:
#     df_tmp = xl.parse(sheet)
#     df = df.append(df_tmp, ignore_index=True)
#
# print(len(df))
#
# csvfile = 'sample.csv'
# df.to_csv(csvfile, index=False)


# data=pd.read_csv('sample.csv')
# df=pd.DataFrame(data)
#
#
#
#
# df1 = df[df['NTN'].str.contains("/", na=False)]
#
# # df1[['First','Last']] = df1['NTN'].str.split("/",n=1,expand=True)
# csvfile = 'test44.csv'
# df1.to_csv(csvfile, index=False)
# data=pd.read_csv('test44.csv')
#
# dd=pd.DataFrame(data)
# dd['NTN'] = dd['NTN'].str.split('/')
#
# # convert list of pd.Series then stack it
# dd = (dd
#  .set_index(['SR_NO','NAME','BUSINESS_NAME'])['NTN']
#  .apply(pd.Series)
#  .stack()
#  .reset_index()
#  .drop('level_3', axis=1)
#  .rename(columns={0:'NTN'}))
# dd2=pd.DataFrame(dd)
# csvfile = 'test45.csv'
# dd.to_csv(csvfile, index=False)
#
# # print(dd)

