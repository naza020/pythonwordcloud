def twetty(input):
    from typing import List

    try:
        import json
    except ImportError:
        import simplejson as json

    import tweepy

    # Config
    ACCESS_TOKEN = 'ACCESS_TOKEN'
    ACCESS_SECRET = 'ACCESS_SECRET'
    CONSUMER_KEY = 'CONSUMER_KEY'
    CONSUMER_SECRET = 'CONSUMER_SECRET'

    #connect twitter
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

    #datainput
    input=input.lower()
    input=input.encode("utf-8")
    tweets = tweepy.Cursor(api.search, q=input, lang='en').items(100);  # กำหนด#,ภาษา และ จำนวนทวีต
    # loop สร้างไฟล์ text
    with open('D:\WordcloudBigdata\datfromtweet\Rawdata.txt', 'r+',encoding="utf-8") as writefile:
        writefile.write("Text\n")
        for status in tweets:
            jtmp = status._json
            tmp = ""
            # เลือกเฉพาะtext ข้อความออกมา
            for i in jtmp['text']:
                if i != ',':
                    tmp += i
            writefile.write(tmp)
            writefile.write("\n")
            # print(tmp)

    # นำ space การเว้นบรรทัดออก แล้ว save เป็น text
    with open('D:\WordcloudBigdata\datfromtweet\Rawdata.txt', 'r+',encoding="utf-8") as f:
        with open('D:\WordcloudBigdata\datfromtweet\datatomongo.txt', 'w',encoding="utf-8") as writefile:
            for i in f.readlines():
                tmpslip: List[str] = i.split(" ")
                for j in tmpslip:
                    if j != ' ':
                        writefile.write(j)
                        writefile.write(" ")
                        # print(j)

    import matplotlib
    matplotlib.use('Agg') #run plt at bg
    import matplotlib.pyplot as plt
    import numpy as np
    from PIL import Image
    from wordcloud import WordCloud

    # อ่านไฟล์ text
    textdata = open('D:\WordcloudBigdata\datfromtweet\datatomongo.txt', 'r', encoding="utf-8").readlines()
    text = str(textdata)

    #path ของ Fonts
    path = 'D:\WordcloudBigdata\output\THSarabun.ttf'

    # เลือกคำที่ไม่ต้องการใส่ใน stopwords
    stopword=["RT","'","n'","|"]
    wordcloud = WordCloud(
        font_path=path,
        relative_scaling=0.3,
        min_font_size=1,
        background_color="white",
        width=1200,
        height=750,
        max_words=2000,
        colormap='plasma',
        scale=3,
        font_step=4,
        #   contour_width=3,
        #   contour_color='steelblue',
        collocations=False,
        # regexp=regexp,
        margin=2,
        stopwords=stopword
    ).generate(text)

    #

    plt.imshow(wordcloud, cmap=plt.cm.gray, interpolation='bilinear')
    plt.axis("off")
    fig = plt.gcf()
    fig.set_size_inches(8, 5)
    fig.savefig('D:\WordcloudBigdata\static\wordcloudcovid1.png', pad_inches=0, bbox_inches='tight', dpi=500) #save file
    # plt.show()

    return 1