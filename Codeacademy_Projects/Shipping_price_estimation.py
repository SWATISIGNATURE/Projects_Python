ground_flat_charge = 20.00
premium_ground_flat_charge = 125.00
def cost_ground_shipping(weight):
  if weight <= 2:
    cost = weight * 1.50 + ground_flat_charge
  elif weight > 2 or weight <= 6:
    cost = weight * 3.00 + ground_flat_charge
  elif weight > 6 or weight <= 10:
    cost = (weight * 4.00) + ground_flat_charge
  elif weight > 10:
     cost = weight * 4.75 + ground_flat_charge
  return cost

drone_flat_charge = 0.00
def cost_drone_shipping(weight):
  if weight <= 2:
    cost = weight * 4.50 + drone_flat_charge
  elif weight > 2 or weight <= 6:
    cost = weight * 9.00 + drone_flat_charge
  elif weight > 6 or weight <= 10:
    cost = (weight * 12.00) + drone_flat_charge
  elif weight > 10:
     cost = weight * 14.25 + drone_flat_charge
  return cost

print(cost_ground_shipping(8.4))
print(cost_drone_shipping(1.5))

def find_cheapest_method(weight):
  if cost_ground_shipping(weight) < cost_drone_shipping(weight) and cost_ground_shipping(weight) <  premium_ground_flat_charge:
    return "cost_ground_shipping " + str (cost_ground_shipping(weight))
  elif cost_drone_shipping(weight) < cost_ground_shipping(weight) and cost_drone_shipping(weight) < premium_ground_flat_charge:
    return "cost_drone_shipping " + str (cost_drone_shipping(weight))
  else:
    return "premium_ground_flat_charge " + str(premium_ground_flat_charge)

cheapest_method = find_cheapest_method(4.8)
print(cheapest_method)

cheapest_method = find_cheapest_method(41.5)
print(cheapest_method)



