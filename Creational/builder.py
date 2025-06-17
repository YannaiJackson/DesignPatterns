

class HttpRequest:
    def __init__(
            self,
            method,
            url,
            headers=None,
            body=None,
            params=None,
            timeout=None
    ):
        self.method = method
        self.url = url
        self.headers = headers or {}
        self.body = body
        self.params = params or {}
        self.timeout = timeout

    def __str__(self):
        return (
            f"Method: {self.method}\n"
            f"URL: {self.url}\n"
            f"Headers: {self.headers}\n"
            f"Params: {self.params}\n"
            f"Body: {self.body}\n"
            f"Timeout: {self.timeout}s"
        )


# --- Builder ---
class HttpRequestBuilder:
    def __init__(self, method, url):
        self._method = method
        self._url = url
        self._headers = {}
        self._params = {}
        self._body = None
        self._timeout = 10

    def add_header(self, key, value):
        self._headers[key] = value
        return self

    def set_params(self, params: dict):
        self._params = params
        return self

    def set_body(self, body):
        self._body = body
        return self

    def set_timeout(self, timeout):
        self._timeout = timeout
        return self

    def build(self):
        return HttpRequest(
            self._method, self._url, self._headers,
            self._body, self._params, self._timeout
        )


# Usage
if __name__ == "__main__":
    request = (
        HttpRequestBuilder("POST", "https://api.example.com/login")
        .add_header("Content-Type", "application/json")
        .add_header("Authorization", "Bearer abc123")
        .set_body({"username": "admin", "password": "secret"})
        .set_timeout(5)
        .build()
    )
    print(request)
