# Created by Daniel
import sunpath
import math
import sys
import os

from svg_util import *


def draw_angles(x,y,zone,lat,lon,heading) :
	svg = ""

	for m in range(12) :
		month = m+1
		day = 1
		p = []
		
		for hour in range(25):
			alt,az = sunpath.sunpath(month, day, str(hour) + ':00', zone, lat, lon)
			r = 200
			if alt <0 : continue
			py = r * math.sin(alt/360.0 * math.pi * 2)
			px = az
			
			p.append([x+px,y-py])
		svg += path(p,'rgb(%s,0,%s)' % ( m*20, 255-m*20) )

	return svg


def draw_day(x,y, zone,lat,lon) :
	svg = ""

	svg += semibold(x,y,12,"altitude")

	for hour in range(25) :
		svg += semibold(x+hour*20,100,9,str(hour))


	for m in range(12) :
		month = m+1
		day = 1
		p = []
		
		for hour in range(25):
			alt,az = sunpath.sunpath(month, day, str(hour) + ':00', zone, lat, lon)
			r = 200
			if alt <0 : continue
			py = r * math.sin(alt/360.0 * math.pi * 2)
			px = 20*hour
			
			p.append([x+px,y-py])
		svg += path(p,'rgb(%s,0,%s)' % ( m*20, 255-m*20) )

	return svg

def draw_heading(x,y, zone, lat,lon,heading) :
	svg=""
	r = 200

	
	for m in range(12) :
		r = 100 + m*10
		month = m+1
		day = 1
		p = []
		for hour in range(25) :
			alt,az = sunpath.sunpath(month, day, str(hour) + ':00', zone, lat, lon)
			
			if ( alt < 0 ) : continue
			
			x1 = x - r * math.cos(az/360* math.pi * 2)
			y1 = y + r * math.sin(az/360* math.pi * 2)
			p.append( [x1,y1] )
			#svg += circle(x1,y1,3)
		svg += path(p,'rgb(%s,0,%s)' % ( m*20, 255-m*20) )
	

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
	


	#svg += draw_day(500,500,zone,lat,lon)
	
	#svg += draw_heading(250,250,zone,lat,lon,heading)
	
	svg += draw_angles(250,250,zone,lat,lon,heading)
	
	svg += svg_footer()

	print svg	


if __name__ == "__main__":
        sys.exit(main())






