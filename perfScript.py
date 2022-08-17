import sys

attempt_run = sys.argv[1]
step_name = sys.argv[2]

time_exec = 0.0
consum_total = 0.0
with open("all_output.txt") as file:
  for line in file:
    if "Joules" in line:
      all_text = line.split()
      value_str = all_text[0].replace(",", "")
      consum_total += float(value_str)

    elif "seconds time elapsed" in line:
      all_text = line.split()
      value_str = all_text[0].replace(",", "")
      time_exec += float(value_str)


print(f"{attempt_run},{step_name},{consum_total},{time_exec}")
