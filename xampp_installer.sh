#!/bin/bash

#version 2

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
echo "This programm will install XAMPP for linux version 1.7.4"
echo "Installation will start in 5 seconds..."
sleep 5
echo "..."
echo "Started.."
echo "Creating folder for files..."
cd /tmp
echo "Done"
echo "Downloading files..."
wget "http://sourceforge.net/projects/xampp/files/XAMPP%20Linux/1.7.4/xampp-linux-1.7.4.tar.gz/download" -O Xampp.tar.gz
echo "Finished...."
sleep 1
echo "Installation procees will start soon"
sleep 3
echo "Started..."
echo "Unpackaging data and copying to /opt..."
sudo tar xvfz Xampp.tar.gz -C /opt
echo "done..."
echo "Deleting folder with download..."
sudo rm -r xamppfiles/ #Does not work (yet)
echo "Done"
echo "Goodbye..."
sleep 2
