def binarify(num):
    if num<=0.0: return '0'

    number = []

    # while True:
    while num != 0:
        if num % 2 == 0:
            number.append(0)
            num = num // 2
        else:
            number.append(1)
            num = num // 2
    result = [str(i) for i in number]
    return ''.join(result[::-1])

print("Test to convert 29 to base 2")
binarify(num = 29)
print("Test to convert 357 to base 2")
binarify(num = 357)
print("Test to convert 69 to base 2")
print(binarify(69))

#############

def int_to_base(num, base):
    number = []
    if num<=0:  
        return '0'
    else:
        while num != 0:
            if num % base == 0:
                number.append(0)
                num = num // base
            else:
                number.append(num % base)
                num = num // base
    result = [str(i) for i in number]
    return ''.join(result[::-1])

print("Test to convert 357 to base 3")
int_to_base(357, 3)
print("Test to convert 69 to base 7")
int_to_base(69, 7)

#############

def base_to_int(string, base):
    if string=="0" or base <= 0 : return 0

    base_ori = int(base)
    base_exp = len(string) - 1
    result = 0
    numbers = list(string)
    for i in numbers:
        result += int(i) * (base_ori ** base_exp)
        base_exp -= 1
    return result

print("Test to convert 11101 from base 2 to base 10")
base_to_int("11101", 2)
print("Test to convert 111020 from base 3 to base 10")
base_to_int("111020", 3)

##########

def flexibase_add(str1, str2, base1, base2):
  return base_to_int(str1, base1) + base_to_int(str2, base2)

print("Add 11101 (base 2) to 111020 (base 3)")
flexibase_add("11101", "111020", 2, 3)

#######
def flexibase_multiply(str1, str2, base1, base2):
  return base_to_int(str1, base1) * base_to_int(str2, base2)

print("Multiply 11101 (base 2) to 111020 (base 3)")
flexibase_multiply("11101", "111020", 2, 3)

#######
def romanify(num):
  if num <= 0:
      return "Please provide a positive integer"
  else:
      result = []
      while num != 0:
         if num >= 1000:
              result.append("M")
              num -= 1000
         elif num >= 900:
              result.append("CM")
              num -= 900
         elif num >= 500:
              result.append("D")
              num -= 500
         elif num >= 400:
              result.append("CD")
              num -= 400
         elif num >= 100:
             result.append("C")
             num -= 100
         elif num >= 90:
             result.append("XC")
             num -= 90
         elif num >= 50:
             result.append("L")
             num -= 50
         elif num >= 40:
             result.append("XL")
             num -= 40
         elif num >= 10:
             result.append("X")
             num -= 10
         elif num == 9:
             result.append("IX")
             num -= 9
         elif num in (8, 7, 6, 5):
             result.append("V")
             num -= 5
         elif num == 4:
             result.append("IV")
             num -= 4
         elif num in (3, 2, 1):
             result.append("I")
             num -= 1
         else:
             break
  return ''.join(result)

print("Convert 1001 to Roman")
romanify(1001)
print("Convert 3549 to Roman")
romanify(3549)
print("Try to convert 0, it will return an error.")
romanify(0)
