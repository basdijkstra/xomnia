class StringUtil:

    @staticmethod
    def string_length(string):
        return len(string)

    @staticmethod
    def count_occurrences(string, char):
        return string.count(char)

    @staticmethod
    def reverse_string(string):
        return string[::-1]

    @staticmethod
    def raise_error(string):
        raise ValueError('I will not accept ' + string + ' as a parameter')
