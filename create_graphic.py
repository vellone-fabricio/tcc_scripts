import matplotlib.pyplot as plt
import csv
import sys

class StepInfos:
  def __init__(self, step_name) -> None:
    self.name = step_name
    self.x = []
    self.y = []

  def add_x(self, value):
    self.x.append(value)

  def add_y(self, value):
    self.y.append(value)


# Configs =================
PROJECT_NAME = sys.argv[1]
step_name=["yarn", "yarn build", "yarn test", "yarn test:docker:up", "yarn test:integration", "yarn test:docker:down"]
# =========================

for step in step_name:
  my_step = StepInfos(step)

  with open("filtered.csv", "r") as csv_file:
    plots = csv.reader(csv_file, delimiter=",")

    for row in plots:
      if "attempt" in row:
        continue

      if my_step.name == row[1]:
        my_step.add_x(int(row[0]))
        my_step.add_y(float(row[2]))



  plt.plot(my_step.x, my_step.y, marker="*", label=my_step.name)


plt.xlabel('Attempt')
plt.ylabel('Consumption (J)')
plt.title(f"Consumption per attempt - {PROJECT_NAME}")
plt.legend()

plt.savefig('consumption_output.png')
