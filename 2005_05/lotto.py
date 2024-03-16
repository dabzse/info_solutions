# http://oktatas.hu/bin/content/dload/erettsegi/feladatok2005tavasz/emelt/e_info_fl.pdf

print("1. feladat")

# week52_numbers = [89, 24, 34, 11, 64]

week52_numbers = []
for i in range(5):
    input_nr = int(input(f"Adja meg [a|az] {i + 1}. nyerőszámot: "))
    week52_numbers.append(input_nr)
print(week52_numbers)


print("2. feladat")

week52_numbers.sort()
print(week52_numbers)


print("3. feladat")

# user_input = 16
user_input = int(input("Adjon meg egy egész számot 1-51 között: " ))


print("4. feladat")

selected_numbers = []
with open("lottosz.dat", "r") as f:
    for row in f:
        row = row.split()
        row = [int(i) for i in row]
        selected_numbers.append(row)
print(selected_numbers[user_input - 1])


print("5. feladat")

all_chosen_numbers = []
for ch_nr in selected_numbers:
    for nr in ch_nr:
        all_chosen_numbers.append(nr)

all_nr = True
for i in range(1, 91):
    if i not in selected_numbers:
        print("Van")
        all_nr = False
        break
if all_nr:
    print("Nincs")


print("6. feladat")

odd_nrs = [x for x in all_chosen_numbers if x % 2 == 1]
print(len(odd_nrs))


print("7. feladat")

selected_numbers.append(week52_numbers)
print_it = ""
for row in selected_numbers:
    row = [str(x) for x in row]
    row = " ".join(row)
    print_it += row + "\n"
print(print_it)
with open("lotto52.ki", "w") as f:
    f.writelines(print_it)


print("8. feladat")

all_chosen_numbers = []
with open("lotto52.ki") as f:
    for row in f:
        row = row.split()
        row = [int(x) for x in row]
        for nr in row:
            all_chosen_numbers.append(nr)

print_it = ""
for i in range(1, 91):
    print_it += str(all_chosen_numbers.count(i)) + " "
    if i % 15 == 0:
        print_it += "\n"
print(print_it)


print("9. feladat")

# prime_nrs = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
def prime(x, y):
    prime_list = []
    for i in range(2, 90):
        for j in range(2, int(i/2)+1):
            if i % j == 0:
                break
        else:
            prime_list.append(i)
    return prime_list
prime_nrs = prime(2, 90)

for nr in prime_nrs:
    if nr not in all_chosen_numbers:
        print(f"A {nr}, mint prímszám még nem volt kihúzva a 2003-as évben!")
