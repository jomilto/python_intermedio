def palindrome(string):
    # assert not string.isnumeric(), "It shouldn't be a number"
    assert len(string) > 0 , "It shouldn't be and empty string"
    return string == string[::-1]

def run():
    print(palindrome(4))

if __name__ == '__main__':
    run()