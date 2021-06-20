###
  # Yaappilakkanam 0.1
  # Copyright 2021 The Author Alagar Prabu
  #Licensed under GPL V3
 ###
 
import character
import sys

rule_1 = ["KKOOO", "KNOOO"]
rule_2 = ["KKOO", "KNOO"]
rule_3 = ["KKO", "KNO"]
rule_4 = ["KK", "KN"]
rule_5 = ["KOOO", "NOOO"]
rule_6 = ["KOO", "NOO"]
rule_7 = ["KO", "NO"]
rule_8 = ["K", "N"]

formula_formation = ""
splitted_formation = ""
initial_length = 0

def word_convert(word):
  
    converted_word = ""
    global formula_formation
    formula_formation =""
    get_letters = character.character(word)
    for get_letter in get_letters:
        letter_conversion = character.kuril(get_letter)
        if(letter_conversion != False):
            converted_word += letter_conversion
        else:
            print("Unknown tamil characters found")
            sys.exit()
    return formula_verify(converted_word)


def formula_verify(actual_text):

    global formula_formation
    global splitted_formation
    if len(actual_text) != 0:

        length_actual_word = len(actual_text)
        rule_word = actual_text

        if(length_actual_word >= 5):
            word_specific_length = rule_word[initial_length:5]
            if word_specific_length in rule_1:
                formula_formation += "NIRAI "
                cut_length = 5
                splitted_formation = actual_text[cut_length:]
                formula_verify(splitted_formation)
            else:
                word_specific_length = rule_word[initial_length:4]
                if word_specific_length in rule_2:
                    formula_formation += "NIRAI "
                    cut_length = 4
                    splitted_formation = actual_text[cut_length:]
                    formula_verify(splitted_formation)
                else:
                    word_specific_length = rule_word[initial_length:4]
                    if word_specific_length in rule_5:
                        formula_formation += "NER "
                        cut_length = 4
                        splitted_formation = actual_text[cut_length:]
                        formula_verify(splitted_formation)

                    else:
                        word_specific_length = rule_word[initial_length:3]
                        if word_specific_length in rule_3:
                            formula_formation += "NIRAI "
                            cut_length = 3
                            splitted_formation = actual_text[cut_length:]
                            formula_verify(splitted_formation)
                        else:
                            word_specific_length = rule_word[initial_length:3]
                            if word_specific_length in rule_6:
                                formula_formation += "NER "
                                cut_length = 3
                                splitted_formation = actual_text[cut_length:]
                                formula_verify(splitted_formation)

                            else:
                                word_specific_length = rule_word[initial_length:2]
                                if word_specific_length in rule_4:
                                    formula_formation += "NIRAI "
                                    cut_length = 2
                                    splitted_formation = actual_text[cut_length:]
                                    formula_verify(splitted_formation)
                                else:
                                    word_specific_length = rule_word[initial_length:2]
                                    if word_specific_length in rule_7:
                                        formula_formation += "NER "
                                        cut_length = 2
                                        splitted_formation = actual_text[cut_length:]
                                        formula_verify(splitted_formation)
                                    else:
                                        word_specific_length = rule_word[initial_length:1]
                                        if word_specific_length in rule_8:
                                            formula_formation += "NER "
                                            cut_length = 1
                                            splitted_formation = actual_text[cut_length:]
                                            formula_verify(splitted_formation)
        elif(length_actual_word == 4):

            word_specific_length = rule_word[initial_length:4]
            if word_specific_length in rule_2:
                formula_formation += "NIRAI "
                cut_length = 4
                splitted_formation = actual_text[cut_length:]
                formula_verify(splitted_formation)
            else:
                word_specific_length = rule_word[initial_length:4]
                if word_specific_length in rule_5:
                    formula_formation += "NER "
                    cut_length = 4
                    splitted_formation = actual_text[cut_length:]
                    formula_verify(splitted_formation)

                else:
                    word_specific_length = rule_word[initial_length:3]
                    if word_specific_length in rule_3:
                        formula_formation += "NIRAI "
                        cut_length = 3
                        splitted_formation = actual_text[cut_length:]
                        formula_verify(splitted_formation)
                    else:
                        word_specific_length = rule_word[initial_length:3]
                        if word_specific_length in rule_6:
                            formula_formation += "NER "
                            cut_length = 3
                            splitted_formation = actual_text[cut_length:]
                            formula_verify(splitted_formation)

                        else:
                            word_specific_length = rule_word[initial_length:2]
                            if word_specific_length in rule_4:
                                formula_formation += "NIRAI "
                                cut_length = 2
                                splitted_formation = actual_text[cut_length:]
                                formula_verify(splitted_formation)
                            else:
                                word_specific_length = rule_word[initial_length:2]
                                if word_specific_length in rule_7:
                                    formula_formation += "NER "
                                    cut_length = 2
                                    splitted_formation = actual_text[cut_length:]
                                    formula_verify(splitted_formation)
                                else:
                                    word_specific_length = rule_word[initial_length:1]
                                    if word_specific_length in rule_8:
                                        formula_formation += "NER "
                                        cut_length = 1
                                        splitted_formation = actual_text[cut_length:]
                                        formula_verify(splitted_formation)
        elif(length_actual_word == 3):
            word_specific_length = rule_word[initial_length:3]
            if word_specific_length in rule_3:
                formula_formation += "NIRAI "
                cut_length = 3
                splitted_formation = actual_text[cut_length:]
                formula_verify(splitted_formation)
            else:
                word_specific_length = rule_word[initial_length:3]
                if word_specific_length in rule_6:
                    formula_formation += "NER "
                    cut_length = 3
                    splitted_formation = actual_text[cut_length:]
                    formula_verify(splitted_formation)

                else:
                    word_specific_length = rule_word[initial_length:2]
                    if word_specific_length in rule_4:
                        formula_formation += "NIRAI "
                        cut_length = 2
                        splitted_formation = actual_text[cut_length:]
                        formula_verify(splitted_formation)
                    else:
                        word_specific_length = rule_word[initial_length:2]
                        if word_specific_length in rule_7:
                            formula_formation += "NER "
                            cut_length = 2
                            splitted_formation = actual_text[cut_length:]
                            formula_verify(splitted_formation)
                        else:
                            word_specific_length = rule_word[initial_length:1]
                            if word_specific_length in rule_8:
                                formula_formation += "NER "
                                cut_length = 1
                                splitted_formation = actual_text[cut_length:]
                                formula_verify(splitted_formation)
        elif(length_actual_word == 2):
            word_specific_length = rule_word[initial_length:2]
            if word_specific_length in rule_4:
                formula_formation += "NIRAI "
                cut_length = 2
                splitted_formation = actual_text[cut_length:]
                formula_verify(splitted_formation)
            else:
                word_specific_length = rule_word[initial_length:2]
                if word_specific_length in rule_7:
                    formula_formation += "NER "
                    cut_length = 2
                    splitted_formation = actual_text[cut_length:]
                    formula_verify(splitted_formation)
                else:
                    word_specific_length = rule_word[initial_length:1]
                    if word_specific_length in rule_8:
                        formula_formation += "NER "
                        cut_length = 1
                        splitted_formation = actual_text[cut_length:]
                        formula_verify(splitted_formation)
        elif(length_actual_word == 1):
            word_specific_length = rule_word[initial_length:1]
            if word_specific_length in rule_8:
                formula_formation += "NER "
                cut_length = 1
                splitted_formation = actual_text[cut_length:]
                formula_verify(splitted_formation)
        return formula_formation
    else:
        return False


