import re, time

class RunParams:
  SLEEP_SECONDS = 10
  OPEN_BROWSER = True
  STOP_ON_FIND = True
  DEBUG = False

class Regex:
  K_TOKEN = re.compile('<input id="k" type="hidden" value="([A-F0-9]+?)" \/>')
  P_TOKEN = re.compile('<input id="p" type="hidden" value="([A-F0-9]+?)" \/>')

class TermColors:
  PINK = '\033[95m'
  BLUE = '\033[94m'
  CYAN = '\033[96m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
  END_COLOR = '\033[0m'

def log(msg):
  msg = TermColors.PINK + '[' + time.strftime("%Y-%m-%d %H:%M:%S") + '] - ' + TermColors.END_COLOR + msg
  print(msg)