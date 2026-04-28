import os
import sys


def resource_path(path):
    meipass = getattr(sys, "_MEIPASS", None)
    if meipass is not None:
        return os.path.join(meipass, path)
    return os.path.join(os.path.abspath("."), path)
