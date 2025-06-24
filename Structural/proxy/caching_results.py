

class DataFetcher:
    def get_data(self, query: str) -> str:
        print(f"Fetching data from {query}...")
        return f"Data from {query}"


class CachingProxyDataFetcher:
    def __init__(self):
        self._cache = {}
        self._data_fetcher = DataFetcher()

    def get_data(self, query: str):
        if query in self._cache:
            print(f"Returning query result from cache...")
            return f"Data: {self._cache[query]}"
        else:
            print(f"Cache miss for {query}.")
            result = self._data_fetcher.get_data(query=query)
            print(f"Caching result...")
            self._cache[query] = result
            return f"Data: {result}"


# Usage
if __name__ == "__main__":
    data_fetcher = CachingProxyDataFetcher()
    print(data_fetcher.get_data("GET:weather"))
    print(data_fetcher.get_data("GET:time"))
    print(data_fetcher.get_data("GET:weather"))
