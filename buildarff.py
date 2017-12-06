import sys
import os
import re

first = ["I", "me", "my", "mine", "we", "us", "our", "ours"]
second = ["you", "your", "yours", "u", "ur", "urs"]
third = ["he", "him", "his", "she", "her", "hers", "it", "its", "they", "them", "their", "theirs"]
future_tense = ["'ll", "will", "gonna"]
slang = ["smh", "fwb", "lmfao", "lmao", "lms", "tbh", "rofl", "wtf", "bff", "wyd", "lylc", "brb", "atm", "imao", "sml", "btw", "bw", "imho", "fyi", "ppl", "sob", "ttyl", "imo", "ltr", "thx", "kk", "omg", "ttys", "afn", "bbs", "cya", "ez", "f2f", "gtr","ic", "jk", "k", "ly", "ya", "nm", "np", "plz", "ru", "so", "tc", "tmi", "ym", "ur", "u", "sol"]

def feat1(line):
    count = 0
    for fir in first:
        f = re.findall(' '+fir+'/' ,line)
        if f:
            count += len(f)
    return count


def feat2(line):
    count = 0
    for sec in second:
        f = re.findall(' '+sec+'/' ,line)
        if f:
            count += len(f)
    #for word in line.split():
    #    for sec in second:
    #        if sec+'/' in word.lower():
    #            count += 1
    return count


def feat3(line):
    count = 0
    for thir in third:
        f = re.findall(' '+thir+'/' ,line.lower())
        if f:
            count += len(f)
    #for word in line.split():
    #    for thir in third:
    #        if thir+'/' in word.lower():
    #            count += 1
    return count


def feat4(line):
    count = 0
    for word in line.split():
        if '/CC' in word:
            count += 1
    return count


def feat5(line):
    count = 0
    for word in line.split():
        if "/VBD" in word:
            count += 1
    return count


def feat6(line):
    count = 0
    i = 0
    l = line.split()
    for word in l:
        for fur in future_tense:
            if (fur+'/' in word.lower()) or (i < len(l) -1 and "going/" in l[i].lower() and "to/" in l[i+1].lower()):
                count += 1
        i += 1
    return count


def feat7(line):
    commas = re.findall('[,]', line)
    return len(commas)


def feat8(line):
    colons = re.findall(':/:|;/:', line)
    return len(colons)


def feat9(line):
    dashes = re.findall('[-]', line)
    return len(dashes)


def feat10(line):
    parentheses = re.findall('[()]', line)
    return len(parentheses)


def feat11(line):
    ellipses = re.findall('\.{2,}', line)
    return len(ellipses)


def feat12(line):
    comn_noun = re.findall('/NN |/NNS ', line)
    return len(comn_noun)


def feat13(line):
    propr_noun = re.findall('/NNP |/NNPS ', line)
    return len(propr_noun)


def feat14(line):
    adverbs_noun = re.findall('/RB |/RBR |/RBS ', line)
    return len(adverbs_noun)


def feat15(line):
    wh_wrds = re.findall('/WDT |/WP |/WP$ |/WRB ', line)
    return len(wh_wrds)


def feat16(line):
    count = 0
    for slg in slang:
        f = re.findall(' '+slg+'/' ,line.lower())
        if f:
            count += len(f)
    return count


def feat17(line):
    caps = re.findall('[A-Z]{2,}/', line)
    return len(caps)


def feat18(line):
    return len(line.split())


def feat19(line):
    count = 0
    words = re.findall('[A-Za-z]+/', line)
    for word in words:
        for c in word:
            if c != '/':
                count += 1
    return count


def feat20(line):
    words = re.findall('[A-Za-z]+/', line)
    if words == []:
        return 1
    return len(words)


if __name__=="__main__":
    if len(sys.argv) < 3 or len(sys.argv)>4:
        print "Usage: %s <input filename> <arff file> [<max number>]" %(sys.argv[0])
        sys.exit(0)

    if not os.path.exists(sys.argv[1]):
        print(sys.argv[1] + " file does not exist")
        sys.exit(0)

    ismax = False
    tweet_file = sys.argv[1]
    arff_file =  open(sys.argv[2],'w')
    if len(sys.argv) == 4:
        max_twtts = int(sys.argv[3])
    else:
        max_twtts = 20000
        ismax = True

    print >> arff_file, '@relation tweet\n'
    print >> arff_file, '@attribute 1st_person numeric'
    print >> arff_file, '@attribute 2nd_person numeric'
    print >> arff_file, '@attribute 3rd_person numeric'
    print >> arff_file, '@attribute coord_conjunction numeric'
    print >> arff_file, '@attribute past_tense_verb numeric'
    print >> arff_file, '@attribute future_tense_verb numeric'
    print >> arff_file, '@attribute commas numeric'
    print >> arff_file, '@attribute colons numeric'
    print >> arff_file, '@attribute dashes numeric'
    print >> arff_file, '@attribute parentheses numeric'
    print >> arff_file, '@attribute ellipses numeric'
    print >> arff_file, '@attribute common_nouns numeric'
    print >> arff_file, '@attribute proper_nouns numeric'
    print >> arff_file, '@attribute adverbs numeric'
    print >> arff_file, '@attribute wh_words numeric'
    print >> arff_file, '@attribute modern_slang numeric'
    print >> arff_file, '@attribute upper_case_words numeric'
    print >> arff_file, '@attribute avg_length_sentences numeric'
    print >> arff_file, '@attribute avg_length_token numeric'
    print >> arff_file, '@attribute num_sentences numeric'
    print >> arff_file, '@attribute class {0,4}\n'
    print >> arff_file, '@data'

    first_person =0
    second_person = 0
    third_person = 0
    coord = 0
    past = 0
    future = 0
    commas = 0
    colons = 0
    dashes = 0
    parentheses = 0
    ellipses = 0
    common_nouns = 0
    proper_nouns = 0
    adverbs = 0
    wh_words = 0
    modern_slang = 0
    upper_case = 0
    avg_sentece_length = 0.0
    avg_token_length = 0.0
    num_words = 0
    num_sentences = 0
    pol = 0

    pos_twtts= max_twtts
    neg_twtts = max_twtts
    count = 0
    with open(tweet_file, 'r') as f:
        for line in f:
            if '<A=' in line:
                if count != 0:
                    data = str(first_person)+', '+str(second_person)+', '+str(third_person)+', '+str(coord)+', '+str(past)+', '+str(future)+', '+str(commas)+', '+str(colons)+', '+str(dashes)+', '+str(parentheses)+', '+str(ellipses)+', '+str(common_nouns)+', '+str(proper_nouns)+', '+str(adverbs)+', '+str(wh_words)+', '+str(modern_slang)+', '+str(upper_case)+', '+str(avg_sentece_length/num_sentences)+', '+str(avg_token_length/num_words)+', '+str(num_sentences)+', '+str(pol)
                    if not ismax:
                        if pos_twtts > 0 and  int(pol) == 4:
                            print >> arff_file, data
                            pos_twtts -= 1
                        if neg_twtts > 0 and int(pol) == 0:
                            print >> arff_file, data
                            neg_twtts -= 1
                    else:
                        print >> arff_file, data

                    first_person =0
                    second_person = 0
                    third_person = 0
                    coord = 0
                    past = 0
                    future = 0
                    commas = 0
                    colons = 0
                    dashes = 0
                    parentheses = 0
                    ellipses = 0
                    common_nouns = 0
                    proper_nouns = 0
                    adverbs = 0
                    wh_words = 0
                    modern_slang = 0
                    upper_case = 0
                    avg_sentece_length = 0.0
                    avg_token_length = 0.0
                    num_words = 0
                    num_sentences = 0
                pol = re.findall('[\d]', line)[0]
            else:
                first_person += feat1(line)
                second_person += feat2(line)
                third_person += feat3(line)
                coord += feat4(line)
                past += feat5(line)
                future += feat6(line)
                commas += feat7(line)
                colons += feat8(line)
                dashes += feat9(line)
                parentheses += feat10(line)
                ellipses += feat11(line)
                common_nouns += feat12(line)
                proper_nouns += feat13(line)
                adverbs += feat14(line)
                wh_words += feat15(line)
                modern_slang += feat16(line)
                upper_case += feat17(line)
                avg_sentece_length += feat18(line)
                avg_token_length += feat19(line)
                num_words += feat20(line)
                num_sentences += 1
            count += 1
    f.close()

    if ismax:
        data = str(first_person)+', '+str(second_person)+', '+str(third_person)+', '+str(coord)+', '+str(past)+', '+str(future)+', '+str(commas)+', '+str(colons)+', '+str(dashes)+', '+str(parentheses)+', '+str(ellipses)+', '+str(common_nouns)+', '+str(proper_nouns)+', '+str(adverbs)+', '+str(wh_words)+', '+str(modern_slang)+', '+str(upper_case)+', '+str(avg_sentece_length/num_sentences)+', '+str(avg_token_length/num_words)+', '+str(num_sentences)+', '+str(pol)
        print >> arff_file, data

    arff_file.close()
