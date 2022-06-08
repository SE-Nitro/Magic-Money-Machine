import random

modules = ["mrtruthyrandom", "mrlierrandom"]
rounds_won = []
total_tickets = []


for _round in range(1, 4):
    shared_tickets = []
    tickets = []
    shared_values = []

    for index, module_name in enumerate(modules):
        module = __import__(module_name)
        public_val, shared = module.public_number(
            _round, [1 if round == index else 0 for _round in rounds_won]
        )
        shared_values.append(shared)
        shared_tickets.append(public_val)

    for index, module_name in enumerate(modules):
        module = __import__(module_name)
        ticket = module.real_number(
            _round,
            [1 if _round == index else 0 for _round in rounds_won],
            shared_tickets,
            shared_values[index],
        )
        tickets.append(ticket)

    draw_list = []
    for index, ticket in enumerate(tickets):
        draw_list += [index] * ticket

    rounds_won.append(random.choice(draw_list))
    total_tickets.append(len(draw_list))


print("Results:")
points_list = [0] * len(modules)
for index, _round in enumerate(rounds_won):
    if index == 0:
        points_list[_round] = 100 / total_tickets[index]
    elif index == 1:
        points_list[_round] = 300 / total_tickets[index]
    else:
        points_list[_round] = 500 / total_tickets[index]

for index, module in enumerate(modules):
    print(f"{module}, {str(round(points_list[index]))} points")
