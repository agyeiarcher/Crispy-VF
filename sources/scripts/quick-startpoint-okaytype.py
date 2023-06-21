# quick and dirty auto start points 
# set a command+shift+t keyboard shortcut to match prepolator

def getKey1(item): return item[1]
def getKey0(item): return item[0]

g = glyph = CurrentGlyph()

g.prepareUndo("Lazy Startpoint")

for contour in g:
	points = []
	for segment in contour:
		segment.selected = False
		for point in segment:
			point.selected = False
			points.append((point.x, point.y, point))
	points = sorted(points, key=getKey0)
	points = sorted(points, key=getKey1)
	p = points[0][2]
	p.selected = True
	for segment in contour:
	    for point in segment:
	        if point.selected == True:
	            startSegment = (segment.index + 1) % len(contour) 
	            contour.setStartSegment(startSegment)
	            point.selected = False

g.performUndo()