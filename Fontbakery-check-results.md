## Fontbakery report

Fontbakery version: 0.7.14

<details>
<summary><b>[1] Family checks</b></summary>
<details>
<summary>ℹ <b>INFO:</b> Do we have the latest version of FontBakery installed?</summary>

* [com.google.fonts/check/fontbakery_version](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version)
* ℹ **INFO** fontbakery (0.7.17)  - Well designed Font QA tool, written in Python 3
  INSTALLED: 0.7.14
  LATEST:    0.7.17


</details>
<br>
</details>
<details>
<summary><b>[19] Crispy[GRAD,wdth,wght].ttf</b></summary>
<details>
<summary>💔 <b>ERROR:</b> Check variable font instances have correct coordinate values</summary>

* [com.google.fonts/check/varfont_instance_coordinates](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/varfont_instance_coordinates)
* 💔 **ERROR** Failed with KeyError: 'GRAD'
* 🔥 **FAIL** Instance "Condensed Thin" wdth value is "100.0". It should be "75.0" [code: bad-coordinate]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check glyph coverage.</summary>

* [com.google.fonts/check/glyph_coverage](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage)
* 🔥 **FAIL** Missing required codepoints: 0x000D (CARRIAGE RETURN), 0x00AD (SOFT HYPHEN), 0x00B5 (MICRO SIGN), 0x2074 (SUPERSCRIPT FOUR) and 0x20AC (EURO SIGN) [code: missing-codepoints]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Checking OS/2 usWeightClass.</summary>

* [com.google.fonts/check/usweightclass](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/usweightclass)
* 🔥 **FAIL** OS/2 usWeightClass expected value for 'Regular' is 400 but this font has 1.
 GlyphsApp users should set a Custom Parameter for 'Axis Location' in each master to ensure that the information is accurately built into variable fonts. [code: bad-value]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check name table: TYPOGRAPHIC_SUBFAMILY_NAME entries. </summary>

* [com.google.fonts/check/name/typographicsubfamilyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/typographicsubfamilyname)
* 🔥 **FAIL** TYPOGRAPHIC_SUBFAMILY_NAME entry for Win "Cond Thin-MaxGrade" must be "Regular". Please note, since the font style is RIBBI, this record can be safely deleted. [code: bad-win-name]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check variable font instances have correct names</summary>

* [com.google.fonts/check/varfont_instance_names](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/varfont_instance_names)
* 🔥 **FAIL** Instance name "Condensed Semibold" is incorrect. It should be "Condensed" [code: bad-name]
* 🔥 **FAIL** Instance name "Extended Thin" is incorrect. It should be "Thin" [code: bad-name]
* 🔥 **FAIL** Instance name "Extended ExtraLight" is incorrect. It should be "ExtraLight" [code: bad-name]
* 🔥 **FAIL** Instance name "Extended Light" is incorrect. It should be "Light" [code: bad-name]
* 🔥 **FAIL** Instance name "Extended Regular" is incorrect. It should be "Regular" [code: bad-name]
* 🔥 **FAIL** Instance name "Extended Medium" is incorrect. It should be "Medium" [code: bad-name]
* 🔥 **FAIL** Instance name "Extended SemiBold" is incorrect. It should be "SemiBold" [code: bad-name]
* 🔥 **FAIL** Instance name "Extended Bold" is incorrect. It should be "Bold" [code: bad-name]
* 🔥 **FAIL** Instance name "Extended ExtraBold" is incorrect. It should be "ExtraBold" [code: bad-name]
* 🔥 **FAIL** Instance name "Extended Black" is incorrect. It should be "Black" [code: bad-name]
* 🔥 **FAIL** This will cause problems with some of the Google Fonts systems that look up fonts by their style names. This must be fixed! [code: bad-instance-names]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Checking OS/2 Metrics match hhea Metrics.</summary>

* [com.google.fonts/check/os2_metrics_match_hhea](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea)
* 🔥 **FAIL** OS/2 sTypoAscender (1600) and hhea ascent (2000) must be equal. [code: ascender]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Whitespace and non-breaking space have the same width?</summary>

* [com.google.fonts/check/whitespace_widths](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/hmtx.html#com.google.fonts/check/whitespace_widths)
* 🔥 **FAIL** Whitespace and non-breaking space have differing width: Whitespace (uni0020) is 114 font units wide, non-breaking space (uni00A0) is 402 font units wide. Both should be positive and the same. [code: different-widths]

</details>
<details>
<summary>🔥 <b>FAIL:</b> The variable font 'wdth' (Width) axis coordinate must be 100 on the 'Regular' instance.</summary>

* [com.google.fonts/check/varfont/regular_wdth_coord](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/regular_wdth_coord)
* 🔥 **FAIL** The "wdth" coordinate of the "Regular" instance must be 100. Got 300.0 as a default value instead. [code: not-100]

</details>
<details>
<summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
* ⚠ **WARN** OS/2 VendorID value '!666' is not a known registered id. You should set it to your own 4 character code, and register that code with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx [code: unknown]

</details>
<details>
<summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters.</summary>

* [com.google.fonts/check/name/family_and_style_max_length](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length)
* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Crispy Cond Thin-MaxGrade' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]

</details>
<details>
<summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps.</summary>

* [com.google.fonts/check/linegaps](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/hhea.html#com.google.fonts/check/linegaps)
* ⚠ **WARN** OS/2 sTypoLineGap is not equal to 0. [code: OS/2]

</details>
<details>
<summary>⚠ <b>WARN:</b> Does GPOS table have kerning information?</summary>

* [com.google.fonts/check/gpos_kerning_info](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info)
* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]

</details>
<details>
<summary>ℹ <b>INFO:</b> Show hinting filesize impact.</summary>

* [com.google.fonts/check/hinting_impact](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/hinting_impact)
* ℹ **INFO** Hinting filesize impact:

|  | font/variable_ttf/Crispy[GRAD,wdth,wght].ttf |
|:--- | ---:|
| Dehinted Size | 53.7kb |
| Hinted Size | 53.5kb |
| Increase | -152 bytes |
| Change   | -0.3 % |
 [code: size-impact]

</details>
<details>
<summary>ℹ <b>INFO:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
* ℹ **INFO** Could not detect which version of ttfautohint was used in this font. It is typically specified as a comment in the font version entries of the 'name' table. Such font version strings are currently: ['Version 1.000'] [code: version-not-detected]

</details>
<details>
<summary>ℹ <b>INFO:</b> EPAR table present in font?</summary>

* [com.google.fonts/check/epar](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/epar)
* ℹ **INFO** EPAR table not present in font. To learn more see https://github.com/googlefonts/fontbakery/issues/818 [code: lacks-EPAR]

</details>
<details>
<summary>ℹ <b>INFO:</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table set to optimize rendering?</summary>

* [com.google.fonts/check/gasp](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/gasp)
* ℹ **INFO** These are the ppm ranges declared on the gasp table:

PPM <= 65535:
	flag = 0x0F
	- Use grid-fitting
	- Use grayscale rendering
	- Use gridfitting with ClearType symmetric smoothing
	- Use smoothing along multiple axes with ClearType®
 [code: ranges]

</details>
<details>
<summary>ℹ <b>INFO:</b> Check for font-v versioning </summary>

* [com.google.fonts/check/fontv](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fontv)
* ℹ **INFO** Version string is: "Version 1.000"
The version string must ideally include a git commit hash and either a "dev" or a "release" suffix such as in the example below:
"Version 1.3; git-0d08353-release" [code: bad-format]

</details>
<details>
<summary>ℹ <b>INFO:</b> Font contains all required tables?</summary>

* [com.google.fonts/check/required_tables](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/required_tables)
* ℹ **INFO** This font contains the following optional tables [loca, prep, GSUB, gasp, DSIG]

</details>
<details>
<summary>ℹ <b>INFO:</b> Font follows the family naming recommendations?</summary>

* [com.google.fonts/check/family_naming_recommendations](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/family_naming_recommendations)
* ℹ **INFO** Font does not follow some family naming recommendations:

| Field | Value | Recommendation |
|:----- |:----- |:-------------- |
| Postscript Name | Crispy-CondThin-MaxGrade | May contain not more than a single hyphen |
 [code: bad-entries]

</details>
<br>
</details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 1 | 7 | 4 | 31 | 8 | 63 | 0 |
| 1% | 6% | 4% | 27% | 7% | 55% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **PASS**
* **DEBUG**
