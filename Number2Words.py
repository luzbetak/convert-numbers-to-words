class Number2Words:

    # -------------------------------------------------------------------------#
    def unit(self, number):
        word = ''
        if number == "1":
            word = 'One'
        if number == "2":
            word = 'Two'
        if number == "3":
            word = 'Three'
        if number == "4":
            word = 'Four'
        if number == "5":
            word = 'Five'
        if number == "6":
            word = 'Six'
        if number == "7":
            word = 'Seven'
        if number == "8":
            word = 'Eight'
        if number == "9":
            word = 'Nine'
        word.strip()
        return word

    # -------------------------------------------------------------------------#
    def tens(self, number):
        word = ''
        if number[0] == '1':
            if number[1] == '0':
                word = 'Ten'
            if number[1] == '1':
                word = 'Eleven'
            if number[1] == '2':
                word = 'Twelve'
            if number[1] == '3':
                word = 'Thirteen'
            if number[1] == '4':
                word = 'Fourteen'
            if number[1] == '5':
                word = 'Fifteen'
            if number[1] == '6':
                word = 'Sixteen'
            if number[1] == '7':
                word = 'Seventeen'
            if number[1] == '8':
                word = 'Eighteen'
            if number[1] == '9':
                word = 'Nineteen'
        else:
            after = self.unit(number[1])
            if number[0] == '2':
                word = 'Twenty'
            if number[0] == '3':
                word = 'Thirty'
            if number[0] == '4':
                word = 'Fourty'
            if number[0] == '5':
                word = 'Fifty'
            if number[0] == '6':
                word = 'Sixty'
            if number[0] == '7':
                word = 'Seventy'
            if number[0] == '8':
                word = 'Eighty'
            if number[0] == '9':
                word = 'Ninety'
            word = word + " " + after
        word = word.strip()
        return word

    # -------------------------------------------------------------------------#
    def hundreds(self, number):
        word = ''
        after = self.tens(number[1:])
        if number[0] == "1":
            word = 'One'
        if number[0] == "2":
            word = 'Two'
        if number[0] == "3":
            word = 'Three'
        if number[0] == "4":
            word = 'Four'
        if number[0] == "5":
            word = 'Five'
        if number[0] == "6":
            word = 'Six'
        if number[0] == "7":
            word = 'Seven'
        if number[0] == "8":
            word = 'Eight'
        if number[0] == "9":
            word = 'Nine'
        if number[0] != '0':
            word = word + ' Hundred '
        word = word + after
        word.strip()
        return word
