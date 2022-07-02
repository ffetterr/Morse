# напишем функцию, с помощью которой уберём символы, которых нет в азбуке морзе и приведём к всё к нижнему регистру

def chistaya_str(morse): 
    
    result = [] # объявляем список, в котором будет результат с "чистой строкой"
    

    morse = str(morse).lower() # поступающую строку приводим к нижнему регистру для удоства.

    for element in morse: # проходим по списку, проверяем является ли элемент "недопустимым символом"

        if ord(element) >= 1072 and ord(element) <= 1103: # ord - метод, возвращающий числовой номер символа в кодировке unicode с помощью utf-8,
            result.append(element) # .append метод списков, добавляющий элемент 

    return result 
    

def Perevod(morse):
    # rus_to_morse - ассоциативный массив с алфавитом.
    rus_to_morse = {'а': '.-',
                    'б': '-...',
                    'в': '.--',
                    'г': '--.',
                    'д': '-..',
                    'е': '.',
                    'ж': '...-',
                    'з': '--..',
                    'и': '..',
                    'й': '.---',
                    'к': '-.-',
                    'л': '.-..',
                    'м': '--',
                    'н': '-.',
                    'о': '---',
                    'п': '.--.',
                    'р': '.-.',
                    'с': '...',
                    'т': '-',
                    'у': '..-',
                    'ф': '..-.',
                    'х': '....',
                    'ц': '-.-.',
                    'ч': '---.',
                    'ш': '----',
                    'щ': '--.-',
                    'ъ': '.--.-.',
                    'ы': '-.--',
                    'ь': '-..-',
                    'э': '..-..',
                    'ю': '..--',
                    'я': '.-.-'}
    morse = chistaya_str(morse) # преобразовываем в "чистую строку"
    result = []
 
    for element in morse:
        result.append(rus_to_morse[element]) # преобразуем каждую букву из слова в кодировку Морзе
 
    return result

# Далее нам остаётся лишь ввести слово, вызвать к нему функции и вывести результат.
print('Введите слово для перевода в азбуку Морзе :')
word = input()
morse = Perevod(word)
print('Данное слово в азбуке Морзе :', end = ' ')
# выводим слово переведённое в азбуку Морзе
for c in morse:
    print(c, end = '')
    
