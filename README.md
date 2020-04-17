# QuickSQL

                                                              
QuickSQL - a lightweight MSSQL connection and query tool that does not require  administrative level rights. Quick explanation on why this was useful. On a penetration, compromised a system under the context of a user account. When pillaging, found a web.config which contained high level SQL accounts. Needed to query SQL directly (for xp_cmdshell specifically) on the Windows machine and without administrator level rights. This works through the pymssql modules within Python and compiled using PyInstaller. Allows you to use the Python MSSQL modules directly on Windows in a compiled binary without the need of Python or administrative level rights. 

## Usage
<pre>
Written by: David Kennedy (@HackingDave)
Company: TrustedSec (@TrustedSec)
usage: quicksql.py [-h] [-db DATABASE] -un USERNAME -pw PASSWORD -ip IPADDRESS
                   -port PORT

optional arguments:
  -h, --help            show this help message and exit
  -db DATABASE, --database DATABASE
                        Database you are selecting to connect to.
  -un USERNAME, --username USERNAME
                        The username to specify to authenticate to the
                        database.
  -pw PASSWORD, --password PASSWORD
                        The password for the database. Type blank to
                        authenticate without a password.
  -ip IPADDRESS, --ipaddress IPADDRESS
                        The IP address or hostname of the remote SQL server.
  -port PORT, --port PORT
                        The port of the Microsoft SQL port default is 1433.
</pre>
QuickSQL is a simple MSSQL query tool that allows you to connect to a SQL server that you already have credentials for and execute raw queries. You do not need to install the ODBC drivers for Windows and this works without administrative level permissions. 

There are two files, the quicksql.py which is the source code for quicksql and can be run on anything that has Python3 installed on it. The second is quicksql.exe which can be run on Windows operating systems.

Example:\
\
quicksql.exe -ip 192.168.5.5 -db blank -un test -pw test -port 1433\
\
Or run help for the parameter names:\
\
quicksql.exe -h
