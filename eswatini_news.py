import requests 
x=requests.get("https://www.times.co.sz/news/readmore.php?bhsadjgfoh=Ezulwini+Palazzo+hosts+1st+conference%2C+over+500+delegates&yiphi=3785&bvhdgsj=News")
print(x.text)