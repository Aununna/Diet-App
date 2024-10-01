class DietApp:
    def __init__(self):
        self.meals = []
        self.calorie_goal = 2000 # Default calorie goal
    def add_meal(self):
        meal_name = input("Enter the name of the meal: ")
        calories = int(input("Enter the calories for this meal: "))
        self.meals.append({'name': meal_name, 'calories': calories})
        print(f"Added {meal_name} with {calories} calories.")
    def view_meals(self):
        if not self.meals:
            print("No meals logged yet.")
            return
        print("\nLogged Meals:")
        for meal in self.meals:
            print(f"{meal['name']} - {meal['calories']} calories")
        total_calories = sum(meal['calories'] for meal in self.meals)
        print(f"Total Calories Intake: {total_calories}/{self.calorie_goal}")
    def set_calorie_goal(self):
        self.calorie_goal = int(input("set your daily calorie goal: "))
        print(f"Daily calorie goal set to {self.calorie_goal} calories.")
    def meal_suggestions(self):
        print("Here are some healthier meal suggestion:")
        suggestions = [
            {"name": "Grilled Chicken Salad", "calories": 350},
            {"name": "Quinoa and Black Beans", "calories": 400},
            {"name": "Vegetable Stir-fry", "calories": 300},
            {"name": "Greek Yogurt with Fruits", "calories": 200}
        ]
        for suggestion in suggestions:
            print(f"{suggestion['name']} - {suggestion['calories']} calories")
    def run(self):
        while True:
            print("\n--- Diet App Menu ---")
            print("1. Add Meal")
            print("2. View Meals")
            print("3. Set Calorie Goal")
            print("4. Meal Suggestions")
            print("5. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                self.add_meal()
            elif choice == "2":
                self.view_meals()
            elif choice == "3":
                self.set_calorie_goal()
            elif choice == "4":
                self.meal_suggestions()
            elif choice == "5":
                print("Exiting the app. Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    app = DietApp()
    app.run()




