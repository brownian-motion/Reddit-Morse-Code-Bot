import re

LATIN_TO_MORSE = {
        'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' ,

        ' ': '/',      '.': '.-.-.-', ',': '--..--',
        ':': '---...', '?': '..--..', "'": '.----.', '"': '.----.',
        '-': '-....-', '/': '-..-.',  '@': '.--.-.',
        '=': '-...-',  '(': '-.--.',  ')': '-.--.-',
        '+': '.-.-.'
 }

MORSE_TO_LATIN = {v: k for k,v in LATIN_TO_MORSE.iteritems()}

def _morse_match_to_latin(morse_match):
    morse_text = morse_match.group(0).strip();
    if(MORSE_TO_LATIN.has_key(morse_text)):
        return MORSE_TO_LATIN[morse_text]
    else:
        return morse_text;

def to_latin(text_with_morse):
    return re.sub(r'([.-]+|/)[ ]?', _morse_match_to_latin, text_with_morse);

def _latin_match_to_morse(latin_match):
    latin_char = latin_match.group(0).upper();
    if(LATIN_TO_MORSE.has_key(latin_char)):
        return LATIN_TO_MORSE[latin_char] + ' '
    else:
        return latin_char;

def to_morse(text_with_latin):
    return re.sub(r'[\w\d .,:?\'-/@=()+]{1}', _latin_match_to_morse, text_with_latin);
