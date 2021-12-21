def get_keyword_repeated(keyword, text):

    keyword = keyword.upper()
    keyword_repeated = ""
    keyword_length = len(keyword)
    index = 0

    for i, letter in enumerate(text):
        if letter == " ":
            keyword_repeated += letter
        else:
            a = index % keyword_length
            keyword_repeated += keyword[a]
            index += 1
            if index > keyword_length - 1:
                index = 0

    return keyword_repeated
