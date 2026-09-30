# =========================================================
# Wolvias PDF Question
# constants.py
# =========================================================

ADDON_NAME = "Wolvias PDF Question"

QUESTION_FIELD = "Question"
IMAGE_FIELD = "Image"
RECTANGLES_FIELD = "Rectangles"

# Preferred marker used by current WA-PDF Studio exporter.
RECTANGLE_CONTAINER_MARKER = '<div id="wolvias-rectangles"></div>'

# Legacy marker kept for compatibility with older exports.
LEGACY_RECTANGLE_MARKER = "<!-- WOLVIAS_RECTANGLES -->"

SUPPORTED_CONTEXTS = {
    "reviewQuestion",
    "reviewAnswer",
    "previewQuestion",
    "previewAnswer",
    "clayoutQuestion",
    "clayoutAnswer",
}

WOLVIAS_CSS = r"""
.wolvias-question
{
    width: 100%;
    margin: 0 0 16px 0;

    box-sizing: border-box;

    text-align: center;

    font-size: 1.25em;
    font-weight: 700;
    line-height: 1.5;
}

.wolvias-stage
{
    width: 100%;
    box-sizing: border-box;

    text-align: center;
}

.wolvias-image
{
    position: relative;

    display: inline-block;

    max-width: 100%;

    line-height: 0;
}

.wolvias-image img
{
    display: block;

    width: auto;
    max-width: 100%;
    height: auto;
}

#wolvias-rectangles
{
    position: absolute;

    inset: 0;

    pointer-events: none;

    z-index: 100;
}

.wolvias-rect
{
    position: absolute;

    box-sizing: border-box;

    pointer-events: none;

    z-index: 101;

    border:
        2px solid
        transparent;

    border-radius:
        1px;
}

"""