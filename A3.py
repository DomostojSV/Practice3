
prev = int(input("Показания счетчиков газа за прошлый месяц "))
curr = int(input("Показания счетчиков газа за текущий месяц "))


if curr >= prev:
    used = curr - prev
else:
    used = (10000 - prev) + curr


if used <= 300:
    payment = 21.5
elif used <= 600:
    payment = 21.5 + (used - 300) * 0.065
elif used <= 800:
    payment = 21.5 + 300 * 0.065 + (used - 600) * 0.045
else:
    payment = 21.5 + 300 * 0.065 + 200 * 0.045 + (used - 800) * 0.025


if used > 0:
    avg_price = payment / used
else:
    avg_price = 0


payment = round(payment, 2)
avg_price = round(avg_price, 2)


print(f"Предыдущее   Текущее    Использовано   К оплате   Ср. цена m^3")

print(f"{prev:<12} {curr:<10} {used:<14} {payment:<10} {avg_price:<12}")
