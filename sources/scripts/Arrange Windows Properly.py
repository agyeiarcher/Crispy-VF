import vanilla
import AppKit

class WindowTabCollector:
    
    windowNames = [        
        "GlyphWindow",
        "FontWindow",
        "SpaceCenter",
        "ScriptingWindow",
        "SingleFontWindow"
    ]
    
    def __init__(self):
        
        self.w = vanilla.Window((180, 300), "Tab Collector")
        y = 10
        
        for name in self.windowNames:
            obj = vanilla.CheckBox((10, y, -10, 22), name)
            setattr(self.w, name, obj)
            y += 30
        
        self.w.resize(180, y + 40)
        
        self.w.collect = vanilla.Button((10, -30, -10, 22), "Collect", callback=self.collectCallback)
        self.w.open()

    def collectCallback(self, sender):
        openWindows = [w for w in AppKit.NSApp().orderedWindows() if hasattr(w, "windowName")]
        windowsMap = dict()
        
        for name in self.windowNames:
            checkBox = getattr(self.w, name)
            if checkBox.get():
                windowsMap[name] = [w for w in openWindows if w.windowName() == name]
        
        for name, windows in windowsMap.items():
            if windows:
                main = windows[0]
                for window in windows[1:]:
                    main.addTabbedWindow_ordered_(window, AppKit.NSWindowAbove)
                
        
WindowTabCollector()