def generate_password(n):

    if n < 3 or n > 20:
        return "Ошибка: число должно быть от 3 до 20."

    password = ""

    for i in range(1, n):
        for j in range(i + 1, n + 1):
            pair_sum = i + j
            if n % pair_sum == 0:
                password += f"{i}{j}"

    return password

for i in range(3, 21):
    result = generate_password(i)
    print(f"{i} - {result}")