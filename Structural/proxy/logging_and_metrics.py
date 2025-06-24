import time


class DataFetcher:
    def get_data(self, query):
        time.sleep(0.7)
        print(f"Fetching data from {query}...")
        return f"Data from {query}"


class MetricProxyDataFetcher:
    def __init__(self):
        self._data_fetcher = DataFetcher()
        self._call_count = {}

    def get_data(self, query):
        start_time = time.time()
        self._call_count[query] = self._call_count.get(query, 0) + 1
        result = self._data_fetcher.get_data(query=query)
        duration = time.time() - start_time
        print(f"Finished call for {query} in {duration:.2f}s "
              f"(called {self._call_count[query]} times)")
        return result


# Usage
if __name__ == "__main__":
    data_fetcher = MetricProxyDataFetcher()
    print(data_fetcher.get_data("GET:weather"))
    print(data_fetcher.get_data("GET:time"))
    print(data_fetcher.get_data("GET:weather"))
