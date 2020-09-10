# using pulse-VPN-API
# to create user in existing auth-server
# code by @dyjang

__author__ = "dyjang"

import requests
import json
import logging
import config  # need to set

_LOGFILE = config.DEBUGFILE
logging.basicConfig(level=logging.INFO, filename=_LOGFILE,
                    format='[%(asctime)s][%(levelname)s] %(message)s')

# _AUTH_SERV = CS_Homework_Local
_AUTH_SERV = config.AUTH_SERV
_HOST = config.HOST
_TOKEN = config.TOKEN
_PWD_TXT = config.PWD_TXT
_FILENAME = config.FILENAME


def add_user(user_id, desc):
    ''' api call for adding new user '''

    url = f'https://{_HOST}/api/v1/configuration/authentication/auth-servers/auth-server/{_AUTH_SERV}/local/users/user'

    hd = {
        "Authorization": f'Basic {_TOKEN}',
        "Content-Type": "application/json"
    }

    dt = {
        "change-password-at-signin": "True",
        "console-access": "false",
        "enabled": "true",
        "fullname": desc,
        "one-time-use": "false",
        # "password-encrypted": "3u+U",
        "password-cleartext": _PWD_TXT,
        "username": user_id
    }

    resp = requests.post(url, headers=hd, data=json.dumps(dt), verify=False)
    resp.status_code

    logging.info(f'[-] USER_ID : {user_id}')
    logging.info(f'[-] Response : {resp.status_code}')


def main():
    ''' get new user information from txt-file and call add_user func '''
    filename = "list-id.txt"
    with open(filename, 'r') as f:
        lines = f.readlines()
        cnt = 1
        for line in lines:
            a, b, c = line.split(',')
            logging.info(f'[-] Count : {cnt}')
            add_user(a, f"{b} / {c}")
            cnt = cnt + 1


if __name__ == "__main__":
    main()
