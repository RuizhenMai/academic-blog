from calendar import monthrange 

def generate_palindrome_date(year):
    '''
    param:
        year (string)
    return:
        number of palindrome date of the century the year is in(int)
    '''
    century_start = year // 100 * 100 + 1 # 2001 is the start of 21st century
    century_end = century_start + 99
    count = 0

    for yyyy in range(century_start, century_end):
        for mm in range(1,13):
            num_days = monthrange(yyyy,mm)[1] # 28 days or 30 days etc 
            for dd in range(1,num_days+1):
                if dd < 10:
                    dd = "0" + str(dd)
                else:
                    dd = str(dd)
                
                date = str(mm) + dd + str(yyyy)

                # check if 7 digits palindrome
                if date == date[::-1]:
                    count+=1
                    
                # check if 8 digits palindrome
                if mm < 10:
                    date_prime = "0" + str(mm) + dd + str(yyyy)
                    if date_prime == date_prime[::-1]:
                        count += 1

    
    return count
                

print(generate_palindrome_date(2016)) # output 38