from abc import ABC, abstractmethod


# Product Interface
class Connection(ABC):
    @abstractmethod
    def connect(self):
        pass


# Concrete Products
class MSSQLConnection(Connection):
    def __init__(self, server: str, username: str, password: str, port: int):
        self.server = server
        self.username = username
        self.password = password
        self.port = port

    def connect(self):
        print(f"connecting to mssql server: {self.server}...")


class PostgreSQLConnection(Connection):
    def __init__(self, server: str, username: str, password: str, port: int):
        self.server = server
        self.username = username
        self.password = password
        self.port = port

    def connect(self):
        print(f"connecting to postgresql server: {self.server}...")


# Factory
def database_factory(
        database: str,
        server: str,
        username: str,
        password: str,
        port: int
):
    if database == "MSSQL":
        return MSSQLConnection(
            server=server,
            username=username,
            password=password,
            port=port
        )
    elif database == "PostgreSQL":
        return PostgreSQLConnection(
            server=server,
            username=username,
            password=password,
            port=port
        )
    else:
        raise ValueError("Invalid database option.")


# Usage
if __name__ == "__main__":
    database_connection = database_factory(
        database="PostgreSQL",
        server="example-server",
        username="example-user",
        password="example-pass",
        port=1234
    )
    database_connection.connect()
