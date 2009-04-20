# Created by Daniel
import sunpath
import math
import sys
import os
import datetime

from svg_util import *


def convert_time(p) :
	minutes = p* 24*60 # minutes per day
	# convert seconds into hour:minute
	m = minutes % 60
	h = (minutes -m) / 60 
	return '%s:%s' % (int(h),int(m))
	
def convert_date(day) :
	d = datetime.date(2009, 1,1)
	delta  = datetime.timedelta(days=day*365)
	d = d+delta
	return d.month, d.day


### [date][time] [azimuth][altitude]

def generate_table(width,height,zone, lat,lon,heading) :
	pt = []
	for x in range(width) :
		month, day = convert_date(float(x)/float(width))
		p=[]
		for y in range(height) :
			time = convert_time(float(y)/float(height))
			
			alt,az = sunpath.sunpath(month,day,time,zone,lat,lon)
			p.append( [ az, math.sin(alt/360.0 * math.pi * 2) ] )	
			#print month, day,time, "**&*", az, math.sin(alt/360.0 * math.pi * 2) 
		pt.append(p)
	return pt
	
def draw_angles(x,y,table) :
	svg = ""
	w = len(table)
	h = len(table[0])

	for date in range(w/2) : # only first 6 months
		for time in range(h) :
			az, alt = table[date][time]
			if alt < 0 : continue
			
			px = x + az #float(time)/float(w) * 1000
			py = y - 100*alt #alt*500
			
			
			t = float(time) / float(h)
			
			svg += circle(px,py,3, 'rgb(%s,255,0)' % ( int( t*255.0) ) )

	# sys.exit(1)
	return svg

def main(argv=None) :
	if len(sys.argv) != 4:
		print "Usage:" + sys.argv[0] + "lat long heading" 
		sys.exit(1)
		
	lat = sys.argv[1]
	lon = sys.argv[2]
	heading = sys.argv[3]
	zone = "EDT"


	svg = svg_header();

		
	# draw a grid

	svg += line(0,500,1000,500,"rgb(20,20,20)")

	for a in range(1,25) :
		svg += line(500+a*20,0,500+a*20,500,"rgb(200,200,200)")
		
	
	svg += line(500,0,500,1000,"rgb(20,20,20)")
	svg += line(1000,0,1000,1000,"rgb(20,20,20)")
	
	# svg += line(1500,0,1500,1000,"rgb(200,200,200)")

	svg += line(250,0,250,500,"rgb(200,200,200)")
	svg += line(0,250,500,250,"rgb(200,200,200)")
	

	table = generate_table(24,24,zone, lat, lon, heading)
	svg += draw_angles(250,250,table)	
	svg += svg_footer()

	print svg	


if __name__ == "__main__":
        sys.exit(main())






