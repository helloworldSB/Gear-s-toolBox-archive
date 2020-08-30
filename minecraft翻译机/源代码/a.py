#在遵守 CC BY-NC-SA 4.0的协议下，你可以随意传播、使用、分发此程序
#作者：齿轮-gear
#这个翻译程序用到了有道翻译的API
#有道翻译提供了一个免费的API
#不需要APPID等识别工具
#示例地址：
#http://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i=计算
print("程序已经启动！")
from urllib import request,parse
from json import loads,load,dump
from time import sleep
from string import printable
from traceback import print_exc
from concurrent.futures import ThreadPoolExecutor
file = None
fuck = 0
with open("en_us.json",'r',True,'utf-8') as f:
    file = load(f)
result = {}
errorNum = 0
#nmsl = 0
#nmzl = 0
def Translate(translateStr,oldKey):
    global result,errorNum#,nmsl,nmzl
    while True:
        if isinstance(translateStr,str):
            #print('正在启动……')
            sleep(3)
            #if nmsl <= 10:nmsl += 1
            #elif nmzl <= 10:
            #    sleep(10)
            #else:
            #    nmsl,nmzl = 0,0
            #    sleep(10)
            URL = 'http://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i=' + parse.quote(str(translateStr))
            try:
                #print('正在等待网络I/O')
                req = request.Request(URL)
                req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36\
                (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36")
                with request.urlopen(req) as f:
                    #print(f)
                    temp1 = f.read()
                    #print(temp1)
                    temp1 = loads(temp1)
                    #print(temp1)
                    #print('正在进行翻译')
                    if temp1['errorCode'] != 0:
                        print('翻译错误！错误值：' + oldKey + ":" + translateStr)
                        errorNum += 1
                        return False
                    temp2 = temp1["translateResult"][0][0]
                    print('翻译成功！被翻译的文本：%s , 翻译后的文本：%s' %(temp2['src'],temp2['tgt']) )
                    result[oldKey] = temp2['tgt']
                    del temp1,temp2
                    return True
            except ConnectionResetError:
                print_exc()
                continue
def Translate_done(future):
    global fuck
    if future.result():
        if fuck < 40:
            fuck += 1
        else:
            sleep(0.75)
            with open('zh_tw.json','w',True,'utf-8') as f:
                dump(result,f)
            fuck = 0

with ThreadPoolExecutor(max_workers = 5) as Pool:
    for key , value in file.items():
    #如果你需要自动保存，请删除下面一行代码的#号
        Pool.submit(Translate,value,key).add_done_callback(Translate_done)
        #Translate(value,key)
fuck = 20
Translate_done()
print(f'完成！共有{errorNum}个错误')