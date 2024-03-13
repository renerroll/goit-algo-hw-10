import pulp


def drinks_production():
    model = pulp.LpProblem("Drinks_production", pulp.LpMaximize)

    Lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat="Integer")  
    Fruit_Juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat="Integer")  

    model += Lemonade + Fruit_Juice, "Profit"

    model += 2 * Lemonade + 1 * Fruit_Juice <= 100  
    model += 1 * Lemonade <= 50  
    model += 1 * Lemonade <= 30 
    model += 2 * Fruit_Juice <= 40  

    model.solve()

    print("Лимонад, од.:", Lemonade.varValue)  
    print("Фруктовий сік, од.:", Fruit_Juice.varValue)  
    print("Загальний обсяг, од.:", pulp.value(model.objective))  


if __name__ == "__main__":
    drinks_production()