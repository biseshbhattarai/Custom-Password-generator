import random




def password(header):
    print('Given password :', header)
    headers = []
    keywords  = ['@', '$', '!', '%', '^', '&', '*']
    rand_cha = random.sample(keywords, 2)
    for i in header:
        headers.append(i)
    j = random.randint(0, 4)
    k = random.randint(4, 15)
    first = headers[0:j]
    second = headers[j:k]
    third = headers[k:]
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
    try:
        final_password[j] = final_password[j].upper()
    except Exception:
        final_password[j+1] = final_password[j+1].upper()
    try:
        final_password[k] = final_password[k].upper()
    except Exception:
        final_password[k+1] = final_password[k+1].upper()
    try:
        final_password[m] = final_password[m].upper()
    except Exception:
        final_password[m+1] = final_password[m+1].upper()


      
        
    for i in password:
        a += i
    for i in final_password:
        b += str(i)
    print('Password generated : ', b)
   

password("Iamapassword") # Give the initil plain password here.
# Converts something like this (Iamacoder) to ----> (I$1am5ac!oder)
# Hashes update are coming soon......