###
  # Yaappilakkanam 0.12
  # Copyright 2021 The Author Alagar Prabu
  #Licensed under GPL V3
 ###

import asai_process
import character
import re

thalai_formation = []
formatted_cheyyul =[]
line_count = ""

def format(source):
    global formatted_cheyyul
    formatted_cheyyul = source
    venba_format_checking() 
        

def venba_format_checking():
    line_count = 0
    for line in formatted_cheyyul:
            line_count += 1
    if((line_count >= 2) and (line_count <= 12)):
            line_counts()
    else:
       print("ERROR: Venba should have minimum 2 lines and maximum 12 lines")
       exit()


def line_counts():
    global line_count
    line_count = 0
    for line in formatted_cheyyul:
            line_count += 1
    line_format_check()


def line_format_check():
        current_line =0
        for lines in formatted_cheyyul:
            current_line += 1
            one_line = lines.replace('-', ' ')
            words_in_line = len(one_line.split())
            if(current_line != line_count):
                if(words_in_line != 4):
                    print("ERROR:Line " + str(current_line)+" should have 4 words")
                    exit()
            elif(current_line == line_count):
                if(words_in_line != 3):
                    print("ERROR:Line " + str(current_line)+" should have 3 words")
                    exit()
                else:
                    letter_conversion()


def letter_conversion():
        global thalai_formation
        last_line_detect = 0
        for line in formatted_cheyyul:
            thalai_formation = []
            last_line_detect += 1
            if(line_count == last_line_detect):
                for i in range(0, 3):
                    if(i == 2):
                        hyphen_detect = line.replace('-', ' ')
                        string_change = str(hyphen_detect.split()[i])
                        get_words = asai_process.word_convert(string_change)
                        if (get_words != False):
                            asai_result = venba_etru_asai_rule_check(get_words)
                            if(asai_result == True):
                                length_etru_asai = len(get_words.split())
                                if(length_etru_asai == 2):
                                    get_characters = character.character(
                                        string_change)
                                    last_letter = get_characters[-1]
                                    last_letter_verification = kutriyalugaram_verification(
                                        last_letter)
                                    if(last_letter_verification == True):

                                        thalai_formation.append(get_words)

                                    else:
                                        print("Should end with kutriyalugaram")
                                        exit()
                                else:
                                    thalai_formation.append(get_words)
                            else:
                                print("ERROR:Line "+str(last_line_detect) +
                                      " word "+str(i+1)+" not following venba asai rule")
                                exit()

                        elif (get_words == False):
                            print("ERROR:Line "+str(last_line_detect) +
                                  " word "+str(i+1)+" not following venba asai rule")
                            exit()
                    else:
                        hyphen_detect = line.replace('-', ' ')
                        string_change = str(hyphen_detect.split()[i])
                        get_words = asai_process.word_convert(string_change)
                        if (get_words != False):
                            asai_result = venba_asai_rule_check(get_words)
                            if(asai_result == True):
                                thalai_formation.append(get_words)
                            else:
                                print("ERROR:Line "+str(last_line_detect) +
                                      " word "+str(i+1)+" not following venba asai rule")
                                exit()

                        else:
                            print("ERROR:Line "+str(last_line_detect) +
                                  " word "+str(i+1)+" not following venba asai rule")
                            exit()
            else:
                for i in range(0, 4):
                    hyphen_detect = line.replace('-', ' ')
                    string_change = str(hyphen_detect.split()[i])
                    get_words = asai_process.word_convert(string_change)
                    if (get_words != False):
                        asai_result = venba_asai_rule_check(get_words)
                        if(asai_result == True):
                            thalai_formation.append(get_words)
                        else:
                            print("ERROR:Line "+str(last_line_detect) +
                                  " word "+str(i+1)+" not following venba asai rule")
                            exit()
                    else:
                        print("ERROR:Line "+str(last_line_detect) +
                              " word "+str(i+1)+" not following venba asai rule")
                        exit()
            thalai_verify(last_line_detect)


def sub_classification():
    if(line_count == 2):
        print("This is Kural Venba")
    elif(line_count == 3):
        thanichol_check()
    elif(line_count == 4):
        thanichol_check()
    elif(line_count > 4):
        print("This is Paktrodai Venba")


def thanichol_check():
        no_thanichol = 0
    
        current_line =0
        for lines in formatted_cheyyul:
            current_line += 1
            if re.search('-', lines):
                if(current_line == 2):
                    if(line_count == 4):
                        nerisai_vigarpa_check()
                    elif(line_count == 3):
                        sinthiyal_check()
                else:
                    if(line_count == 4):
                        innisai_vigarpa_check()
                    elif(line_count == 3):
                        sinthiyal_check()

            elif not re.search('-', lines):
                no_thanichol += 1
                if(no_thanichol == line_count):
                    if(line_count == 4):
                        innisai_vigarpa_check()
                    elif(line_count == 3):
                        print("This is Innisai Sinthiyal Venba")


def nerisai_vigarpa_check():
        nerisai_vigarpa = []
        for line in formatted_cheyyul:
            hyphen_detect = line.replace('-', ' ')
            string_change = str(hyphen_detect.split()[0])
            get_words = character.character(string_change)
            nerisai_vigarpa.append(get_words[1])
        if(nerisai_vigarpa[0] == nerisai_vigarpa[1] == nerisai_vigarpa[2] == nerisai_vigarpa[3]):

            print("This is Oru Vigarpa Nerisai Venba")
        elif((nerisai_vigarpa[0] == nerisai_vigarpa[1]) and (nerisai_vigarpa[2] == nerisai_vigarpa[3])):

            print("This is Iru Vigarpa Nerisai Venba")
        elif(((nerisai_vigarpa[0] == nerisai_vigarpa[1]) and (nerisai_vigarpa[2] != nerisai_vigarpa[3])) or ((nerisai_vigarpa[0] != nerisai_vigarpa[1]) and (nerisai_vigarpa[2] == nerisai_vigarpa[3]))):

            print("This is Innisai Venba")


def sinthiyal_check():
        nerisai_vigarpa = []

        for line in formatted_cheyyul:
            hyphen_detect = line.replace('-', ' ')
            string_change = str(hyphen_detect.split()[0])
            get_words = character.character(string_change)
            nerisai_vigarpa.append(get_words[1])
        if(nerisai_vigarpa[0] == nerisai_vigarpa[1] == nerisai_vigarpa[2]):

            print("This is Nerisai Sinthiyal Venba")
        elif((nerisai_vigarpa[0] == nerisai_vigarpa[1]) or (nerisai_vigarpa[1] == nerisai_vigarpa[2])):

            print("This is Nerisai Sinthiyal Venba")
        else:

            print("This is Innisai Sinthiyal Venba")


def innisai_vigarpa_check():
        innisai_vigarpa = []
        for line in formatted_cheyyul:
            hyphen_detect = line.replace('-', ' ')
            string_change = str(hyphen_detect.split()[0])
            get_words = character.character(string_change)
            innisai_vigarpa.append(get_words[1])
        if(innisai_vigarpa[0] == innisai_vigarpa[1] == innisai_vigarpa[2] == innisai_vigarpa[3]):

            print("This is Innisai Venba")
        elif((innisai_vigarpa[0] == innisai_vigarpa[1]) and (innisai_vigarpa[2] == innisai_vigarpa[3])):

            print("This is Innisai Venba")
        else:
            print("This is Venba")


def venba_asai_rule_check(verify_rule):
    asai_formula = ["NER NER ", "NER NIRAI ", "NIRAI NER ", "NIRAI NIRAI ",
                    "NER NER NER ", "NER NIRAI NER ", "NIRAI NER NER ", "NIRAI NIRAI NER "]
    if(verify_rule in asai_formula):
        return True
    else:
        return False


def venba_etru_asai_rule_check(verify_rule):
    asai_formula = ["NER ", "NIRAI ", "NER NER ", "NER NIRAI ", "NIRAI NER "]
    if(verify_rule in asai_formula):
        return True
    else:
        return False


def kutriyalugaram_verification(verify_rule):
    kutriyalugaram = ["கு", "சு", "டு", "து", "பு", "று"]
    if (verify_rule in kutriyalugaram):
        return True
    else:
        return False


def thalai_rule(letter):
    thalai_rule_1 = ["NER NER NER ", "NER NIRAI NER "]
    thalai_rule_2 = ["NIRAI NER NER ", "NIRAI NIRAI NER "]
    thalai_rule_3 = ["NER NER "]
    thalai_rule_4 = ["NIRAI NER "]
    thalai_rule_5 = ["NER NIRAI "]
    thalai_rule_6 = ["NIRAI NIRAI "]
    thalai_rule_7 = ["NER"]
    thalai_rule_8 = ["NIRAI"]

    if(letter in thalai_rule_1):
        return "NERKAAI"

    elif(letter in thalai_rule_2):
        return "NIRAIKAAI"

    elif(letter in thalai_rule_3):
        return "NERMAA"

    elif(letter in thalai_rule_4):
        return "NIRAIMAA"

    elif (letter in thalai_rule_5):
        return "NERVILAM"

    elif(letter in thalai_rule_6):
        return "NIRAIVILAM"

    elif (letter in thalai_rule_7):
        return "NER"

    elif((letter in thalai_rule_8)):
        return "NIRAI"


def thalai_verify(line_length):
    thalai_formations = ""
    thalai_count = 0

    for formation_word in thalai_formation:

        thalai_count += 1

        thalai_verify_result = thalai_rule(formation_word)
        if(thalai_formations == ""):
            thalai_formations = thalai_verify_result

        else:
            if (thalai_formations == "NERKAAI"):
                if ((thalai_verify_result == "NIRAIKAAI") or (thalai_verify_result == "NIRAIMAA") or (thalai_verify_result == "NIRAIVILAM") or (thalai_verify_result == "NIRAI")):
                    print("Line" + str(line_length) + " word" +
                          str(thalai_count) + " not following thalai rule")
                    exit()

                else:
                    thalai_formations = thalai_verify_result

            elif(thalai_formations == "NIRAIKAAI"):
                if ((thalai_verify_result == "NIRAIKAAI") or (thalai_verify_result == "NIRAIMAA") or (thalai_verify_result == "NIRAIVILAM") or (thalai_verify_result == "NIRAI")):
                    print("Line" + str(line_length) + " word" +
                          str(thalai_count) + " not following thalai rule")
                    exit()
                else:
                    thalai_formations = thalai_verify_result

            elif (thalai_formations == "NERMAA"):
                if ((thalai_verify_result == "NERKAAI") or (thalai_verify_result == "NERMAA") or (thalai_verify_result == "NERVILAM") or (thalai_verify_result == "NER")):
                    print("Line" + str(line_length) + " word" +
                          str(thalai_count) + " not following thalai rule")
                    exit()
                else:
                    thalai_formations = thalai_verify_result

            elif (thalai_formations == "NIRAIMAA"):
                if ((thalai_verify_result == "NERKAAI") or (thalai_verify_result == "NERMAA") or (thalai_verify_result == "NERVILAM") or (thalai_verify_result == "NER")):
                    print("Line" + str(line_length) + " word" +
                          str(thalai_count) + " not following thalai rule")
                    exit()
                else:
                    thalai_formations = thalai_verify_result

            elif (thalai_formations == "NERVILAM"):
                if ((thalai_verify_result == "NIRAIKAAI") or (thalai_verify_result == "NIRAIMAA") or (thalai_verify_result == "NIRAIVILAM") or (thalai_verify_result == "NIRAI")):
                    print("Line" + str(line_length) + " word" +
                          str(thalai_count) + " not following thalai rule")
                    exit()
                else:
                    thalai_formations = thalai_verify_result

            elif (thalai_formations == "NIRAIVILAM"):
                if ((thalai_verify_result == "NIRAIKAAI") or (thalai_verify_result == "NIRAIMAA") or (thalai_verify_result == "NIRAIVILAM") or (thalai_verify_result == "NIRAI")):
                    print("Line" + str(line_length) + " word" +
                          str(thalai_count) + " not following thalai rule")
                    exit()
                else:
                    thalai_formations = thalai_verify_result

    if(line_count == (line_length)):
        sub_classification()



