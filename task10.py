# 2) Если вы были на Луне сейчас, ваш вес будет 16,5% от вашего веса земли.
# Для его расчета необходимо умножить на 0,165. Если в ближайшие 15 лет ваш вес
# будет
# увеличение на 1 кг каждый год. Какой будет ваш вес каждый год на Луне в следующем
# 15 лет?

import datetime
import time

earth_weight = 50
moon_index = 0.165
year_now = datetime.date.today().year

for i in range(1, 16):
    print(f"Ваш вес в {year_now} году: {round(earth_weight * moon_index, 2)} кг" )
    earth_weight += 1
    year_now +=1