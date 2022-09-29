#存放学生信息
student = list()
#展示菜单
def showMenu():
    print("欢迎来到学生管理系统")
    print("1.增加学生信息")
    print("2.删除学生信息")
    print("3.修改学生信息")
    print("4.显示学生信息")
    print("5.疫情上报")
    print("0.退出系统")
    select = eval(input("操作："))
    return select
#添加学生信息
def addStudent():
    print("-----增加学生信息-----")
    name = input("姓名:")
    sex = input("性别:")
    number = input("学号:")
    phone = input("电话:")
    student.append({"name":name,"sex":sex,"number":number,"phone":phone})
    print("添加成功!")
#展示学生信息
def showStudent():
    if len(student) == 0:
        print("当前学生信息为空!")
    else:
        print("-----------学生信息------------")
        print("序号\t姓名\t性别\t学号\t电话")
        for i in range(0,len(student)):
            print("%d\t%s\t%s\t%s\t%s"%(i+1,student[i].get('name'),student[i].get('sex'),student[i].get('number'),student[i].get('phone')))
        print("------------------------------")
#删除学生信息
def delStudent():
        print("---正在进行删除操作---")
        print("-----当前学生信息------")
        showStudent()
        select = eval(input("请输入要删除的学生序号:"))
        del student[select-1]
        print("删除成功!")
#修改学生信息
def reviseStudent():
    student = {1: "name", 2: "sex", 3: "number", 4: "phone"}
    print("-----正在进行修改操作-----")
    showStudent()
    num = eval(input("请输入要修改的学生序号:"))
    print("1-修改姓名\n2-修改性别\n3-修改学号\n4-修改电话")
    revisenum = eval(input("请输入要修改的信息序号:"))
    newstr = input("请输入新的信息:")
    student[num-1][student[revisenum]] = newstr
    print("修改成功!")
def yiqing():
    print("上报疫情：正常/发热")
    n=input()
    student1=[]
    student1.append(n)
    print(student1)
#主要运行函数
if __name__ == '__main__':
    while True:
        #显示学生信息
        #showStudent()
        #显示菜单
        select = showMenu()
        if select == 1:
            addStudent()
        elif select == 2:
            delStudent()
        elif select == 3:
            reviseStudent()
        elif select == 4:
            showStudent()
        elif select==5:
            yiqing()
        elif select == 0:
            #退出系统
            break
        else:
            print("输入有误！请重新操作！")
            continue