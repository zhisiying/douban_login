import requests
from  lxml import etree
import main
import time


class Douban():
    def __init__(self):
        self.session = requests.session()
        self.url = ''
        print('请输入你的账号:')
        self.account = input()
        print('请输入你的密码:')
        self.password = input()

    def login_indouban(self, url):

        data = {
            'source': 'index_nav',
            'form_email': self.account,
            'form_password': self.password
        }
        self.session.post(url, data=data)
        res = self.session.get('https://www.douban.com/people/158189784/')
        cs = etree.HTML(res.text)
        if cs.xpath('//li[@class="nav-user-account"]/a/span/text()') == '颖®的帐号':
            print('登陆成功')
        else:
            session = requests.session()
            self.yzm_login(session)

    def yzm_login(self, session):
        urlx = requests.get(url)
        x = etree.HTML(urlx.text)
        image_url = x.xpath('//img[@id="captcha_image"]/@src')[0]
        value = x.xpath('//input[@name="captcha-id"]/@value')[0]
        time.sleep(5)
        tu = requests.get(image_url).content
        f = open('image.jpg', 'wb')
        f.write(tu)
        f.close()

        datas = {
            'source': 'index_nav',
            'redir': 'https://www.douban.com',
            'form_email': self.account,
            'form_password': self.password,
            'captcha-solution': main.yzm()[0].lower(),
            'captcha-id': value,
            'login': '登录',}
        session.post(url, data=datas)
        res = session.get('https://www.douban.com/people/158189784/').text
        print(res)
        self.write_html(res)

    def write_html(self, res):
        f = open('./douban.html', 'w', encoding='utf8')
        f.write(res)
        f.close()


login = Douban()

url = 'https://www.douban.com/accounts/login'
login.login_indouban(url)
