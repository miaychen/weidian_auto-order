#Package requared
import re
from bs4 import BeautifulSoup
import requests
import json


def SKU(link):

    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'} 
    soup_response = requests.get(url = link,headers=header)
    soup = BeautifulSoup(soup_response.content, 'html.parser')

    script = str(soup.select("script#__rocker-render-inject__")[0])
    #locate the start of json 
    start = script.find("{")
    #locate the end of json
    end = script.find("}}}'")
    beauty = script[(start):(end+3)]
    #convert to jason
    res = json.loads(beauty)
    
    #on sale time
    try:
               
        SellTime = res['result']['default_model']['item_info']['buyLimitInfo']['limitBarText']
        re_SellTime = re.compile('[0-9]{4}\-[0-9]{2}\-[0-9]{2}\s[0-9]{2}\:[0-9]{2}')
        Selltime_time = str(re_SellTime.findall(SellTime)[0])
    except: 
        SellTime = "Already on sale"
        Selltime_time = 0
  
    print(SellTime) 
    
    #get item id
    Item_ID = res['result']['default_model']['item_info']['item_id']
    print("Item ID: ",Item_ID)
    
    #get sku id
    try: 
        
        sku_dict = res['result']['default_model']['sku_properties']['sku']
        sku_key = list(sku_dict.keys())
        #number of sku
        item_no = len(sku_key)
        sku_list=list()
        sku_list_amount=list()
        for i in range(len(sku_key)):

            print(i+1, sku_key[i], sku_dict[sku_key[i]]['title'], sku_dict[sku_key[i]]['stock'])
            sku_list = sku_list+[sku_dict[sku_key[i]]['title']]
            sku_list_amount = sku_list_amount+[sku_dict[sku_key[i]]['stock']]
    except:
        #if seller did not set sku
        item_no = 0
        sku_key = []
        sku_list = []
        sku_list_amount=[]

    summary = {"SellTime":Selltime_time, "ItemID":Item_ID, "No.SKU":item_no, "SKUID":sku_key, "SKUName":sku_list, "Stock": sku_list_amount}
    return(summary)
