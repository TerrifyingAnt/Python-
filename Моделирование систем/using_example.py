import numpy as np
from DecisionHelper import DecisionHelper

if __name__ == '__main__':
    name = ['Blender', '3ds Max', 'Maya', 'Cinema 4d', 'ZBrush']
    param = ['Цена', 'Функциональная пригодность', 'Уровень производительности', 'Удобство использования',
          'Совместимость', 'Завершенность', 'Эстетика пользовательского интерфейса']
    matrix = np.array([[5, 90, 80, 50, 90, 70, 40],
                  [1, 80, 85, 90, 75, 75, 80],
                  [1, 70, 75, 40, 80, 80, 50],
                  [2, 80, 50, 60, 80, 70, 60],
                  [3, 70, 80, 90, 70, 80, 90]])
    weights = [0.3, 0.2, 0.2, 0.05, 0.025, 0.025, 0.2]

    dh = DecisionHelper(matrix, weights, name)
    print("Таблица:")
    print("\t", end="")
    for i in param:
        print(i, end="; ")
    print("")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="; ")
        print("")
    print("~~~~~~")
    dh.saw()
    dh.topsis()
    dh.electre()
