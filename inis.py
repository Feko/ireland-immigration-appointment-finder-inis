import requests, urllib3, sys, webbrowser
from contants import TermColors, Regex, RunParams, log
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


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


class InisClient:
  def __init__(self):
    self.k_token = None
    self.p_token = None
  
  def _refresh_tokens(self):
    site_html = requests.request("GET", InisConstants.FORM_URL, verify=False).text
    k = Regex.K_TOKEN.search(site_html).groups()[0]
    p = Regex.P_TOKEN.search(site_html).groups()[0]
    self.k_token, self.p_token = k, p

  def get_nearest_appointments(self):
    self._refresh_tokens()
    url = InisConstants.WEBSERVICE_URL.format(k=self.k_token, p=self.p_token)
    return requests.request("GET", url, headers=InisConstants.HEADERS, data={}, verify=False)

  def navigate():
    webbrowser.open(InisConstants.FORM_URL)


class InisResponseParser:
  def __check_empty(response):
    if InisConstants.EMPTY_PATTERN in response.text:
      log('No appointments available.')

  def __check_error(response):
    if response.status_code != 200 or InisConstants.ERROR_PATTERN in response.text:
      print(TermColors.RED + 'ERROR ON RESPONSE!! ' + TermColors.END_COLOR + 'There was an error checking for appointments. Mostly likely to be on INIS website')
      if RunParams.DEBUG:
        print(response.text)

  def __check_appointments(response):
    if not InisConstants.APPOINTMENTS_FOUND_PATTERN in response.text:
      return

    for i in range(20):
      for j in [TermColors.PINK, TermColors.BLUE, TermColors.CYAN, TermColors.GREEN, TermColors.YELLOW, TermColors.RED]:
        print(j + 'FOUND!!! ' + TermColors.END_COLOR, end='')
    if RunParams.OPEN_BROWSER: InisClient.navigate()
    if RunParams.STOP_ON_FIND: sys.exit()

  def parse(response):
    [func(response) for func in [InisResponseParser.__check_empty, InisResponseParser.__check_error, InisResponseParser.__check_appointments]]
