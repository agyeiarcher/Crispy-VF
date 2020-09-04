from pyNewsApi import PYNEWS

variableFontPath = '/Users/aamacbook/Work Interim/Crispy-VF/font/variable_ttf/Crispy[SRIF,wdth,wght]-VF.ttf'

allCapSpacingString = "HAHBHCHDHEHFHGHHHIHJHKHLHMHNHOHHHPHQHRHSHTHUHVHWHXHYHZH \n OAOBOCODOEOFOGOHOIOJOKOLOMONOOOOOPOQOROSOTOUOVOWOXOYOZO"

randomWordsString = "AARDVARK ABLUTION ACRIMONIOUS ADVENTURES AEOLIAN AFRICA AGAMEMNON AHOY AILERON AJAX AKIMBO ALTRUISM AMERICA ANECDOTE AORTA APTITUDE AQUARIUM ARCADE ASPARTAME ATTRITION AURELIUS AVUNCULAR AWNING AXMINSTER AYERS AZURE BANISHMENT BENIGHTED BHAGAVAD BIBLICAL BJORN BLANCMANGE BOLTON BRUSQUE BURNISH BWANA BYZANTIUM CABBALA CETACEAN CHARLEMAGNE CICERO CLAMOROUS CNIDARIAN CONIFER CRUSTACEAN CTENOID CULLED CYNOSURE CZARINA DALMATIAN DELPHI DHURRIE DINNER DJINN DOCUMENT DRILL DUNLEARY DVORAK DWINDLE DYNAMO EAMES EBULLIENT ECHO EDIFY EELS EFTSOONS EGRESS EHRLICH EINDHOVEN EJECT EKISTICS ELZEVIR EMINENCE ENNOBLE EOCENE EPHEMERAL EQUATOR ERSTWHILE ESTIENNE ETIQUETTE EUCALYPTUS EVERYMAN EWEN EXETER EYELET EZEKIEL FANFARE FEROCIOUS FFESTINIOG FINICKY FJORD FLANDERS FORESTRY FRILLS FURNITURE FYLFOT GARRULOUS GENEROUS GHASTLY GIMLET GLORIOUS GNOMON GOLFER GRIZZLED GUMPTION GWENDOLYN GYMKHANA HARROW HEIFER HINDEMITH HORACE HSI HUBRIS HYBRID IAMBIC IBARRA ICHTHYOLOGY IDENTITY IEVGENY IFRIT IGNITE IHRE IKON ILIAD IMMINENT INNOVATION IOLANTHE IPANEMA IRASCIBLE ISLAND ITALIC IVORY IWIS IXTAPA IYAR IZZARD JANACEK JENSON JITTER JOINERY JR. JUNGIAN KAISER KENILWORTH KHAKI KINDRED KLONDIKE KNOWLEDGE KOHLRABI KRAKEN KUDZU KVETCH KWACHA KYRIE LABRADOR LENT LHASA LINIMENT LLAMA LONGBOAT LUDDITE LYCEUM MANDARIN MBANDAKA MCINTYRE MDINA MENDACIOUS MFG. MG MILLINERY MLLE. MME. MNEMONIC MORIBUND MR. MS. MTN. MUNITIONS MYRA NARRAGANSETT NEFARIOUS NGUYEN NILE NKOSO NNENNA NONSENSE NR. NUNNERY NYACK OARSMAN OBLATE OCULAR ODESSA OEDIPUS OFTEN OGRE OHMS OILERS OKRA OLFACTORY OMINOUS ONEROUS OOGAMOUS OPINE ORNATE OSSIFIED OTHELLO OUBLIETTE OVENS OWLISH OXEN OYSTER OZYMANDIAS PARISIAN PB PD. PENROSE PFENNIG PG. PHARMACY PIROUETTE PLEISTOCENE PNEUMATIC PORRIDGE PP. PRINCIPLE PSALTERY PTARMIGAN PUNDIT PYRRHIC QAID QED QIBRIS QOM QUILL RANSOM RB. RD. RENFIELD RHEUMATIC RINGLET RM. RONSARD RP. RTE. RUNCIBLE RWANDA RYE SALACIOUS SBEITLA SCHERZO SERPENTINE SFORZA SHACKLES SINFUL SJOERD SKULL SLALOM SMELTING SNIPE SORBONNE SPARTAN SQUIRE SRI STULTIFIED SUMMONER SVELTE SWARTHY SYKES SZENTENDRE TARRAGON TBLISI TCHERNY TENNYSON THAUMATURGE TINCTURE TLALOC TOREADOR TREACHEROUS TSUNAMI TURKEY TWINE TYROLEAN TZARA UBIQUITOUS UCELLO UDDER UFOLOGY UGRIC UHLAN UITLANDER UKULELE ULSTER UMBER UNGUENT UOMO UPLIFT URSINE USURIOUS UTRECHT UVULA UXORIOUS UZBEK VANISHED VD. VENOMOUS VINDICATE VORACIOUS VRILLIER VS. VT. VULNERABLE VYING WASHINGTON WENDELL WHARF WINDOW WM. WORTH WRUNG WT. WUNDERMAN WYES XANTHAN XENON XIAO XMAS XRAY XUXA XYLEM YARROW YBARRA YCAIR YDS. YELLOWSTONE YGGDRASIL YIN YLANG YOURS YPSILANTI YQUEM YRS. YS. YTTERBIUM YUNNAN YVONNE ZANZIBAR ZERO ZHORA ZINFANDEL ZONE ZUNI ZWIEBACK ZYGOTE"

spacingStringBox = (40, 0, 690, 500)


def randomHeadline():
    news = PYNEWS()
    data = news.get_headline_by_source(source='google-news')
    return data[randint(0, len(data)-1)]["title"]

def calcTextSizeForBox(txt, box, minSize=5, maxSize=300, tolerance=0.1):
    #this should get refactored for a binary search
    fs = (minSize + maxSize) / 2
    
    fontSize(fs)
    lineHeight(fs)
    overflow = textOverflow(txt, box)
    if overflow:
        while overflow:
            fs += -0.5
            fontSize(fs)
            lineHeight(fs)
            overflow = textOverflow(txt, box)
    else:
        while not overflow:
            fs += 0.5
            fontSize(fs)
            lineHeight(fs)
            overflow = textOverflow(txt, box)
    return fs


def pageLabel(instanceName):
    font("")
    text(str(instanceName), (40, height() - 40))

def makeProof():
    for instanceName, setupMatrix in listNamedInstances(variableFontPath).items():
        newPage("LetterLandscape")
        print(instanceName, setupMatrix)
        pageLabel(instanceName)
        font(variableFontPath)
        fontVariations(wght= setupMatrix['wght'], wdth = setupMatrix['wdth'], SRIF = setupMatrix['SRIF'])
        fs = calcTextSizeForBox(allCapSpacingString, spacingStringBox)
        print(fs)
        fontSize(fs*0.7)
        lineHeight(fs*0.8)
        spacingText = textBox(allCapSpacingString, spacingStringBox, align="left")
        newPage("LetterLandscape")
        pageLabel(instanceName)
        font(variableFontPath)
        fontVariations(wght= setupMatrix['wght'], wdth = setupMatrix['wdth'], SRIF = setupMatrix['SRIF'])
        fs = calcTextSizeForBox(randomHeadline().upper(), spacingStringBox)
        print(fs)
        fontSize(fs*0.7)
        lineHeight(fs*0.8)
        spacingText = textBox(randomHeadline().upper(), spacingStringBox, align="left")
        
makeProof()
# saveImage("Crispy Proof.pdf")