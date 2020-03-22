# Create pizza toppings list
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

# Create pizza price list
prices=[2, 6, 1, 3, 2, 7, 2]

num_pizzas = len(toppings)
print("We sell " + str(num_pizzas) +" different kinds of pizza!")

pizzas = list(zip(toppings,prices))
print(pizzas)

cheapest_pizza = (pizzas.sort())[0]
priciest_pizza = pizzas.sort()[-1]
three_cheapest = list(pizzas.sort()[0:3])
print(three_cheapest)

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
