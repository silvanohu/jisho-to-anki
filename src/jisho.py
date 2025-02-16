import requests


def search_word(word):
    """
    Searches the Jisho API for the given word.

    This function sends a GET request to the Jisho API with the provided word
    and retrieves a JSON response containing information about the word.

    :param word: A string representing the word to search for in the Jisho API.
    :return: A JSON object containing the search results from the Jisho API.
    """
    url = "https://jisho.org/api/v1/search/words?keyword=" + word
    response = requests.get(url)
    return response.json()
