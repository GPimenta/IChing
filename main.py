# Generate hexagram using coins like demonstrated in wikipedia: Three-coin method

import random


# Generate hexagram through coin method.
# We toss 3 coins 6 times to generate 6 bits
# Number for each type of line: 6 (for an old yin line), 7 (young yang), 8 (young yin), or 9 (old yang),
# in other words:  6,8 = yin (0); 7,9 = yang (1)
def generate_hexagram():
    lines = []

    for _ in range(6):
        toss = sum(random.choice([2, 3]) for _ in range(3))

        if toss in (7, 9):
            lines.append(1)
        else:
            lines.append(0)

    return lines


# Convert the hexagram binary to integer
def hexagram_binary_to_int(lines):
    return int(''.join(str(bit) for bit in reversed(lines)), 2)


# Generate several hexagram accordingly the quantity bits indicated
def generate_number_via_hexagrams(bits_needed):
    total_bits = []

    while len(total_bits) < bits_needed:
        hexagram = generate_hexagram()
        total_bits.extend(hexagram)

    total_bits = total_bits[:bits_needed]

    return hexagram_binary_to_int(total_bits)


# lines_r = generate_hexagram()
# print("Hexagram lines:", lines_r)
# value = hexagram_binary_to_int(lines_r)
# print("Hexagram value:", value)


def main():
    start = int(input("Enter start of range (e.g., 0): "))
    end = int(input("Enter end of range (e.g., 2^160): "))
    count = int(input("How many numbers do you want to generate? "))

    bits_needed = (end - 1).bit_length()

    print(f"\nGenerating {count} random I Ching numbers in range [{start}, {end}]...\n")

    for _ in range(count):
        while True:
            number = generate_number_via_hexagrams(bits_needed)
            if start <= number <= end:
                print(number)
                break


if __name__ == '__main__':
    main()
