from base64 import b64encode,b64decode
from binascii import Error as binasciiErr
from traceback import print_exc
from os.path import isfile
while True:
    print('您需要编码还是解码？\n 1.解码 2.编码 (按下Ctrl-X 来结束)\n')
    control = input()
    if control == '\x18':break
    if control == '1':
        control = input('请输入Base64码\n')
        ctrl = input('输出到文件还是直接显示？1.输出到控制台 2.输出到文件\n')
        if ctrl == '1':
            typer = input('请输入编码方式(如UTF-8等,如果只需要字节可以输入raw\n\
            输入错误的编码方式将会没有输出)\n')
            try:
                result = b64decode(control)
                if typer == 'raw' or typer == 'RAW':print(result)
                else:print(result.decode(typer,'ignore'))
            except binasciiErr:
                print('您输入的并不是ASCII码！')
                print_exc()
        elif ctrl == '2':
            print('输出到哪个文件？')
            file_path = input()
            try:result = b64decode(control)
            except binasciiErr:
                print('您输入的并不是ASCII码！')
                print_exc()
                continue
            with open(file_path,'wb') as f:print(result,file = f)
    elif control == '2':
        control = input('请问你要输入纯文本还是二进制数据\n\
        1.纯文本 2.数据流\
        \n')
        if control == '1':
            control = input("请输入文字(默认使用UTF-8编码)\n（注:输出中b'和'框起来的部分才是BASE64码！）\n")
            print(b64encode(control.encode()))
        elif control == '2':
            print('''
请问您想打开文件还是直接输入？
1.打开文件 2.直接输入
            ''')
            control = input()
            if control == '1':
                print('请输入文件名称')
                control = input()
                if isfile(control):
                    with open(control,'rb',True) as f:print(b64encode(f.read()))
                else:print('文件不存在！请输入正确的文件路径！')
            elif control == '2':
                print('请输入字节码')
                control = input()
                if ('b' not in control) or ('\'' not in control):print('输入错误！请检查输入的字节码格式！')
                else:
                    try:
                        control = eval(control)
                        print(control)
                    except SyntaxError:
                        print('您的输入出错啦！请检查格式是否正确！')
                        print_exc()