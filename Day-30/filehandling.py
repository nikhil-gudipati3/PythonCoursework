with open('demo.txt','r') as file:
    print(file.read())
    file.seek(0) #place the cursor at starting character
    print(file.readline())
    file.seek(0)
    print(file.readlines())


with open('demo.txt','w') as file:
    file.write('Hello World') #Overwrite the entire file.

with open('demos.txt','w') as file:
    file.write('It creates new file with name demos.txt')

with open('demo.txt','a') as file:
    file.write('\n File Operations')


with open('demo.txt','a+') as file: #append + read
    file.write('\nNew Line')
    file.seek(0)
    print(file.read())
