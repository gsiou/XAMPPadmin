#!/usr/bin/python
# -*- coding: utf-8 -*-
#  run.py
# version 1

#Copyright 2011 George Anastasiou

#This file is part of XAMPPadmin.
#
#    XAMPPadmin is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    XAMPPadmin is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#   along with XAMPPadmin.  If not, see <http://www.gnu.org/licenses/>.


#imports,os for linux commands and time for time.sleep :)
import os
import time
import webbrowser #for update-check

#functions
def update_check():
	print("Redirecting to updates page...")
	webbrowser.open_new("http://xamppadmin.sf.net")

def restart():
    print("Restarting...")
    os.system("clear")
    start()
    return

def finish():
    end = raw_input("If you want to return to menu type 1 , otherwise the script will finish.:")
    if end == "1":
        restart()
    else:
        quit()
    return
    
def install():
	os.system("./xampp_installer.sh")
	return

def configure():
	os.system("sudo /opt/lampp/lampp security")
	return
	
def server_start():
	os.system("sudo /opt/lampp/lampp start")
	return

def server_stop():
    os.system("sudo /opt/lampp/lampp stop")
    return 

def server_restart():
	os.system("sudo /opt/lampp/lampp restart")
	return

def server_delete():
	conf = raw_input("Are you sure you want to delete XAMPP?If yes press 1 , otherwise you will return to main menu!:")
        if conf == "1":
            print("Deleting XAMPP...")
            os.system("sudo rm -rf /opt/lampp")
            print("Done...")
        else:
            print("Returning to main menu...")
            time.sleep ( 2 )
            restart()
            return

def install_wordpress():
        checkvar = os.system("cd /opt/lampp")
        if checkvar == 0 :
            os.system("./wordpress_installer.sh")
        else:
	    print("You dont have XAMPP installed!!!")
	    time.sleep( 2 )
	    restart()
	return
    
    
  
def options():
    print("Hello")
    print("To install XAMPP press 1")
    print("To configure XAMPP press 2")
    print("To start XAMPP press 3")
    print("To stop XAMPP press 4")
    print("To delete XAMPP press 5")
    print("To terminate this programm press 6")
    print("To restart XAMPP press 7")
    print("Please make sure that if you want to do") 
    print("actions 2 to 7 you must have XAMPP installed...")
    print("To check for updates press u,updates are important in case of bugs or if a new \n XAMPP version is available.")
    print("To download wordpress files into your htdocs folder type drupal")
    return

def actions():
    sel = raw_input("What would you like to do?:")
    if sel == "1":
        install() #Password for this action is asked during the execution
    elif sel == "2":
        configure()
    elif sel == "3":
        server_start()
    elif sel == "4":
        server_stop()
    elif sel == "5":
        server_delete()
    elif sel == "6":
        print("Closing Programm")
        time.sleep ( 2 )
        quit()
    elif sel == "7":
        server_delete()
    elif sel == "u":
	update_check()
    elif sel == "wp":
        install_wordpress()
    else:
        print("Please Select one of the available options.")
        time.sleep ( 3 ) 
        restart()
        return


def start():
#Script Start
    options()
    actions()
    finish()
    return


start()


    



