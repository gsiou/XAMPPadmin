#!/usr/bin/python
# -*- coding: utf-8 -*-

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
from Tkinter import * 
import os
import webbrowser


#-----------------------------------#
#Classess---------------------------#
#-----------------------------------#
class NewForm():
	def __init__(self ,title ,result):
		self.form = Tk()
		self.title = title 
		self.form.title(self.title)
		self.form.geometry("200x200") 
		self.result = result 
		l1 = Label(self.form, text = self.result)
		l1.pack()
		b_exit = Button(self.form, text="Close Window", command=self.form.destroy)
		b_exit.pack()

class NewButton():
	def __init__(self ,text ,command):
		self.text = text
		self.command = command
		self.button =  Button(top ,text= self.text , command = self.command)
		self.button.pack() 



#-----------------------------------#
#MAIN FUNCTIONS---------------------#
#-----------------------------------#

def gotopage():
    webbrowser.open_new("http://xamppadmin.sf.net")

def onClick():
	return 
	
def server_start(): #Needs Testing
	check = os.system("/opt/lampp/lampp start")
	if check == 0:
	   NewForm("Succes", "Started XAMPP successfully")
	else:
		status() 
	return 
	
def server_stop():
    check = os.system("/opt/lampp/lampp stop")
    if check == 0:
	    NewForm("Succes", "Stopped XAMPP successfully")
    else:
		status() 
    return 
    
def server_restart():
    check = os.system("/opt/lampp/lampp restart")
    if check == 0:
	    NewForm("Succes", "Stopped XAMPP successfully")
    else:
		status() 
    return 
	
def configure(): #Needs Testing
	os.system("/opt/lampp/lampp security")
	return
	
def install_wordpress():
    checkvar = os.system("cd /opt/lampp")
    if checkvar == 0 :
        os.system("./wordpress_installer.sh")
    else:
        NewForm("Error","You dont have XAMPP installed!!!")
       # l4 = Label(top, text= result)
       # l4.pack()
	return
	
def status():
    checkvar = os.system("cd /opt/lampp")
    if checkvar == 0:
        NewForm("XAMPPadmin" , "XAMPPadmin is installed") 
    else:
        NewForm("XAMPPadmin","You dont have XAMPP installed!!!")
	return

#-----------------------------------#
#GUI--------------------------------#
#-----------------------------------#

top = Tk()
top.title("XAMPPadmin")
top.geometry("400x300")
NewButton("Install XAMPP" , onClick)
NewButton("Configure XAMPP" , configure) 
NewButton("Start XAMPP" , server_start) 
NewButton("Stop XAMPP" , server_stop) 
NewButton("Restart XAMPP" , server_restart)
NewButton("Visit Homepage" , gotopage)
NewButton("Install Wordpress Files" , install_wordpress )
NewButton("Check Status" , status)

mainloop() 




