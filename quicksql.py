#!/usr/bin/env python3
import argparse
import pymssql
import sys
import decimal

#
# QuickSQL - a quick way to execute SQL commands on a remote system. 
# Written by: Dave Kennedy (@HackingDave)
# Company: TrustedSec (@TrustedSec)
#

print(r"""
  █████   █    ██  ██▓ ▄████▄   ██ ▄█▀  ██████   █████   ██▓    
▒██▓  ██▒ ██  ▓██▒▓██▒▒██▀ ▀█   ██▄█▒ ▒██    ▒ ▒██▓  ██▒▓██▒    
▒██▒  ██░▓██  ▒██░▒██▒▒▓█    ▄ ▓███▄░ ░ ▓██▄   ▒██▒  ██░▒██░    
░██  █▀ ░▓▓█  ░██░░██░▒▓▓▄ ▄██▒▓██ █▄   ▒   ██▒░██  █▀ ░▒██░    
░▒███▒█▄ ▒▒█████▓ ░██░▒ ▓███▀ ░▒██▒ █▄▒██████▒▒░▒███▒█▄ ░██████▒
░░ ▒▒░ ▒ ░▒▓▒ ▒ ▒ ░▓  ░ ░▒ ▒  ░▒ ▒▒ ▓▒▒ ▒▓▒ ▒ ░░░ ▒▒░ ▒ ░ ▒░▓  ░
 ░ ▒░  ░ ░░▒░ ░ ░  ▒ ░  ░  ▒   ░ ░▒ ▒░░ ░▒  ░ ░ ░ ▒░  ░ ░ ░ ▒  ░
   ░   ░  ░░░ ░ ░  ▒ ░░        ░ ░░ ░ ░  ░  ░     ░   ░   ░ ░   
    ░       ░      ░  ░ ░      ░  ░         ░      ░        ░  ░
                      ░                                         
                                                              """)

print("QuickSQL - a lightweight MSSQL connection and query tool that does not require \nadministrative level rights.\n")
print("Written by: David Kennedy (@HackingDave)")
print("Company: TrustedSec (@TrustedSec)")

# parse the options for the tool
ap = argparse.ArgumentParser()
ap.add_argument("-db", "--database" , required=False, help="Database you are selecting to connect to. Type blank for no database.")
ap.add_argument("-un", "--username", required=True, help="The username to specify to authenticate to the database.")
ap.add_argument("-pw", "--password", required=True, help="The password for the database. Type blank to authenticate without a password.")
ap.add_argument("-ip", "--ipaddress", required=True, help="The IP address or hostname of the remote SQL server.")
ap.add_argument("-port", "--port", required=True, help="The port of the Microsoft SQL port default is 1433.")
args = vars(ap.parse_args())

# if a blank password is specified
password = args['password']
if password == 'blank': password = ""

database = args['database']
if database == 'blank': database = ""

# attempt a connection to MSSQL server
try:
    if database != "":
        conn = pymssql.connect("{0}:{1}".format(args['ipaddress'],args['port']), args['username'], password, database)
    else:
        conn = pymssql.connect("{0}:{1}".format(args['ipaddress'],args['port']), args['username'], password)

except pymssql.OperationalError as error:
    print("[!] There was a connection error to the MSSQL server. Printing the error below : ")
    print(str(error))
    sys.exit()

if conn:
    print("[*] Connection successful. Dropping you to a prompt to execute raw SQL queries.")
    print("[-] To exit, just type exit or quit.")
    cursor = conn.cursor()
    while 1:
        execute_command = input(str(database) + ">")
        # quit out of quicksql
        if execute_command in ["quit", "exit"]: 
            break

        # execute the sql query here
        else:
            try:
                cursor.execute(execute_command)
                for row in cursor: print(row)
            # if we run into an exception
            except Exception as error:
                print("\n[!] The SQL Server returned an error. Printing below: ")
                print(str(error))
