#!/usr/bin/env bash
python ../buildarff.py testdata.twtt testdata.arff
python ../buildarff.py training.1600000.twtt training.1600000.arff
