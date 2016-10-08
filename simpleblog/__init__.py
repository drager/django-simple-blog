VERSION = (0, 2, 0)

def get_version():
    """Return the Django Simple Blog version as a string."""
    return '.'.join(map(str, VERSION))
