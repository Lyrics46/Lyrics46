import codecs
import hashlib
import http
import json
import os
import random
import urllib

import streamlit as st
from PIL.Image import Image


def main():

    st.title("Attention-GAN app")
    st.text(" you can write a sentence and the attngan can transfer it to a picuture.")
    text = st.text_input('请描述你心中的鸟', 'a red bird with ...')
    #sentence = translate(text)

    if st.button('生成鸟') and text:
        sentence=translate(text)

        #将sentence写入txt中  清空写
        textpath='./data/birds/example_captions.txt'
        with codecs.open(textpath,'a','utf-8') as w:
            w.seek(0)
            w.truncate()
            w.write(sentence)

        os.system("python /code/main.py --cfg cfg/eval_bird.yml --gpu 0")
        imagepath='/models/bird_AttnGAN2/example_captions/0_s_0_g2.png'
        img=Image.open(imagepath);

        st.image(img,caption=text)


    #st.write('The current movie title is', sentence)


#https://blog.csdn.net/weixin_44259720/article/details/104648444
def translate(text):
    appid='20220212001081221'
    secretKry='3GylVRuw7LMQ9VtBxFWk'

    httpClient=None
    myurl='/api/trans/vip/translate'
    #myurl='https://fanyi-api.baidu.com/api/trans/vip/fieldtranslate'

    formLang='zh'
    toLang='en'
    salt=random.randint(32768,65536)
    sign=appid+text+str(salt)+secretKry
    sign=hashlib.md5(sign.encode()).hexdigest()
    myurl=myurl+'?appid='+appid+'&q='+urllib.parse.quote(text)+'&from='+formLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign

    try:
        httpClient=http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET',myurl)
        response=httpClient.getresponse()
        result_all=response.read().decode("utf-8")
        result=json.loads(result_all)
        result=result['trans_result'][0]['dst']


        return result
    except Exception as e:
        return e
    finally:
        if httpClient:
            httpClient.close()




if __name__ == "__main__":
    #print("fefef")
    #print(translate("一只可爱的鸟"))
    main()
