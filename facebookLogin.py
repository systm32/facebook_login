#python script for login to facebook

import requests;
from BeautifulSoup import BeautifulSoup

def getLoginSession():
	try:
		#define the dummy headers as facebook server might reject the python header
		headers={"Connection": "keep-alive", "Accept": "*/*", "User-Agent": "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0", "Accept-Encoding": "gzip", "Content-Type": "application/x-www-form-urlencoded; charset=utf-8", "Proxy-Connection": "keep-alive"}

		#define the proxy set it to None if not required
		proxies = {'https':'127.0.0.1:8081','http':'127.0.0.1:8081'}

		#request to get the default cookies
		r_cookies = requests.get('https://www.facebook.com',headers=headers,proxies=proxies,verify=False)
		cookies = r_cookies.cookies

		#define the parameters to pass
		params = {}
		params['email'] = 'UserName'
		params['pass'] = 'Password'
		login_url = 'https://www.facebook.com/login.php?login_attempt=1'
		r_login = requests.post(login_url,params=params,proxies=proxies,cookies=cookies,headers=headers,verify=False,allow_redirects=False)
		login_cookies = r_login.cookies

		#check login is successful or not
		homepage = 'https://www.facebook.com/'
		r_home = requests.get(homepage,proxies=proxies,headers=headers,verify=False,cookies=login_cookies)
		content = r_home.text
		if(content.find('logout') != -1):
			return login_cookies;
		else:
			return False;
	except Exception,e:
		raise e;
		return False;


if __name__ == '__main__':
	pass