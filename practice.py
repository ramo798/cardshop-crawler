from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
from Seikei import seikei

options = Options()
#options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)

#ここから記述する

driver.get('https://www.ka-nabell.com/') #カーナベルにアクセスする
sleep(3) #サイトの読み込み待ち


input_elem = driver.find_element_by_name('key_word') #検索窓を探す
input_elem.send_keys('オシリスの天空竜') #検索窓に文字入れる
input_elem.send_keys(Keys.RETURN) #エンターキー押す
sleep(3) #サイトの読み込み待ち

#↓xpathから要素を取得
price1 = driver.find_elements_by_xpath('//*[@id="ListSell"]/table/tbody/tr[1]/td[1]')

#find_element's'の場合はprice1にlist形式で帰ってくるからforで要素取り出して表示
for a in price1:
    print(a.text)


#ここまで

driver.quit()
