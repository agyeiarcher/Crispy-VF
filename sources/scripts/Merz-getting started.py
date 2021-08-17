import vanilla
import merz

class GlyphVisualizer:

    def __init__(self):
        myGlyph = CurrentGlyph()

        self.w = vanilla.FloatingWindow((300, 400), "Glyph Visualizer", minSize=(200, 300))
        self.merzView = merz.MerzView("auto")

        self.w.stack = vanilla.VerticalStackView(
            (0, 0, 0, 0),
            views=[dict(view=self.merzView)],
            edgeInsets=(15, 15, 15, 15)
        )
        container = self.merzView.getMerzContainer()

        # a layer for the glyph and the baseline
        groupLayer = container.appendBaseSublayer(
            size=(myGlyph.width, myGlyph.font.info.unitsPerEm),
            backgroundColor=(1, 1, 1, 1)
        )

        glyphLayer = groupLayer.appendPathSublayer(
            position=(0, -myGlyph.font.info.descender)
        )
        glyphPath = myGlyph.getRepresentation("merz.CGPath")
        glyphLayer.addScaleTransformation(0.2, name='scale', center=(0,0))
        glyphLayer.setPath(glyphPath)
        print(glyphLayer)

        lineLayer = groupLayer.appendLineSublayer(
            startPoint=(0, -myGlyph.font.info.descender),
            endPoint=(myGlyph.width, -myGlyph.font.info.descender),
            strokeWidth=1,
            strokeColor=(1, 0, 0, 1)
        )

        self.w.open()


if __name__ == '__main__':
    GlyphVisualizer()