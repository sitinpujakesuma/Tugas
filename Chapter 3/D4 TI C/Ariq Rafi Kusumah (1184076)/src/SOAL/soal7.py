# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 00:01:27 2019

@author: Asus
"""

def NPM7(npm):
    
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
        X*=int(this)
    print(X)
    
NPM7(npm)