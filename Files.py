#In Python, file handling is managed primarily through the built-in open() function, 
# which creates a file object to read, write, or modify data. The safest and most 
# efficient way to handle files is by using the with statement, which ensures the file 
# is automatically closed after the code executes, preventing resource leaks or data 
# corruption.
#1. Read the Entire File
with open("simple.txt", "r", encoding="utf-8") as file:
    con = file.read()
    print(con)
#2. For Large files.
with open("sample-2mb-text-file.txt", "r", encoding="utf-8") as file:
    for l in file:
        print(l.strip())
# 3. Read All Lines into a List  
with open("simple.txt", "r", encoding="utf-8") as file:
    ls = file.readlines()
    print(ls)
# 4. "w" mode completely erases its previous contents before 
# writing the new text 
with open("simple.txt", "w", encoding="utf-8") as file:
    file.write("My name is B.Gayathri Bhargavi.\n")
# "a" mode adds data at the bottom of the existing data.
with open("simple.txt", "a", encoding="utf-8") as file:
    file.write("Completed my graduation from G.Pulla Reddy Engineering College\n")
# 5. Writing Multiple Lines at Once
nl= ["YOG: 2026\n", "Branch: CSD\n", "CGPA: 8.63\n"]
with open("simple.txt", "w", encoding="utf-8") as file:
    file.writelines(nl)



