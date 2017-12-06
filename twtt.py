import sys
import csv
import re
import NLPlib

try:
    from HTMLParser import HTMLParser
except ImportError:
    from html.parser import HTMLParser

corpus = []
new_corpus = []
tweet_path = '/u/cs401/A1/tweets/'

def twtt1(text):
    html_tag = re.sub(r'/<[^>]+>/', '', text)
    return html_tag


def twtt2(tweet):
    h = HTMLParser()
    for match in re.finditer("&[^\s]*;", tweet):
        try:
            tweet = tweet.replace(match.group(), str(h.unescape(match.group())))
        except UnicodeDecodeError:
            continue
    return tweet


def twtt3(text):
    url = re.sub(r'([^\w\d])(http://|https://|www\.)[^\s\"]+', r'\1', text)
    return url


def twtt4(text):
    hashtag = re.sub(r'#', '', text)
    user = re.sub(r'@', '', hashtag)
    return user


def twtt5(text):
    final_sentence = ''
    sentence = ''
    words = text.split()
    i = 1
    for word in words:
        if word in abbrev:
            if i == len(words):
                sentence += word+'\n'
                final_sentence += sentence
                sentence = ''
            else:
                sentence += word+' '
        else:
            match = re.match(r'[A-Za-z;\_\-,\'\"]+[.!?]+', word)
            if not match:
                sentence += word+' '
            else:
                sentence += word+'\n'
                final_sentence += sentence
                sentence = ''
        i += 1

    if final_sentence == '':
        i = 1
        sentence = ''
        for word in words:
            if i == len(words):
                sentence += word +'\n'
            else:
                sentence += word+' '
            i += 1
        final_sentence += sentence

    return final_sentence


def twtt7(text):
    final_array = ''
    for sentence in text.split('\n'):
        line = ''
        i = 1
        words = sentence.split()
        for word in words:
            punctuation = re.findall('[.,?!\']+', word)
            apostraphe = re.findall('[\'][\w]+', word)
            nt_case = re.findall('[n][\'][t]', word)

            if nt_case:
                mod_word = word.replace(nt_case[0], "")
                word = mod_word +' '+nt_case[0]
            elif apostraphe:
                mod_word = word.replace(apostraphe[0], "")
                word = mod_word +' '+apostraphe[0]
            elif punctuation:
                mod_word = word.replace(punctuation[0], "")
                word = mod_word +' '+punctuation[0]
            if i == len(words):
                line += word
            else:
                line += word+' '
            i += 1
        final_array += line+'\n'

    return final_array


def twtt8(text,tagger):
    result = ''
    for sentence in text.split('\n'):
        words = sentence.split()
        tags = tagger.tag(words)
        for i in range(len(words)):
            result += words[i]+'/'+tags[i]+' '
        result += '\n'
    return result.strip()


def twtt9(text, pol):
    return '<A='+pol+'>\n' + text


def print_lines(corpus):
    for item in corpus:
        line = 0
        for it in item:
            line +=1
            if line ==6:
                print it

if __name__ == '__main__':
    file = sys.argv[1]
    student_num = int(sys.argv[2])
    outfile = sys.argv[3]

    if file == 'large':
        file = '/u/cs401/A1/tweets/testdata.manualSUBSET.2009.06.14.csv'

    elif file == "subset":
        file = 'subset.csv'


    file_size = 0
    with open(file, 'rb') as csvfile:
        file_size += 1

    with open(file, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        if file_size > 20000:
            ptr = 1
            start = student_num%80*10000
            end = 800000+student_num%80*10000
            for row in reader:
                if (start <= ptr and ptr < start+10000) or (end <= ptr and ptr < end+10000):
                    corpus.append(row)
                ptr += 1
        else:
            for row in reader:
                corpus.append(row)


    with open('/u/cs401/Wordlists/abbrev.english', 'r') as f:
        abbrev = [line.rstrip('\n') for line in f]

    tagger = NLPlib.NLPlib()
    result_file = open(sys.argv[3], "w")

    for item in corpus:
        line = 0
        for tweet in item:
            line += 1
            if line == 1:
                pol = tweet
            if line == 6:
                tweet = twtt1(tweet)
                tweet = twtt2(tweet)
                tweet = twtt3(tweet)
                tweet = twtt4(tweet)
                tweet = twtt5(tweet)
                tweet = twtt7(tweet)
                tweet = twtt8(tweet, tagger)
                print >> result_file, twtt9(tweet,pol)
    result_file.close()
