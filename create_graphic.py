import matplotlib.pyplot as plt
import csv
import sys

PROJECT_NAME = sys.argv[1]

x_yarn = []
y_yarn = []

x_build = []
y_build = []

x_unit = []
y_unit = []

x_int = []
y_int = []
step_name=["yarn", "yarn build", "yarn test:unit", "yarn test:integration"]

with open("filtered.csv", "r") as csv_file:
  plots = csv.reader(csv_file, delimiter=",")

  for row in plots:
    if "attempt" in row:
      continue

    match row[1]:
      case "yarn":
        x_yarn.append(int(row[0]))
        y_yarn.append(float(row[2]))
      case "yarn build":
        x_build.append(int(row[0]))
        y_build.append(float(row[2]))
      case "yarn test:unit":
        x_unit.append(int(row[0]))
        y_unit.append(float(row[2]))
      case "yarn test:integration":
        x_int.append(int(row[0]))
        y_int.append(float(row[2]))


for step in step_name:
  match step:
    case "yarn":
      plt.plot(x_yarn, y_yarn, marker="*", label=step)
    case "yarn build":
      plt.plot(x_build, y_build, marker="*", label=step)
    case "yarn test:unit":
      plt.plot(x_unit, y_unit, marker="*", label=step)
    case "yarn test:integration":
      plt.plot(x_int, y_int, marker="*", label=step)


plt.xlabel('Attempt')
plt.ylabel('Consumption (J)')
plt.title(f"Consumption per attempt - {PROJECT_NAME}")
plt.legend()

plt.show()
plt.savefig('consumption_output.png')
