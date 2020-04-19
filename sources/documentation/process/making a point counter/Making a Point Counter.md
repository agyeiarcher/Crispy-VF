# Making a points counter

I started working on this 3D extrusion thing for a variable font project I'm working on, and ran into a snag: because of the 100+ masters that I'd be ultimately working with, I had no sustainable way of checking for point compatibility across their glyphs. A simple point counter would work, but what would be ideal is if I could see this as some kind of report on all the glyphs, on the fly.

A lot of recommendations for existing tools came up, which I was grateful for, but as soon as I sat with the problem I decided I wanted to make my own. I haven't been writing nearly enough Python, and I haven't been learning vanilla as aggressively as I said I'd wanted to (Vanilla is a wrapper that allows users to make GUIs with python).

### 1. The Basic Core of the Thing / Complexity Won't Hurt

So, technically, I don't need to make a GUI for this at all. It would be fine if I just made a script that generated an output window that gave me the report I wanted. I mention the output window thing as I type this, which gives some insight into how my brain works, but even without it, making a tool to count the points in a specific glyph across multiple masters should not be hard. The processs can be simple described as:
1. Access that specific glyph
2. For every contour, in each one of those glyphs, count the points. *On/Offcurve status isn't our business in this instance, and that's because this font hasn't got any curves. Still not sure it'd be useful for this if it did though.*

Two steps, easy enough. In weird not-really-code:

for each font in the list of fonts that are open (AllFonts()), 
for each glyph with the same name as the glyph we're looking at now,
*start a counter at 0*
for every contour in each of these glyphs,
Add one to the counter for each point in each counter in each glyph

It's helpful to take a look at the FontParts object model. it's really useful, and if you stare at it for long it enough, bam, it makes sense. Give it a go.

In Python, a simple function to get this is:

	def getReport(fontsList):
	    report = ""
	    for fonts in fontsList:
	        #you can look up RFont in the FontParts documentation to see more things you can do with this 
	        for glyph in fonts: 
	            #you can look up RGlyph in the FontParts documentation to see more things you can do with this
	            if glyph.name == g.name:
	                i=0
	                for contour in glyph:
	                    for p in contour.points:
	                        i+=1 #add 1 to i every time you encounter a point, done for each counter in the specified glyph
	                report+= f"{glyph.name} in {fonts.info.styleName} has {i} points \n"
	    return report

This should return something like:

	ydieresis in Bold has 18 points 
	ydieresis in Light has 18 points 
	ydieresis in Regular has 18 points 
	ydieresis in Medium has 18 points 
	ydieresis in Semibold has 18 points 
	ydieresis in Black has 18 points 

Technically, this is the work done here. We could use the Output window to generate this on a shortcut, which is really closer to the workflow I'm accustommed to, but it has the potential to limit the things I get to explore, if I only respond to fixing the immediate problem as quickly as possible.

I decided this would make a nice thing to be visualised. Immediately, we could just throw it into a vanilla window with a textBox to make:

	from vanilla import *
	
	af = AllFonts()
	g = CurrentGlyph()
	
	def getReport(fontsList):
	    report = ""
	    for fonts in fontsList:
	        #you can look up RFont in the FontParts documentation to see more things you can do with this 
	        for glyph in fonts: 
	            #you can look up RGlyph in the FontParts documentation to see more things you can do with this
	            if glyph.name == g.name:
	                i=0
	                for contour in glyph:
	                    for p in contour.points:
	                        i+=1 #add 1 to i every time you encounter a point, done for each counter in the specified glyph
	                report+= f"{glyph.name} in {fonts.info.styleName} has {i} points \n"
	    return report
	
	class PointCounter(object):
	    def __init__(self):
	        self.w = FloatingWindow((300, 22*len(af)), "Points Counter")  
	        self.w.PointsReport = TextBox((10, 10, -10, 20*len(af)), getReport(af), alignment='left')
	        #i made the height of the text box here relative to the amount of fonts open. not sustainable, should do something scrollable        
	        self.w.open()
	
	PointCounter()

And that would give:

![](screenshot-basictextoutput.png)

And this is fine, and yes, it technically does what I need. But, it would be better with a few improvements: **firstly**, it would be good for these masters to be flagged for compatibility. This would mean most likely checking glyphs against an average of compatibility. So, if a glyph isn't compatible with most of the glyphs, it shouyld get flagged. It'll likely also have an aberrant point count, but in a list of 100+ masters (which is where this may end up) that would get unwieldy. **Second**, the textbox used is currently infeasible for a very large number of masters, because my current method expands the window and textbox relative to the amount of open fonts. Bad idea. Something scrollable should get implemented. **Finally**, a list view would feel a little sleeker, with the option to click to go to a specific glyph to investigate further. Extra credit could be flagging abberant points (which would likely make use of the points index (thanks, [Erik!](https://twitter.com/i/status/1251321655076454401))) with some visualisation. 

It's not the only thing I'm working on, and the effect I'm trying to diagnose with this tool isn't mandatory for my project's completion, so I'm giving myself a couple hours every evening to work on it, to complete in a week. Will track changes and update this text and the accompanying code with Git.