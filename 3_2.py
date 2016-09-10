
#This program transforms the fahrenheit 
#degree the user input into centigrade degree
#It's periodic.
#If the input is 'done',the program ends.


F=input('Pleasse input fahrenheit degree or done: ')

while F!='done':
    F=float(F)

    #transform into centigrade degree
    c=5/9*(F-32)

    #print the results
    print('The centigrade degree is '+str(c))
    
    #input the fahrenheit degree
    F=input('Pleasse input fahrenheit degree or done: ')

print('The program is over.')

