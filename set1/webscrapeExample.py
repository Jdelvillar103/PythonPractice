import bs4,requests

def getEbayPrice(productUrl):
    res = requests.get(productUrl, headers={"User-Agent":"Defined"})
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    price = soup.find(id="prcIsum", class_="notranslate")
    price_string = price.get_text()
    return(price_string)

price = getEbayPrice('https://www.ebay.com/itm/Sony-PlayStation-4-Pro-1TB-Console-Black-PS4-Pro/283830269017?epid=21027542977&hash=item42159a3459:g:QVwAAOSww~heIlSo')   
print('The price is ' + price)

