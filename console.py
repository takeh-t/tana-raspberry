#!/usr/bin/python3
# -*- coding: utf-8 -*-
#(0
#  console.py
#  
#  Copyright 2014 Takehito Tanaka <takeh-t@tana2133>
#  

import serial
import io

port='/dev/ttyACM0'
baurate=19200

ser = serial.Serial(port, baurate, timeout=10)

line = ser.readline()
print line

ser.close()


