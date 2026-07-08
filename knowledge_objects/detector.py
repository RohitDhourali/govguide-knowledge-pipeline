import re

# अध्याय १
CHAPTER_PATTERN = re.compile(
    r'^अध्याय\s+[०-९\d]+'
)

# भाग २
PART_PATTERN = re.compile(
    r'^भाग\s+[०-९\d]+'
)

# १. कम्पनी
MAIN_PATTERN = re.compile(
    r'^[०-९\d]+[.)]?\s+.+'
)

# २.१ आवेदन
SUB_PATTERN = re.compile(
    r'^[०-९\d]+(?:\.[०-९\d]+)+[.)]?\s+.+'
)

# २.१.१ विवरण
SUBSUB_PATTERN = re.compile(
    r'^[०-९\d]+(?:\.[०-९\d]+){2,}[.)]?\s+.+'
)

# (क) विवरण
ALPHA_PATTERN = re.compile(
    r'^\([क-ह]\)\s+.+?:?$'
)

# क) विवरण
ALPHA2_PATTERN = re.compile(
    r'^[क-ह]\)\s+.+?:?$'
)

# (१) विवरण
CLAUSE_PATTERN = re.compile(
    r'^\([०-९\d]+\)\s+.+'
)

# १) विवरण
CLAUSE2_PATTERN = re.compile(
    r'^[०-९\d]+\)\s+.+'
)


def heading_type(line):

    line = line.strip()

    if not line:
        return None

    if CHAPTER_PATTERN.match(line):
        return "chapter"

    if PART_PATTERN.match(line):
        return "part"

    if SUBSUB_PATTERN.match(line):
        return "subsub"

    if SUB_PATTERN.match(line):
        return "sub"

    if MAIN_PATTERN.match(line):
        return "main"

    if ALPHA_PATTERN.match(line):
        return "alpha"

    if ALPHA2_PATTERN.match(line):
        return "alpha"

    if CLAUSE_PATTERN.match(line):
        return "clause"

    if CLAUSE2_PATTERN.match(line):
        return "clause"

    return None
