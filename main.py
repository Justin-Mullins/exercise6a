'''

Exercise 6a

Take a text file, creating (and printing) a nonsensical sentence from the nth
word on each of the first 10 lines, where n is the line number.

'''

def read_nth_words(n):
    output = []
    word_count = 1
    line_count = 0
    with open('test.txt', 'r') as file:
        for line in file:
            if line_count == 10:
                break
            for word in line.split():
                if word_count == n:
                    word_count = 1
                    output.append(word)
                    break
                word_count += 1
            line_count += 1
    return ' '.join(output)

print(read_nth_words(3))
