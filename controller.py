from colorama import Fore

modules = ["beepboopy_random", "random_copycat"]
others_money = []  # The `money_insert` var of the other bots, list of tuples
money = [0] * len(modules)  # Each players own money


for stage in range(1, 4):
    mmm = []  # Money put into the Money Making Machine
    rounds_money = []  # Current rounds `money_insert` var`
    money_pub = []

    for index, module_name in enumerate(modules):
        module = __import__(module_name)
        money_insert_pub = module.plan(stage, others_money)
        money_pub.append(money_insert_pub)

    for index, module_name in enumerate(modules):
        module = __import__(module_name)
        money_insert = module.main(stage, others_money, money_pub)
        mmm.append(money_insert)
        rounds_money.append(money_insert)
        money[index] += 100 - money_insert

    others_money.append(tuple(rounds_money))

    for index in range(len(modules)):
        if stage == 1:
            boost = 1.2
        if stage == 2:
            boost = 1.5
        else:
            boost = 2

        money[index] += round((sum(mmm) / len(modules)) * boost)

results = []

for index, module in enumerate(modules):
    results.append((money[index], module))

results.sort(reverse=True)

print(f"{Fore.RED}\033[1mResults:\033[0m{Fore.WHITE}")

for points, module in results:
    print(f"{Fore.GREEN}{module}{Fore.WHITE}, {Fore.CYAN}{points}{Fore.WHITE} points")
