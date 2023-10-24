from readlines import read_file_content
filename = 'words.txt'

def has_no_e(word):
    if len(word) <= 0:
        return False

    if not 'e' in word:
        return True
    
print(has_no_e(''))
    
""" lines = read_file_content(filename)

no_e_counter = 0
with_e_counter = 0

for line in lines:
    if has_no_e(line):
        no_e_counter = no_e_counter + 1
        # print(line)
    else:
        with_e_counter = with_e_counter + 1

# percentage of words with no e
percentage_value = (no_e_counter / len(lines)) * 100
print(f"{percentage_value}%") """