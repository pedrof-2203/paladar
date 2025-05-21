#db/neo4j_driver.py
from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
USER = "neo4j"
PASSWORD = "12345678"

def get_driver():
    driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))
    return driver 

