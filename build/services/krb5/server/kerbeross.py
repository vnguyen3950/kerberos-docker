import requests
from requests_kerberos import HTTPKerberosAuth, REQUIRED
import kerberos
def main():
    try:
        username = input("What is your username?")
        password = input("What is your password?")
        if (kerberos.checkPassword(username, password, "krbtgt/EXAMPLE.COM@EXAMPLE.COM", "EXAMPLE.COM") == True):
            print("Authentication Successful!")
    except:
        print("Authentication Failed!")
main()