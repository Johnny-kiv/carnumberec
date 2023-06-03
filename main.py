import easyocr
def text_rec(path):
    reader = easyocr.Reader(["en"])
    result = reader.readtext(path)
    return result
p = text_rec(path="img.jpg")
l=0
for i in p:

    print(i[1])
    l+=1

