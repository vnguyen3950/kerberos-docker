First, run the server.sh bash script to initialize the initial Kerberos users aka principals

Next, type the command "kadmin.local" without quotation marks

Now, you are in the Kerberos menu

"addprinc username" will prompt you to enter a password for the new user and then will create that principal.

"delprinc username" will delete a principal from Kerberos

You can also run "python3 kerbeross.py" to test authentication. The script will ask you username and password.

It will print "Authentication Successful if correct username and password and "Authentication Failed" if not