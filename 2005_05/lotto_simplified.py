# http://oktatas.hu/bin/content/dload/erettsegi/feladatok2005tavasz/emelt/e_info_fl.pdf

print("\n1. feladat\n")

# week52_numbers = [89, 24, 34, 11, 64]
week52_numbers = [int(input(f"Adja meg [a|az] {i + 1}. nyerőszámot: ")) for i in range(5)]
print(week52_numbers)


print("\n2. feladat\n")

week52_numbers.sort()
print(week52_numbers)


print("\n3. feladat\n")

# user_input = 16
user_input = int(input("Adjon meg egy egész számot 1-51 között: "))


print("\n4. feladat\n")

with open("lottosz.dat", "r") as f:
    selected_numbers = [list(map(int, line.split())) for line in f]

print(selected_numbers[user_input - 1])


print("\n5. feladat\n")

all_chosen_numbers = [number for sublist in selected_numbers for number in sublist]
if set(range(1, 91)).issubset(all_chosen_numbers):
    print("Nincs")
else:
    print("Van")


print("\n6. feladat\n")

odd_nrs = len([x for x in all_chosen_numbers if x % 2 == 1])
print(odd_nrs)


print("\n7. feladat\n")

selected_numbers.append(week52_numbers)
with open("lotto52.ki", "w") as f:
    for row in selected_numbers:
        f.write(' '.join(map(str, row)) + '\n')


print("\n8. feladat\n")

with open("lotto52.ki") as f:
    all_chosen_numbers = [int(number) for line in f for number in line.split()]

output = ''
for i in range(1, 91):
    output += str(all_chosen_numbers.count(i)) + " "
    if i % 15 == 0:
        output += "\n"
print(output)


print("\n9. feladat\n")

# prime_nrs = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
prime_nrs = [num for num in range(2, 90) if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]
for nr in prime_nrs:
    if nr not in all_chosen_numbers:
        print(f"{nr}, ez a prímszám még nem volt kihúzva a 2003-as évben!")
