OUTPUT_DIR=build_output
SOURCE_DIR= /sources/designspaces/WEIGHTWIDTHGRADE/
#
rm $OUTPUT_DIR -rf
mkdir $OUTPUT_DIR
cp fonts/CRISPY[weight,width,grade].ttf $OUTPUT_DIR
cp ofl.txt $OUTPUT_DIR/OFL.txt
#cp METADATA.pb $OUTPUT_DIR
#cp DESCRIPTION.*.html $OUTPUT_DIR

#build variable font from designspace file

for src in $SOURCE_DIR/*.designspace
do
  fontmake -m $src -o variable -i --output-dir $OUTPUT_DIR/
done

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

fontbakery check-googlefonts $OPTIONS $OUTPUT_DIR/*.ttf
