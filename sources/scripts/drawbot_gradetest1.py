nFrames = 143
variableFont = '../../font/variable_ttf/Crispy[GRAD,wdth,wght]-VF.ttf'
margin = 20

for i in range(1, nFrames+1):
    newPage(500,500)
    txt = FormattedString()
    frameDuration(1/24)
    gradeValue = -25
    weightValue = 1000
    phase = (2 * pi * i)/nFrames
    phaseMultiplier = (1 * sin(phase + (0.5 * pi)))
    doublephaseMultiplier = (2 * sin(phase + (0.5 * pi)))
    # this shit right here is praxis. just use this for looping shit, use it everywhere
    phasedGrade = gradeValue * doublephaseMultiplier
    phasedWeight = weightValue * phaseMultiplier
    if phasedWeight > 1:
        txt.append("FAIL", font=variableFont , fontSize=420, lineHeight=height()-(margin*2),align="center", fill=(1, 1, 1), fontVariations = {'wght':2, 'wdth':phasedWeight, 'GRAD':phasedGrade})    
        # print(phasedGrade)
        print(phasedGrade, phasedWeight, i)
        with savedState():
            fill(0)
            stroke(1,0,0)
        fill(0)
        rect(0,0, width(), height())
        textBox(txt, (margin, margin, width()-(margin*2), height()-(margin*2)))


saveImage("gradetest.gif")
        