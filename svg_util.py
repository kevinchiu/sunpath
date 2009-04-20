#

def svg_header():
	return '<?xml version="1.0" standalone="no"?>\n<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n<svg width="100%" height="100%" version="1.1" xmlns="http://www.w3.org/2000/svg">\n'

def svg_footer():
	return "</svg>"

def circle(x,y,r, color="black"):
	s='<circle cx="%s" cy="%s" r="%s" stroke="%s" fill="%s" stroke-width="1"/>\n' % (x, y, r, color, color)
	return s	

def semibold(x, y, size, text) :
	return '<text x="%s" y="%s" font-family="\'MyriadPro-Semibold\'" font-size="%s">%s</text>\n' % (x,y, size,text)


def line(x1,y1,x2,y2, color="black") :
	return '<line x1="%s" y1="%s" x2="%s" y2="%s" style="stroke:%s;stroke-width:1"/>\n' % (x1,y1,x2,y2,color)

def path(p, color="black") :
	svg = ""
	
	pt = p.pop(0)
	
	svg+='<path d="M%s %s' % ( str(pt[0]), str(pt[1]))
		
	for pt in p :
		svg += 'L%s %s ' % ( str(pt[0]), str(pt[1]))
	
	svg +='" style="fill: none; stroke-width:2; stroke:%s"/>"\n' % color 
	
	return svg