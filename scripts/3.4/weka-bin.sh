#!/usr/bin/env bash
# this saves all output to $DESTINATION
# to use this script, cd to bin folder then run ../weka-bin.sh 
# make sure this script has chmod +x
function callweka ()
{
 java -cp /u/cs401/WEKA/weka.jar $1 -t concat.arff -T main.arff -v -o -i
}

  DESTINATION=weka_results.txt

  echo 'SVM classfier' > $DESTINATION
  echo '********************************************************************' >> $DESTINATION
  callweka weka.classifiers.functions.SMO >> $DESTINATION

  echo 'naive Bayes classifier' >> $DESTINATION
  echo '********************************************************************' >> $DESTINATION
  callweka weka.classifiers.bayes.NaiveBayes >> $DESTINATION

  echo 'decision trees classifier' >> $DESTINATION
  echo '********************************************************************' >> $DESTINATION
  callweka weka.classifiers.trees.J48 >> $DESTINATION

