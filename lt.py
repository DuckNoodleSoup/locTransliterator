import sys

cyrillic_to_roman = {'А': 'A', # Cyrillic Upper Case to Roman Upper Case
                     'Б': 'B',
                     'В': 'V',
                     'Г': 'G',
                     'Д': 'D',
                     'Е': 'E',
                     'Ё': 'E',
                     'Ж': 'Zh',
                     'З': 'Z',
                     'И': 'I',
                     'І': 'I',
                     'Й': 'I',
                     'К': 'K',
                     'Л': 'L',
                     'М': 'M',
                     'Н': 'N',
                     'О': 'O',
                     'П': 'P',
                     'Р': 'R',
                     'С': 'S',
                     'Т': 'T',
                     'У': 'U',
                     'Ф': 'F',
                     'Х': 'Kh',
                     'Ц': 'Ts',
                     'Ч': 'Ch',
                     'Ш': 'Sh',
                     'Щ': 'Shch',
                     'Ъ': '"',
                     'Ы': 'Y',
                     'Ь': "'",
                     'Ѣ': 'IE',
                     'Э': 'E',
                     'Ю': 'IU',
                     'Я': 'IA',
                     'Ѳ': 'F',
                     'Ѵ': 'Y',
                     'а': 'a', # Cyrillic Lower Case to Roman Lower Case
                     'б': 'b',
                     'в': 'v',
                     'г': 'g',
                     'д': 'd',
                     'е': 'e',
                     'ё': 'e',
                     'ж': 'zh',
                     'з': 'z',
                     'и': 'i',
                     'і': 'i',
                     'й': 'i',
                     'к': 'k',
                     'л': 'l',
                     'м': 'm',
                     'н': 'n',
                     'о': 'o',
                     'п': 'p',
                     'р': 'r',
                     'с': 's',
                     'т': 't',
                     'у': 'u',
                     'ф': 'f',
                     'х': 'kh',
                     'ц': 'ts',
                     'ч': 'ch',
                     'ш': 'sh',
                     'щ': 'shch',
                     'ъ': '"',
                     'ы': 'y',
                     'ь': "'",
                     'ѣ': 'ie',
                     'э': 'e',
                     'ю': 'iu',
                     'я': 'ia',
                     'ѳ': 'f',
                     'ѵ': 'y'}

# Converts from Cyrillic to Roman
def convert(title):
    converted_title = ""
    for i, v in enumerate(title):
        try:
            c = cyrillic_to_roman[v]
        except KeyError:
            c = str(v)
        converted_title = converted_title + c
    # final conversion printed
    print(converted_title)


def main():
    args = sys.argv[1:]
    convert(args[0])

if __name__ == "__main__":
    main()
