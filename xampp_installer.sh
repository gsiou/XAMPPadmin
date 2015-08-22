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
echo "This programm will install XAMPP for linux version 1.8.3"
echo "Installation will start in 5 seconds..."
sleep 5
echo "..."
echo "Started.."
echo "Creating folder for files..."
cd /tmp
echo "Done"
echo "Downloading files..."
wget "https://www.apachefriends.org/xampp-files/5.6.11/xampp-linux-x64-5.6.11-1-installer.run" -O Xampp.run
echo "Finished...."
sleep 1
echo "Installation procees will start soon"
sleep 3
chmod a+x Xampp.run
./Xampp.run
echo "Done"
echo "Goodbye..."
sleep 2
