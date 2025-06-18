from abc import ABC, abstractmethod


# Product Interface
class ConnectToDB(ABC):
    @abstractmethod
    def connect(self, connection_string: str):
        pass


class ExecuteQuery(ABC):
    @abstractmethod
    def build_query(self, query: str):
        pass


# Concrete Products
class ConnectPostgreSQL(ConnectToDB):
    def connect(self, connection_string: str):
        print("connecting to postgresql databse...")


class QueryPostgreSQL(ExecuteQuery):
    def build_query(self, query: str):
        print(f"executing: '{query}' on postgresql database...")


class ConnectMSSQL(ConnectToDB):
    def connect(self, connection_string: str):
        print("connecting to mssql databse...")


class QueryMSSQL(ExecuteQuery):
    def build_query(self, query: str):
        print(f"executing: '{query}' on mssql database...")


# Factory Interface
class DBFactory(ABC):
    @abstractmethod
    def create_connection(self) -> ConnectToDB:
        pass

    @abstractmethod
    def create_query_builder(self) -> ExecuteQuery:
        pass


# Concrete Factories
class PostgreSQLFactory(DBFactory):
    def create_connection(self):
        return ConnectPostgreSQL()

    def create_query_builder(self):
        return QueryPostgreSQL()


class MSSQLFactory(DBFactory):
    def create_connection(self):
        return ConnectMSSQL()

    def create_query_builder(self):
        return QueryMSSQL()


# Usage
if __name__ == "__main__":
    def run_db_workflow(factory: DBFactory):
        connection = factory.create_connection()
        connection.connect(connection_string="connection_string")
        builder = factory.create_query_builder()
        builder.build_query(query="SELECT * FROM tableA")

    run_db_workflow(PostgreSQLFactory())
    run_db_workflow(MSSQLFactory())
