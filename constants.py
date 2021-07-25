import re, time

class RunParams:
  SLEEP_SECONDS = 10
  OPEN_BROWSER = True
  STOP_ON_FIND = True
  DEBUG = False

class TermColors:
  PINK = '\033[95m'
  BLUE = '\033[94m'
  CYAN = '\033[96m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
  END_COLOR = '\033[0m'

class InisConstants:
  FORM_URL = 'https://burghquayregistrationoffice.inis.gov.ie/Website/AMSREG/AMSRegWeb.nsf/AppSelect?OpenForm'
  WEBSERVICE_URL = 'https://burghquayregistrationoffice.inis.gov.ie/Website/AMSREG/AMSRegWeb.nsf/(getAppsNear)?readform&cat=All&sbcat=All&typ=New&k={k}&p={p}'
  HEADERS = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'CookieScriptConsent={"action":"accept","categories":"[\\"performance\\",\\"targeting\\"]"}; _ga=GA1.3.1805604899.1609865661; _ga=GA1.4.1805604899.1609865661; _gid=GA1.4.1398526851.1620633251; _gat=1',
    'Host': 'burghquayregistrationoffice.inis.gov.ie',
    'Referer': 'https://burghquayregistrationoffice.inis.gov.ie/Website/AMSREG/AMSRegWeb.nsf/AppSelect?OpenForm',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
  }
  EMPTY_PATTERN='empty'
  APPOINTMENTS_FOUND_PATTERN='slots'
  ERROR_PATTERN='There was a problem finding'

def log(msg):
  msg = TermColors.PINK + '[' + time.strftime("%Y-%m-%d %H:%M:%S") + '] - ' + TermColors.END_COLOR + msg
  print(msg)