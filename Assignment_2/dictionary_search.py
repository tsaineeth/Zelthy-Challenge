import requests


class Dictionary:
    """

        A class used to extract the dictionary meaning of a word.

        Parameters
        ----------

        @:param: query - str
            A string whose meaning need to be displayed.

        Methods
        -------

        search_dictionary()
            Queries the word using the dictionary api.
            Extracts Part of speech, meaning of the word.

        """

    def __init__(self, query):
        self.query = query

    def search_dictionary(self):
        url = f'https://api.dictionaryapi.dev/api/v2/entries/en_US/{self.query}'
        request_url = requests.get(url)
        res = request_url.json()

        res = res[0]
        queried_for = res["word"]
        res = res['meanings']
        res = res[1]
        part_of_speech = res["partOfSpeech"]
        definition = res["definitions"][0]["definition"]

        print(f"{queried_for}. {part_of_speech}. {definition}.")


if __name__ == "__main__":
    word = input("Enter the Word: ")
    temp = Dictionary(word)
    temp.search_dictionary()
