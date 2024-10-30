import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read().lower()
                    content = content.translate(str.maketrans('', '', string.punctuation + ' -'))
                    words = content.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл '{file_name}' не найден.")
            except Exception as e:
                print(f"Произошла ошибка при чтении файла '{file_name}': {e}")

        return all_words

    def find(self, word):
        results = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            word_lower = word.lower()
            if word_lower in words:
                results[file_name] = words.index(word_lower) + 1  # Позиция с 1

        return results

    def count(self, word):
        results = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            word_lower = word.lower()
            results[file_name] = words.count(word_lower)

        return results


# Пример использования
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # Позиция первого вхождения
print(finder2.count('teXT'))  # Количество вхождений