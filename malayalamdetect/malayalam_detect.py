from malayalamdetect import detect
def cleanup_malayalam_sentence(input_sentence):
    '''
    Uses minimal lading from langdetect library to provide a clean malayalam sentence.
    :param input_sentence:
    :return: malayalam words from the input sentence.
    '''
    return_string=[]
    for word in input_sentence.split():
        try:
            if(detect(word)=='ml'):
                return_string.append(word)
        except:
            continue
    return ' '.join(return_string).strip()