#!/usr/bin/python3
# This Python file uses the following encoding: utf-8
import random 
import subprocess
import ctypes
import sys
import os
#import requests 
import urllib
#from urllib import urlopen
from os import system, getuid, path
from time import sleep
from platform import system as systemos, architecture
from subprocess import check_output
from Checks import *
#from gif_for_cli.execute import execute

def banner():
    RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2, BRED= '\033[91m', '\033[46m', '\033[36m', '\033[1;91m', '\033[0m' , '\033[1;32m' , '\033[1;93m', '\033[1;92m',"\033[5;35m"
    BLINK ,Magenta ="\033[5m","\033[1;34m"
    y='\033[1;33m'
    lred,lyellow,lblue="\033[91m","\033[93m","\033[94m"
    system('clear')
    # loadingTextPrint()
    system('clear')
    print(r'''

  ██████╗██╗   ██╗██████╗ ██╗  ██╗███████╗██████╗ 
  ██╔════╝╚██╗ ██╔╝██╔══██╗██║  ██║██╔════╝██╔══██╗
  ██║      ╚████╔╝ ██████╔╝███████║█████╗  ██████╔╝
  ██║       ╚██╔╝  ██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
  ╚██████╗   ██║   ██║     ██║  ██║███████╗██║  ██║
   ╚═════╝   ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

                                                                 {lblue}•·.·''·.·•·.·''·.·•{DEFAULT}
                                                                   {YELLOW}BY: {RED}AsHfIEXE {RED}<Cypher>{DEFAULT}     
                                                                 {lblue}•·.·''·.·•·.·''·.·•{DEFAULT}
                         {GREEN2}GitHub Profile{y}{RED} : {DEFAULT}{YELLOW}{{https://github.com/AsHfIEXE{DEFAULT} 
                      {GREEN2}LinkedIn Profile{y}{RED} : {DEFAULT}{YELLOW}{{https://www.linkedin.com/in/salehinashfi{DEFAULT}
           
           
    '''.format(RED=RED, BRED=BRED, CYAN=CYAN, GREEN=GREEN, DEFAULT=DEFAULT ,YELLOW=YELLOW, Magenta=Magenta,y=y, lred=lred, lyellow=lyellow, BLINK=BLINK, GREEN2=GREEN2, YELLOW2=YELLOW2, lblue=lblue))

def android_banner():
    RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2, BRED= '\033[91m', '\033[46m', '\033[36m', '\033[1;91m', '\033[0m' , '\033[1;32m' , '\033[1;93m', '\033[1;92m',"\033[5;35m"
    BLINK ,Magenta ="\033[5m","\033[1;34m"
    y='\033[1;33m'
    lred,lyellow,lblue="\033[91m","\033[93m","\033[94m"
    print(r'''
  ██████╗██╗   ██╗██████╗ ██╗  ██╗███████╗██████╗ 
  ██╔════╝╚██╗ ██╔╝██╔══██╗██║  ██║██╔════╝██╔══██╗
  ██║      ╚████╔╝ ██████╔╝███████║█████╗  ██████╔╝
  ██║       ╚██╔╝  ██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
  ╚██████╗   ██║   ██║     ██║  ██║███████╗██║  ██║
   ╚═════╝   ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

                                               {lblue}•·.·''·.·•·.·''·.·•{DEFAULT}
                                                 {YELLOW}BY: {RED}AsHfIEXE {RED}<Cypher>{DEFAULT} 
                                               {lblue}•·.·''·.·•·.·''·.·•{DEFAULT}
           {GREEN2}GitHub Profile{y}{RED} : {DEFAULT}{YELLOW}https://github.com/AsHfIEXE{DEFAULT}               
       {GREEN2}LinkedIn Profile{y}{RED} : {DEFAULT}{YELLOW}https://www.linkedin.com/in/salehinashfi{DEFAULT}
  
'''.format(RED=RED, BRED=BRED, CYAN=CYAN, GREEN=GREEN, DEFAULT=DEFAULT ,YELLOW=YELLOW, BLINK=BLINK, GREEN2=GREEN2, YELLOW2=YELLOW2, lred=lred, lyellow=lyellow, Magenta=Magenta, y=y, lblue=lblue))

def sbanner():
    RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2, BRED= '\033[1;31m', '\033[46m', '\033[1;36m', '\033[1;32m', '\033[0m' , '\033[1;33m' , '\033[1;93m', '\033[1;92m',"\033[5;35m"
    lred,blink,lyellow,lblue="\033[91m",'\033[5m',"\033[93m","\033[94m"
    Magenta = "\033[1;34m"
    y = '\033[1;33m'
    print(r'''
  ██████╗██╗   ██╗██████╗ ██╗  ██╗███████╗██████╗ 
  ██╔════╝╚██╗ ██╔╝██╔══██╗██║  ██║██╔════╝██╔══██╗
  ██║      ╚████╔╝ ██████╔╝███████║█████╗  ██████╔╝
  ██║       ╚██╔╝  ██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
  ╚██████╗   ██║   ██║     ██║  ██║███████╗██║  ██║
   ╚═════╝   ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

                                               {lblue}•·.·''·.·•·.·''·.·•{DEFAULT}
                                                 {YELLOW}BY: {RED}AsHfIEXE {RED}<Cypher>{DEFAULT} 
                                               {lblue}•·.·''·.·•·.·''·.·•{DEFAULT}
           {GREEN2}GitHub Profile{y}{RED} : {DEFAULT}{YELLOW}https://github.com/AsHfIEXE{DEFAULT}               
       {GREEN2}LinkedIn Profile{y}{RED} : {DEFAULT}{YELLOW}https://www.linkedin.com/in/salehinashfi{DEFAULT}
  
'''.format(RED=RED, WHITE=WHITE, CYAN=CYAN, GREEN=GREEN, DEFAULT=DEFAULT ,YELLOW=YELLOW, blink=blink, GREEN2=GREEN2, YELLOW2=YELLOW2, lred=lred, lyellow=lyellow, Magenta=Magenta, BRED=BRED, y=y, lblue=lblue))

def end():
    RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2, BRED= '\033[1;91m', '\033[46m', '\033[1;36m', '\033[1;32m', '\033[0m' , '\033[1;33m' , '\033[1;93m', '\033[1;92m',"\033[5;35m"
    blink='\033[5m'
    Magenta = "\033[1;34m"
    y = '\033[1;33m'
    print(r'''
  ██████╗██╗   ██╗██████╗ ██╗  ██╗███████╗██████╗ 
  ██╔════╝╚██╗ ██╔╝██╔══██╗██║  ██║██╔════╝██╔══██╗
  ██║      ╚████╔╝ ██████╔╝███████║█████╗  ██████╔╝
  ██║       ╚██╔╝  ██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
  ╚██████╗   ██║   ██║     ██║  ██║███████╗██║  ██║
   ╚═════╝   ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

                                                                                                        {0}<Cypher> {5}BY: {0}AsHfIEXE
                                                                                    {0}[[{6}{2}*{4}{0}]] {7}IF YOU LIKE THIS TOOL, THEN PLEASE HELP TO BECOME BETTER.       
                                                                                    {0}[[{6}{2}*{4}{0}]] {7}PLEASE LET ME KNOW , IF ANY PROBLEM IN THIS. 
                                                                                    {0}[[{6}{2}*{4}{0}]] {7}MAKE PULL REQUEST, LET US KNOW YOU SUPPORT US. 
                                                                                    {0}[[{6}{2}*{4}{0}]] {7}IF YOU HAVE ANY IDEA, THEN JUST LET ME KNOW .   
                                                                                    {0}[[{6}{2}*{4}{0}]] {7}PLEASE DON'T HARM ANYONE , IT'S ONLY FOR EDUCATIONAL PURPOSE.
                                                                                    {0}[[{6}{2}*{4}{0}]] {7}WE WILL NOT BE RESPONSIBLE FOR ANY MISUSE OF THIS TOOL.  
                                                                                    {0}[[{6}{2}*{4}{0}]] {7}THANKS FOR USE THIS TOOL. {0}"HAPPY HACKING ... GOOD BYE" {4}
                       
                                                                                          {7}GitHub Profile{6}{0} : {4}{5}https://github.com/AsHfIEXE{4}
                                  
                                                                                       {7}LinkedIn Profile{6}{0} : {4}{5}https://www.linkedin.com/in/salehinashfi
                             
'''.format(RED=RED, BRED=BRED, CYAN=CYAN, GREEN=GREEN, DEFAULT=DEFAULT ,YELLOW=YELLOW, blink=blink, GREEN2=GREEN2, Magenta=Magenta, y=y))
    
def android_end():
    RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2, BRED= '\033[1;91m', '\033[46m', '\033[1;36m', '\033[1;32m', '\033[0m' , '\033[1;33m' , '\033[1;93m', '\033[1;92m',"\033[5;35m"
    blink='\033[5m'
    Magenta = "\033[1;34m"
    y = '\033[1;33m'
    print(r'''
  ██████╗██╗   ██╗██████╗ ██╗  ██╗███████╗██████╗ 
  ██╔════╝╚██╗ ██╔╝██╔══██╗██║  ██║██╔════╝██╔══██╗
  ██║      ╚████╔╝ ██████╔╝███████║█████╗  ██████╔╝
  ██║       ╚██╔╝  ██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
  ╚██████╗   ██║   ██║     ██║  ██║███████╗██║  ██║
   ╚═════╝   ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

                        {0}<Cypher> {5}BY: {0}AsHfIEXE
    {0}[[{6}{2}*{4}{0}]] {7}IF YOU LIKE THIS TOOL, THEN PLEASE HELP TO BECOME BETTER.
    {0}[[{6}{2}*{4}{0}]] {7}PLEASE LET ME KNOW , IF ANY PROBLEM IN THIS.
    {0}[[{6}{2}*{4}{0}]] {7}MAKE PULL REQUEST, LET US KNOW YOU SUPPORT US.
    {0}[[{6}{2}*{4}{0}]] {7}IF YOU HAVE ANY IDEA, THEN JUST LET ME KNOW .
    {0}[[{6}{2}*{4}{0}]] {7}PLEASE DON'T HARM ANYONE, IT'S ONLY FOR EDUCATIONAL PURPOSE.
    {0}[[{6}{2}*{4}{0}]] {7}WE WILL NOT BE RESPONSIBLE FOR ANY MISUSE OF THIS TOOL.
    {0}[[{6}{2}*{4}{0}]] {7}THANKS FOR USE THIS TOOL. {0}"HAPPY HACKING ... GOOD BYE" {4}

                 {7}GitHub Profile{6}{0} : {4}{5}https://github.com/AsHfIEXE{4}
              {7}LinkedIn Profile{6}{0} : {4}{5}https://www.linkedin.com/in/salehinashfi

'''.format(RED=RED, BRED=BRED, CYAN=CYAN, GREEN=GREEN, DEFAULT=DEFAULT ,YELLOW=YELLOW, blink=blink, GREEN2=GREEN2, Magenta=Magenta, y=y))
