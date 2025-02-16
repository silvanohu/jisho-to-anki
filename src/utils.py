def load_words(filename):
    """
    Reads a file containing words, each on a new line, and returns a list of these words.

    :param filename: Path to the file containing the words, one per line.
    :return: A list of words (strings) from the file.
    """
    with open(filename) as f:
        return f.read().splitlines()


def extract_info(jisho_data):
    """
    Extracts relevant Japanese word information from Jisho API response.

    :param jisho_data: Dictionary containing data from the Jisho.org API response.
                       Expected structure includes 'data' at the top level, with at least one
                       entry containing 'japanese' and 'senses'.
    :return: A formatted string containing the word, its reading, and its English definitions.
             If an error occurs (e.g., missing data), a message is printed, and no result is returned.
    """
    try:
        info = jisho_data['data'][0]['japanese'][0]['word']
        info += ';"Reading: '
        info += jisho_data['data'][0]['japanese'][0]['reading']

        i = 1
        for sense in jisho_data['data'][0]['senses'][0]['english_definitions']:
            info += '\n' + str(i) + '. ' + sense
            i = i + 1

        info += '"\n'

        return info
    except (IndexError, KeyError) as e:
        print("Error occurred extracting info")
        return ''
