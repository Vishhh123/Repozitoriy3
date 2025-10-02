probezhal = 10
vesb_putb = probezhal

print(f"1 день: {probezhal:.2f} км")

for day in range(2, 8):
    probezhal = probezhal * 1.10  # увеличение дневной нормы на 10%
    vesb_putb += probezhal
    print(f"{day} день: {probezhal:.2f} км")

print(f"Суммарный путь за 7 дней: {vesb_putb:.2f} км")



    