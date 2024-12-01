first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']



first_result = [len(string) for string in first_strings if len(string) >= 5]
print(first_result)


second_result = [(f1, s2) for f1 in first_strings for s2 in second_strings if len(f1) == len(s2)]
print(second_result)

third_result = { string:len(string) for string in (first_strings +second_strings ) if not len(string) % 2}
print(third_result)