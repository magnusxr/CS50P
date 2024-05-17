def main():

    faces = input("Enter your message: ")

    faces = convert(faces)

    print(faces)


def convert(str):

    str = str.replace(":)", "🙂").replace(":(", "🙁")

    return str


main()
