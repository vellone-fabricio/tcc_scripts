#! /bin/bash

command_base="sudo -E env PATH=$PATH perf stat -e power/energy-cores/,power/energy-ram/,power/energy-gpu/,power/energy-pkg/,power/energy-psys/"

step_name=("yarn"  "yarn build"  "yarn test:unit"  "yarn test:integration")


echo "Creating .csv file to have all data..."
echo "attemp,step,consumption(J),time(s)" > filtered.csv
echo "File created!"


for run in 1; do
  echo "Run number: #${run} ---------------"
  for step in "${step_name[@]}"; do
    echo "Step name: '${step}'"

    full_command="${command_base} ${step}"

    $full_command > all_output.txt 2>&1

    echo "Filter file with Python..."
    python perfScript.py "${run}" "${step}" >> filtered.csv
    echo "Save in .csv!...\n"
  done

  echo "Attempt done\n\n\n"
done

echo "Finished!"
