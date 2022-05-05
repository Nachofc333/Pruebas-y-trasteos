from time import sleep
from selenium import webdriver
from requests_html import HTMLSession
from selenium.common.exceptions import NoSuchElementException

def check_stock(url, session):

    while True:
        webpage = session.get(url)
        buy_zone = webpage.html.find("#a-button-input")
        driver = webdriver.Edge()
        driver.get(url)
        try:
            driver.find_element(by="buy-now-button").click()
            driver.find_element()

        except NoSuchElementException:
            print("No habia anuncio")

        if len(buy_zone) > 0:
            print(buy_zone)
            print("Hay stock")
        else:
            print("no hay stock")

        sleep(100)


def main():
    url = "https://www.amazon.es/Numskull-Estatua-Oficial-Pulgadas-Coleccionable/dp/B09K47DBV8/?_encoding=UTF8&pd_rd_w=AbkhY&pf_rd_p=5f6951c0-9d61-4e03-b39a-a5647d9ae575&pf_rd_r=TMYHB4B1H37SWC0HGXE4&pd_rd_r=4f3b81e4-b3e1-4219-9648-50c52d8da014&pd_rd_wg=zNFWm&ref_=pd_gw_ci_mcx_mr_hp_atf_m&th=1"
    session = HTMLSession()
    check_stock(url,session)


if __name__ == '__main__':

    main()

'''from requests_html import HTMLSession, AsyncHTMLSession


url = "https://www.pccomponentes.com/tempest-conquer-silla-gaming-negra"

session = HTMLSession()
code = session.get(url)

buy_zone = code.html.find("#btnsWishAddBuy")

print(buy_zone)'''
