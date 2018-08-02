TAX_RATE = 8
rate = [13600, 14500, 16000, 11111, 11667]
print(list(map(lambda x: round(x * (1 + TAX_RATE / 100)), rate)))
