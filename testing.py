from neo4j import GraphDatabase

# Make sure to add edit your proper connection configuration for testing here.
def test_connection():
    uri = "neo4j://localhost:7687"
    user = "neo4j"
    password = "Pass@1995"
    
    try:
        driver = GraphDatabase.driver(uri, auth=(user, password))
        print("Driver successfully initialized.")
        with driver.session() as session:
            result = session.run("RETURN 1")
            for record in result:
                print(record)
        driver.close()
    except Exception as e:
        print(f"Failed to create the driver with URI: {uri}, User: {user}")
        print(f"Error: {e}")

if __name__ == "__main__":
    test_connection()
