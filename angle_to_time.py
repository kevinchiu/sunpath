#!/usr/bin/env python
# encoding: utf-8
"""
angle_to_date.py

Created by kevin on 2009-04-20.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""

import sys
import math
import datetime

help_message = '''
usage: python angle_to_date.py latitude longitude altitude azimuth
'''

def main(argv=None):
	argv = sys.argv
	if len(argv) != 5:
		print help_message
		exit(1)
	
def air_mass(h):
	"""h is altitude
	If we are interested to study how light from a source outside 
	Earth's atmosphere (e.g. the Sun) is affected by the atmosphere 
	we often need to know the air mass X, which is the amount of air 
	between us and the object. When viewing towards zenith (altitude 
	90 degrees) we are looking through one air mass. The air mass 
	increases with decreasing altitude. A good representation is 
	Rozenberg's empirical relation"""
	return 1/(math.sin(h + 0.025 * math.exp(-11*math.sin(h))))

def seconds(d):
	"""return seconds since unix epoch given days since J2000.0"""
	diff = datetime.timedelta(days=d)
	jtime = datetime.datetime(2000,1,1,12,0,0,0,"UTC") + diff
	jtime = time.mktime(jtime.timetuple())
	epoch = time.gmtime()
	return jtime - epoch
	
def day(centuries):
	"""days d from the reference time 2000 January 1, 12h Universal Time (epoch J2000.0)"""
	d = centuries * 36525

def altitude_to_seconds(alt, lon):
	"""convert the altitude of the sun to seconds in a day given longitude"""
		
def angle_to_date(lat, lon, alt, az):
	"""Convert latitude, longitude, altitude, azimuth of observer and 
	Sun to get date in seconds from epoch"""
	pass

if __name__ == "__main__":
	sys.exit(main())
