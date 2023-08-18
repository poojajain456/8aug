#prg to identify all the unique words and element from list and insert all the duplicate elements in another list
mylist=[10,20,10,40,30,60,80,50,40]
uni_words=[]
duplicate_words=[]
for elements in mylist:
    if mylist.count(elements)>1:
        if elements not in duplicate_words:
            duplicate_words.append(elements)
    else:
        if elements not in uni_words:
            uni_words.append(elements)
print("unique words",uni_words)
print("duplicate words",duplicate_words)

#create a prg to get string element which have more than 2 vowels and append it into the vowel list
mylist=["pooja",'rakhi',"antima","sakshi","harshit","siddharth","khushii","dipika"]
vwl_list=[]
vowel="aeiou"
for words in mylist:
    count=0
    for letters in words:
        if letters.lower() in vowel:
            count+=1
    if count>2:
        vwl_list.append(words)
print("words with more than 2 voweels",vwl_list)


#create a tuple containg multiple element and if the element is the integer and also  multiple of 2 and 3 so will insert into the list othrwise append into another list
mytuple=(34,66,22,45,67)
new=[]
old=[]
for i in mytuple:
    if type(i)is int:
        if(i%2==0 and i%3==0):
            new.append(i)
        else:
            old.append(i)
print("new list",new)
print("old list",old)
