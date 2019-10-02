#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  console.py
#  
#  Copyright 2019 Takehito Tanaka <takeh.tanaka@gmail.com>
#  

import serial
import io

port='/dev/ttyACM0'
baurate=9600

ser = serial.Serial(port, baurate, timeout=10)

i = 0 
while i < 2: 
    a,b,c = str(ser.readline()).split(",")
    hum = int(a[2]+a[3]+a[4])
    temp = float(b[0]+b[1]+b[2]+b[3])
    print(hum, temp)
    i=i+1

ser.close()


