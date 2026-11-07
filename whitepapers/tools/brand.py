"""Shared brand constants for the Infinitum Whitepaper Series tooling.

Fill EMAIL (or export INFINITUM_EMAIL) once William provides the address.
Nothing here invents an address: while EMAIL is empty the email line is
simply omitted from covers/graphics and a warning is printed.
"""
import os

EMAIL = os.environ.get("INFINITUM_EMAIL", "info@theinfinitumcorporation.com")   # provided by William

SERIES = "Infinitum Whitepaper Series"
COMPANY = "Infinitum Corporation"
WORDMARK = "INFINITUM CORPORATION"
PERSON = "William Aaron Turner, Founder & President"
LOCATION = "Infinitum Corporation, Washington, DC"
TELEGRAM_DISPLAY = "t.me/infinitumcorporation"
TELEGRAM_URL = "https://t.me/infinitumcorporation"
WEBSITE_DISPLAY = "www.theinfinitumcorporation.com"
WEBSITE_URL = "https://www.theinfinitumcorporation.com"
PHONE = "(202) 729-9509"
X_URL = "https://x.com/infinitumceo"
DATE_LABEL = "October 2026"

FONT_DIR = "/usr/share/fonts/truetype/sand-box/google/Poppins"
FONTS = {  # weight -> file
    300: "Poppins-Light.ttf",
    400: "Poppins-Regular.ttf",
    500: "Poppins-Medium.ttf",
    600: "Poppins-SemiBold.ttf",
    700: "Poppins-Bold.ttf",
}

def font_face_css():
    out = []
    for w, f in FONTS.items():
        out.append(
            "@font-face{font-family:'PoppinsBrand';font-weight:%d;src:url('file://%s/%s');}"
            % (w, FONT_DIR, f))
    return "\n".join(out)

def warn_if_no_email():
    if not EMAIL:
        print("WARNING: EMAIL is empty in tools/brand.py (or INFINITUM_EMAIL). "
              "Email line omitted from cover/graphic.")
