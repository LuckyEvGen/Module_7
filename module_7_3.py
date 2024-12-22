class WordsFinder:
    def __init__(self, *args):
        self.file_names = []
        for arg in args:
            self.file_names.append(arg)

    def get_all_words(self):
        all_words = {}
        punkt = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as f:
                bad_str = (f.read()).lower()
                good_str = ''
                for char in bad_str:
                    if char not in punkt:
                        good_str += char
                    list_ = str.split(good_str)
            all_words[file_name] = list_
        return all_words

    def find(self, word):
        answer = {}
        res = self.get_all_words()
        for key, value in res.items():
            answer[key] = value.index(str(word).lower()) + 1
        return answer

    def count(self, word):
        answer = {}
        res = self.get_all_words()
        for key, value in res.items():
            counter_ = 0
            for elem in value:
                if elem == str(word).lower():
                    counter_ += 1
            answer[key] = counter_
        return answer


info = [
    "It's a text for task Найти везде,",
    "Используйте его для самопроверки.",
    "Успехов в решении задачи!",
    "text text text"
]

with open('test_file.txt', 'w', encoding='utf-8') as f:
    for line in info:
        f.write(line + '\n')

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))

