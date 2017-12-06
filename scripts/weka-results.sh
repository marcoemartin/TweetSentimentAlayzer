#!/usr/bin/env bash
# saves weka results to weka_results.txt
function callweka ()
{
 java -cp /u/cs401/WEKA/weka.jar $1 -t training.1600000.arff -T testdata.arff -o -i >> weka_results.txt
}
echo 'SVM classfier' > weka_results.txt
echo '********************************************************************' >> weka_results.txt
callweka weka.classifiers.functions.SMO

echo 'naive Bayes classifier' >> weka_results.txt
echo '********************************************************************' >> weka_results.txt
callweka weka.classifiers.bayes.NaiveBayes

echo 'decision trees classifier' >> weka_results.txt
echo '********************************************************************' >> weka_results.txt
callweka weka.classifiers.trees.J48
