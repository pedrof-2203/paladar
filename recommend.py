#recommend.py
from db.neo4j_driver import get_driver
from models.restaurant_recommender import RestaurantRecommenderDB

def main():
    driver = get_driver()
    db = RestaurantRecommenderDB(driver)

    user_name = input("Digite seu nome para receber recomendações: ").strip()

    recommendations = db.recommend_restaurants(user_name)

    if recommendations is None:
        print(f"❌ Usuário '{user_name}' não encontrado.")
    elif recommendations:
        print(f"\n 🍽️ Recomendações para {user_name}:")
        for i, restaurant in enumerate(recommendations, 1):
            print(f"{i}. {restaurant}")
    else:
        print("⚠️ Nenhuma recomendação encontrada para você no momento.")

if __name__ == "__main__":
    main()
