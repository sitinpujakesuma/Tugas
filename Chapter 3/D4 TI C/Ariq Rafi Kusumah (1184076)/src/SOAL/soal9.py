# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 23:57:12 2019

@author: Asus
"""

def NPM9(npm):
    
    i=0
    NPM = input("NPM : ")
    while i<1:
        if len(NPM)<7:
            print("NPM kurang dari 7!")
            NPM = input("NPM : ")
        elif len(NPM)>7:
            print("NPM lebih dari 7!")
            NPM = input("NPM : ")
        else:
            i=1
            
    A=NPM[0]
    B=NPM[1]
    C=NPM[2]
    D=NPM[3]
    E=NPM[4]
    F=NPM[5]
    G=NPM[6]
    
    X=1
    
    for this in A,B,C,D,E,F,G:
        
        if int(this)%2==1:
            print(this,end=" ") 
    
NPM9(npm)