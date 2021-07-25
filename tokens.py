import re, requests, os, shutil
import subprocess as sbp

class TokenRegex:
  K_TOKEN = re.compile('<input id="k" type="hidden" value="([A-F0-9]+?)">')
  P_TOKEN = re.compile('<input id="p" type="hidden" value="([A-F0-9]+?)">')

class TokenExtractor:
  def get_tokens(self, url):
    html = self._get_site_html(url)
    k = TokenRegex.K_TOKEN.search(html).groups()[0]
    p = TokenRegex.P_TOKEN.search(html).groups()[0]
    return k, p

  def _get_site_html(self, url):
    return requests.request("GET", InisConstants.FORM_URL, verify=False).text


class PhantomJSTokenExtractor(TokenExtractor):
  def __init__(self):
    if shutil.which('phantomjs') is None:
      raise Exception('PhantomJS command line not found in your computer PATH. Please get it from: https://phantomjs.org/download.html - and set your PATH environment variable.')

    self.cmd = ['phantomjs', '--load-images=false', '--ignore-ssl-errors=true', os.path.join(os.path.dirname(__file__), 'get_source_wait_for.js')]

  def _get_site_html(self, url):
    proc = sbp.Popen(self.cmd, stdout=sbp.PIPE, stderr=sbp.PIPE)
    output, errors = proc.communicate(timeout=120)
    if errors:
        raise Exception(errors)
    return output.decode('utf-8')

    