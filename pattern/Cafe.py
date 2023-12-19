import copy

class CafeMenu:
    def __init__(self, items=None):
        self.items = items if items else []

    def add_item(self, item):
        self.items.append(item)

    def __str__(self):
        return ", ".join(self.items)

class Cafe:
    def __init__(self, name, location, menu):
        self.name = name
        self.location = location
        self.menu = menu

    def __str__(self):
        return f"Cafe: {self.name}, Location: {self.location}, Menu: {self.menu}"

class CafePrototype:
    def __init__(self):
        self._objects = {}

    def register_cafe(self, name, cafe):
        self._objects[name] = cafe

    def unregister_cafe(self, name):
        del self._objects[name]

    def clone(self, name, **attrs):
        cafe = copy.deepcopy(self._objects.get(name))
        cafe.__dict__.update(attrs)
        return cafe

# Приклад використання Прототипу для кав'ярні
if __name__ == "__main__":
    prototype = CafePrototype()

    # Створення оригінальної кав'ярні
    original_menu = CafeMenu(["Coffee", "Tea", "Pastries"])
    original_cafe = Cafe("Coffee Time", "123 Main St", original_menu)
    prototype.register_cafe("original_cafe", original_cafe)

    # Клонування кав'ярні за допомогою прототипу
    cloned_cafe = prototype.clone("original_cafe", location="456 Oak St")
    cloned_cafe.menu.add_item("Sandwiches")  # Додано новий елемент до меню
    print(cloned_cafe)  # Виведе інформацію про клоновану кав'ярню
    print(cloned_cafe.menu)  # Виведе оновлене меню клонованої кав'ярні

