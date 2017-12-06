echo "3.3 Feature analysis" >> 3.3output.txt
/u/cs401/WEKA/infogain.sh 3.2/500.TRAINING.some.arff >> 3.3output.txt
/u/cs401/WEKA/infogain.sh 3.2/10000.TRAINING.some.arff >> 3.3output.txt
echo "Explanation: " >> 3.3output.txt
echo "explain what features, if any, retain their importance at both low and high(er) amounts of input data.  Also provide a possible explanation as to why this might be." >> 3.3output.txtv
