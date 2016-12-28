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
echo "This programm will install Wordpress"
echo "What path would you like to use??(i.e if you type blog the visit path will be http://localhost/blog):"
read path
echo "Installation will start in 5 seconds..."
sleep 5
cd /tmp
echo "Downloading files..."
wget "http://wordpress.org/latest.tar.gz" -O WP.tar.gz
echo "Unpackaging data and copying..."
sudo tar xvfz WP.tar.gz
sudo mv wordpress /opt/lampp/htdocs/$path
echo "done..."
echo "Now enter http://localhost/$path and setup your wordpress"
echo "Exiting..."
sleep 5
