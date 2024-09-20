#Variables
a = 500;
print("This is number:",a,"of type:",type(a));

b = 20.8;
print("This is number:",b,"of type:",type(b));

c = 'String of 2 escaped back-slashes:\\\\';
print(c);

d = 'Hello'
e = 'This is adding the word: {}'.format(d);
print(e);

#Datatypes

#Tuple
#a tuple is constant, i.e. you cannot add another element to it. A "constant" list
x = (1,2,3,4,5);
print(type(x),x);

#List
#Index starts at 0
y = [1,2,3,4,5];
print(type(y),y);
y.append(6);
print(type(y),y);
print("Index 5 element, check:",y[5]);

#Dictionary; Think associative array
f = {'one':1, 'two':2};
print(type(f),f);

#another way to declare dictionary; easier to recognize
g = dict(
        one = 1,
        two = 'two'
    );
print(type(g),g);

#Booleans
boolean = True;
a,b = 0,1;
if a == b:
    print(True);
else:
    print(False);

print(type(boolean),boolean);
    
