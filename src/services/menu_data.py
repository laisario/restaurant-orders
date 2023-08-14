from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.file_path = source_path
        self.dishes = set()
        self.read_file()
        self.process_dishes()

    def read_file(self):
        try:
            lines = []
            with open(self.file_path) as file:
                for line in file:
                    line = line.strip()
                    words = line.split(',')
                    lines.append(words)
            lines.pop(0)
            self.lines = lines
        except FileNotFoundError:
            print(f'Arquivo {self.file_path} não encontrado')

    def find_dish_by_name(self, name):
        for dish in self.dishes:
            if dish.name == name:
                return dish
        return None

    def process_dishes(self):
        for line in self.lines:
            dish = self.find_dish_by_name(line[0])
            ingredient = Ingredient(line[2])
            if dish:
                dish.add_ingredient_dependency(ingredient, float(line[3]))
            else:
                dish = Dish(line[0], float(line[1]))
                dish.add_ingredient_dependency(ingredient, float(line[3]))
                self.dishes.add(dish)
