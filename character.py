###
  # Yaappilakkanam 0.12
  # Copyright 2021 The Author Alagar Prabu
  #Licensed under GPL V3
 ###
import sys

def character(word):
    processed_character = []
    splitted_character = ""
    tamil_vowels = ["அ", "இ", "உ", "எ", "ஒ","ஆ", "ஈ", "ஊ", "ஏ", "ஐ", "ஓ", "ஔ", "ஃ"]
    tamil_consonent = ["க", "ங", "ச", "ஞ", "ட", "ண", "த","ந", "ப", "ம", "ய", "ர", "ல", "வ", "ழ", "ள", "ற", "ன"]
    grandha_letters = ["ஜ", "ஷ", "ஸ", "ஹ", "க்ஷ"]
    for get_character in word:
        if get_character in tamil_vowels:
            processed_character.append(get_character)
        elif get_character in tamil_consonent:
            if(splitted_character == ""):
                splitted_character += get_character
            else:
                processed_character.append(splitted_character)
                splitted_character = ""
                splitted_character += get_character
        elif get_character in grandha_letters:
            print("Grandha letters not to be used in yappilakkanam")
            sys.exit()
        else:
            splitted_character += get_character
            processed_character.append(splitted_character)
            splitted_character = ""
    if(splitted_character != ""):
        processed_character.append(splitted_character)
        splitted_character = ""

    return (processed_character)


def kuril(letter):
    Kuril = ["அ", "இ", "உ", "எ", "ஒ", "க", "ங", "ச", "ஞ", "ட", "ண", "த", "ந", "ப", "ம", "ய", "ர", "ல", "வ", "ழ", "ள", "ற", "ன", "கி", "ஙி", "சி", "ஞி", "டி", "ணி", "தி", "நி", "பி", "மி", "யி", "ரி", "லி", "வி", "ழி", "ளி", "றி", "னி", "கு", "ஙு", "சு", "ஞு", "டு", "ணு", "து", "நு",
             "பு", "மு", "யு", "ரு", "லு", "வு", "ழு", "ளு", "று", "னு", "கெ", "ஙெ", "செ", "ஞெ", "டெ", "ணெ", "தெ", "நெ", "பெ", "மெ", "யெ", "ரெ", "லெ", "வெ", "ழெ", "ளெ", "றெ", "னெ", "கொ", "ஙொ", "சொ", "ஞொ", "டொ", "ணொ", "தொ", "நொ", "பொ", "மொ", "யொ", "ரொ", "லொ", "வொ", "ழொ", "ளொ", "றொ", "னொ"]
    if letter in Kuril:
        return "K"
    else:
        return nedil(letter)


def nedil(letter):
    Nedil = ["ஆ", "ஈ", "ஊ", "ஏ", "ஐ", "ஓ", "ஔ", "கா", "ஙா", "சா", "ஞா", "டா", "ணா", "தா", "நா", "பா", "மா", "யா", "ரா", "லா", "வா", "ழா", "ளா", "றா", "னா", "கீ", "ஙீ", "சீ", "ஞீ", "டீ", "ணீ", "தீ", "நீ", "பீ", "மீ", "யீ", "ரீ", "லீ", "வீ", "ழீ", "ளீ", "றீ", "னீ", "கூ", "ஙூ", "சூ", "ஞூ", "டூ", "ணூ", "தூ", "நூ", "பூ", "மூ", "யூ", "ரூ", "லூ", "வூ", "ழூ", "ளூ", "றூ", "னூ", "கே", "ஙே", "சே", "ஞே", "டே",
             "ணே", "தே", "நே", "பே", "மே", "யே", "ரே", "லே", "வே", "ழே", "ளே", "றே", "னே", "கை", "ஙை", "சை", "ஞை", "டை", "ணை", "தை", "நை", "பை", "மை", "யை", "ரை", "லை", "வை", "ழை", "ளை", "றை", "னை", "கோ", "ஙோ", "சோ", "ஞோ", "டோ", "ணோ", "தோ", "நோ", "போ", "மோ", "யோ", "ரோ", "லோ", "வோ", "ழோ", "ளோ", "றோ", "னோ", "கௌ", "ஙௌ", "சௌ", "ஞௌ", "டௌ", "ணௌ", "தௌ", "நௌ", "பௌ", "மௌ", "யௌ", "ரௌ", "லௌ", "வௌ", "ழௌ", "ளௌ", "றௌ", "னௌ"]
    if letter in Nedil:
        return "N"
    else:
        return otru(letter)


def otru(letter):
    Otru = ["க்", "ங்", "ச்", "ஞ்", "ட்", "ண்", "த்", "ந்", "ப்",
            "ம்", "ய்", "ர்", "ல்", "வ்", "ழ்", "ள்", "ற்", "ன்", "ஃ"]
    if letter in Otru:
        return "O"
    else:
        return False
