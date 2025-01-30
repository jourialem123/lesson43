def convtodect(lst):
    result={}
    for item in lst:
        result[item[0]]=item[1:]
    print(result)

students=[[1,"Ali",3],[2,"Bushra",2],[3,"Sama",1],[4,"Ahmed",2],[5,"Jouri",3]]    

print(convtodect(students))