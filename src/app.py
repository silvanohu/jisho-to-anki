from dotenv import load_dotenv
import os
import jisho
import utils


load_dotenv()

file = os.getenv("INPUT_FILE")
output_file = os.getenv("OUTPUT_FILE")

words = utils.load_words(file)

output = ''
for word in words:
    res = jisho.search_word(word)
    info = utils.extract_info(res)
    if info != '':
        output += info
        print("Handled word: ", word, "\n")
    else:
        print("Error handling word: ", word, "\n")

with open(output_file, "w", encoding="utf-8") as f:
    f.write(output)

print(f"Output saved to {output_file}")
