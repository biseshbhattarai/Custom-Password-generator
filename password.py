import random


def password(header):
    print('Given password :', header)
    headers = []
    numbers = [1, 3, 4, 5, 8, 9, 0]
    keywords  = ['@', '$', '!', '%', '^', '&', '*']
    rand_cha = random.sample(keywords, 2)
    # print(rand_cha)
    for i in header:
        headers.append(i)
    j = random.randint(0, 4)
    k = random.randint(4, 15)
    first = headers[0:j]
    second = headers[j:k]
    third = headers[k:]
    if first != [] and second != [] and third != [] :
        password = first  + rand_cha[0:1] +  second + rand_cha[1:] + third
        # print(password)
        l = random.randint(0, 3)
        m = random.randint(2, 6)
        final_first = password[0:l]
        final_second = password[l:m]
        final_third = password[m:]
        random_number = [j , k]
        final_password = final_first + random_number[:1] + final_second + random_number[1:] + final_third
        a = ''
        b = ''
        if final_password[j] and final_password[k] and final_password[m] != int:
            final_password[j] = final_password[j].upper()
            final_password[k] = final_password[k].upper()
            final_password[m] = final_password[m].upper()


        for i in password:
            a += i
        # print(a)
        for i in final_password:
            b += str(i)
        print('Password generated : ', b)
    else:
        pass
    

    

password("Iamapassword") # Give the initil plain password here.
# Converts something like this (Iamacoder) to ----> (I$1am5ac!oder)
# Hashes update are coming soon......