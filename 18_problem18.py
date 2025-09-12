text = int(input("Enter the number: "))

if text == text[::-1]:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")