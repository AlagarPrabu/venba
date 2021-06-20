###
  # Yaappilakkanam 0.12
  # Copyright 2021 The Author Alagar Prabu
  #Licensed under GPL V3
 ###
import sys
import venba

text=[]
paa_type =""
def init():
    print("select your paa:")
    print()
    print("1) Venba     2) Aasiriyappa     3) Vanjappa     4)Kalippa")

    paa_selection = input()
    selection_verify(paa_selection)

def selection_verify(selected_paa):
    global paa_type
    if(selected_paa == "1"):
        print("Success: Venba selected")
        paa_type ="VE"
        file_input()
    elif(selected_paa == "2"):
        print("Feature Not Found")
    elif(selected_paa == "3"):
        print("Feature Not Found")
    elif(selected_paa == "4"):
        print("Feature Not Found")
    

        
def file_input():
    print()
    
    file_path = input("File Name: ")
    with open(file_path, encoding="utf8") as source_lines:
        for line in source_lines:
            text.append(line)
        proceed()
def proceed():
    check = input("Proceed to Check (Y/N): ")
    if((check == "Y")or (check == "y")):
        print("---------------------------------------------------------------")
        for line in text:
            print(line)
        print("---------------------------------------------------------------")
        venba.format(text)
    else:
        sys.exit()
    
    
if __name__ == "__main__":
    init()
