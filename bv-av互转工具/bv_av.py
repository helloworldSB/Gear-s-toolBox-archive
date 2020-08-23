class av_bv_cls:
    def __init__(self):
        self.table='fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
        self.tr={}
        for i in range(58):
            self.tr[self.table[i]]=i
        self.s=[11,10,3,8,4,6]
        self.xor=177451812
        self.add=8728348608
    def dec(self,x):
	    r=0
	    for i in range(6):
		    r+=self.tr[x[self.s[i]]]*58**i
	    return (r-self.add)^self.xor
    def enc(self,x):
	    x=(x^self.xor)+self.add
	    r=list('BV1  4 1 7  ')
	    for i in range(6):
		    r[self.s[i]]=self.table[x//58**i%58]
	    return ''.join(r)
from urllib import request,parse
from json import loads#,dumps
while True:
    ctrl_num = input(r'''
您希望采用哪种API？（输入数字）
1.官方API   2.离线算法
按 CTRL+C 结束
''')
    if ctrl_num == '1' or ctrl_num == '2':
        video_num = input('''
请输入视频号
记得带上av或BV前缀
''')
        if video_num[:2] == 'av' or video_num[:2] == 'AV':flag = False
        elif video_num[:2] == 'BV' or video_num[:2] == 'bv':flag = True
        if ctrl_num == '1':
            URL = r'http://api.bilibili.com/x/web-interface/archive/stat?'
            if flag:URL += r'bvid='
            else:URL += r'aid='
            URL += video_num[2:]
            req = request.Request(URL)
            req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36")
            with request.urlopen(req) as f:
                temp1 = f.read()
                temp1 = loads(temp1)
                if temp1['code'] != 0:
                    print('转换错误！错误代码：',temp1['code'],'错误值：',temp1['message'])
                    continue
                print('\n转换成功！')
                temp2 = temp1['data']
                print('av号：',temp2['aid'])
                print('bv号：',temp2['bvid'])
                print('投币数：',temp2['coin'])
                print('共被浏览过',temp2['view'],'次')
                print('共有',temp2['reply'],'个评论')
                print('点赞数：',temp2['like'])
                print('收藏数：',temp2['favorite'])
                print('分享数：',temp2['share'])
                print(r'授权方式(1代表原创，2代表搬运):',temp2['copyright'],'\n')
        elif ctrl_num == '2':
            if flag:print('av号：av',av_bv_cls().dec(video_num))
            else:print('bv号：av',av_bv_cls().enc(int(video_num[2:])))
