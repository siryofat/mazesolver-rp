def tag(name: str, value: str | None = None, **attributes) -> str:
    attrs = "" if not attributes else " " + " ".join(
        f'{key.replace("_", "-")}="{value}"' for key, value in attributes.items()
    )
    if value is None:
        return f'<{name}{attributes} />'
    return f'<{name}{attributes}>{value}</{name}>'