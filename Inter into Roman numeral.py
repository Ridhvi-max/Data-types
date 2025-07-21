class RomanConverter:
    def __init__(self, number):
        self.number = number
    def convert(self):
        numbers = [1000, 500, 100, 50, 10, 5, 1]
        letters = ["M", "D", "C", "L", "X", "V", "I"]
        result = ""
        num = self.number
        for i in range(len(numbers)):
            value = numbers[i]
            letter = letters[i]
            while num >= value:
                result = result + letter
                num = num - value
        return result
user_input = int(input("Enter a number: "))
converter = RomanConverter(user_input)
roman = converter.convert()
print("Roman Numeral is:", roman)
