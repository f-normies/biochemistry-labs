import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd

# Экспериментальные данные (оптическая плотность)
data = np.array([0.263, 0.481, 0.733, 0.849, 1.089])
experiment = 0.331  # Экспериментальное значение

# Расчет концентрации (%)
volume = 0.9  # Объем раствора
mass = np.array([0.001, 0.002, 0.003, 0.004, 0.005])  # Масса вещества
concentrations = (mass / volume) * 100  # Расчет концентраций

# Подгонка кривой (линейная регрессия)
coefficients = np.polyfit(data, concentrations, 1)  # Получение коэффициентов
slope, intercept = coefficients  # Коэффициенты уравнения прямой

# Функция линейной модели
def linear_model(x):
    return slope * x + intercept

# Прогнозирование концентрации
predicted_concentration = linear_model(experiment)

# Графики
plt.scatter(data, concentrations, label='Data Points')
plt.plot(data, linear_model(data), label='Fitted Line', color='r')
plt.scatter(experiment, predicted_concentration, color='g', label=f'Prediction ({predicted_concentration:.4f})')
plt.xlabel('Optical Density')
plt.ylabel('Concentrations (%)')
plt.legend()
plt.savefig('data.png', dpi=300)
plt.show()

# Создание таблички с данными и прогнозом
table = pd.DataFrame({
    'Optical Density': np.append(data, experiment),
    'Concentrations (%)': np.append(concentrations, predicted_concentration)
})
table.to_csv('data.csv', index=False)