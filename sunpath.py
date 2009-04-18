#!/usr/bin/env python
# encoding: utf-8
"""
sunpath.py

Created by kevin on 2009-04-18.
"""

import sys
import getopt
import os

help_message = '''
Month Day Time Timezone Lat Lon
example:
7 4 14:30 EDT 42 89
'''

class Usage(Exception):
	def __init__(self, msg):
		self.msg = msg

def main(argv=None):
	argv = sys.argv

	if len(argv) != 7:
		print help_message
		exit(1)

	month 	= argv[1]
	day 		= argv[2]
	time 		= argv[3]
	zone		= argv[4]
	lat			= argv[5]
	lon			= argv[6]
	
	command = './gensky ' + month + ' ' + day + ' ' + time + zone + ' +s -a' + lat + ' -o' + lon 
	result = os.popen(command).read()
	return result

if __name__ == "__main__":
	sys.exit(main())
