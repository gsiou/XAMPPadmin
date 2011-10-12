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
	def confirm(self,command):
		self.command = command 
		b_del = Button(self.form , text="Yes" , command=self.command)
		b_del.pack()

class NewButton():
	def __init__(self ,text ,command):
		self.text = text
		self.command = command
		f = Frame(top, height=30, width=300)
		f.pack_propagate(0)
		f.pack()
		self.button =  Button(f ,text= self.text , command = self.command)
		self.button.pack(fill=BOTH) 



#-----------------------------------#
#MAIN FUNCTIONS---------------------#
#-----------------------------------#

def gotopage():
    webbrowser.open_new("http://xamppadmin.sf.net")

def install_xampp():
	check = os.system("xterm -e sh xampp_installer.sh")
	return 
	
def server_start(): 
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
	check = os.system("xterm -e /opt/lampp/lampp security")
	if check == 0:
		return
	else:
		status() 
	return
	
def install_wordpress():
    checkvar = os.system("cd /opt/lampp")
    if checkvar == 0 :
        os.system("xterm -e ./wordpress_installer.sh")
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

def remove():
     NewForm("Warning" , "Are you sure you want to delete XAMPP?").confirm(c_remove)
     return

def c_remove():
    checkvar = os.system("cd /opt/lampp")
    if checkvar == 0:
        os.system("rm -rf /opt/lampp")
	NewForm("Success","XAMPP successfully deleted")
    else:
        NewForm("XAMPPadmin","You dont have XAMPP installed!!!")
	return
    
def backup():
    os.system("mkdir /home/xampp_backup")
    os.system("cp -r /opt/lampp/htdocs /home/xampp_backup")
    NewForm("Success" , "Backup created at /home/xampp_backup")

#-----------------------------------#
#GUI--------------------------------#
#-----------------------------------#

top = Tk()
top.title("XAMPPadmin")
top.geometry("400x300")
NewButton("Install XAMPP" , install_xampp)
NewButton("Configure XAMPP" , configure) 
NewButton("Start XAMPP" , server_start) 
NewButton("Stop XAMPP" , server_stop) 
NewButton("Restart XAMPP" , server_restart)
NewButton("Visit Homepage" , gotopage)
NewButton("Install Wordpress Files" , install_wordpress )
NewButton("Check Status" , status)
NewButton("Backup htdocs/" , backup)
NewButton("Remove XAMPP" , remove)
mainloop() 




