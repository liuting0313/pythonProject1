

student1 = [ \
    {1: "jam", 'age': 17, 'socer': 99},
    {2: 'kol', 'age': 18, 'socer': 89},
    {3: 'avlir', 'age': 19, 'socer': 100}]


# 页面
def menu():
    print('-' * 30)
    print("欢迎来到学生管理系统")
    print("1.输入学号查询成绩")
    print("2.添加学生信息")
    print("3.删除学生信息")
    print("4.打印所有学生信息")
    print("5.修改学生信息")
    print("6.保存学生信息到指定文件")
    print("0.退出系统")
    print("-" * 30)


# 打印信息
def lookup():
    sid = int(input("输入查询学号:")) - 1  # 学号
    if sid > len(student1) - 1:
        print("输入错误，返回菜单")
    else:
        print(student1[sid])  # 输出信息
    input("按回车键继续")


# 添加信息
def append():
    newsid = eval(input('输入新同学学号(从4开始)：'))
    newname = eval(input('输入新同学姓名:'))
    newage = eval(input('输入新同学年龄：'))
    newsocer = eval(input('输入新同学成绩：'))
    newstudent1 = {}
    newstudent1[newsid] = newname  # 添加 学号、姓名
    newstudent1['age'] = newage  # 添加年龄
    newstudent1['socer'] = newsocer  # 添加成绩
    student1.append(newstudent1)  # 加入列表
    input("按回车键继续")


# 删除信息
def delete():
    did = int(input("输入需要删除的成绩对应的学号：")) - 1
    del student1[did]  # 删除指定信息
    input("按回车键继续")


##输出所有学生信息
def allinformation():
    print("所有信息如下：")
    i = 1
    for show in student1:
        print("{}".format(show))  # 打印学生信息
        i += 1
    input("按回车键继续")


##修改信息
def revise():
    resid = int(input("输入要修改的学生学号：")) - 1
    r = input("要修改的对象(1.年龄；2.成绩;否则，都修改)：")
    if r == '1':
        newage = input("修改后的年龄")
        student1[resid]['age'] = newage
    elif r == '2':
        newsocer = input("修改后的成绩")
        student1[resid]['socer'] = newsocer
    else:
        newage = input("修改后的年龄")
        newsocer = input("修改后的成绩")
        student1[resid]['socer'] = newsocer
        student1[resid]['age'] = newage
    input("按回车键继续")


##保存学生信息
def save():
    f = open('student.txt', 'w')  # 打开文件
    f.write(str(student1))  # 写入文件
    f.close()  # 关闭文件
    input("保存成功按回车键继续")


if __name__ == '__main__':
    while True:
        menu()
        key = input("输入选项数字 查询/输入 信息：")
        if key == '1':
            lookup()  # 打印指定学生信息
        elif key == '2':
            append()  # 添加新的学生信息
        elif key == '3':
            delete()  # 删除指定学生信息
        elif key == '4':
            allinformation()  # 打印所有信息
        elif key == '5':
            revise()  # 修改指定学生信息
        elif key == '6':
            save()  # 保存信息
        elif key == '0':
            print("确定退出？")
            exit = input("输入yes退出：")
            if exit == 'yes':
                break
            else:
                print("输入错误，返回 ")
