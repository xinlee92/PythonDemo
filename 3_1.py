#This program is to calculate the values of circle,sphere and cylinder.
#It's periodic.
#If one of the inputs is 'done',the program ends.

#import the math function
import math

#input values
r=input('Please input r (r>0) or done:')
h=input('Please input h (h>0) or done:')

while r!='done' and h!='done':
    r=float(r)
    h=float(h)
    #get the result of circle , sphere and cylinder
    l_circle=2*math.pi*r
    s_circle=math.pi*r**2
    s_sphere=4*math.pi*r**2
    v_sphere=4/3*math.pi*r**3
    v_cylinder=s_circle*h

    #print the results
    print('The perimeter of the circle is '+str(l_circle))
    print('The area of the circle is '+str(s_circle))
    print('The area of the sphere is '+str(s_sphere))
    print('The volume of the sphere is '+str(v_sphere))
    print('The volume of the cylinder is '+str(v_cylinder))
    
    #input values
    r=input('Please input r (r>0) or done:')
    h=input('Please input h (h>0) or done:')
print('The program is over.')




