"""
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'                                                                 '
'CWRU Data Analytics                                  Robert Wood '
'                                                                 '
'                                                                 '
'Unit 3 | Assignment (Extra Content) - Pyparagraph       3/2/2019 '
'                                                                 '
'                                                                 '
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"""

# This will allow us to create file paths across operating systems
import os

# Import Regular Expressions library
import re

# Initialize variables
paragraph = ""
sentences = []
sentenceLength = []
words = []
i = 0
letters = 0
paragraphNum = 0

# Allow the user to select which paragraph to analyze (1 or 2)
while paragraphNum != 1 and paragraphNum != 2:
    paragraphNum = int(input("Paragraph 1 or Paragraph 2? (enter 1 or 2) "))

# Determine file name based on user input
importName = "paragraph_" + str(paragraphNum) + ".txt"

# Define path of our text file
importPath = os.path.join('raw_data', importName)

# Open text file
importFile = open(importPath, "r")

# Read file, saving the text in variable 'paragraph'
f1 = importFile.readlines()
for line in f1:
    paragraph = paragraph + " " + line.strip("\n\r")

# Close text file
importFile.close()

# Split text into sentences
sentences = re.split("(?<=[.!?]) +", paragraph)

# Loop through sentences, breaking each sentence into individual words
while i < len(sentences):
    j = 0
    words = [x.strip() for x in sentences[i].split(' ')]
    while j < len(words):
        letters += int(len(words[j]))
        j += 1
    sentenceLength.append(len(words))
    i += 1

#--------------------------------------------------------

# Print Results to terminal
print("Paragraph Analysis")
print("-----------------")
print(f"Approximate Word Count: {sum(sentenceLength)}")
print(f"Approximate Sentence Count: {len(sentences)}")
print(f"Average Letter Count: {round(letters / sum(sentenceLength),1)}")
print(f"Average Sentence Length: {sum(sentenceLength) / len(sentenceLength)}")

#--------------------------------------------------------

# Determine output file name (paragraph 1 or 2)
exportName = "results_" + str(paragraphNum) + ".txt"

# Create results .txt file
exportFile = open(exportName, "w+")

# Write results to text file
exportFile.write("Paragraph Analysis\n")
exportFile.write("-----------------\n")
exportFile.write(f"Approximate Word Count: {sum(sentenceLength)}\n")
exportFile.write(f"Approximate Sentence Count: {len(sentences)}\n")
exportFile.write(f"Average Letter Count: {round(letters / sum(sentenceLength),1)}\n")
exportFile.write(f"Average Sentence Length: {sum(sentenceLength) / len(sentenceLength)}")

# Close .txt file
exportFile.close()