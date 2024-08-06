from neo4j import GraphDatabase

class Neo4jConnection:
    def __init__(self, uri, user, pwd):
        self.__uri = uri
        self.__user = user
        self.__password = pwd
        self.__driver = None
        try:
            self.__driver = GraphDatabase.driver(self.__uri, auth=(self.__user, self.__password))
            print("Driver successfully initialized.")
        except Exception as e:
            print(f"Failed to create the driver with URI: {self.__uri}, User: {self.__user}")
            print(f"Error: {e}")

    def close(self):
        if self.__driver is not None:
            self.__driver.close()

    def query(self, query, parameters=None, db=None):
        assert self.__driver is not None, "Driver not initialized!"
        session = None
        response = None
        try:
            session = self.__driver.session(database=db) if db is not None else self.__driver.session() 
            response = list(session.run(query, parameters))
        except Exception as e:
            print(f"Query failed: {e}")
        finally:
            if session is not None:
                session.close()
        return response

# Replace 'your_password' with your actual Neo4j password
db = Neo4jConnection(uri="neo4j://localhost:7687", user="neo4j", pwd="Pass@1995")
