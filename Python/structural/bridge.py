from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def execute_query(self, query: str):
        pass

class SQLDatabase(Database):
    def connect(self):
        print("Connecting to SQL Database")

    def disconnect(self):
        print("Disconnecting from SQL Database")

    def execute_query(self, query: str):
        print(f"Executing SQL query: {query}")

class NoSQLDatabase(Database):
    def connect(self):
        print("Connecting to NoSQL Database")

    def disconnect(self):
        print("Disconnecting from NoSQL Database")

    def execute_query(self, query: str):
        print(f"Executing NoSQL query: {query}")

class DatabaseBridge:
    def __init__(self, database: Database):
        self._database = database

    def connect(self):
        self._database.connect()

    def disconnect(self):
        self._database.disconnect()

    def execute_query(self, query: str):
        self._database.execute_query(query)


if __name__ == "__main__":
    sql_db = SQLDatabase()
    sql_bridge = DatabaseBridge(sql_db)
    
    sql_bridge.connect()
    sql_bridge.execute_query("SELECT * FROM users")
    sql_bridge.disconnect()

    print()

    nosql_db = NoSQLDatabase()
    nosql_bridge = DatabaseBridge(nosql_db)
    
    nosql_bridge.connect()
    nosql_bridge.execute_query("{find: 'users'}")
    nosql_bridge.disconnect()
