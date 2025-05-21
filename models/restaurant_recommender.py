#models/restaurant_recommender.py
class RestaurantRecommenderDB:
    def __init__(self, driver):
        self.driver = driver

    def clear_database(self):
        """Remove todos os nós e relacionamentos do banco."""
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")

    def insert_users(self, users):
        """Insere usuários no banco."""
        with self.driver.session() as session:
            for user in users:
                session.run(
                """
                CREATE (:User {name: $name, age: $age, gender: $gender})
                """,
                name=user["name"],
                age=user["age"],
                gender=user["gender"]
            )

    def insert_restaurants(self, restaurants):
        """Insere restaurantes no banco."""
        with self.driver.session() as session:
            for restaurant in restaurants:
                session.run(
                """
                CREATE (:Restaurant {name: $name, cuisine: $cuisine, price: $price})
                """,
                name=restaurant["name"],
                cuisine=restaurant["cuisine"],
                price=restaurant["price"]
            )

    def create_likes_relationships(self, relations):
        """Cria relacionamentos de curtidas entre usuários e restaurantes."""
        with self.driver.session() as session:
            for user_name, restaurant_name in relations:
                session.run(
                """
                MATCH (u:User {name: $user_name})
                MATCH (r:Restaurant {name: $restaurant_name})
                CREATE (u)-[:LIKES]->(r)
                """,
                user_name=user_name,
                restaurant_name=restaurant_name
            )

    def recommend_restaurants(self, user_name):
        with self.driver.session() as session:
            result = session.run(
                """
                MATCH (:User {name: $user_name})-[:LIKES]->(r:Restaurant)
                RETURN collect(r.name) AS liked_restaurants
                """,
                user_name=user_name
            )
            record = result.single()
            if not record:
                return None

            liked_restaurants = record["liked_restaurants"]

            result = session.run(
                """
                MATCH (u1:User {name: $user_name})-[:LIKES]->(r:Restaurant)<-[:LIKES]-(u2:User)-[:LIKES]->(rec:Restaurant)
                WHERE NOT rec.name IN $liked_restaurants
                RETURN rec.name AS recommendation, count(*) AS score
                ORDER BY score DESC, recommendation
                LIMIT 10
                """,
                user_name=user_name,
                liked_restaurants=liked_restaurants
            )

            # Itera uma única vez para coletar recomendações
            recommendations = []
            for record in result:
                recommendations.append(record["recommendation"])

            return recommendations