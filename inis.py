import requests, urllib3, sys, webbrowser
from tokens import PhantomJSTokenExtractor
from constants import TermColors, RunParams, log, InisConstants
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class InisClient:
  def __init__(self):
    self.k_token = None
    self.p_token = None
    self.token_provider = PhantomJSTokenExtractor()
  
  def _refresh_tokens(self):
    self.k_token, self.p_token = self.token_provider.get_tokens(InisConstants.FORM_URL)

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
