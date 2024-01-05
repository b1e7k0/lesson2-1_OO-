
while True:

    word = input('Введите слово(или "стоп" для завершения): ')
    word = word.lower()

    if word == 'стоп':
        print('досвидания!')
        break

    vowels = ['e', 'y', 'u', 'i', 'o', 'a', 'ё', 'у', 'ы', 'я', 'э', 'ю', 'и', 'а', 'е', "о"]
    consonants = ['q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', "р", 'v', 'b', 'n', 'm', 'й', 'ц', 'к', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ', 'ф', 'в', 'п', 'л', 'д', 'ж', 'ч', 'м', 'т', 'ь', 'б']

    vowel_count = sum(word.count(vowel) for vowel in vowels)
    consonant_count = sum(word.count(consonant) for consonant in consonants)

    print(f'Всего букв: {len(word)}\n'
        f'Гласных: {vowel_count}\n'
        f'Согласных: {consonant_count}\n'
        f'Согласные/гласные: {"%.2f" % ((vowel_count / len(word)) * 100)}% / {"%.2f" % ((consonant_count / len(word)) * 100)}%')
    