"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""


text = ('')

stop_words = ('ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about',
              'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be',
              'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself',
              'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the',
              'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through',
              'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should',
              'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all',
              'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in',
              'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over',
              'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has',
              'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few',
              'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing',
              'it', 'how', 'further', 'was', 'here', 'than')

stop_symbols = ['!', '?', ';', ':', ')', '(', '@', '#', '$', '%', '^', '&', '*', '-', '/', '.', ',', '~', '@', '$', '%', '\n', '"', "'", '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


def calculate_frequences(text):
    frequencies = {}
    if text is None or len(str(text)) == 0:
        return frequencies
    else:
        if not isinstance(text, str):
            return frequencies
    text1 = text.lower()
    for symbol in text1:
        if symbol in stop_symbols:
            text1 = text1.replace(symbol, '  ')
        text2 = text1.split()
    for key in text2:
        if key in frequencies:
            value = frequencies[key]
            frequencies[key] = value + 1
        else:
            frequencies[key] = 1
    return frequencies


def filter_stop_words(frequencies, stop_words):
    if frequencies is None:
        return frequencies
    elif len(frequencies) == 0:
        return frequencies
    elif type(frequencies) is not dict:
        return frequencies
    else:
        if stop_words is None:
            return frequencies
        elif len(stop_words) == 0:
            return frequencies
        else:
            no_stop_words_frequencies = frequencies.copy()
            for stop_word in stop_words:
                if no_stop_words_frequencies.get(stop_word):
                    no_stop_words_frequencies.pop(stop_word)
            for key in no_stop_words_frequencies:
                if key in stop_words or isinstance(key, int):
                    no_stop_words_frequencies.pop(key)
                    return no_stop_words_frequencies
            return no_stop_words_frequencies


def get_top_n(no_stop_words_frequencies, top_n):
    if not isinstance(top_n, int):
        no_stop_words_frequencies = ()
        return no_stop_words_frequencies
    else:
        if top_n < 0:
            top_n = 0
        else:
            if top_n > len(no_stop_words_frequencies):
                top_n = len(no_stop_words_frequencies)
    sorted_frequencies = sorted(no_stop_words_frequencies, key=lambda x: int(no_stop_words_frequencies[x]), reverse=True)
    final_frequencies = tuple(sorted_frequencies[:top_n])
    return final_frequencies
