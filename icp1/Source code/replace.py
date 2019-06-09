user = input("enter a sentence which consists the word python atleast once")
if user.find('python'):
    print('success')
print(user.replace('python', 'pythons'))