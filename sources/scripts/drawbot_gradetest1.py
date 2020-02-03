size(500,500)
variableFontFolderPath = '../../font/variable_ttf/Crispy[GRAD,wdth,wght]-VF.ttf'
fontName = installFont(variableFontFolderPath)

txt = FormattedString()
txt.append("AB", font=fontName , fontSize=40, fill=(1, 0, 0))
text(txt, (10, 200))