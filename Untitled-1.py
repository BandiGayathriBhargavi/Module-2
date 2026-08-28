with open("annual-enterprise-survey-2025-financial-year-provisional-size-bands.csv", "r", encoding="utf-8") as file:
    con = file.read()
    print(con)
#2. For Large files.
with open("annual-enterprise-survey-2025-financial-year-provisional-size-bands.csv", "r", encoding="utf-8") as file:
    for l in file:
        print(l.strip())
# 3. Read All Lines into a List  
with open("annual-enterprise-survey-2025-financial-year-provisional-size-bands.csv", "r", encoding="utf-8") as file:
    ls = file.readlines()
    print(ls)
# 4. "w" mode completely erases its previous contents before 
# writing the new text 
with open("annual-enterprise-survey-2025-financial-year-provisional-size-bands.csv", "w", encoding="utf-8") as file:
    file.write("My name is B.Gayathri Bhargavi.\n")
# "a" mode adds data at the bottom of the existing data.
with open("annual-enterprise-survey-2025-financial-year-provisional-size-bands.csv", "a", encoding="utf-8") as file:
    file.write("Completed my graduation from G.Pulla Reddy Engineering College\n")
# 5. Writing Multiple Lines at Once
nl= ["YOG: 2026\n", "Branch: CSD\n", "CGPA: 8.63\n"]
with open("annual-enterprise-survey-2025-financial-year-provisional-size-bands.csv", "w", encoding="utf-8") as file:
    file.writelines(nl)