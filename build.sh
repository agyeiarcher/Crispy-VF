OUTPUT_DIR=build_output
#SOURCE_DIR=source
#
rm $OUTPUT_DIR -rf
mkdir $OUTPUT_DIR

#for src in $SOURCE_DIR/*.glyphs
#do
#  fontmake -g $src -o ttf -i --output-dir $OUTPUT_DIR/
#done

#for font in $OUTPUT_DIR/*.ttf
#do
#  gftools fix-nonhinting $font $font
#  gftools fix-dsig $font --autofix
#done

## Cleanup gftools mess:
#rm $OUTPUT_DIR/*-backup-fonttools-prep-gasp.ttf

cp fonts/KRSPY-WEIGHWIDTHGRADE-XYT.ttf $OUTPUT_DIR
#cp METADATA.pb $OUTPUT_DIR
#cp DESCRIPTION.*.html $OUTPUT_DIR

export OPTIONS="--no-progress"
export OPTIONS="$OPTIONS --exclude-checkid /check/ftxvalidator" # We lack this on Travis.
export OPTIONS="$OPTIONS --exclude-checkid /check/metadata" # Comment this out after creating a METADATA.pb file.
export OPTIONS="$OPTIONS --exclude-checkid /check/description" # Comment this out after creating a DESCRIPTION.en_us.html file.
# export OPTIONS="$OPTIONS --exclude-checkid /check/varfont" # Comment this out when making a variable font.
export OPTIONS="$OPTIONS --loglevel INFO --ghmarkdown Fontbakery-check-results.md"
fontbakery check-googlefonts $OPTIONS $OUTPUT_DIR/*.ttf
