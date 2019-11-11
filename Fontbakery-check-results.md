## Fontbakery report

Fontbakery version: 0.7.14

<details>
<summary><b>[1] Family checks</b></summary>
<details>
<summary>ℹ <b>INFO:</b> Do we have the latest version of FontBakery installed?</summary>

* [com.google.fonts/check/fontbakery_version](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version)
* ℹ **INFO** fontbakery (0.7.15)  - Well designed Font QA tool, written in Python 3
  INSTALLED: 0.7.14
  LATEST:    0.7.15


</details>
<br>
</details>
<details>
<summary><b>[19] Crispy[GRAD,wdth,wght].ttf</b></summary>
<details>
<summary>💔 <b>ERROR:</b> Check variable font instances have correct coordinate values</summary>

* [com.google.fonts/check/varfont_instance_coordinates](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/varfont_instance_coordinates)
* 💔 **ERROR** Failed with KeyError: 'GRAD'
* 🔥 **FAIL** Instance "100 Wide MaxGrade" wdth value is "400.0". It should be "100.0" [code: bad-coordinate]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Checking OS/2 fsType.</summary>

* [com.google.fonts/check/fstype](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fstype)
* 🔥 **FAIL** OS/2 fsType is a legacy DRM-related field.
In this font it is set to 264 meaning that:
The font may be embedded but must only be installed temporarily on other systems.The font may not be subsetted prior to embedding.

No such DRM restrictions can be enabled on the Google Fonts collection, so the fsType field must be set to zero (Installable Embedding) instead.
Fonts with this setting indicate that they may be embedded and permanently installed on the remote system by an application.

More detailed info is available at:
https://docs.microsoft.com/en-us/typography/opentype/spec/os2#fstype [code: drm]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check glyph coverage.</summary>

* [com.google.fonts/check/glyph_coverage](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage)
* 🔥 **FAIL** Missing required codepoints: 0x000D (CARRIAGE RETURN), 0x00AD (SOFT HYPHEN), 0x00B5 (MICRO SIGN), 0x2074 (SUPERSCRIPT FOUR) and 0x20AC (EURO SIGN) [code: missing-codepoints]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Checking OS/2 usWeightClass.</summary>

* [com.google.fonts/check/usweightclass](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/usweightclass)
* 🔥 **FAIL** OS/2 usWeightClass expected value for 'Regular' is 400 but this font has 100.
 GlyphsApp users should set a Custom Parameter for 'Axis Location' in each master to ensure that the information is accurately built into variable fonts. [code: bad-value]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check name table: TYPOGRAPHIC_SUBFAMILY_NAME entries. </summary>

* [com.google.fonts/check/name/typographicsubfamilyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/typographicsubfamilyname)
* 🔥 **FAIL** TYPOGRAPHIC_SUBFAMILY_NAME entry for Win "Narrow Thin MaxGrade" must be "Regular". Please note, since the font style is RIBBI, this record can be safely deleted. [code: bad-win-name]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check variable font instances have correct names</summary>

* [com.google.fonts/check/varfont_instance_names](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/varfont_instance_names)
* 🔥 **FAIL** Instance name "100 Wide MaxGrade" is incorrect. It should be "" [code: bad-name]
* 🔥 **FAIL** This will cause problems with some of the Google Fonts systems that look up fonts by their style names. This must be fixed! [code: bad-instance-names]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Checking OS/2 Metrics match hhea Metrics.</summary>

* [com.google.fonts/check/os2_metrics_match_hhea](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea)
* 🔥 **FAIL** OS/2 sTypoAscender (1622) and hhea ascent (2000) must be equal. [code: ascender]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Are there unwanted tables?</summary>

* [com.google.fonts/check/unwanted_tables](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unwanted_tables)
* 🔥 **FAIL** The following unwanted font tables were found:
Table: MVAR
Reason: Produces a bug in DirectWrite which causes https://bugzilla.mozilla.org/show_bug.cgi?id=1492477, https://github.com/google/fonts/issues/2085

They can be removed by using fonttools/ttx.

</details>
<details>
<summary>🔥 <b>FAIL:</b> Whitespace and non-breaking space have the same width?</summary>

* [com.google.fonts/check/whitespace_widths](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/hmtx.html#com.google.fonts/check/whitespace_widths)
* 🔥 **FAIL** Whitespace and non-breaking space have differing width: Whitespace (space) is 140 font units wide, non-breaking space (nbspace) is 406 font units wide. Both should be positive and the same. [code: different-widths]

</details>
<details>
<summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
* ⚠ **WARN** OS/2 VendorID value 'NONE' is not a known registered id. You should set it to your own 4 character code, and register that code with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx [code: unknown]

</details>
<details>
<summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters.</summary>

* [com.google.fonts/check/name/family_and_style_max_length](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length)
* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Crispy Narrow Thin MaxGrade' / SUBFAMILY_NAME = 'Regular'

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

|  | font/Crispy[GRAD,wdth,wght].ttf |
|:--- | ---:|
| Dehinted Size | 50.3kb |
| Hinted Size | 50.2kb |
| Increase | -128 bytes |
| Change   | -0.2 % |
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
* ℹ **INFO** This font contains the following optional tables [DSIG, GSUB, loca, prep, gasp]

</details>
<br>
</details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 1 | 8 | 4 | 34 | 7 | 60 | 0 |
| 1% | 7% | 4% | 30% | 6% | 53% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **PASS**
* **DEBUG**
