import requests
from bs4 import BeautifulSoup
import pandas as pd
import time



def page_loader(url,retry=3):
    """loads the page and returns soup data"""
    for i in range(retry):
        try:
            site = requests.get(url)
            if site.status_code == 200:
                soup = BeautifulSoup(site.text,'html.parser')
                return soup
            else:
                print(f'{url} cannot be reached attempt: {i+1}')
        except Exception as e:
            print(f'error loading{e}')
        time.sleep(5)
    return None
    
    


def collect_listing_link():
    """collects soup data and parses it in order to get the websites to the direct page that has the house listing """
    links=[]
    soup=page_loader(url)
    listings=soup.find_all('div',class_="wp-block-content clearfix text-xs-left text-sm-left")
    for house in listings:
        link=house.find('a')
        format_link=f"https://nigeriapropertycentre.com{link.get('href')}"
        links.append(format_link)
   
    return links

def house_dataset():
    """collects listed property data and saves in csv"""
    links=collect_listing_link()
    print
    props=[]
    column=['price','address','description','property ref','lsited on','last updated','market status','type','bedrooms','bathrooms','toilets','parking spaces','total area','covered area']
    for link in links:
        soup=page_loader(link)
        #price_loc=soup.find('div',class_='wp-block-content clearfix hidden-md hidden-sm hidden-lg voffset-15')
        price=soup.find_all('span',class_='price')
        house_price=price[1].text.strip()
        location=soup.find('p').text.strip()
        other_details=soup.find('div',class_='tab-body')
        prop_desc=other_details.find('p').text.strip()
        other_prop_deets=other_details.find('table')
        table_data= other_prop_deets.find_all('td')
        properties=[house_price,location]
        for items in table_data:
            items=items.text.strip()
            properties.append(items)
        props.append(properties)
    df=pd.DataFrame(props)
    df.to_csv('Abuja_houses.csv',mode='a',index=False,header=False)



for i in range(1,350): 
    url = f'https://nigeriapropertycentre.com/for-sale/houses/abuja/showtype?page={i}' 
    print(f"Scraping page {i}...")
    house_dataset() 
    time.sleep(5)









