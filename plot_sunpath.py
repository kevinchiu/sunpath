# Created by Daniel
import sunpath
import math


def svg_header():
	return '<?xml version="1.0" standalone="no"?>\n<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n<svg width="100%" height="100%" version="1.1" xmlns="http://www.w3.org/2000/svg">\n'

def svg_footer():
	return "</svg>"

def circle(x,y,r, color="black"):
	s='<circle cx="%s" cy="%s" r="%s" stroke="%s" fill="%s" stroke-width="1"/>\n' % (x, y, r, color, color)
	return s	

def semibold(x, y, size, text) :
	return '<text x="%s" y="%s" font-family="\'MyriadPro-Semibold\'" font-size="%s">%s</text>\n' % (x,y, size,text)

def draw(day,month,zone,lat,long, color):
	x = 400;
	y = 400;
	svg = ""
	for hour in range(24):
		alt,az = sunpath.sunpath(month, day, str(hour) + ':00', zone, lat, lon)
	
		if alt < 0 : continue
	
		r = 200
	
		y1 = y - r * math.sin(alt/360.0 * math.pi * 2)
		x1 = 20* hour
	
		svg += circle(x1,y1,3, color)
		svg += semibold(x1+5,100,9,str(hour))
	
		az -= 90
	
		r = 200 + 5 * month
	
		x1 = x + 600 - r * math.cos(az/360* math.pi * 2)
		y1 = y + r * math.sin(az/360* math.pi * 2)
	
		svg += circle(x1,y1,3, color)

	return svg

svg = svg_header()


day = 18
month = 6
zone = "EDT"
lat = 42
lon = 71

x = 400
y = 400

svg += '<line x1="1000" y1="00" x2="1000" y2="800" style="stroke:rgb(200,200,200);stroke-width:1"/>\n'
svg += '<line x1="400" y1="00" x2="400" y2="800" style="stroke:rgb(200,200,200);stroke-width:1"/>\n'

svg += '<line x1="00" y1="400" x2="800" y2="400" style="stroke:rgb(200,200,200);stroke-width:1"/>\n'
svg += '<line x1="00" y1="200" x2="800" y2="200" style="stroke:rgb(200,200,200);stroke-width:1"/>\n'


svg += semibold(x,y,14,"altitude")
svg += semibold(x+600,y,14,"azimuth")

svg += draw(18,6,"EDT",42,71,"black")
svg += draw(18,12,"EDT",42,71,"red")
svg += draw(18,3,"EDT",42,71,"blue")
svg += draw(18,9,"EDT",42,71,"green")
	
svg += svg_footer()

print svg