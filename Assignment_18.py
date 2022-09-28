
my_self={"name":'Soumik',"age":'17',"gender":'male'}
print(my_self)

person={"name":'Rohit',"country":'IND',"mobile no.":12364789}
print(person["name"])
print(person.get("mobile no."))

st_data={"name":"soumik","class":12,"marks_11":'89_persentage'}
print(*st_data.values())#list(st_data.values())

person={"name":'Mohit',"country":'USA',"mobile no.":987456321}
person["name"]="Rahul"#person.update({"name":'Rahul'})
print(person)

house={"color":'White',"Room":8,"playground":1}
for key in house:
    print(key)

person={'person':{"name":'Rohit',"gender":'male',"age":28,"mobile no.":12364789},'company':{"1st":'Google',"2nd(now)":"TATA"},'address':{"Country":"India","State":"Bengal","City":"BUrdwan"}}
print(person)

rohit={"name":'Rohit',"country":'IND',"mobile no.":12364789}
mohit={"name":'Mohit',"country":'USA',"mobile no.":987456321}
rahul={'name': 'Rahul', 'country': 'CANADA', 'mobile no.': 789456123}
class_12={'student1':rohit,'student2':mohit,"student3":rahul}
print(class_12)
print("Student 2 name ",class_12["student3"]["name"])    
print("Student 3 mobile_no ",class_12["student3"]["mobile no."])    


lst1=['rohit','soham','kali']
lst2=['Bengal','Bihar','Delhi']
d=dict(zip(lst1,lst2))
print(d)


rohit={"name":'Rohit',"gender":'male',"age":28,"mobile no.":12364789}
address={"Country":"India","State":"Bengal","City":"BUrdwan"}
person={'person':rohit,'address':address}
print(person)

sample_dict = {'C': 92,'Java': 66,'Python': 85}
print("the key of lowest value from the dictionary=",min(sample_dict))


