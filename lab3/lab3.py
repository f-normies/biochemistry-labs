# Функция для расчета концентрации холестерина
def calculate_cholesterol(ao, ak):
    concentration = (ao / ak) * 5.2  # Используем формулу из документа
    return concentration

# Расчет концентрации холестерина
cholesterol_concentration = calculate_cholesterol(0.003, 0.019)
print(f"Концентрация холестерола = {cholesterol_concentration:.2f} ммоль/л")