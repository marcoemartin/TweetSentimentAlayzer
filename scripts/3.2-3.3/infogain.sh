#!/usr/bin/env bash
# Run infogain on every single arff in directory
DESTINATION=./results/increment.infogain.txt
for ARFF in *.arff;do
  echo $ARFF >> $DESTINATION
  sh /u/cs401/WEKA/infogain.sh $ARFF >> $DESTINATION
done
cat $DESTINATION

