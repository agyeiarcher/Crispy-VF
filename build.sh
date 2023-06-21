OUTPUT_DIR=font/variable_ttf
SOURCE_DIR=sources/designspaces/WEIGHTWIDTHGRADE/
rm $OUTPUT_DIR
mkdir $OUTPUT_DIR
cp ofl.txt $OUTPUT_DIR/OFL.txt
#cp METADATA.pb $OUTPUT_DIR
#cp DESCRIPTION.*.html $OUTPUT_DIR

	#build source instances - this is really messy and could be a lot better

#robofont -p "sources/designspaces/SOURCE PARAMETRIC MASTERS/generateUFOs.py"

	#run grade matcher script - this is really messy and could be a lot better

#cd sources/designspaces/WEIGHTWIDTHGRADE/
#python matchGrades.py
#cd ..
#cd ..
#cd ..

	#build variable font from designspace file - same. need to get better at shell scripting

#fontmake -m sources/designspaces/WEIGHTWIDTHGRADE/Crispy[GRAD,wdth,wght].designspace -o variable --output-dir $OUTPUT_DIR/

    #rename file without -VF

mv $OUTPUT_DIR/Crispy[GRAD,wdth,wght]-VF.ttf $OUTPUT_DIR/Crispy[GRAD,wdth,wght].ttf

    #test exported variable font file

for font in $OUTPUT_DIR/*.ttf
do
  gftools fix-nonhinting $font $font
  gftools fix-dsig $font --autofix
done

    ## Cleanup gftools mess:
rm $OUTPUT_DIR/*-backup-fonttools-prep-gasp.ttf

export OPTIONS="--no-progress"
export OPTIONS="$OPTIONS --exclude-checkid /check/ftxvalidator" # We lack this on Travis.
export OPTIONS="$OPTIONS --exclude-checkid /check/metadata" # Comment this out after creating a METADATA.pb file.
export OPTIONS="$OPTIONS --exclude-checkid /check/description" # Comment this out after creating a DESCRIPTION.en_us.html file.
#export OPTIONS="$OPTIONS --exclude-checkid /check/varfont" # Comment this out when making a variable font.
export OPTIONS="$OPTIONS --loglevel INFO --ghmarkdown Fontbakery-check-results.md"

fontbakery check-googlefonts $OPTIONS $OUTPUT_DIR/*Crispy[GRAD,wdth,wght].ttf