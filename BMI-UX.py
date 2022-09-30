import random 
import string
#database
  
print("Please input name and weight and height")

# database_store

bmi_set_formal,bmi_set_heave,bmi_set_light = {} ,{}, {}    

#output_method

def show(a):    
    for k,v in a.items():
        print('The BMI of {} is {}'.format(k, v))

#test_database

for test in range(100):    
    
    n = ''.join(random.choice(string.ascii_letters) for x in range(10))
    
    #deal_with

    while True:
        try:
            #w = float(input("Please input the weight" +  "\033[1;32;1m(kg)\033[0m" ))
            
            w = random.uniform(10.0,500.0)
            if (w < 10 or w > 500):
                print("re-enter!!")
                continue
        except ValueError:
            print('Input should be a value, please re-input ')
            continue
        break

    while True:
        try:
            #h = float(input('Please input the height (cm) '))
            h = random.uniform(100.0,220.0)
            h = h / 100
            if (h < 1.0 or h > 2.2):
                print("re-enter!!")
                continue
        except ValueError:
            print('Input should be a value, please re-input ')
            continue
        break
    
    #judge = input("繼續請輸入1,終止請按0:")

    #if judge == "0":
        #break
    #else:
        #continue
    
    #count & store
    
    bmi = round(w/(h**2), 1)

    if bmi > 24:
        bmi_set_heave[n] = bmi
    elif bmi < 18:
        bmi_set_light[n] = bmi
    else:
        bmi_set_formal[n] = bmi
        

        


#  ouput
print ('-----------------------------------------------------------------------------------------------------------')
print("\033[1;32;1m正常數值有"+str(len(bmi_set_formal))+"個\033[0m")
print("\033[1;32;1m占總資料中 " + str(len(bmi_set_formal)) + "%\033[0m")
show(bmi_set_formal)
print("------------------------------------------------------------------------------------------------------------")
print("\033[1;32;1m過胖數值有"+str(len(bmi_set_heave))+"個\033[0m")
print("\033[1;32;1m占總資料中 " + str(len(bmi_set_heave)) + "%\033[0m")
show(bmi_set_heave)
print("------------------------------------------------------------------------------------------------------------")
print("\033[1;32;1m過輕數值有"+str(len(bmi_set_light))+"個\033[0m")
print("\033[1;32;1m占總資料中 " + str(len(bmi_set_light)) + "%\033[0m")
show(bmi_set_light)
