def main():

    time = input("What time is it? ").strip()
    hours = convert(time)

    if 7<= hours <=8:
        print("breakfast time")

    elif 12<= hours <=13:
        print("lunch time")

    elif 18<= hours <=19:
        print("dinner time")


def convert(time):

    time = time.split(":")

    minutes = float(time[1]) / 60

    return (float(time[0]) + minutes)


if __name__ == "__main__":
    main()
