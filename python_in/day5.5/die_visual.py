from die import Die
import pygal



die_1 = Die(8)
die_2 = Die(10)

# 开摇
results = []
times = 50000
for roll_num in range(times):
    rusult = die_1.roll() + die_2.roll()
    results.append(rusult)

# 统计
frequencies = []
sum_num = die_2.num_sides +die_1.num_sides
for value in range(2,sum_num + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.title = f"results of 2 rollings in {times} times"

hist.x_labels = []
for num in range(2,sum_num+1):
    hist.x_labels.append(str(num))


hist._x_title = 'Result'
hist.y_title = 'Frequency'

hist.add(f"D{die_1.num_sides}+D{die_2.num_sides}",frequencies)
hist.render_to_file('die_visual.svg')