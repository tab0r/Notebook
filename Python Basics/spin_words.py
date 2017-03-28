def spin_words(sentence):
    if sentence:
        s_list = list(sentence)
        print s_list
        s_list.reverse()
        r_string = ''
        for char in s_list:
            r_string = r_string + char
        print s_list
        return r_string
    else:
        pass

print spin_words('Welcome')
