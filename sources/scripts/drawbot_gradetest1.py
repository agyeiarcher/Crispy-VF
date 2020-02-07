nFrames = 5
variableFont = '../../font/variable_ttf/Crispy[GRAD,wdth,wght]-VF.ttf'
margin = 20

for i in range(1, nFrames):
    newPage(500,500)
    txt = FormattedString()
    frameDuration = 1/24
    gradeValue = -25    
    phase = (2 * pi * i)/nFrames
    phaseMultiplier = (1 * sin(phase + (0.5 * pi)))
    # this shit right here is praxis. just use this for looping shit, use it everywhere
    phasedGrade = gradeValue * phaseMultiplier
    txt.append("TEST", font=variableFont , fontSize=220, lineHeight=height()-(margin*2),align="center", fill=(0, 0, 0), fontVariations = {'wght':1000, 'wdth':2, 'GRAD':phasedGrade})    
    print(phasedGrade)
    with savedState():
        fill(1)
        stroke(1,0,0)
        rect(margin, margin, width()-(margin*2), height()-(margin*2))
    textBox(txt, (margin, margin, width()-(margin*2), height()-(margin*2)))


saveImage("gradetest.gif")
        