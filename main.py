from mamastop import MaMaStop

if __name__ == "__main__":
    tl = MaMaStop()
    result = tl.string_to_nouns(tl.img_to_string('80/3.jpg'))
    print(result)