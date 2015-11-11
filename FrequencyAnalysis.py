
class FrequencyAnalysis:

    def __init__(self):
        self.frequency_dictionary = {
            'a': 8.167,
            'b': 1.492,
            'c': 2.782,
            'd': 4.253,
            'e': 12.702,
            'f': 2.228,
            'g': 2.015,
            'h': 6.094,
            'i': 6.966,
            'j': 0.153,
            'k': 0.772,
            'l': 4.025,
            'm': 2.406,
            'n': 6.749,
            'o': 7.507,
            'p': 1.929,
            'q': 0.095,
            'r': 5.987,
            's': 6.327,
            't': 9.056,
            'u': 2.758,
            'v': 0.978,
            'w': 2.361,
            'x': 0.150,
            'y': 1.974,
            'z': 0.074,
        }

    # Returns a dictionary containing the frequency of letters in a string
    def frequency_generate(self,message):
        frequency_table = {}
        str = message.lower()
        for char in str:
            if char in frequency_table:
                frequency_table[char] += 1.0
            elif char in self.frequency_dictionary:
                frequency_table[char] = 1.0
        for key in frequency_table:
            frequency_table[key] = (frequency_table[key]/len(str))*100

        for key in self.frequency_dictionary:
            if key not in frequency_table:
                frequency_table[key] = 0.0

        return frequency_table

    # Returns a possible decrypted message
    def frequency_analysis(self, decrypted_list):
        dictionary = {}
        for string in decrypted_list:
            frequency_table = self.frequency_generate(string)
            for key in frequency_table:
                if key in self.frequency_dictionary:
                    difference = abs(frequency_table[key] - self.frequency_dictionary[key])
                    if key in dictionary:
                        if difference < dictionary[key][2]:
                            dictionary[key] = [string, frequency_table[key], difference]
                    else:
                        dictionary[key] = [string, frequency_table[key], difference]

        possible_decrypts = {}

        for value in dictionary.values():
            if value[0] in possible_decrypts:
                possible_decrypts[value[0]] += 1
            else:
                possible_decrypts[value[0]] = 1

        maximum = 0
        decrypt = ""
        for key in possible_decrypts:
            if possible_decrypts[key] > maximum:
                decrypt = key
                maximum = possible_decrypts[key]

        return decrypt


























