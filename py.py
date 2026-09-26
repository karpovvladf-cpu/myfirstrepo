# Инвентарь героя
inventory = {"Зелье лечения": 2, "Деревянный меч": 1, "Хлеб": 5}

def show_inventory():
    """Выводит все предметы из инвентаря в формате: 'Название: Количество шт.'"""
    pass # TODO: 
    for item,kolvo in inventory.items():
        print(f"{item}: {kolvo}шт")

def add_item(item_name, count):
    """Добавляет предмет. Если предмет уже есть, увеличивает количество. Если нет - добавляет новый."""
    pass # TODO: 
    inventory[item_name] = inventory.get(item_name, 0) + count

def use_item(item_name):
    """Использует предмет: уменьшает количество на 1. Если предмет кончился (стал 0), удаляет его из словаря."""
    pass # TODO: Напиши код здесь
    if item_name in inventory:
        inventory[item_name] -= 1
    else:
        print("нет такого предмета")

# --- ТЕСТОВАЯ ЗОНА ---
print("--- Начальный инвентарь ---")
show_inventory()

print("\n--- Находим 3 золотых монеты ---")
add_item("Золотая монета", 3)
show_inventory()

print("\n--- Выпиваем 1 зелье лечения ---")
use_item("Зелье лечения")
show_inventory()