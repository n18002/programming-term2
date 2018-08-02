arashi ={
    "Aiba": 35,
    "Matshumoto": 34,
    "Ninomiya": 35,
    "Oono": 37,
    "Skurai": 36
}

li = sorted(
    arashi.items(),
    key=lambda x: x[1],
    reverse=True)
for name,age in li:
    print(name, age)
