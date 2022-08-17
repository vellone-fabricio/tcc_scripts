#! /bin/bash

# Define control variables ===============
command_base="sudo -E env PATH=$PATH perf stat -e power/energy-cores/,power/energy-ram/,power/energy-gpu/,power/energy-pkg/,power/energy-psys/"
steps_amount=$(seq 1 1)

project_name="Marble"
steps_name=("yarn"  "yarn build"  "yarn test:unit"  "yarn test:integration")
has_caching="true" # of "false"
# ==================================

echo "Creating .csv file to have all data..."
echo "attempt,step,consumption(J),time(s)" > filtered.csv
echo "File created!"
echo


for run in $steps_amount; do
  echo "Run number: #${run} ---------------"
  echo

  echo "Removing node_modules..."
  sudo rm -rf node_modules

  if [[ has_caching -eq "true" ]]; then
    echo "Removing dock images from cache..."
    docker rmi -f $(docker images -aq)
    echo
  fi


  for step in "${steps_name[@]}"; do
    echo "Step name: '${step}'"

    full_command="${command_base} ${step}"

    $full_command > all_output.txt 2>&1

    echo "Filter file with Python..."
    python perfScript.py "${run}" "${step}" >> filtered.csv
    echo "Save in .csv!..."
    echo
  done

  echo "Attempt done"
  echo
  echo
  echo
done

rm all_output.txt
echo "Creating graph.."
python create_graphic.py $project_name

echo "Finished!"
