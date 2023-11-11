def main():
    sets = [
        [1, 3, 5, 7, 9, 11, 13, 15],
        [2, 3, 6, 7, 10, 11, 14, 15],
        [4, 5, 6, 7, 12, 13, 14, 15],
        [8, 9, 10, 11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
    ]
    
    birthdate = 0

    for i in range(5):
        print(f"Is your birthday in Set{i + 1}?\n")
        for j in range(5):
            print(" ".join(map(str, sets[j])))
        choice = input("Enter N for No and Y for Yes: ")
        if choice.upper() == 'Y':
            birthdate += sets[i][0]

    print(f"Your birthday is {birthdate}!")

if __name__ == "__main__":
    main()
