# Инвентарь героя
inventory = {"Зелье лечения": 2, "Деревянный меч": 1, "Хлеб": 5}

def show_inventory():
    """Выводит все предметы из инвентаря в формате: 'Название: Количество шт.'"""
    pass # TODO: 
    for item,kolvo in inventory.items():
        print(f"{item}: {kolvo}шт")

