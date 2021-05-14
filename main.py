import json, time, urllib3
from contants import TermColors, RunParams, log
from inis import InisClient, InisResponseParser
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main():
  inis_client = InisClient()
  while(True):
    response = None
    try:
      log('Looking for appointment slots...')
      response = inis_client.get_nearest_appointments()
    except Exception as e:
      log(f'{TermColors.RED}ERROR trying to reach INIS. {str(e) if RunParams.DEBUG else ""}')

    if response is not None:
      InisResponseParser.parse(response)
      if RunParams.DEBUG: 
        print(json.dumps(response.json(), indent=4))

    log(f'Waiting for {RunParams.SLEEP_SECONDS} seconds')
    time.sleep(RunParams.SLEEP_SECONDS)

if __name__ == '__main__':
  main()