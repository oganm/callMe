#! /usr/bin/env python3


# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 19:51:53 2015

@author: omancarci
"""
import configparser

config = configparser.ConfigParser()

config['gmailInfo'] = {'senderMail': '',
                       'receiverMail': '',
                       'password': '',
                       'message': ''}

config['piConfig'] = {'buttonIn' : '',
                      'lightOut' : ''}                       
with open(".config",'w') as configFile:
    config.write(configFile)
