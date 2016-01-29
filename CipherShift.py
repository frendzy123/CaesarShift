import FrequencyAnalysis

# Take user's input. Input expected to be encrypted message. Message has to be encrypted using Caesar shift.
message = raw_input('Enter the encrypted message: ')
message = message.lower()

# Create an array containing the message shifted by a cipher shift of 1 to 26
possibleDecryptList = []
for num in range(1,27):
    possibleDecrypt = ""
    for char in message:
        if char.isalpha():
            characterASCII = ord(char) - num
            if characterASCII < 97:
                characterASCII = 122 - (96 - characterASCII)
            possibleDecrypt += chr(characterASCII)
    possibleDecryptList.append(possibleDecrypt)

fa = FrequencyAnalysis.FrequencyAnalysis()
print fa.frequency_analysis(possibleDecryptList);

