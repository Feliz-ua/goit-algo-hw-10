from pulp import LpMaximize, LpProblem, LpVariable, PULP_CBC_CMD

# Створюємо задачу максимізації
model = LpProblem(name="production-optimization", sense=LpMaximize)

# Змінні: кількість Лимонаду та Фруктового соку
lemonade = LpVariable(name="lemonade", lowBound=0, cat='Integer')
fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat='Integer')

# Обмеження ресурсів
# Вода: 2 * Лимонад + 1 * Сік <= 100
model += (2 * lemonade + fruit_juice <= 100, "Water_constraint")

# Цукор: 1 * Лимонад <= 50
model += (lemonade <= 50, "Sugar_constraint")

# Лимонний сік: 1 * Лимонад <= 30
model += (lemonade <= 30, "Lemon_juice_constraint")

# Фруктове пюре: 2 * Сік <= 40
model += (2 * fruit_juice <= 40, "Fruit_puree_constraint")

# Цільова функція: максимізувати загальну кількість продуктів
model += lemonade + fruit_juice, "Total_products"

# Викликаємо CBC з вимкненим логом
solver = PULP_CBC_CMD(msg=False)
model.solve(solver)

# Вивід результатів
print(f"Лимонад: {lemonade.varValue}")
print(f"Фруктовий сік: {fruit_juice.varValue}")
print(f"Загальна кількість продуктів: {model.objective.value()}")

