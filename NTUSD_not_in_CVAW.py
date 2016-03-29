from load_data import load_CVAW
from load_data import load_NTUSD

def save_list(filename, list):
    with open(filename,'w',encoding='utf-8') as f:
        for l in list:
            if l != "":
                f.write(l+"\n")
lexicon_data = load_CVAW()
cvaw_words = [line[0] for line in lexicon_data]
print('The words in CVAW lexicons: %s' % str(cvaw_words))
NTUSD_positive_words = load_NTUSD('./resources/ntusd-positive (zh-tw).txt')
NTUSD_negative_words = load_NTUSD('./resources/ntusd-negative (zh-tw).txt')
print('NTUSD')
print("Positive: %s"%str(NTUSD_positive_words))
print("Negative: %s"%str(NTUSD_negative_words))
print('same words in ntusd_postive')
print(sorted(list(set(NTUSD_positive_words) & set(cvaw_words))))
print('same words in ntusd_negative')
print(sorted(list(set(NTUSD_negative_words) & set(cvaw_words))))
common_words = sorted(list((set(NTUSD_positive_words) & set(cvaw_words)) | (set(NTUSD_negative_words) & set(cvaw_words))))


ntusd_p = (sorted(list(set(NTUSD_positive_words) - set(cvaw_words))))
ntusd_n = (sorted(list(set(NTUSD_negative_words) - set(cvaw_words))))

not_in_CVAW = sorted(list((set(NTUSD_positive_words) - set(cvaw_words)) | (set(NTUSD_negative_words) - set(cvaw_words))))

save_list('./resources/common_words.txt', common_words)
save_list('./resources/different_words.txt', not_in_CVAW)
save_list('./resources/NTUSD_p.txt', ntusd_p)
save_list('./resources/NTUSD_n.txt', ntusd_n)