def palindrome(string):
	if len(string) <= 1:
		return True
	else:
		return string[0] == string[-1] and palindrome(string[1:-1])
        