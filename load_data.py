import codecs

def load_CVAW(extended=False):
    lexicon_data = []
    filename = './resources/CVAW.txt'
    fr = codecs.open(filename, 'r', 'utf-8')
    for line in fr.readlines():
        line = line.strip().split(',')
        lexicon_data.append([line[0], float(line[1]), float(line[2])])

    if extended == True:
        extended_filename = './resources/neural_cand.txt'
        for line in codecs.open(extended_filename, 'r', 'utf-8').readlines():
            line = line.strip().split()
            lexicon_data.append([line[0], float(line[1]), float(line[2])])

    return lexicon_data

def load_NTUSD(filename):
    words = []
    with open(filename,'r', encoding='utf-8-sig') as f:
        for line in f:
            words.append(str(line[:-1]))
    return words

# print(load_NTUSD('./resources/ntusd-negative (zh-tw).txt'))