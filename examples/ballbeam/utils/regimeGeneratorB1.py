#!/usr/bin/python2
# -*- coding: utf-8 -*-

import numpy as np
import os

controllerList = ['FController', 'GController', 'JController',\
                'LSSController', 'PIFeedbackController']
parameterList = ['Jb', 'M']
lines = ''

print 'Regimefile Generator'
print 'Choose one of the following parameters: (0-1)'
print parameterList
number = -1
while not(number >= 0 and number <= 4):
    print 'Number: '
    number = input()

parameter = parameterList[number]


# load head file
filePath = os.path.join(os.curdir, 'B_head.sray')
with open(filePath, 'r') as f:
    head = f.read()

lines += '\n'

# how many poles?
if controller == 'PIFeedbackController':
    multiplicator = 5
else:
    multiplicator = 4


if controller == 'FController':
    pole = -3.6
elif controller == 'GController':
    pole = -3
elif controller == 'JController':
    pole == -2
elif controller == 'LSSController':
    pole = -3.3
elif controller == 'PIFeedbackController':
    pole = -1.5

Jb = np.arange(0.5e-6, 10.5e-6, 1e-6)
    
for jb in Jb:
        lines += '- name: B1_' + controller + '_poles(' + str(pole) \
                    + ')_Jb(' + str(jb) + ')\n'
        lines += '  clear previous: !!python/bool False' + '\n'
        lines += '\n'
        lines += '  model:' + '\n'
        lines += '   type: BallBeamModel' + '\n'
        lines += '   Jb: ' + str(jb) + '\n'
        lines += '\n'
        lines += '  controller: ' + '\n'
        lines += '   type: '  + controller + '\n'
        lines += '   poles: ' + str([pole]*multiplicator) + '\n'
        if (controller == 'PIFeedbackController' or controller == 'LSSController'):
            lines += '   r0: 3'
        lines += '\n'

fileName = 'B1_' + controller + '_poles' + str(pole) \
                    + '_Jb(' + str(Jb[0]) + ',' + str(Jb[-1]) + ').sreg'
filePath = os.path.join(os.curdir, fileName)
with open(filePath, 'w') as f:
    f.write(head)    
    f.write(lines)
