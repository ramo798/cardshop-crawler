from Kanaberu import kanaberu_kensaku,kanaberu_end
import csv

list = ['ヴァレルロード・S・ドラゴン',
        '幻創龍ファンタズメイ',
        'ヴァレルソード・ドラゴン',
        #'SNo.39 希望皇ホープONE',
        'E・HERO コスモ・ネオス',
        'TG スター･ガーディアン',
        'サイバース・クアンタム・ドラゴン'
        ]

header = [
            'card_name',
            'card_rare',
            'card_price',
            'shop_name',
          ]
with open('info.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
    writer.writerow(header)
    for tmp in list:
        b = kanaberu_kensaku(tmp)
        print(b)
        for q in b:
            writer.writerow(q)


kanaberu_end()
f.close()
