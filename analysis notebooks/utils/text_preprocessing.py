import string
import re


PUNCTUATION = set(string.punctuation)
PUNCTUATION.add('...')
PUNCTUATION.add('„')
PUNCTUATION.add('“')


def separate_punctuation(sent) -> str:
    """Separates out punctuations from beginning and end of words.

    :param sent: string
    :param lowercase: boolean

    :return: string
    """

    tokenized = []
    for w in sent.split():
        if w == '':
            continue
        elif w in PUNCTUATION:
            tokenized.append(w)
        else:
            end_puncts = []
            if w[-3:] in PUNCTUATION:
                end_puncts.append(w[-3:])
                w = w[:-3]

            while len(w) > 0 and w[0] in PUNCTUATION:
                tokenized.append(w[0])
                w = w[1:]

            while len(w) > 0 and w[-1] in PUNCTUATION:
                end_idx = -1
                end_puncts.append(w[end_idx:])
                w = w[:end_idx]

            if len(w) > 0:
                hyp_idx = w.find('-')
                if hyp_idx > -1:
                    tokenized.append(w[:hyp_idx])
                    if (hyp_idx+1) < len(w):
                        tokenized.append(w[hyp_idx+1:])
                else:
                    tokenized.append(w)

            if len(end_puncts) > 0:
                end_puncts.reverse()
                tokenized = tokenized + list(end_puncts)

    return ' '.join(tokenized)


def separate_special_symbols_and_measure_units(s):
    s = re.sub('(\d)([m |mm |cm ])', r'\1 \2', s)
    s = re.sub(' *\$ *', ' $ ', s)
    s = re.sub(' *£ *', ' £ ', s)
    return s


def bring_to_long_form(s):
    s = re.sub(' won\'t ', ' will not ', s)
    s = re.sub('n\'t ', ' not ', s)
    s = re.sub('\'re ', ' are ', s)
    s = re.sub(' it\'s ', ' it is ', s)
    if s.startswith('it\'s '):
        s = re.sub('it\'s ', 'it is ', s)
    return s


def rmv_punkt(s):
    for char in PUNCTUATION:
        s = s.replace(char, '')
    return s


def preprocessing_func_for_yisi(snts):
    new_snts = []
    for snt in snts:
        s = re.sub('\n', '', snt)
        s = re.sub(' *\. *', ' . ', s)
        s = re.sub('(\d) \. (\d)', r'\1.\2', s)
        s = re.sub('(\d)([m |mm |cm ])', r'\1 \2', s)
        s = re.sub(' *\? *', ' ? ', s)
        s = re.sub(' *! *', ' ! ', s)
        s = re.sub(' *, ', ' , ', s)
        s = re.sub(' *- *', ' - ', s)
        s = re.sub(' *\$ *', ' $ ', s)
        s = re.sub(' *£ *', ' £ ', s)
        s = re.sub(' *\* *', ' * ', s)
        s = re.sub(' *\( *', ' ( ', s)
        s = re.sub(' *\) *', ' ) ', s)
        s = re.sub(' *: *', ' : ', s)
        s = re.sub(' \'', ' ', s)
        s = re.sub('"', '', s)
        s = re.sub('\'re ', ' \'re ', s)
        s = re.sub('\'s ', ' \'s ', s)
        s = re.sub('n \' t ', ' n\'t ', s)
        s = re.sub(' +', ' ', s)
        new_snts.append(s)
    return new_snts


def custom_preprocess(s, lowercase, additional_preproc, long_form, remove_punkt):
    if lowercase == True:
        s = s.lower()

    s = separate_punctuation(s)

    if additional_preproc:
        s = separate_special_symbols_and_measure_units(s)

    if long_form:
        s = bring_to_long_form(s)

    if remove_punkt:
        s = rmv_punkt(s)

    # remove redundant spaces which may emerge after punctuation removal
    s = re.sub(r'( )+', ' ', re.sub(r'(\. \.)+', '', s))

    return s
