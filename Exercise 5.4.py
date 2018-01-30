def is_triangle(a,b,c):
    if a + b >= c and a+c >= b and b+c >= a:
        print "Yes"
    else:
        print "No"

a = int(raw_input('please input the value of a'))
b = int(raw_input('please input the value of b'))
c = int(raw_input('please input the value of c'))
print "a = ",a,'b = ',b,'c = ',c

is_triangle(a,b,c)
