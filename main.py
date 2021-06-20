###
  # Venba
  # Copyright 2021 The Author Alagar Prabu
 ###
import sys
import venba

text=[]
      
def file_input():
    print()
    
    file_path = input("Source file: ")
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
    file_input()
