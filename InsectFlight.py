import insectClass as i

housefly = i.Insect(2,4)

mosquito = i.Insect(6,8)

housefly.flight_length()

mosquito.flight_length()

print('the housefly can fly up to', housefly.get_flight())

print('the mosquito can fly up to', mosquito.get_flight())