# x = int(input())

# def rev_input():
#     while x > 0:
#         x = x//2
#         print(x % 2, end=' ')
        
rev_input(x)
text = input()
# endchar = ('Done','done','d')

# if endchar in text:
#     exit()
    
# print(text)
# text_1 = input()
# endchar_1 = ('Done','done','d')

# if text_1 == endchar_1:
#     SystemExit
def reverse_text(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

while True:
    user_input = input("Enter a line of text (or 'Done' to exit): ")
    if user_input.lower() in ['done', 'd']:
        print("Exiting the program.")
        break
    else:
        reversed_text = reverse_text(user_input)
        print("Reversed text:", reversed_text)