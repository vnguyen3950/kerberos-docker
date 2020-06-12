import requests
from requests_kerberos import HTTPKerberosAuth, REQUIRED
import kerberos
def main():
    username = input("What is your username?") + "@EXAMPLE.COM"
    password = input("What is your password?")
    if (kerberos.checkPassword(username, password, "EXAMPLE.COM", "EXAMPLE.COM") == True):
        print("Authentication Successful!")
main()