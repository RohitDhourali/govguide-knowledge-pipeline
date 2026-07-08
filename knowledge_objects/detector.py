import re

# Main Sections
# Example:
# १ कम्पनी :
# २ कम्पनी दर्ता :
MAIN_SECTION_PATTERN = re.compile(
    r'^[०-९\d]+\s+.+?:?$'
)

# Sub Sections
# Example:
# २.१ नेपाली नागरिक...
# २.५ विदेशी कम्पनी...
SUB_SECTION_PATTERN = re.compile(
    r'^[०-९\d]+(?:\.[०-९\d]+)+\s+.+?:?$'
)

# Alphabetical subsections
# Example:
# (क) कम्पनी :
# (ख) प्राइभेट कम्पनी :
ALPHA_SECTION_PATTERN = re.compile(
    r'^\([क-ह]\)\s+.+?:?$'
)


def heading_type(line):

    line = line.strip()

    if not line:
        return None

    if SUB_SECTION_PATTERN.match(line):
        return "sub"

    if MAIN_SECTION_PATTERN.match(line):
        return "main"

    if ALPHA_SECTION_PATTERN.match(line):
        return "alpha"

    return None