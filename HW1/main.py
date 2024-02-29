import requests
from lfu_cache import cache
from memory_profiler import profile


@cache(2)
def fetch_url(url, first_n=100):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content


@profile
def generate_list(amount: int):
    return [i for i in range(1, amount)]


if __name__ == '__main__':
    fetch_url('https://dou.ua')
    fetch_url('https://dou.ua')
    fetch_url('https://dou.ua')
    fetch_url('https://google.com')
    fetch_url('https://google.com')
    fetch_url('https://uk.wikipedia.org')
    fetch_url('https://uk.wikipedia.org')

    generate_list(10000)
