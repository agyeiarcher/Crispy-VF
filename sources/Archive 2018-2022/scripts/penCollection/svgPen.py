#MenuTitle: SVG Pen
from fontTools.pens.basePen import BasePen


# See also:
# http://www.w3.org/TR/SVG/paths.html#PathDataBNF
# https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths


# SVG path parsing code from:
# http://codereview.stackexchange.com/questions/28502/svg-path-parsing


def parse_svg_path(path_data):
    digit_exp = '0123456789eE'
    comma_wsp = ', \t\n\r\f\v'
    drawto_command = 'MmZzLlHhVvCcSsQqTtAa'
    sign = '+-'
    exponent = 'eE'
    float = False
    entity = ''
    for char in path_data:
        if char in digit_exp:
            entity += char
        elif char in comma_wsp and entity:
            yield entity
            float = False
            entity = ''
        elif char in drawto_command:
            if entity:
                yield entity
                float = False
                entity = ''
            yield char
        elif char == '.':
            if float:
                yield entity
                entity = '.'
            else:
                entity += '.'
                float = True
        elif char in sign:
            if entity and entity[-1] not in exponent:
                yield entity
                float = False
                entity = char
            else:
                entity += char
    if entity:
        yield entity



def drawSVGPath(pen, path=""):
    """
Draw an SVG path that is supplied as a string. This is limited to SVG paths that contain only elements that can be matched to the usual path elements found in a glyph.
"""
    path_data = list(parse_svg_path(path))
    #print path_data
    i = 0
    prev_x = 0
    prev_y = 0
    while i < len(path_data):
        #print i, path_data[i]
        v = path_data[i]
        if v in "Cc":
            # Cubic curve segment
            x1, y1, x2, y2, x3, y3 = path_data[i+1:i+7]
            #print "    ", x1, y1, x2, y2, x3, y3
            x1 = float(x1)
            y1 = float(y1)
            x2 = float(x2)
            y2 = float(y2)
            x3 = float(x3)
            y3 = float(y3)
            if v == "c":
                x1 += prev_x
                y1 += prev_y
                x2 += prev_x
                y2 += prev_y
                x3 += prev_x
                y3 += prev_y
            pen.curveTo(
                (x1, y1),
                (x2, y2),
                (x3, y3),
            )
            prev_x = x3
            prev_y = y3
            i += 7
        elif v in "Hh":
            # Horizontal line segment
            x = path_data[i+1]
            #print "    ", x
            x = float(x)
            if v == "h":
                x += prev_x
            pen.lineTo((x, prev_y))
            prev_x = x
            i += 2
        elif v in "LlMm":
            # Move or Line segment
            x, y = path_data[i+1:i+3]
            #print "    ", x, y
            x = float(x)
            y = float(y)
            if v in "lm":
                x += prev_x
                y += prev_y
            if v in "Ll":
                pen.lineTo((x, y))
            else:
                pen.moveTo((x, y))
            prev_x = x
            prev_y = y
            i += 3
        elif v in "Qq":
            # Quadratic curve segment
            x1, y1, x2, y2 = path_data[i+1:i+5]
            #print "    ", x1, y1, x2, y2
            x1 = float(x1)
            y1 = float(y1)
            x2 = float(x2)
            y2 = float(y2)
            if v == "q":
                x1 += prev_x
                y1 += prev_y
                x2 += prev_x
                y2 += prev_y
            pen.qCurveTo(
                (x1, y1),
                (x2, y2),
            )
            prev_x = x2
            prev_y = y2
            i += 5
        elif v in "Vv":
            # Vertical line segment
            y = path_data[i+1]
            #print y
            y = float(y)
            if v == "v":
                y += prev_y
            pen.lineTo((prev_x, y))
            prev_y = y
            i += 2
        elif v in "Zz":
            pen.closePath()
            i += 1
        else:
            print "SVG path element '%s' is not supported for glyph paths." % path_data[i]
            break


class SVGpen(BasePen):
    def __init__(self, glyphSet, round_coordinates=False, relative_coordinates=False, optimize_output=False):
        """
A pen that converts a glyph outline to an SVG path. After drawing, SVGPen.d contains the path as string. This corresponds to the SVG path element attribute "d".

   glyphSet (RFont or GSFont)      The font object
   round_coordinates (Boolean)     Round all coordinates to integer. Default is False.
   relative_coordinates (Boolean)  Store all coordinates as relative. Default is False, i.e. choose whichever notation (absolute or relative) produces shorter output for each individual segment.
   optimize_output (Boolean)       Make the output path string as short as possible. Default is True. Setting this to False also overrides the relative_coordinates option.
        """
        self._rnd = round_coordinates
        self._rel = relative_coordinates
        self._opt = optimize_output
        self.prev_x = 0
        self.prev_y = 0
        BasePen.__init__(self, glyphSet)
        self.d = ''
    
    def reset(self):
        self.d = ''
        
    def _append_shorter(self, absolute, relative):
        if not self._rel and len(absolute) <= len(relative) or not self._opt:
            self.d += absolute
        else:
            self.d += relative
    
    def _get_shorter_sign(self, value):
        if value < 0 and self._opt:
            return '%s' % value
        else:
            return ' %s' % value
    
    def _moveTo(self, (x,y)):
        if self._rnd:
            a = 'M%s' % int(round(x))
            a += self._get_shorter_sign(int(round(y)))
        else:
            a = 'M%s' % x
            a += self._get_shorter_sign(y)
        self.d += a
        self.prev_x = x
        self.prev_y = y
    
    def _lineTo(self, (x,y)):
        if y == self.prev_y:
            if self._rnd:
                a = 'H%d' % (int(round(x)))
                r = 'h%d' % (int(round(x - self.prev_x)))
            else:
                a = 'H%s' % (x)
                r = 'h%s' % (x - self.prev_x)
        elif x == self.prev_x:
            if self._rnd:
                a = 'V%d' % (int(round(y)))
                r = 'v%d' % (int(round(y - self.prev_y)))
            else:
                a = 'V%s' % (y)
                r = 'v%s' % (y - self.prev_y)
        else:
            if self._rnd:
                a = 'L%d' % int(round(x))
                a += self._get_shorter_sign(int(round(y)))
                r = 'l%d' % int(round(x - self.prev_x))
                r += self._get_shorter_sign(int(round(y - self.prev_y)))
            else:
                a = 'L%s' % x
                a += self._get_shorter_sign(y)
                r = 'l%s' % (x - self.prev_x)
                r += self._get_shorter_sign(y - self.prev_y)
        self._append_shorter(a, r)
        self.prev_x = x
        self.prev_y = y
    
    def _curveToOne(self, (x1,y1), (x2,y2), (x3,y3)):
        if self._rnd:
            a = 'C%s' % int(round(x1))
            for coord in [
                                int(round(y1)),
                int(round(x2)), int(round(y2)),
                int(round(x3)), int(round(y3))
            ]:
                a += self._get_shorter_sign(coord)
            r = 'c%s' % int(round(x1 - self.prev_x))
            for coord in [
                                              int(round(y1 - self.prev_y)),
                int(round(x2 - self.prev_x)), int(round(y2 - self.prev_y)),
                int(round(x3 - self.prev_x)), int(round(y3 - self.prev_y))
            ]:
                r += self._get_shorter_sign(coord)
        else:
            a = 'C%s' % x1
            for coord in [y1, x2, y2, x3, y3]:
                a += self._get_shorter_sign(coord)
            r = 'c%s' % (x1 - self.prev_x)
            for coord in [
                                  y1 - self.prev_y,
                x2 - self.prev_x, y2 - self.prev_y,
                x3 - self.prev_x, y3 - self.prev_y
            ]:
                r += self._get_shorter_sign(coord)
        self._append_shorter(a, r)
        self.prev_x = x3
        self.prev_y = y3
    
    def _closePath(self):
        self.d += u'z'
