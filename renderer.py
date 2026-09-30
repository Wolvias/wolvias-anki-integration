# =========================================================
# Wolvias PDF Question
# renderer.py
# =========================================================

from __future__ import annotations

import html
import json
import re
from typing import Any

from .constants import (
    ADDON_NAME,
    IMAGE_FIELD,
    LEGACY_RECTANGLE_MARKER,
    QUESTION_FIELD,
    RECTANGLES_FIELD,
    RECTANGLE_CONTAINER_MARKER,
    SUPPORTED_CONTEXTS,
    WOLVIAS_CSS,
)


# =========================================================
# HTML
# =========================================================

def clean_json_field(
    value: Any
) -> str:

    text = str(
        value
        or
        ""
    )

    text = html.unescape(
        text
    )

    text = re.sub(
        r"<[^>]*>",
        "",
        text
    )

    return text.strip()


# =========================================================
# COLOR
# =========================================================

def normalize_color(
    value: Any
) -> str:

    if not isinstance(
        value,
        str
    ):
        return "#ff0000"

    value = value.strip()

    if re.fullmatch(
        r"#(?:[0-9a-fA-F]{6})",
        value
    ):
        return value

    return "#ff0000"


# =========================================================
# RECTANGLES
# =========================================================

def normalize_rectangle(
    rectangle: Any
) -> dict[str, Any] | None:

    if not isinstance(
        rectangle,
        dict
    ):
        return None

    try:
        left = float(
            rectangle.get(
                "left",
                rectangle.get(
                    "x",
                    0
                )
            )
        )

        top = float(
            rectangle.get(
                "top",
                rectangle.get(
                    "y",
                    0
                )
            )
        )

        width = float(
            rectangle.get(
                "width",
                rectangle.get(
                    "w",
                    0
                )
            )
        )

        height = float(
            rectangle.get(
                "height",
                rectangle.get(
                    "h",
                    0
                )
            )
        )

    except (
        TypeError,
        ValueError
    ):
        return None

    if (
        left < 0
        or top < 0
        or width <= 0
        or height <= 0
    ):
        return None

    left = max(
        0.0,
        min(
            1.0,
            left
        )
    )

    top = max(
        0.0,
        min(
            1.0,
            top
        )
    )

    width = max(
        0.0,
        min(
            1.0 - left,
            width
        )
    )

    height = max(
        0.0,
        min(
            1.0 - top,
            height
        )
    )

    if (
        width <= 0
        or height <= 0
    ):
        return None

    color = normalize_color(
        rectangle.get(
            "color"
        )
    )

    return {
        "left":
            left,

        "top":
            top,

        "width":
            width,

        "height":
            height,

        "color":
            color
    }


def parse_rectangles(
    raw_value: Any
) -> list[dict[str, Any]]:

    cleaned = clean_json_field(
        raw_value
    )

    if not cleaned:
        return []

    try:
        parsed = json.loads(
            cleaned
        )

    except (
        json.JSONDecodeError,
        TypeError,
        ValueError
    ):
        print(
            "[Wolvias] Invalid Rectangles JSON."
        )

        print(
            "[Wolvias] Raw:",
            repr(
                cleaned
            )
        )

        return []

    if not isinstance(
        parsed,
        list
    ):
        print(
            "[Wolvias] Rectangles field is not an array."
        )

        return []

    result = []

    for rectangle in parsed:

        normalized = normalize_rectangle(
            rectangle
        )

        if normalized is not None:
            result.append(
                normalized
            )

    return result


# =========================================================
# RECTANGLE HTML
# =========================================================

def create_rectangle_html(
    rectangles,
    is_question
) -> str:

    overlays = []

    for rectangle in rectangles:

        color = rectangle[
            "color"
        ]

        if is_question:
            background = color_to_rgba(
                color,
                1.0
            )
        else:
            background = color_to_rgba(
                color,
                0.08
            )

        overlays.append(
            (
                '<div class="wolvias-rect" '
                'style="'
                f'left:{rectangle["left"] * 100:.6f}%;'
                f'top:{rectangle["top"] * 100:.6f}%;'
                f'width:{rectangle["width"] * 100:.6f}%;'
                f'height:{rectangle["height"] * 100:.6f}%;'
                f'border-color:{color};'
                f'background:{background};'
                '"></div>'
            )
        )

    return "".join(
        overlays
    )


def color_to_rgba(
    color,
    alpha
) -> str:

    value = normalize_color(
        color
    )[1:]

    red = int(
        value[0:2],
        16
    )

    green = int(
        value[2:4],
        16
    )

    blue = int(
        value[4:6],
        16
    )

    return (
        f"rgba("
        f"{red}, "
        f"{green}, "
        f"{blue}, "
        f"{alpha}"
        f")"
    )


# =========================================================
# INJECTION
# =========================================================
def inject_rectangles(
    html_content,
    rectangle_html
):

    if not rectangle_html:
        return html_content

    container = (
        '<div id="wolvias-rectangles">'
        f'{rectangle_html}'
        '</div>'
    )

    if RECTANGLE_CONTAINER_MARKER in html_content:

        return html_content.replace(
            RECTANGLE_CONTAINER_MARKER,
            container,
            1
        )

    if LEGACY_RECTANGLE_MARKER in html_content:

        return html_content.replace(
            LEGACY_RECTANGLE_MARKER,
            container,
            1
        )

    image_match = re.search(
        r'(<img\b[^>]*>)',
        html_content,
        flags=re.IGNORECASE
    )

    if image_match:

        image_end = (
            image_match.end()
        )

        return (
            html_content[
                :image_end
            ]
            +
            container
            +
            html_content[
                image_end:
            ]
        )

    return html_content

# =========================================================
# NOTE TYPE
# =========================================================

def is_wolvias_card(
    card
) -> bool:

    try:
        note_type = card.note_type()

    except Exception:
        return False

    if not note_type:
        return False

    if (
        note_type.get("name")
        !=
        ADDON_NAME
    ):
        return False

    fields = note_type.get(
        "flds",
        []
    )

    field_names = {
        str(field.get("name", ""))
        for field in fields
        if isinstance(field, dict)
    }

    required_fields = {
        QUESTION_FIELD,
        IMAGE_FIELD,
        RECTANGLES_FIELD
    }

    return required_fields.issubset(
        field_names
    )

# =========================================================
# CARD RENDER
# =========================================================

def render_card(
    html_content,
    card,
    context
):

    if (
        context
        not in
        SUPPORTED_CONTEXTS
    ):
        return html_content

    if not is_wolvias_card(
        card
    ):
        return html_content

    try:
        note = card.note()

        raw_rectangles = note[
            RECTANGLES_FIELD
        ]

        image = note[
            IMAGE_FIELD
        ]

        question = note[
            QUESTION_FIELD
        ]

    except Exception as error:

        print(
            "[Wolvias] Failed to read card:",
            repr(error)
        )

        return html_content

    rectangles = parse_rectangles(
        raw_rectangles
    )

    is_question = context.endswith(
        "Question"
    )

    rectangle_html = create_rectangle_html(
        rectangles,
        is_question
    )

    if (
        '<style id="wolvias-pdf-question-style">'
        not in
        html_content
    ):

        html_content += (
            '<style '
            'id="wolvias-pdf-question-style">'
            f"{WOLVIAS_CSS}"
            "</style>"
        )

    rendered = inject_rectangles(
        html_content,
        rectangle_html
    )

    print(
        "[Wolvias]",
        context,
        "|",
        "question:",
        is_question,
        "|",
        "rectangles:",
        len(rectangles),
        "|",
        "image:",
        bool(image),
        "|",
        "question text:",
        repr(question)
    )

    return rendered


# =========================================================
# ANKI HOOK
# =========================================================

def prepare_wolvias_card(
    html_content,
    card,
    kind
):

    try:
        return render_card(
            html_content,
            card,
            kind
        )

    except Exception as error:

        print(
            "[Wolvias] Rendering error:",
            repr(error)
        )

        return html_content