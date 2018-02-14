from werkzeug.contrib.cache import SimpleCache

TIMEOUT = 5 * 60
cache = SimpleCache()


def add_to_cache(key, value):
    cache.set(key, value, timeout=TIMEOUT)


def get_from_cache(key):
    return cache.get(key)
