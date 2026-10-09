import re
import unicodedata


def slugify(text: str, sep: str = "-", max_length: int | None = None) -> str:
    """Turn arbitrary text into a URL slug.

    >>> slugify("Héllo World")
    'hello-world'
    """
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^A-Za-z0-9]+", sep, text).lower()
    if max_length is not None:
        text = text[:max_length]
    # Punctuation at the edges (and a cut made by max_length) can leave
    # separators at either end; they are never part of a useful slug.
    return text.strip(sep)
