import requests
from bs4 import BeautifulSoup as bs

def getdata(value):
	try:
		if(value=='news'):
			r=requests.get("https://technews.lk/").text
		else:
			r=requests.get(f"https://technews.lk/{value}").text
		soup=bs(r,'lxml')
		x=soup.find_all('div',class_="post-feed")
		val={}
		val["data"]=[]
		for i in range(0,len(x)):
			dic={}
			dic["title"]=x[i].find('div', itemprop="title").text
			dic["decription"]=x[i].find('div',itemprop="title").text
			dic["images"]=x[i].find('div', class_="post-card-image")['style'].split("url(")[1].split(")")[0].replace("'",'')
			if(x[i].find('a', class_="source")==None):
				dic["read-more"]="None"
			else:
				dic["read-more"]=x[i].find('a', class_="source").attrs['href']
			val["data"].append(dic)
		val["category-collection"]=value
		return val
	except Exception as e:
		return {"status":False,"error":e}
