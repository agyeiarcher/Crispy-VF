af = AllFonts()
for f in af:
    f["nbspace"].width = f["space"].width
    f["nbspace"].changed()
    f.save()