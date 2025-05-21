# scripts/populate_db.py
from models.restaurant_recommender import RestaurantRecommenderDB
from db.neo4j_driver import get_driver
import random

def main():
    driver = get_driver()
    db = RestaurantRecommenderDB(driver)
    db.clear_database()

    users = [
        {"name": "Ana", "age": 25, "gender": "F"},
        {"name": "Bob", "age": 30, "gender": "M"},
        {"name": "Carol", "age": 28, "gender": "F"},
        {"name": "David", "age": 35, "gender": "M"},
        {"name": "Eve", "age": 22, "gender": "F"},
        {"name": "Felipe", "age": 40, "gender": "M"},
        {"name": "Gabi", "age": 31, "gender": "F"},
        {"name": "Henrique", "age": 27, "gender": "M"},
        {"name": "Isabela", "age": 26, "gender": "F"},
        {"name": "João", "age": 34, "gender": "M"},
        {"name": "Karen", "age": 29, "gender": "F"},
        {"name": "Lucas", "age": 33, "gender": "M"},
        {"name": "Marina", "age": 24, "gender": "F"},
        {"name": "Nando", "age": 38, "gender": "M"},
        {"name": "Olívia", "age": 21, "gender": "F"},
    ]
    db.insert_users(users)

    # Lista de restaurantes reais fictícios organizados por culinária
    restaurants_data = {
        "Italiana": [
            "Trattoria da Mario", "Pasta Bella", "Osteria Firenze", "Cantina Toscana", "Bella Napoli"
        ],
        "Japonesa": [
            "Sakura Sushi", "Tokyo Grill", "Hanami", "Kaisen House", "Nippon Delights"
        ],
        "Chinesa": [
            "Dragão Dourado", "Palácio de Jade", "Mandarim", "Casa do Wok", "Pérola do Oriente"
        ],
        "Brasileira": [
            "Sabor do Brasil", "Churrascaria Gaúcha", "Casa do Acarajé", "Boteco do Zé", "Cantinho Brasileiro"
        ],
        "Mexicana": [
            "El Mariachi", "Cantina Guadalajara", "Taco Loco", "La Catrina", "Sombrero Mexicano"
        ],
        "Francesa": [
            "Le Bistro", "Chez Pierre", "Café de Paris", "La Petite Maison", "Maison du Fromage"
        ],
        "Indiana": [
            "Taj Mahal", "Spice of India", "Mumbai Masala", "Curry Palace", "Bombay Bistro"
        ],
        "Árabe": [
            "Aladdin", "Cedro Libanês", "Oásis Árabe", "Shawarma House", "Souk Oriental"
        ],
        "Vegana": [
            "Verde Vida", "Raiz Natural", "Veggie Delight", "Pura Plantas", "Semente Viva"
        ],
        "Hamburgueria": [
            "Burger King (Fake)", "Mr. Grill", "Hamburgueria do Chef", "Big Bite", "Smoke Burger"
        ]
    }

    # Montar lista final de restaurantes (50 no total)
    restaurants = []
    price_ranges = ["$", "$$", "$$$"]

    # Para equilibrar, repetir os nomes dos restaurantes por culinária até atingir 50
    while len(restaurants) < 50:
        for cuisine, names in restaurants_data.items():
            for name in names:
                if len(restaurants) >= 50:
                    break
                restaurants.append({
                    "name": name,
                    "cuisine": cuisine,
                    "price": random.choice(price_ranges)
                })

    db.insert_restaurants(restaurants)

    # Criar relações de likes aleatórias, cada usuário curte de 5 a 10 restaurantes
    relations = []
    restaurant_names = [r["name"] for r in restaurants]

    for user in users:
        liked = random.sample(restaurant_names, random.randint(5, 10))
        for r_name in liked:
            relations.append((user["name"], r_name))

    db.create_likes_relationships(relations)

    print("📦 Base de dados populada com sucesso.")

if __name__ == "__main__":
    main()
