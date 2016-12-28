#!/bin/bash

#version 3

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


clear
echo "This programm will install XAMPP for linux version 7.0.13"
echo "Installation will start in 5 seconds..."
sleep 5
cd /tmp
echo "Downloading files..."
wget "https://sourceforge.net/projects/xampp/files/XAMPP%20Linux/7.0.13/xampp-linux-x64-7.0.13-1-installer.run/download" -O Xampp.run
echo "Finished downloading. Installing"
chmod a+x Xampp.run
./Xampp.run --mode unattended --launchapps 0
echo "Done"
sleep 2
