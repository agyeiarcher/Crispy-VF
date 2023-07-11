#MenuTitle: JSON Pen
# -*- coding: utf-8 -*-

import json

from hashlib import sha256

from defcon import Glyph, Anchor, Component


sync_info_keys = [
    'ascender',
    'capHeight',
    'descender',
    'familyName',
    'italicAngle',
    
    'openTypeHheaAscender',
    'openTypeHheaDescender',
    'openTypeHheaLineGap',
    
    'openTypeOS2StrikeoutPosition',
    'openTypeOS2StrikeoutSize',
    
    'openTypeOS2SubscriptXOffset',
    'openTypeOS2SubscriptXSize',
    'openTypeOS2SubscriptYOffset',
    'openTypeOS2SubscriptYSize',
    
    'openTypeOS2SuperscriptXOffset',
    'openTypeOS2SuperscriptXSize',
    'openTypeOS2SuperscriptYOffset',
    'openTypeOS2SuperscriptYSize',
    
    'openTypeOS2TypoAscender',
    'openTypeOS2TypoDescender',
    'openTypeOS2TypoLineGap',
    
    'openTypeOS2WeightClass',
    'openTypeOS2WidthClass',
    
    'openTypeOS2WinAscent',
    'openTypeOS2WinDescent',
    
    'postscriptBlueFuzz',
    'postscriptBlueScale',
    'postscriptBlueShift',
    'postscriptBlueValues',
    'postscriptFontName',
    'postscriptIsFixedPitch',
    'postscriptUnderlinePosition',
    'postscriptUnderlineThickness',
    'styleName',
    'unitsPerEm',
    'xHeight',
    
    # This info is irrelevant:
    #'macintoshFONDName',
    #'macintoshFONDFamilyID',
    #'openTypeHeadCreated',
    #'openTypeHeadFlags',
    #'openTypeNameDesigner',
    #'openTypeNameDesignerURL',
    #'openTypeNameLicense',
    #'openTypeNameLicenseURL',
    #'openTypeNameManufacturer',
    #'openTypeNameManufacturerURL',
    #'openTypeNameDescription',
    #'openTypeNameSampleText',
    #'openTypeNameUniqueID',
    #'openTypeNameVersion',
    #'openTypeOS2CodePageRanges',
    #'openTypeOS2FamilyClass',
    #'openTypeOS2Panose',
    #'openTypeOS2Selection',
    #'openTypeOS2Type',
    #'openTypeOS2UnicodeRanges',
    #'openTypeOS2VendorID',
    #'postscriptDefaultCharacter',
    #'postscriptForceBold',
    #'postscriptFullName',
    #'postscriptWeightName',
    #'postscriptUniqueID',
    #'styleMapFamilyName',
    #'styleMapStyleName',
    #'trademark',
    #'versionMajor',
    #'versionMinor',
    #'year',
]

def optimizeNumberType(num):
    # Optimize numbers to integer if possible, to avoid running into precision problems.
    # Glyphs stores most numbers as float, and JSON uses double precision.
    if int(num) == float(num):
        return int(num)
    return round(num, 11)


class ConverterGlyph(object):

    def __init__(self, indent=None):
        self.indent = indent
    
    @property
    def as_dict(self):
        '''
The dict representation of the glyph.
        '''
        raise NotImplementedError

    @property
    def json(self):
        '''
The JSON representation of the glyph.
        '''
        # TODO: This could be cached
        return json.dumps(self.as_dict, sort_keys=True, indent=self.indent)
    
    # Digest methods
    
    @property
    def digest(self):
        '''
The calculated :meth:`hashlib.sha256.hexdigest()` of the glyph's JSON representation.
        '''
        return sha256(self.json).hexdigest()
    
    @property
    def visual_digest(self):
        '''
The calculated :meth:`hashlib.sha256.hexdigest()` of the glyph's JSON representation. This variant only uses the visual
characteristics of the glyph, i. e. contours, components, and width.
        '''
        v = self.visual_only
        self.visual_only = True
        digest = sha256(self.json).hexdigest()
        self.visual_only = v
        return digest


class JsonGlyphDF(ConverterGlyph):
    '''
Class to calculate a JSON representation of a :class:`defcon.Glyph` object. Also, it can give you different digests to compare the glyph to other glyphs.

glyph (robofab.RGlyph or defcon.Glyph)
   The glyph object.
visual_only (Boolean)
   If set to True, only include glyph width, outlines and components in the JSON representation. If set to False, include all glyph data.
verbose (Boolean)
   If set to True, empty data sections will be included in the JSON representation (e. g. an empty components list).
indent (Integer or None)
   How many spaces the output should use for formatting. Set to None for no line breaks and no indentation.
include_lib (Boolean)
   Whether to include the glyph lib.
use_ufo3 (Boolean)
   Whether to include the UFO-3-specific extensions.
    '''
    
    def __init__(self, glyph, visual_only=False, verbose=False, indent=None, include_lib=False, use_ufo3=False):
        self.glyph = glyph
        self.visual_only = visual_only
        self.verbose =verbose
        self.indent = indent
        self.include_lib = include_lib
        self.use_ufo3 = use_ufo3
        #self.json = None
    
    @property
    def as_dict(self):
        '''
The dict representation of the glyph.
        '''
        # TODO: This could be cached
        glyph_dict = {}
        
        if not self.visual_only:
            
            anchors = self.anchors
            if anchors or self.verbose:
                glyph_dict['anchors'] = anchors
            
            if self.glyph.name is not None or self.verbose:
                glyph_dict['name'] = self.glyph.name
            
            if self.glyph.unicode or self.verbose:
                glyph_dict['unicode'] = self.glyph.unicode
            
            if self.glyph.unicodes or self.verbose:
                glyph_dict['unicodes'] = self.glyph.unicodes
            
            if self.glyph.note is not None or self.verbose:
                glyph_dict['note'] = self.glyph.note
        
        # Visual data
        
        if self.glyph.width != 0 or self.verbose:
            glyph_dict['width'] = optimizeNumberType(self.glyph.width)
        
        # height is only available in UFO3
        if hasattr(self.glyph, 'height') and self.use_ufo3 and self.glyph.height != 0:
            glyph_dict['height'] = optimizeNumberType(self.glyph.height)
        else:
            if self.verbose:
                glyph_dict['height'] = 0
        
        components = self.components
        if components or self.verbose:
            glyph_dict['components'] = components
        
        contours = self.contours
        if contours or self.verbose:
            glyph_dict['contours'] = contours
        
        # Lib
        
        if self.include_lib:
            lib = self.lib
            if lib or self.verbose:
                glyph_dict['lib'] = lib
        
        return glyph_dict
    
    @property
    def anchors(self):
        anchors = []
        for anchor in self.glyph.anchors:
            anchor_dict = {
                'x': optimizeNumberType(anchor.x),
                'y': optimizeNumberType(anchor.y),
                'name': anchor.name,
                #'color': anchor.color, # UFO 3 only
            }
            if self.use_ufo3 :
                if hasattr(anchor, 'color') and anchor.color is not None:
                    anchor_dict['color'] = anchor.color
                else:
                    if self.verbose:
                        anchor_dict['color'] = None
                if hasattr(anchor, 'identifier') and anchor.identifier is not None:
                    anchor_dict['id'] = anchor.identifier
                else:
                    if self.verbose:
                        anchor_dict['id'] = None
            anchors.append(anchor_dict)
        return anchors
    
    @property
    def components(self):
        components = []
        for c in self.glyph.components:
            t = c.transformation
            # Convert transformation to float for Glyphs
            tf = (optimizeNumberType(t[0]), optimizeNumberType(t[1]), optimizeNumberType(t[2]), optimizeNumberType(t[3]), optimizeNumberType(t[4]), optimizeNumberType(t[5]))
            comp_dict = {
                'ref': c.baseGlyph,
                'transformation': tf,
            }
            components.append(comp_dict)
        return components
    
    @property
    def contours(self):
        contours = []
        for contour in self.glyph:
            contour_dict = []
            if hasattr(contour, 'points'):
                # UFO 2
                points = contour.points
            else:
                # UFO 3
                points = contour
            for point in points:
                point_dict = {
                    'x':      optimizeNumberType(point.x),
                    'y':      optimizeNumberType(point.y),
                    #'type':   point.segmentType, # UFO 3 only
                    'smooth': point.smooth, # Not available in Glyphs
                    'name':   point.name, # Not available in Glyphs
                    #'id':     point.identifier,
                }
                if hasattr(point, 'segmentType'):
                    # UFO 3
                    point_type = point.segmentType
                    if point_type not in ['offCurve', 'offcurve', None]:
                        point_dict['type'] = point_type
                else:
                    # UFO 2
                    point_type = point.type
                    if point_type not in ['offCurve', 'offcurve', None]:
                        point_dict['type'] = point_type
                if self.use_ufo3:
                    if hasattr(point, 'identifier') and point.identifier is not None or self.verbose:
                        # UFO 3
                        point_dict['identifier'] = point.identifier
                # Optional attributes
                if not self.verbose:
                    if not point.smooth:
                        del point_dict['smooth']
                    if not point.name:
                        del point_dict['name']
            
                contour_dict.append(point_dict)
            if contour_dict:
                contours.append(contour_dict)
        return contours
    
    @property
    def lib(self):
        return self.glyph.lib


def getGlyphFromJson(glyph_json):
    glyph_dict = json.load(glyph_json, parse_float=lambda f: round(float(f), 11))
    return getGlyphFromDict(glyph_dict)


def getGlyphFromDict(glyph_dict):
    g = Glyph()
    
    # Set attributes
    
    g.height = glyph_dict.get('height', 0)
    g.lib = glyph_dict.get('lib', {})
    g.name = glyph_dict.get('name', '')
    g.note = glyph_dict.get('note', None)
    g.unicode = glyph_dict.get('unicode', None)
    g.unicodes = glyph_dict.get('unicodes', [])
    g.width = glyph_dict.get('width', 0)
    
    # Draw the outlines with a pen
    pen = g.getPointPen()
    
    for contour in glyph_dict.get('contours', []):
        pen.beginPath()
        for point in contour:
            pen.addPoint(
                (
                    point.get('x'),
                    point.get('y')
                ),
                segmentType = point.get('type', None),
                name = point.get('name', None),
                smooth = point.get('smooth', None),
            )
        pen.endPath()
    
    # Add components
    
    for component in glyph_dict.get('components', []):
        c = Component()
        c.baseGlyph = component.get('ref', '')
        c.transformation = component.get('transformation', (1, 0, 0, 1, 0, 0))
        g.appendComponent(c)
    
    # Add anchors
    
    for anchor in glyph_dict.get('anchors', []):
        a = Anchor(anchorDict = anchor)
        g.appendAnchor(a)
    
    # Return the completed glyph object
    
    return g


class JsonFontInfo(object):
    '''
Class to calculate a JSON representation of a :class:`defcon.Font.info` or :class:`robofab.Font.info` object.

font (robofab.RFont or defcon.Font)
   The font object.
layer_name (String)
   The name of the requested font layer.
indent (Integer or None)
   How many spaces the output should use for formatting. Set to None for no line breaks and no indentation.
    '''
    def __init__(self, font, layer_name='public.default', indent=None):
        self.font = font
        self.layer_name = layer_name
    
    @property
    def as_dict(self):
        '''
The dictionary representation of the font info data.
        '''
        if self.layer_name == 'public.default':
            return {key: value for key, value in self.font.info.iteritems()}
        else:
            all_layer_info = self.font.lib.get('de.kutilek.layerinfo', {})
            layer_info = all_layer_info.get(self.layer_name, {})
            return {key: value for key, value in layer_info.iteritems()}
    
    @property
    def json(self):
        '''
The JSON representation of the font info data.
        '''
        return json.dumps(self.as_dict, sort_keys=True, indent=self.indent)


def updateFontInfoFromDict(font, layer_name, json_data):
    '''
Update the font info in the supplied :class:`defcon.Font` or :class:`robofab.Font` with data from a dictionary.

font (RFont)
   The font object.
layer_name (String)
   The requested layer name.
json_data
   The JSON data as dictionary.
    '''
    if layer_name == 'public.default':
        for key, value in json_data.iteritems():
            setattr(font.info, key, value)
        #keys_to_delete = list(set(font.info) - set(json_data))
        #print 'Delete keys from font info:', keys_to_delete
        #print '(Not actually deleting them for now)'
        #for key in keys_to_delete:
        #    del font.info[key]
    else:
        if not 'de.kutilek.layerinfo' in font.lib:
            font.lib['de.kutilek.layerinfo'] = {}
        # The info dict is replaced by the new one, i.e. data that is not present
        # in the new dict is discarded.
        font.lib['de.kutilek.layerinfo'][layer_name] = {
            key: value for key, value in json_data.iteritems()
        }


class JsonKerning(object):
    '''
Class to calculate a JSON representation of a :class:`defcon.Font.kerning` or :class:`robofab.Font.kerning` and groups objects.

font (robofab.RFont or defcon.Font)
   The font object.
indent (Integer or None)
   How many spaces the output should use for formatting. Set to None for no line breaks and no indentation.
    '''
    def __init__(self, font, indent=None):
        self.font = font
    
    @property
    def as_dict(self):
        groups = {key: value for key, value in self.font.groups.iteritems()}
        kerning = {key: value for key, value in self.font.kerning.iteritems()}
        return {
            'groups': groups,
            'kerning': kerning,
        }
    
    @property
    def json(self):
        return json.dumps(self.as_dict, sort_keys=True, indent=self.indent)


def updateKerningFromDict(font, json_data):
    '''
Update the kerning in the supplied :class:`defcon.Font` or :class:`robofab.Font` with data from a dictionary.

font (RFont)
   The font object.
json_data
   The JSON data as dictionary.
    '''
    groups = json_data.get('groups', {})
    kerning = json_data.get('kerning', {})
    
    #for key, value in groups:
    #    font.groups
    # FIXME



if __name__ == '__main__':
	from robofab.world import CurrentFont
    #from defcon import Font
    
    verbose = False
    
    f = CurrentFont()
    
    g = JsonGlyphDF(f['B'], verbose=verbose, indent=3)
    print '\nJSON for "B":'
    print g.json
    
    g = JsonGlyphDF(f['A'], verbose=verbose, indent=3)
    print '\nJSON for "A":'
    print g.json
    print 'Digest:         ', g.digest
    print 'Digest (Visual):', g.visual_digest