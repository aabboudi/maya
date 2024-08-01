JAZZMIN_SETTINGS = {
    "site_title": "MAYA",
    "site_header": "Moroccan Association for YES Alumni",
    "site_brand": "Site Administration",
    "welcome_sign": "Log in to see the admin dashboard.",
    "copyright": "Moroccan Association for YES Alumni",
    "show_ui_builder": False,

    "site_logo": "/static/assets/yes-logo-transparent.png",
    "login_logo": "/static/assets/yes-logo-transparent.png",
    "site_icon": "/static/assets/favicon.ico",

    "topmenu_links": [
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},
        {"model": "auth.User"},
        {"app": "content"},
    ],

    "icons": {
        "content.post": "fas fa-pen",
        "content.person": "fas fa-user",
    },
}

JAZZMIN_UI_TWEAKS = {
    # "navbar": "navbar-dark",
    # "navbar_fixed": True,
    # "sidebar_nav_small_text": True,
    # "theme": "darkly",
}
