"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""


text = ('''
Hi! 
I am James. I am 24.
Nice to meet you, Buddy!
While i was is in China you have become very dull. I very like to meet new people:) Do you like me? Blah Blah Blah
''')

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

stop_symbols = ['!','?',';',':',')','(','@','#','$','%','^','&','*','-','/','.',',','1','2','3','4','5','6','7','8','9','0']


def calculate_frequences(text):
    global frequencies
    if len(text) == 0:
        print ('error.')
        frequencies = {}
        return frequencies
    else:
        if text is None:
            print ('text was not given.')
            frequencies = {}
            return frequencies
        else:
            if not isinstance(text, str):
                print ('error.')
                frequencies = {}
                return frequencies
            else:
                text1 = text.lower()
                text2 = str(text1)
                for symbol in stop_symbols:
                    if symbol in text2:
                        text2 = text2.replace(symbol, '')
                        text3 = text2.split()
                        frequencies = {}
                        for word in text3:
                            if word in frequencies:
                                frequencies[word] += 1
                            else:
                                frequencies[word] = 1
                return frequencies


def filter_stop_words(frequencies, stop_words):
    global no_stop_words_frequencies
    if frequencies is None:
        print ('error.')
        return {}
    elif len(frequencies) == 0:
        print ('error.')
        return {}
    elif type(frequencies) is not dict:
        print ('error.')
        return {}
    else:
        if stop_words is None:
            print ('error.')
            return {}
        elif len(stop_words) == 0:
            print('error.')
            return {}
        else:
            no_stop_words_frequencies = frequencies.copy()
            for stop_word in stop_words:
                if no_stop_words_frequencies.get(stop_word):
                    no_stop_words_frequencies.pop(stop_word)
            for key in no_stop_words_frequencies:
                if key in stop_words or isinstance (key, int):
                    no_stop_words_frequencies.pop(key)
                    return (no_stop_words_frequencies)
            return no_stop_words_frequencies


def get_top_n(no_stop_words_frequencies, top_n):
    if top_n == 0 or top_n < 0:
        print ('error!')
        return ()
    else:
        if no_stop_words_frequencies == {}:
            print ('error!')
            return ()
        else:
            list_frequencies = list(no_stop_words_frequencies.items())
            sorted_list_frequencies = sorted(list_frequencies, key=lambda value: value[1], reverse = True)
            print(sorted_list_frequencies)
            final_frequencies = tuple(sorted_list_frequencies[:top_n])
            print (final_frequencies)


calculate_frequences(text)
filter_stop_words(frequencies, stop_words)
get_top_n(no_stop_words_frequencies, top_n = 6)



