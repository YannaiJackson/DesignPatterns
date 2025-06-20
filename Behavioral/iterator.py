from collections.abc import Iterable, Iterator


# Iterator
class QueryResultIterator(Iterator):
    def __init__(self, rows: list):
        self._rows = rows
        self._index = 0

    def __next__(self) -> dict:
        if self._index >= len(self._rows):
            raise StopIteration
        row = self._rows[self._index]
        self._index += 1
        return row


# Collection
class QueryResultCollection(Iterable):
    def __init__(self, rows: list):
        self._rows = rows

    def __iter__(self) -> QueryResultIterator:
        return QueryResultIterator(self._rows)

    def first(self) -> dict | None:
        return self._rows[0] if self._rows else None

    def last(self) -> dict | None:
        return self._rows[-1] if self._rows else None

    def all(self) -> list:
        return self._rows

    def count(self) -> int:
        return len(self._rows)


# Usage
if __name__ == "__main__":
    example_query_result = [
        {'id': 1, 'name': 'Alice', 'salary': 20000},
        {'id': 2, 'name': 'Bob', 'salary': 35000},
        {'id': 3, 'name': 'Charlie', 'salary': 30000}
    ]
    result = QueryResultCollection(rows=example_query_result)
    print(f"All rows: {result.all()}")
    print(f"First row: {result.first()}")
    print(f"Last row: {result.last()}")
    print(f"Total rows: {result.count()}")
