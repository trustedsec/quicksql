# QuickSQL

                                                              
QuickSQL - a lightweight MSSQL connection and query tool that does not require  administrative level rights. Quick explanation on why this was useful. 

Why write another MSSQL query tool?

On an engagement, there was a compromised a system under and under the context of a regular user account. When pillaging, found a web.config which contained high level SQL accounts. Needed to query SQL directly (for xp_cmdshell specifically) on the Windows machine that was compromised and without administrator level rights (no SOCKS proxying etc). This works through the pymssql modules within Python and compiled using PyInstaller. Allows you to use the Python MSSQL modules directly on Windows in a compiled binary without the need of Python or administrative level rights. 

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

Example:
<pre>
quicksql.exe -ip 192.168.5.5 -db blank -un test -pw test -port 1433

Or run help for the parameter names:

quicksql.exe -h
</pre>

## Compiling Python to Executable

If you want to create your own binary directly from the Python code, follow these next steps:

<pre>
1. Download the latest version of Python for Windows. When installing, ensure that you add the Python path to your command line arguments.
2. Download the latest version of PyInstaller and unzip the folder. https://github.com/pyinstaller/pyinstaller/zipball/develop
3. Copy quicksql.py to the PyInstaller folder.
4. Install pymssql and pywin32 and pywin32-ctypes by typing: python -m pip install pymssql pywin32 pywin32-ctypes.
5. Run the following command: python pyinstaller.py --onefile quicksql.py.
6. Navigate to quicksql/dist and your execuable is there.
</pre>
