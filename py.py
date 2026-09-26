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
