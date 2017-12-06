# folding.py
import re, shutil, os
def generate_tweets(infilename, size):
    data_match = re.compile(r"@data")
    found_data = False
    ten_tweets = []
    with open(infilename, 'rb') as infile:
        for line in infile:
            if found_data:
                ten_tweets.append(line)

            if data_match.search(line):
                found_data = True

            if len(ten_tweets) == size:
                yield ten_tweets
                ten_tweets = []
        else:
            yield "end"

def partition(bin, bin_list):
    '''
    Take bin, copy it to its folder, copy the other bins over as well but
    concatenate them into a new file.

    :param bin: - Name of bin to partition
    :param bin_list: - List of bin_names for concatenation, including param bin
    :return: None
    '''

    print "BIN LIST", bin_list
    # name of the main bin of its folder
    target_folder = os.path.relpath(bin)

    # name of file to put all other bins in bin_list
    concat_bin = os.path.join(target_folder, "concat.arff")

    arff_header = os.path.relpath("arff_header")
    main_bin =  os.path.join(target_folder, "main.arff")

    shutil.copy(arff_header, main_bin)
    print "Copied ARFF header to main_bin"

    with open(main_bin, 'a') as main_b:
        with open(bin+".arff", 'rb') as in_b:
            shutil.copyfileobj(in_b, main_b)
    print "Wrote header to", main_bin

    # next loop over bin_list and copy its contents to concat_bin for each bin
    with open(concat_bin, 'a') as concat_b:
        with open(arff_header, 'rb') as header_f:
            shutil.copyfileobj(header_f, concat_b)

        print "Copied ARFF header"

        for bin_name in bin_list:
            if not bin_name == bin:
                print "Processing", bin_name

                with open(bin_name + ".arff", 'rb') as input_b:
                    shutil.copyfileobj(input_b, concat_b)

                print "Finished", bin_name, "\n"

    print "Saved", concat_bin

if __name__ == "__main__":
    # Name of training arff we're going to fold over that's in current dir
    master_arff = "training.1600000.arff.master"
    bin_names = []
    stripped_bin_names = []
    for i in range(1, 11):
        name = "bin" + str(i) + ".arff"
        bin_names.append(name)
        stripped_bin_names.append(name.strip(".arff"))


    # Generate bin files by taking in datalines from specified arff
    count = 1
    set_size = 100

    for ten_tweets in generate_tweets(master_arff, set_size):
        for name in bin_names:
            with open(name, 'a') as f:
                if isinstance(ten_tweets, str):
                    break

                f.write(ten_tweets.pop())
        progress = (float(count) / (20000 / set_size)) * 100
        print "Processed ten tweets!", str(progress) + "%"
        count += 1
    print "Done creating bins!"


    # Write function that selects a filename from the list, pops it out of the list, then concatenates everything else
    for folder_name in stripped_bin_names:
        target = os.path.join(os.path.relpath("./"), folder_name)
        if not os.path.exists(target):
            os.mkdir(target)

    for name in stripped_bin_names:
        partition(name, stripped_bin_names)
