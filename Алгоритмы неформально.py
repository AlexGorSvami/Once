# def ball_trajectory(x):
#     location = 10 * x - 5 * (x**2)
#     return location
#
# import matplotlib.pyplot as plt
# xs = [x / 100 for x in list(range(201))]
# ys = [ball_trajectory(x) for x in xs]
# plt.plot(xs, ys)
# plt.title('The Trajectory of a Thrown Ball')
# plt.xlabel('Horizontal Position Ball')
# plt.ylabel('Vertical Position of Ball')
# plt.axhline(y = 0)
# plt.show()


# RPM
import math

n1 = 89
n2 = 18
halving = [n1]
while min(halving) > 1:
    halving.append(math.floor(min(halving)/2))

doubling = [n2]
while len(doubling) < len(halving):
    doubling.append(max(doubling) * 2)
# half double:
import pandas as pd
half_double = pd.DataFrame(zip(halving, doubling))
half_double = half_double.loc[half_double[0] % 2 == 1, :]
answer = sum(half_double.loc[:, 1])
print(answer)
print(half_double)
