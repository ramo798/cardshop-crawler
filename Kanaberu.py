from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
from Seikei import seikei

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)

def kanaberu_kensaku(name):



    url = 'https://www.ka-nabell.com/'
    word = name

    driver.get(url)
    #sleep(2)
    assert 'カーナベル' in driver.title

    input_elem = driver.find_element_by_name('key_word')
    input_elem.send_keys(word)
    input_elem.send_keys(Keys.RETURN)
    sleep(3)

    #要素の存在を確認をする処理を書きたい
    #price1_c = driver.find_elements_by_xpath('//*[@id="ListSell"]/table/tbody/tr[1]/td[1]').size
    #price2_c = driver.find_elements_by_xpath('//*[@id="ListSell"]/table/tbody/tr[1]/td[2]').size
    #price3_c = driver.find_elements_by_xpath('//*[@id="ListSell"]/table/tbody/tr[1]/td[3]').size
    #price4_c = driver.find_elements_by_xpath('//*[@id="ListSell"]/table/tbody/tr[1]/td[4]').size

    price1_c = 1
    price2_c = 1
    price3_c = 1
    price4_c = 1

    if price1_c != 0:
        price1 = driver.find_elements_by_xpath('//*[@id="ListSell"]/table/tbody/tr[1]/td[1]')
    if price2_c != 0:
        price2 = driver.find_elements_by_xpath('//*[@id="ListSell"]/table/tbody/tr[1]/td[2]')
    if price3_c != 0:
        price3 = driver.find_elements_by_xpath('//*[@id="ListSell"]/table/tbody/tr[1]/td[3]')
    if price4_c != 0:
        price4 = driver.find_elements_by_xpath('//*[@id="ListSell"]/table/tbody/tr[1]/td[4]')


    #エレメントから名前と価格の処理
    kekka = []
    price = []
    shop_name = "カーナベル"

    for a in price1:
        price.append(a.text)
    price1_r = seikei(price)
    price1_r.append(shop_name)
    kekka.append(price1_r)
    price.clear()
    #print(price1_r)

    for a in price2:
        price.append(a.text)
    price2_r = seikei(price)
    price2_r.append(shop_name)
    kekka.append(price2_r)
    price.clear()
    #print(price2_r)

    for a in price3:
        price.append(a.text)
    price3_r = seikei(price)
    price3_r.append(shop_name)
    kekka.append(price3_r)
    price.clear()
    #print(price3_r)


#ここの処理がエラーの原因
    '''
    for a in price4:
        price.append(a.text)
    price4_r = seikei(price)
    kekka.append(price4_r)
    #kekka.append("カーナベル")
    price.clear()
    print(price4_r)
    '''



    return kekka



def kanaberu_end():
    driver.quit()
