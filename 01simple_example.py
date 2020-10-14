#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 09:57:18 2020

@author: NamNg
"""

# import the necessary packages
import argparse

# construct the argument parse and parse the arguments

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True, help="name of user")
args = vars(ap.parse_args())

# display a friendly message to the user
# print(f"Hi there {args["name"]}, it's  nice to meet you!")
print("Hi there {}, it's nice to meet you!".format(args["name"]))
