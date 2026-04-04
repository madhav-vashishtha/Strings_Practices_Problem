def decodeCiphertext(encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText

        n = len(encodedText)
        cols = n // rows
        res = []

        for c in range(cols):
            r, j = 0, c
            while r < rows and j < cols:
                res.append(encodedText[r * cols + j])
                r += 1
                j += 1

        return "".join(res).rstrip()

encodedText = "ch   ie   pr"
rows = 3

print(decodeCiphertext(encodedText, rows))

encodedText = "iveo    eed   l te   olc"
rows = 4

print(decodeCiphertext(encodedText, rows))

encodedText = "coding"
rows = 1

print(decodeCiphertext(encodedText, rows))



