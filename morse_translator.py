ko_morse = {'ㄱ' :'.-..', 'ㄴ': '..-.', 'ㄷ': '-...',
            'ㄹ':'...-' , 'ㅁ': '--', 'ㅂ':'.--',
            'ㅅ':'--.', 'ㅇ' :' -.-', 'ㅈ':'.--.',
            'ㅊ':'-.-.','ㅋ':'-..-','ㅌ':'--..',
            'ㅍ':'---','ㅎ':'.---', 'ㅏ':'.',
            'ㅑ':'..', 'ㅓ':'-','ㅕ':'...',
            'ㅗ': '.-', 'ㅛ':'-.','ㅜ':'....',
            'ㅠ':'.-.', 'ㅡ':'-..','ㅣ':'..-',
            '1':'.----', '2':'..---', '3':'...--',
            '4':'....-', '5':'.....', '6':'-....',
            '7':'--...', '8':'---..', '9':'----.',
            '0':'-----', ', ':'--..--', '.':'.-.-.-',
            '?':'..--..', '/':'-..-.', '-':'-....-',
            '(':'-.--.', ')':'-.--.-'}

en_morse = {'A':'.-', 'B':'-...',
            'C':'-.-.', 'D':'-..', 'E':'.',
            'F':'..-.', 'G':'--.', 'H':'....',
            'I':'..', 'J':'.---', 'K':'-.-',
            'L':'.-..', 'M':'--', 'N':'-.',
            'O':'---', 'P':'.--.', 'Q':'--.-',
            'R':'.-.', 'S':'...', 'T':'-',
            'U':'..-', 'V':'...-', 'W':'.--',
            'X':'-..-', 'Y':'-.--', 'Z':'--..',
            '1':'.----', '2':'..---', '3':'...--',
            '4':'....-', '5':'.....', '6':'-....',
            '7':'--...', '8':'---..', '9':'----.',
            '0':'-----', ', ':'--..--', '.':'.-.-.-',
            '?':'..--..', '/':'-..-.', '-':'-....-',
            '(':'-.--.', ')':'-.--.-'}

def text_to_morse(text):
    morse_code = ''
    for letter in text.upper():
        if letter != ' ':
            morse_code += en_morse[letter] + ' '
        else:
            morse_code += ' '# 단어 사이의 공백
    return morse_code


def morse_to_text(morse_code):
    morse_code += ' '
    deciper = ''
    citext = ''
    for letter in morse_code:
        if(letter != ' '):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2 :
                deciper += ' '
            else:
                deciper += list(en_morse.keys())[list(en_morse.values()).index(citext)]
                citext = ''
    return deciper

#초성 중성 종성 구분 함수
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
JONGSUNG_LIST = [''] + ['ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

def split_hangul(syllable):
    UNICODE_BASE = 0xAC00
    CHOSUNG_BASE = len(JUNGSUNG_LIST)*len(JONGSUNG_LIST)
    JUNGSUN_BASE = len(JONGSUNG_LIST)

    #한글 음절을 유니코드로 변환하여 인덱스 계산
    code = ord(syllable)-UNICODE_BASE
    chosung_index = code // CHOSUNG_BASE
    junsung_index = (code % CHOSUNG_BASE) // JUNGSUN_BASE
    jonsung_index = (code % CHOSUNG_BASE) % JUNGSUN_BASE

    return CHOSUNG_LIST[chosung_index], JUNGSUNG_LIST[junsung_index], JONGSUNG_LIST[jonsung_index]

def decompose_hangul(text):
    result = []
    for syllable in text:
        if '가' <= syllable <='힣':#한글 음절인지 확인
            result.append(split_hangul(syllable))
        else:
            result.append((syllable,'',''))# 한글이 아니면 그대로 추가
    sep_result = ''
    for chosung, junsung,jonsung in result:
        sep_result += f"{chosung} {junsung} {jonsung} " 
    return sep_result


#한글 모르스 부호 컨버터
def text_to_morse_ko(text):
    morse_code = ''
    for letter in text:
        if letter != ' ':
            morse_code += ko_morse.get(letter, '') + ' '
        else:
            morse_code += ' ' # 단어사이의 공백
    return morse_code.strip()# 마지막 공백 제거

def main():
    choice = input("영어를 모르스 부호로 변환하려면 1번, 한글을 모르스 부호로 변환하려면 2번을 입력하세요: ")
    if choice == '1':
        text = input("변환할 영어 텍스트를 입력하세요: ")
        print("변환된 모르스 부호 입니다.")
        print(text_to_morse(text))
    elif choice == '2':
        text = input("변환할 한국어 텍스트를 입력하세요: ")
        print("변환된 모르스 부호 입니다. ")
        print(text_to_morse_ko(decompose_hangul(text)))
    else:
        print("잘못 입력하셨네요 ^^ 다시 시도해 주세요.")

if __name__=="__main__":
    main()


