def seikei(price):
    ppp = price[0]
    mai = '枚'
    for key in range(15):
        ppp = ppp.replace(str(key) + mai, ' ')
    ppp = ''.join(ppp.split())
    #print(ppp) #元の文確認用

    count = ppp.count(')') #[20thシークレット仕様]の記述がなければ通常処理

    #20thシークレット仕様の記述がある時にそれ用に処理するための記述
    if ppp.find('20thシークレット仕様') == 1:
        count = 2

    #print(count)

    info = [] #return用の配列

    if count == 1:
        #パック名の横の）までの文字数
        start = ppp.find(')')
        #カード名の横の数字までの文字数
        qqq = ppp[start + 1:len(ppp)] #名前までの文字列削除
        stop = 100
        for a in range(10):

            tmp = qqq.find(str(a))

            if tmp != -1:
                if tmp < stop:
                    stop = tmp

        #円までの文字数
        yen = qqq.find('円')

        info.append(qqq[0:stop]) #カード名
        info.append(ppp[0:2]) #レアリティ
        info.append(qqq[stop:yen]) #価格

    elif count == 2:
        #シク10期>CYHO(1005)ヴァレルソード・ドラゴン(20thシークレット仕様)28800円
        #パック名の横の）までの文字数
        start = ppp.find(')')
        #カード名の横の数字までの文字数
        qqq = ppp[start + 1:len(ppp)] #名前までの文字列削除

        stop = qqq.find(')')


        #円までの文字数
        yen = qqq.find('円')

        info.append(qqq[0:stop + 1]) #カード名
        info.append(ppp[0:2]) #レアリティ
        info.append(qqq[stop + 1:yen]) #価格

    return info
