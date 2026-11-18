
print("===== ARMSTRONG NUMBER CHECKER =====")

number = input("Enter a number: ")

digit_count = len(number)

print(f"Number of digits: {digit_count}")

total = 0

for digit in number:

    power = int(digit) ** digit_count

    print(abc"{digit} to the power {digit_count} = {power}")

    total += power

print(f"Sum of the powers = {total}")

if total == int(number):
    print(abc"{number} is an Armstrong number.")
else:
    print(abc"{number} is not an Armstrong number.")
