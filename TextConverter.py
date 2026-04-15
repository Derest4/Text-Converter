print("Welcome to text converter")
print("For exit press 'ctrl+c' ")

while True:
    text = input("Print your text: ")
    print("\n Result: ")
    for char in text:
       code = ord(char)
       binary = bin(code)[2:]
       print(f"{char} >> {binary}")