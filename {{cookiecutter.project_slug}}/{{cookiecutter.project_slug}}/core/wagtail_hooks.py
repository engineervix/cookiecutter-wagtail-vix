from wagtail import hooks


@hooks.register("register_icons")
def register_icons(icons):
    return icons + [
        "wagtailfontawesomesvg/regular/newspaper.svg",
        "wagtailfontawesomesvg/solid/bullhorn.svg",
        "wagtailfontawesomesvg/solid/download.svg",
        "wagtailfontawesomesvg/solid/location-dot.svg",
    ]
