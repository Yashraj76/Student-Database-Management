
def add_student(id,name,grade,m1,m2,m3,m4,m5):
    file=open(r'E:\\python\\project\\project_1\\student.txt','a')
    login=open(r'E:\\python\\project\\project_1\\login.txt','a')
    file.write(id+'\t'+name+'\t'+grade+'\t'+m1+'\t'+m2+'\t'+m3+'\t'+m4+'\t'+m5+'\n')
    login.write(id+'\t'+'student'+'\t'+'S'+'\n')
    file.close()
    login.close()
    
def add_teacher(id,name,sub,clas):
    file=open(r'E:\\python\\project\\project_1\\teacher.txt','a')
    login=open(r'E:\\python\\project\\project_1\\login.txt','a')
    file.write(id+'\t'+name+'\t'+sub+'\t'+clas+'\n')
    login.write(id+'\t'+'teacher'+'\t'+'T'+'\n')
    file.close()
    login.close()
    
def search_student(id):
    file=open(r'E:\\python\\project\\project_1\\student.txt','r')
    for data in file.readlines():
        lst=list(data.strip().split('\t'))
        if id==lst[0] or id==lst[1]:
            file.close()
            return lst
    file.close()
    
def search_teacher(id):
    file=open(r'E:\\python\\project\\project_1\\teacher.txt','r')
    for data in file.readlines():
        lst=list(data.strip().split('\t'))
        if id == lst[0] or id==lst[1]:
            file.close()
            return lst
    file.close()

def update_marks(id,m1='-1',m2='-1',m3='-1',m4='-1',m5='-1'):
    ch=''
    global u
    if m2=='-1' and m3=='-1' and m4=='-1' and m5=='-1':
         file=open(r'E:\\python\\project\\project_1\\teacher.txt','r')
         for j in file.readlines():
             l=list(j.strip().split('\t'))
             if u==l[0]:
                 ch=l[2]
                 break
         file.close()
    file_r=open(r'E:\\python\\project\\project_1\\student.txt',"r")
    lst=list(i.strip().split('\t')for i in file_r.readlines())			
    file_r.close()
    file_w=open(r'E:\\python\\project\\project_1\\student.txt',"w")
    for i in lst:
        if ch=='phy'and i[0]==id:
            file_w.write(i[0]+"\t"+i[1]+"\t"+i[2]+"\t"+m1+"\t"+i[4]+"\t"+i[5]+"\t"+i[6]+"\t"+i[7]+"\n")
        elif ch=='chem' and i[0]==id:
            file_w.write(i[0]+"\t"+i[1]+"\t"+i[2]+"\t"+i[3]+"\t"+m1+"\t"+i[5]+"\t"+i[6]+"\t"+i[7]+"\n")
        elif ch=='maths' and i[0]==id:
            file_w.write(i[0]+"\t"+i[1]+"\t"+i[2]+"\t"+i[3]+"\t"+i[4]+"\t"+m1+"\t"+i[6]+"\t"+i[7]+"\n")
        elif ch=='cs' and i[0]==id:
            file_w.write(i[0]+"\t"+i[1]+"\t"+i[2]+"\t"+i[3]+"\t"+i[4]+"\t"+i[5]+"\t"+m1+"\t"+i[7]+"\n")
        elif ch=='eng' and i[0]==id:
            file_w.write(i[0]+"\t"+i[1]+"\t"+i[2]+"\t"+i[3]+"\t"+i[4]+"\t"+i[5]+"\t"+i[6]+"\t"+m1+"\n")
        elif ch=='' and i[0]==id:
            file_w.write(i[0]+"\t"+i[1]+"\t"+i[2]+"\t"+m1+"\t"+m2+"\t"+m3+"\t"+m4+"\t"+m5+"\n")
        else:
            file_w.write(i[0]+"\t"+i[1]+"\t"+i[2]+"\t"+i[3]+"\t"+i[4]+"\t"+i[5]+"\t"+i[6]+"\t"+i[7]+"\n")
    file_w.close()

def update_teacher(id,sub,clas):
    file_r=open(r'E:\\python\\project\\project_1\\teacher.txt',"r")
    lst=list(i.strip().split('\t')for i in file_r.readlines())			
    file_r.close()
    file_w=open(r'E:\\python\\project\\project_1\\teacher.txt',"w")
    for i in lst:
        if(i[0]==id):
            file_w.write(i[0]+"\t"+i[1]+"\t"+sub+"\t"+clas+"\n")
        else:
           file_w.write(i[0]+"\t"+i[1]+"\t"+i[2]+"\t"+i[3]+"\n")
    file_w.close()

def delete_student(id):
    file_r=open(r'E:\\python\\project\\project_1\\student.txt',"r")
    log_r=open(r'E:\\python\\project\\project_1\\login.txt',"r")
    lst=list(i.strip().split('\t')for i in file_r.readlines())			
    log=list(i.strip().split('\t')for i in log_r.readlines())
    file_r.close()
    log_r.close()
    file_w=open(r'E:\\python\\project\\project_1\\student.txt',"w")
    log_w=open(r'E:\\python\\project\\project_1\\login.txt',"w")
    for i in lst:
        if(i[0]==id):
            pass
        else:
           file_w.write(i[0]+"\t"+i[1]+"\t"+i[2]+"\t"+i[3]+"\t"+i[4]+"\t"+i[5]+"\t"+i[6]+"\t"+i[7]+"\n")
    for j in log:
        if(j[0]==id):
            pass
        else:
           log_w.write(j[0]+"\t"+j[1]+"\t"+j[2]+"\n")       
    file_w.close()
    log_w.close()
    return 'ID deleted'

def delete_teacher(id):
    file_r=open(r'E:\\python\\project\\project_1\\teacher.txt',"r")
    log_r=open(r'E:\\python\\project\\project_1\\login.txt',"r")
    lst=list(i.strip().split('\t')for i in file_r.readlines())			
    log=list(i.strip().split('\t')for i in log_r.readlines())
    file_r.close()
    log_r.close()
    file_w=open(r'E:\\python\\project\\project_1\\teacher.txt',"w")
    log_w=open(r'E:\\python\\project\\project_1\\login.txt',"w")
    for i in lst:
        if(i[0]==id):
            pass
        else:
           file_w.write(i[0]+"\t"+i[1]+"\t"+i[2]+"\t"+i[3]+"\n")
    for j in log:
        if(j[0]==id):
            pass
        else:
           log_w.write(j[0]+"\t"+j[1]+"\t"+j[2]+"\n")       
    file_w.close()
    log_w.close()
    return 'ID deleted'

def password():
    user=input("Login ID:")
    password=input('Password :')
    global u
    u=user
    if user=='admin' and password=='admin':
        return 1
    login=open(r'E:\\python\\project\\project_1\\login.txt',"r")
    for i in login.readlines():
        lst=list(i.strip().split('\t'))			
        if lst[0]==user:
            if password==lst[1] and lst[2]=='T':
                    return 2
            elif password==lst[1] and lst[2]=='S':          
                    return 3
            else:
                return -1

def display_student():
    file=open(r'E:\\python\\project\\project_1\\student.txt','r')
    for data in file.readlines():
        lst=list(data.strip().split('\t'))
        print(lst)
    file.close()

def display_teacher():
    file=open(r'E:\\python\\project\\project_1\\teacher.txt','r')
    for data in file.readlines():
        lst=list(data.strip().split('\t'))
        print(lst)
    file.close()    

def change_password(id,o_pass):
    log_r=open(r'E:\\python\\project\\project_1\\login.txt',"r")
    lst=list(i.strip().split('\t')for i in log_r.readlines())			
    log_r.close()
    log_w=open(r'E:\\python\\project\\project_1\\login.txt',"w")
    for i in lst:
        if(i[0]==id and i[1]==o_pass):
            n_pass=input('New password :')
            a,ca,d,sp=0,0,0,0
            for k in n_pass:
                if k in 'abcdefghijklmnopqrstuvwxyz':
                    a+=1
                elif k in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    ca+=1
                elif k in '1234567890':
                    d+=1
                elif k in '!@#$&':
                    sp+=1
            if a>=1 and ca>=1 and d>=1 and sp>=1 and 5<len(n_pass)<13:
                 i[1]=n_pass
                 print('password changed')
            else:
                 print('At least 1 letter between [a-z]\nAt least 1 number between [0-9]\nAt least 1 letter between [A-Z]\nAt least 1 special character from [!@#$%&]\nMinimum length of password: 6\nMaximum length of password: 12')
            log_w.write(i[0]+'\t'+i[1]+'\t'+i[2]+'\n')
        else:
            log_w.write(i[0]+'\t'+i[1]+'\t'+i[2]+'\n')
    log_w.close()
        
while True:
    print('WELCOME TO STUDENT MANAGEMENT SYSTEM')          
    ch=password()
    if ch==1 :
        print('\nMenu\n1.Add student\n2.Add teacher\n3.search student\n4.search teacher\n5.update marks\n6.update teacher\n7.delete student\n8.delete teacher\n9.display student\n10.display teacher\n11.log out')
        while(True):
            ch=input('\nEnter your choice :')
            if ch=='1':
                id=input('Enter student ID :')
                name=input('Enter student name :')
                grade=input('Enter grade :')
                m1,m2,m3,m4,m5=input('Enter marks in 5 subject(phy,chem,maths,cs,eng) :').split()
                add_student(id,name,grade,m1,m2,m3,m4,m5)
            elif ch=='2':
                id=input('Enter teacher ID :')
                name=input('Enter teacher name :')
                sub=input('subject teaching :')
                clas=input('classes teaching :')
                add_teacher(id,name,sub,clas)
            elif ch=='3':
                id=input('Enter student ID or name :')
                info=search_student(id)
                if info!=None:
                    print('ID :{}\nName :{}\nGrade :{}\nMarks :{} {} {} {} {}'.format(info[0],info[1],info[2],info[3],info[4],info[5],info[6],info[7]))
                else:
                    print('ID not found')
            elif ch=='4':
                id=input('Enter teacher ID or name :')
                info=search_teacher(id)
                if info!=None:
                    print('ID :{}\nName :{}\nSubject teaching :{}\nClasses taking  :{}'.format(info[0],info[1],info[2],info[3]))
                else:
                    print('ID not found')
            elif ch=='5':
                id=input('Enter student ID or name :')
                m1,m2,m3,m4,m5=input('Enter marks in 5 subject(phy,chem,maths,cs,eng) :').split()
                update_marks(id,m1,m2,m3,m4,m5)
            elif ch=='6':
                id=input('Enter teacher ID :')
                sub=input('Subject teaching :')
                clas=input('class taking :')
                update_teacher(id,sub,clas)
            elif ch=='7':
                id=input('Enter student ID :')
                info=delete_student(id)
                if info!=None:
                    print(info)
                else:
                    print('ID not found')
            elif ch=='8':
                id=input('Enter teacher ID :')
                info=delete_teacher(id)
                if info!=None:
                    print(info)
                else:
                    print('ID not found')
            elif ch=='9':        
                print('student list :')
                display_student()
            elif ch=='10':
                print('Teacher list :')
                display_teacher()
            elif ch=='11':
                break
            else:
                print('INVALID')
    elif ch==2:
        print('\nMenu\n1.search student\n2.teacher delail\n3.update marks\n4.display student\n5.change password\n6.log out')
        while(True):
            ch=input('\nEnter your choice :')
            if ch=='1':
                id=input('Enter student ID or name :')
                info=search_student(id)
                if info!=None:
                    print('ID :{}\nName :{}\nGrade :{}\nMarks :{} {} {} {} {}'.format(info[0],info[1],info[2],info[3],info[4],info[5],info[6],info[7]))
                else:
                    print('ID not found')
            elif ch=='2':
                info=search_teacher(u)
                if info!=None:
                    print('ID :{}\nName :{}\nSubject teaching :{}\nClasses taking  :{}'.format(info[0],info[1],info[2],info[3]))
                else:
                    print('ID not found')
            elif ch=='3':
                id=input('Enter student ID or name :')
                m1=input('Enter mark :')
                update_marks(id,m1)
            elif ch=='4':
                print('student list :')
                display_student()
            elif ch=='5':
                o_pass=input('Enter old password :')
                change_password(u,o_pass)
            elif ch=='6':
                break
            else:
                print('INVALID')
    elif ch==3:           
        print('\nMenu\n1.student delail\n2.change password\n3.log out')
        while(True):
            ch=input('\nEnter your choice :')
            if ch=='1':
                info=search_student(u)
                if info!=None:
                    print('ID :{}\nName :{}\nGrade :{}\nMarks :{} {} {} {} {}'.format(info[0],info[1],info[2],info[3],info[4],info[5],info[6],info[7]))
                else:
                    print('ID not found')
            elif ch=='2':
                o_pass=input('Enter old password :')
                change_password(u,o_pass)
            elif ch=='3':
                break
            else:
                print('INVALID')
    else:
        print('INVALID ID OR PASSWORD')
    n=input('back to login page(y/n) :')
    print('------------------------------')
    if n=='Y' or n=='y':
        continue
    else:
        break
    
                
        
        
