arashi = {
    "Aiba": 175,
    "Matsumoto": 172,
    "Nnomiya": 168,
    "Oono": 166,
    "Sakurai": 171
}

li = sorted(
    arashi.items(),
    key=lambda x: x[1],
    reverse=False)
for name,height in li:
    print(name, height)
