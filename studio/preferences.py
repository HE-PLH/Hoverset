from hoverset.data.preferences import SharedPreferences

defaults = {
    "studio": {
        "recent": [],
        "recent_max": 20,
        "panes": {
            "right": {
                "width": 320,
            },
            "center": {
                "width": 400
            },
            "left": {
                "width": 320
            }
        }
    },
    "features": {},
}


class Preferences(SharedPreferences):

    @classmethod
    def acquire(cls):
        return cls("formation", "hoverset", "config", defaults)