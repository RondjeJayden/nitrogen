import random, string

amount = int(input('How many codes would you generate?'))
value = 1
while value <= amount:
    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    f = open('ghost_nitro.txt', 'a+')
    f.write(f'{code}\n')
    f.close()
    print(f'[GENERATED] {code}')
    value += 1
