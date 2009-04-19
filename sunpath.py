#!/usr/bin/env python
# encoding: utf-8
"""
sunpath.py

Created by kevin on 2009-04-18.
"""

import sys
import getopt
import os
import re

help_message = '''
Month Day Timezone Lat Lon
example:
7 4 EDT 42 89
'''
hours = {}
altitudes = []
azimuths = []
p = re.compile('# Solar altitude and azimuth: (\-?\d*?\.\d*?)\s*?(\-?\d*?\.\d*?)')

class Usage(Exception):
	def __init__(self, msg):
		self.msg = msg

def main(argv=None):
	argv = sys.argv

	if len(argv) != 6:
		print help_message
		exit(1)

	month 	= argv[1]
	day 		= argv[2]
	zone		= argv[3]
	lat			= argv[4]
	lon			= argv[5]
	
	for hour in range(24):
			hours[hour] = sunpath(month, day, str(hour) + ':00', zone, lat, lon)
	print hours
	exit(0)
	
def sunpath(month, day, time, timezone, lat, lon):
	"""get the sun's position as [altitude, azumith]"""
	command = './gensky ' + month + ' ' + day + ' ' + time +  timezone + ' +s -a' + lat + ' -o' + lon 
	result = os.popen(command).read()
	print result
	m = p.search(result)
	if m != None:
		alt = m.group(1)
		az = m.group(2)
		altitudes.append(alt)
		azimuths.append(az)
		return [alt,az]

if __name__ == "__main__":
	sys.exit(main())
