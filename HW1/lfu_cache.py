import functools
from collections import Counter


def cache(max_limit=5):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            cache_key = (args, tuple(kwargs.items()))
            if cache_key in deco._cache:
                # Increase the cache_key frequency counter
                deco._cache_frequency[cache_key] += 1
                return deco._cache[cache_key]

            result = f(*args, **kwargs)
            # Delete if limit is reached
            if len(deco._cache) >= max_limit:
                # Remove the less frequent element
                lf_cache_key = deco._cache_frequency.most_common()[-1][0]
                del deco._cache[lf_cache_key]
                del deco._cache_frequency[lf_cache_key]

            # Add value to the cache
            deco._cache[cache_key] = result
            deco._cache_frequency[cache_key] = 1
            return result
        deco._cache = {}
        deco._cache_frequency = Counter()
        return deco
    return internal
