import requests
from bs4 import BeautifulSoup
import pandas as pd

Product_name=[]
Prices=[]
Description=[]
Reviews=[]

for i in range(1,11):
    url=" https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page= "+str(i)

    r=requests.get(url)
    

    soup=BeautifulSoup(r.text,"lxml")
    box=soup.find("div",class_="_1YokD2 _3Mn1Gg")
    names=box.find_all("div",class_="_4rR01T")

    
    for i in names:
        name=i.text
        Product_name.append(name)
    

    prices=box.find_all("div",class_="_30jeq3 _1_WHN1")
    for i in prices:
        price=i.text
        Prices.append(price)
    
    desc=box.find_all("ul",class_="_1xgFaf")
    for i in desc:
        des=i.text
        Description.append(des)
    
    reviews=box.find_all("div",class_="_3LWZlK")
    for i in reviews:
        review=i.text
        Reviews.append(review)
    
a={"Product Name":Product_name,"Prices":Prices,"Description":Description,"Reviews":Reviews}

df = pd.DataFrame.from_dict(a, orient='index')
df = df.transpose()
df.index+=1
df.index
print(df)
df.to_csv("Mobilecraping project.csv")
    