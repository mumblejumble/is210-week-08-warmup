#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Telling you your blood pressure readings"""

MYINPUT = int(raw_input('What is your blood pressure? '))

if MYINPUT <= 89:
    BP_STATUS = 'Low'
elif MYINPUT <= 119:
    BP_STATUS = 'Ideal'
elif MYINPUT <= 139:
    BP_STATUS = 'Warning'
elif MYINPUT <= 159:
    BP_STATUS = 'High'
else:
    BP_STATUS = 'Emergency'

OUTPUT = 'Your status is currently: {}!'.format(BP_STATUS)
print OUTPUT
