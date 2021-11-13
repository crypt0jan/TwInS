#!/usr/bin/python3

"""
Check if am e-mail address is linked to Twitter, Instagram or a SnapChat account.
Author: @crypt0jan
"""

import sys, getopt
import requests
import json
import time

if len(sys.argv) <= 1:
    sys.exit('ERROR: I need at least two arguments. Run the script with -h to learn more.')


def checkTwitter(email):
    url = "https://api.twitter.com/i/users/email_available.json?email="+email
    headers = {
      "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    }
    request = requests.get(url,headers=headers).json()
    response = str(request)
    #print(response)
    if response.find("'valid': False") == True:
        print(f"TWITTER\t\t: e-mail address ({email}) is LINKED!")
    else:
        print(f"TWITTER\t\t: e-mail address ({email}) is NOT linked.")


def checkInstagram(email):
    url = "https://www.instagram.com/accounts/account_recovery_send_ajax/"
    headers = {
      "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
      "X-CSRFToken": "missing"
    }
    data = {"email_or_username":email}
    request = requests.post(url,data=data,headers=headers).json()
    response = str(request)
    #print(response)
    matches = ["We sent an self.email to", "password", "sent"]
    if any(x in response for x in matches):
        print(f"INSTAGRAM\t: e-mail address ({email}) is LINKED!")
    else:
        print(f"INSTAGRAM\t: e-mail address ({email}) is NOT linked.")


def checkSnapchat(email):
    print(f"SNAPCHAT\t: this API is currently unavailable.")


"""
def checkSnapchat(email):
    xsrf_token = 'hLQpFffDQzedKYqbxGEJxM' # Random 22 character string
    
    url = "https://accounts.snapchat.com/accounts/merlin/login"
    cookies = {
      "xsrf_token":xsrf_token
    }
    headers = {
      "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
      "X-XSRF-TOKEN": xsrf_token
    }
    data = {"email":email,"app":"BITMOJI_APP","xsrf_token":xsrf_token}
    request = requests.post(url,data=data,headers=headers,cookies=cookies).json()
    response = str(request)
    #print(response)
    matches = ["Kan de gebruiker niet vinden", "Cannot find the user"]
    if any(x in response for x in matches):
        print(f"SNAPCHAT\t: e-mail address ({email}) is NOT linked.")
    else:
        print(f"SNAPCHAT\t: e-mail address ({email}) is (probably) LINKED!")
"""


def main(argv):
    email = ""

    try:
      opts, args = getopt.getopt(argv,"e:h:",["--email"])
   
    except getopt.GetoptError:
      print ('Number of arguments given:', len(sys.argv), 'arguments.')
      print ('Argument list:', str(sys.argv))
      print ('Usage: twins.py -e [--email] <emailaddress>')
      sys.exit(2)

    for opt, arg in opts:
      if opt == '-h':
         print ('Usage: twins.py -e [--email] <emailaddress>')
         sys.exit()
      elif opt in ("-e", "--email"):
         email = arg

    if (email != ""):
      #print ('E-mail address is :', email)
      # Perform check()
      checkTwitter(email)
      checkInstagram(email)
      checkSnapchat(email)
    else:
        print ('Usage: twins.py -e [--email] <emailaddress>')
        sys.exit('ERROR: You did not specify the mandatory arguments.')


if __name__ == "__main__":
   main(sys.argv[1:])