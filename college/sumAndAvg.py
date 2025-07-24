
total = 0
count = 0

# Keep accepting numbers until the user enters Zero
while True:
    num = float(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num
    count += 1

# Calculate and print the sum and average
if count == 0:
    print("No numbers entered.")
else:
    print("Sum:", total)
    print("Average:", total / count)
