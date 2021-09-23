def  computepay(h,r):
    if h>40:
        pay1 = h*r
        pay2=(h-40)*(r*0.5)
        pay=pay1+pay2
        return pay
    else:
        pay = h*r
        return pay

hrs = input('Add hours:')
rat = input ('Add rate:')

a = float(hrs)
b = float(rat)

fin =  computepay(a,b)

print('Pay', fin)
