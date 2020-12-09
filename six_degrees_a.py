with open('friends.txt','r') as f:
    unique_people=[]
    details_list=[]
    for line in f:
        line=line.rstrip('\n')
        column=line.split('\t')
        details_list.append(column)
        if not(column[0] in unique_people):
            unique_people.append(column[0])
        if not(column[1] in unique_people):
            unique_people.append(column[1])
my_dict={}
for person in unique_people:
    first_deg_friends=[]
    for details in details_list:
        if person==details[0]:
            first_deg_friends.append(details[1])
        if person==details[1]:
            first_deg_friends.append(details[0])
    my_dict[person]=first_deg_friends
orig_name=input("What's your name? ")
input_deg=int(input("Enter an integer between 1 and 6: "))
current_name=[orig_name]
full_return_list=[]
loopcount=1
while loopcount<=input_deg:
    for name in current_name:
        degree_friends=my_dict[name]
        for friends in degree_friends:
            full_return_list.append(friends)
        loopcount+=1
        current_name=degree_friends
strip_repeats=[]
for item in full_return_list:
    if not(item in strip_repeats):
        strip_repeats.append(item)
if orig_name in strip_repeats:
    strip_repeats.remove(orig_name)
   
print(sorted(strip_repeats))
