def create_file_with_strings():
    # Створення та запис в файл TF2_1
    try:
        with open("TF2_1.txt", "w") as file:
            # Записуємо кілька рядків різної довжини, зокрема рядки з числами
            file.write("Тестовий рядок 123.\n")
            file.write("інший рядок з числами 56789.\n")
            file.write("Рандомний рядок.\n")
            file.write("І 101 рядок який містить будь що 30507.\n")
        print("Файл TF2_1.txt успішно створено та заповнено даними.")
    except Exception as e:
        print(f"Помилка при створенні або записі в файл TF2_1.txt: {e}")

def extract_digit_sequences():
    # Зчитування та обробка даних з файлу TF2_1
    try:
        with open("TF2_1.txt", "r") as file:
            content = file.read()
        
        import re
        # Знаходимо всі послідовності цифр довжиною більше двох
        digit_sequences = re.findall(r"\d{3,}", content)
        # Записуємо знайдені послідовності в TF2_2
        with open("TF2_2.txt", "w") as file:
            file.write(" ".join(digit_sequences))
        print("Файл TF2_2.txt успішно створено з послідовностями цифр.")
    except FileNotFoundError:
        print("Файл TF2_1.txt не знайдено. Будь ласка, створіть файл перед обробкою.")
    except Exception as e:
        print(f"Помилка при зчитуванні або записі в файл TF2_2.txt: {e}")

def display_content_of_TF2_2():
    # Зчитування та виведення вмісту файлу TF2_2
    try:
        with open("TF2_2.txt", "r") as file:
            content = file.read()
            print("Вміст файлу TF2_2.txt:")
            print(content)
    except FileNotFoundError:
        print("Файл TF2_2.txt не знайдено. Перевірте, чи файл створено.")
    except Exception as e:
        print(f"Помилка при зчитуванні файлу TF2_2.txt: {e}")

# Виклик функцій для виконання завдання
create_file_with_strings()
extract_digit_sequences()
display_content_of_TF2_2()
