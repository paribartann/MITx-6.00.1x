#Problem 1
number_of_vowels=0
for letters in str(s):
    if letters=='a' or letters=='e' or letters=='i' or letters=='o' or letters=='u':
        number_of_vowels+=1
        
print("Number of vowels: ",number_of_vowels)

#Problem 2

number_of_bob=0
for i in range(len(s)-2):
    if s[i]=='b' and s[i+1]=='o' and s[i+2]=='b':
        number_of_bob+=1
print('Number of times bob occurs is: ',number_of_bob)

#problem 3

