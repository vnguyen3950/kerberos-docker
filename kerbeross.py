import requests
from requests_kerberos import HTTPKerberosAuth, REQUIRED
r = requests.get("http://172.24.0.2:88", auth=HTTPKerberosAuth())