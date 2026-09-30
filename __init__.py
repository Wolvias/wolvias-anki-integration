# =========================================================
# Wolvias PDF Question
# __init__.py
# =========================================================

from aqt import gui_hooks

from .constants import ADDON_NAME
from .renderer import prepare_wolvias_card


gui_hooks.card_will_show.append(
    prepare_wolvias_card
)


print(
    f"[{ADDON_NAME}] Add-on loaded."
)