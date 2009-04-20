# Created by Daniel
import sunpath
import math
import sys
import os
import datetime
import colorsys

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
			p.append( [ az, alt ] ) # math.sin(float(alt)/360.0 * math.pi * 2) ] )	
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
			if alt > 90 : continue
			
			px = x + az #float(time)/float(w) * 1000
			py = y - 2*alt #alt*500
			
			hue = 0.2 * float(time) / float(h)
			s = 0.4 + 0.6 * float(date) / float(w/2)
			rgb = colorsys.hsv_to_rgb(hue,s,1.0)
			c = 'rgb(%s,%s,%s)' % ( int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255) )			
			svg += circle(px,py,3, c)

	return svg

def draw_hours(x,y,table) :
	svg = ""
	w = len(table)
	h = len(table[0])

	px = 0
	py = 0

	for time in range(int(h/10)) :
		p = []
		for date in range(w/2):
			az, alt = table[date][time*10]
			if alt < 0 : continue
			
			px = x + az #float(time)/float(w) * 1000
			py = y - 2*alt #alt*500
			p.append( [px,py] )
			
		if len(p) > 0 :	
			svg += path(p, "slategrey")
			
			
			svg += semibold(px,py,10,str(time)) 
	return svg



def main(argv=None) :
	if len(sys.argv) != 4:
		print "Usage:" + sys.argv[0] + "lat long heading" 
		sys.exit(1)
		
	lat = sys.argv[1]
	lon = sys.argv[2]
	heading = sys.argv[3]
	zone = "GMT"


	svg = svg_header();

		
	# draw a grid

	svg += line(0,500,1000,500,"rgb(20,20,20)")



	svg += line(0,250,500,250,"rgb(200,200,200)")
	for i in range(1,4) :
		h = i * 60
		svg += line(0,250-h,500,250-h,"rgb(200,200,200)")

	for i in range(5) :
		a = i*30
		svg += line(250+a,0,250+a,250,"rgb(200,200,200)")
		svg += line(250-a,0,250-a,250,"rgb(200,200,200)")
		
	svg += line(250,0,250,250,"rgb(20,20,20)")
	
	svg += semibold(250,260,12,"N")
	svg += semibold(250+90,260,12,"W")
	svg += semibold(250-90,260,12,"E")
	
	table = generate_table(100,240,zone, lat, lon, heading)
	svg += draw_angles(250,250,table)	
	svg += draw_hours(250,250,table)	
	svg += svg_footer()

	print svg	


if __name__ == "__main__":
        sys.exit(main())






