#!/usr/bin/env bash
function callweka ()
{
 CLASSIFIER=$1
 TRAININGFILE=$2
 java -cp /u/cs401/WEKA/weka.jar $CLASSIFIER -t $TRAININGFILE -T testdata.arff -o -no-cv -i
}

# Trains each .arff file in the directory and compares it against testdata.arff

for ARFF in *.arff; do
    echo $ARFF
    RESULTS=$ARFF.results.txt
    touch $RESULTS
    echo "touch"
    echo $ARFF > $RESULTS
    echo 'SVM classfier' >> $RESULTS
    echo '********************************************************************' >> $RESULTS
    callweka weka.classifiers.functions.SMO $ARFF >> $RESULTS

    echo 'naive Bayes classifier' >> $RESULTS
    echo '********************************************************************' >> $RESULTS
    callweka weka.classifiers.bayes.NaiveBayes $ARFF >> $RESULTS

    echo 'decision trees classifier' >> $RESULTS
    echo '********************************************************************' >> $RESULTS
    callweka weka.classifiers.trees.J48 $ARFF >> $RESULTS

done
