import urllib
import urllib.parse
import urllib.request
import ssl
import http.cookiejar
import json
import user

#cookies对象
c=http.cookiejar.LWPCookieJar()
cookie=urllib.request.HTTPCookieProcessor(c)
opener=urllib.request.build_opener(cookie)
urllib.request.install_opener(opener)

#关闭ssl认证证书
ssl._create_default_https_context=ssl._create_unverified_context

#用来标识你所在的机器
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

captcha_check_url='https://kyfw.12306.cn/passport/captcha/captcha-check'

getCode_url='https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.4908068478229397'


def getCode():
    req = urllib.request.Request(getCode_url)
    req.headers=headers
    #把文件读取
    codeFile=opener.open(req).read()
    #保存本地
    with open('code.png','wb') as fn:
        fn.write(codeFile)

def login():
    getCode()

    #坐标型的验证码:宽72，高84
    code=input('请输入验证码:')

    #参数拼接后缀
    req = urllib.request.Request(captcha_check_url)

    #添加请求头
    req.headers=headers

    values = {
        'answer': code,
        'login_site': 'E',
        'rand': 'sjrand'
    }

    #把字典转换成查询字符串-.encode(encoding='UTF8')不加会出现错误
    data = urllib.parse.urlencode(values).encode(encoding='UTF8')

    print(data)

    #开始请求
    html=opener.open(req,data).read().decode("utf8") #打开网站 url/request对象

    result = json.loads(html);
    print(result)
    print(result['result_code'])
    if result['result_code'] == '4' :
        print('验证码效验成功')
        toLogin()
    else:
        print('验证码效验失败')
        login()
    print(html)

#登录地址
login_url='https://kyfw.12306.cn/passport/web/login'

def toLogin():
    req=urllib.request.Request(login_url)
    req.headers=headers
    values={
        'username':user.user_name,
        'password':user.pwd,
        'appid':'otn'
    }
    data = urllib.parse.urlencode(values).encode(encoding='UTF8')

    html = opener.open(req, data).read().decode("utf8")  # 打开网站 url/request对象

    print(html)



login()




































