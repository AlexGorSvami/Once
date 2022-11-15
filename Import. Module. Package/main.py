from datetime import datetime

time = datetime.now()
print(time.date())

from application import salary
from application.db import people

salary.calculate_salary()
people.get_employees()

from tqdm import tqdm
for i in tqdm(range(10000)):
    ...
if __name__ == '__main__':
    print()
