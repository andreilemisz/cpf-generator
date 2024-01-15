########################################################################################
                        # This code generates an 11 digits CPF number #
import random # To generate randomly the 9 digits of the CPF number

generated_cpf = "" # The base 9 digits to calculate the other 2 at the end

multiplication_number = 10 # Part of the algorithm, used in a decreasing way, 10 or 11
next_digit = 0 # Added numbers and result from both operations

########################################################################################

# Creating the 9 digits sequence
for i in range(9):
    generated_cpf += str(random.randint(0, 9))

# Just to prevent a CPF number like 000.000.000-00
while generated_cpf[0] * len(generated_cpf) == generated_cpf:
    generated_cpf = ""
    for j in range(9):
        generated_cpf += str(random.randint(0, 9))

# Taking each digit, multiplying by a decrescing 10 and adding together
for digit_1 in generated_cpf:
    next_digit += (int(digit_1) * multiplication_number)
    multiplication_number -= 1

# Part of the algorithm
next_digit = (next_digit * 10) % 11
next_digit = 0 if next_digit >= 10 else next_digit

# The now 10 digits CPF
generated_cpf += str(next_digit)

# Second part of the process, creating the second last number
multiplication_number = 11
next_digit = 0
for digit_2 in generated_cpf:
    next_digit += int(digit_2) * multiplication_number
    multiplication_number -= 1

next_digit = (next_digit * 10) % 11
next_digit = 0 if next_digit >= 10 else next_digit

generated_cpf += str(next_digit)

# Formatting the number with dots and dash
generated_cpf = generated_cpf[:3] + "." + generated_cpf[3:6] + "." + \
    generated_cpf[6:9] + "-" + generated_cpf[9:]

print(f"Your generated CPF number is {generated_cpf}.")