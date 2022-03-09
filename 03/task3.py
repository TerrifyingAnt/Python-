import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import random
import numpy as np
from matplotlib.animation import FuncAnimation

warnings.filterwarnings(action='once')
large = 22
med = 16
small = 12
params = {'axes.titlesize': large,
          'legend.fontsize': med,
          'figure.figsize': (16, 10),
          'axes.labelsize': med,
          'axes.titlesize': med,
          'xtick.labelsize': med,
          'ytick.labelsize': med,
          'figure.titlesize': large}
plt.rcParams.update(params)
plt.style.use('seaborn-whitegrid')
sns.set_style("white")

random.seed(version=2)
temp_list = []
mylist = []
sprite_len = 10
def generate():
    for l in range(5):
        for i in range(sprite_len):
            for j in range(int(sprite_len / 2) + sprite_len % 2):
                temp_list.append(random.randrange(0, 2))

            new_len = int(sprite_len / 2)
            for k in range(new_len, sprite_len):
                print((len(temp_list)))
                print(sprite_len - k)
                temp_list.append(temp_list[sprite_len - k - 1])
            mylist.append(temp_list)
            temp_list = []
        return mylist

fig = plt.plot

animation = FuncAnimation(
    fig,  # фигура, где отображается анимация
    func=generate,  # функция обновления текущего кадра
    frames=np.empty([5, 5]),  # параметр, меняющийся от кадра к кадру
    fargs=mylist,  # дополнительные параметры для функции update_cos
    interval=30,  # задержка между кадрами в мс
    blit=True,  # использовать ли двойную буферизацию
    repeat=False)  # зацикливать ли анимацию

# Plot
fig.show()

