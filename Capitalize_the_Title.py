def capitalizeTitle(title):
    words = title.split()
    result = []

    for word in words:
        if len(word) <= 2:
            result.append(word.lower())
        else:
            result.append(word.capitalize())

    return " ".join(result)

title = "capiTalIze tHe titLe"
print(capitalizeTitle(title))

title = "First leTTeR of EACH Word"
print(capitalizeTitle(title))

title = "i lOve leetcode"
print(capitalizeTitle(title))
