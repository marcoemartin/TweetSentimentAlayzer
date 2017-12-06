import subprocess


def start_file(arff_file):
    text =  '''@relation tweet\n
@attribute 1st_person numeric
@attribute 2nd_person numeric
@attribute 3rd_person numeric
@attribute coord_conjunction numeric
@attribute past_tense_verb numeric
@attribute future_tense_verb numeric
@attribute commas numeric
@attribute colons numeric
@attribute dashes numeric
@attribute parentheses numeric
@attribute ellipses numeric
@attribute common_nouns numeric
@attribute proper_nouns numeric
@attribute adverbs numeric
@attribute wh_words numeric
@attribute modern_slang numeric
@attribute upper_case_words numeric
@attribute avg_length_sentences numeric
@attribute avg_length_token numeric
@attribute num_sentences numeric
@attribute class {0,4}

@data
'''
    try:
        file = open(arff_file,'w')   # Trying to create a new file or open one
        file.write(text)
        file.close()
    except:
        print('Something went wrong! Can\'t tell what?')
        sys.exit(0) # quit Python


if __name__ == "__main__":
    half = 20000/2
    part = half/10

    for i in range(10):
        start_file('cv'+str(i+1)+'.arff')

    i=0
    j = 0

    n = 0
    m = 0
    t = 0
    print 'partitioning!'
    with open('../training.1600000.arff') as f:
        for line in f:
            if not line[0] == '@' and t <= half:
                if n < part:
                    with open('cv'+str(i+1)+'.arff', "a") as f:
                        f.write(line)
                    n += 1
                else:
                    n = 0
                    i += 1
                t += 1
            if t > half and t <= 20000:
                if m < part:
                    with open('cv'+str(j+1)+'.arff', "a") as f:
                        f.write(line)
                    m += 1
                else:
                    m = 0
                    j += 1

                t += 1

    print "STARTING CROSS VALIDATION!"
    a = open('everything.txt', 'a')
    for i in range(10):
        print i+1
        start_file('tempcv.arff')

        for j in range(10):
            if j == i:
                j += 1

            if j < 10:
                with open('cv'+str(j+1)+'.arff') as f:
                    for line in f:
                        if not line[0] == '@':
                            with open('tempcv.arff', "a") as temp:
                                temp.write(line)
                    temp.close()
                f.close

        command = 'java -cp /u/cs401/WEKA/weka.jar weka.classifiers.trees.J48 -T cv'+str(i+1)+'.arff -t tempcv.arff -x 10 -i'
        print command
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        print(output)
        with open('crossTrees'+str(i+1)+'out.txt', 'w') as out:
            print 'writing trees output to file'
            out.write(output)
            a.write(output)
            out.close()

        command = 'java -cp /u/cs401/WEKA/weka.jar weka.classifiers.functions.SMO -T cv'+str(i+1)+'.arff -t tempcv.arff -x 10 -i'
        print command
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        print(output)
        with open('crossSMOs'+str(i+1)+'out.txt', 'w') as out:
            print 'writing SMO output to file'
            out.write(output)
            a.write(output)
            out.close()

        command = 'java -cp /u/cs401/WEKA/weka.jar weka.classifiers.bayes.NaiveBayes -T cv'+str(i+1)+'.arff -t tempcv.arff -x 10 -i'
        print command
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        print(output)
        with open('crossBayes'+str(i+1)+'out.txt', 'w') as out:
            print 'writing Bayes output to file'
            out.write(output)
            a.write(output)
            out.close()

    a.close()
