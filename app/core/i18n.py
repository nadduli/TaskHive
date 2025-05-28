from pathlib import Path
import i18n
from fastapi import Request
from typing import Optional

# Set up i18n configuration
i18n.load_path.append(str(Path(__file__).parent.parent / "translations"))
i18n.set("filename_format", "{locale}.{format}")
i18n.set("file_format", "json")
i18n.set("skip_locale_root_data", True)
i18n.set("fallback", "en")


def get_locale(request: Optional[Request] = None) -> str:
    """
    Get the locale from the request's Accept-Language header or default to 'en'
    """
    if request and request.headers.get("accept-language"):
        # Get the first language from the Accept-Language header
        return request.headers["accept-language"].split(",")[0].split("-")[0]
    return "en"


def t(key: str, locale: str = "en", **kwargs) -> str:
    """
    Translate a key to the specified locale
    """
    i18n.set("locale", locale)
    return i18n.t(key, **kwargs)
