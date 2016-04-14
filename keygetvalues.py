#!/usr/bin/env python
#coding:utf-8


'''
Created on 2016-4-13

author: Gong Jianting

Purpose:input key and dict,output values of the key

'''  

import simplejson
from os import path

def getvalue(dictionary , key , values):
    #get the values searched in the dict by the key
    if key in dictionary.keys():
        values.append(dictionary[key])
    for itemkey in dictionary.keys():
        if isinstance(dictionary[itemkey], dict):
            getvalue(dictionary[itemkey], key, values)
        else:
            pass
    return values


def formatdict(data):
    #United into dict format
    if  not path.isfile(data):  
        try:
            dictionary  = eval(data)   
        except:
            print('It is wrong format!')        
    else:        
        try:
            tempdict = open(data,'r').readlines()
            dictionary  = eval(tempdict[0]) 
        except:
            print('The file does not exist!')  
    return dictionary


if __name__ == "__main__" :
    
    values = []
    print("Please input the dictionary or the file path with dictionary :")
    #dictionary = {'1':{'1':'A','4':'c'},'2':'b','3':{'1':'a','4':'c'}}
    data = input()
    dictionary = formatdict(data)
    print("Please input the key :")
    key = input()  
    value = getvalue(dictionary , key , values)
    print(value)