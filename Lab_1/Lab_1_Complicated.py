import os
End=1
#建立一个位置数组A、B、C、D、E、F分别为1、2、3、4、5、6
Position_Array={'1':'A','2':'B','3':'C','4':'D','5':'E','6':'F'}
#定义Condition类，存入各个元素的位置信息
class Condition:
    def __init__(Condition,monkey=1,banana=2,poison=3,box_1=4,box_2=5,monkey_onbox_1=0,monkey_onbox_2=0):
        Condition.monkey=monkey
        Condition.banana=banana
        Condition.poison=poison
        Condition.box_1=box_1
        Condition.box_2=box_2
        Condition.monkey_onbox_1=monkey_onbox_1
        Condition.monkey_onbox_2=monkey_onbox_2
#判断输入的元素位置信息是否合法       
def Legal_Judgment(Condition):
    if (Condition.monkey<1 or Condition.monkey>6)\
    or(Condition.banana<1 or Condition.banana>6)\
    or(Condition.poison<1 or Condition.poison>6)\
    or(Condition.box_1<1 or Condition.box_1>6)\
    or(Condition.box_2<1 or Condition.box_2>6)\
    or(Condition.monkey_onbox_1<0 or Condition.monkey_onbox_1>1)\
    or(Condition.monkey_onbox_2<0 or Condition.monkey_onbox_2>1)\
    or(Condition.monkey!=Condition.box_1 and Condition.monkey_onbox_1==1)\
    or(Condition.monkey!=Condition.box_2 and Condition.monkey_onbox_2==1)\
    or(Condition.box_1==Condition.box_2):
        print("输入元素位置信息不合法")
        os._exit(0)
    else:
        return Condition
#猴子运动到1号箱子函数
def Monkey_Move_1(Condition,Moment):
    print("第"+str(Moment)+"步,猴子从位置"+str(Position_Array[str(Condition.monkey)])+ \
          "运动到位置"+ str(Position_Array[str(Condition.box_1)]))
    Condition.monkey=Condition.box_1
    return Condition
#猴子运动到2号箱子函数
def Monkey_Move_2(Condition,Moment):
    print("第"+str(Moment)+"步,猴子从位置"+str(Position_Array[str(Condition.monkey)])+ \
          "运动到位置"+ str(Position_Array[str(Condition.box_2)]))
    Condition.monkey=Condition.box_2
    return Condition
#猴子移动1号箱子1到香蕉函数
def Monkey_Movebox_1_banana(Condition,Moment):
    print("第"+str(Moment)+"步,猴子将1号箱子从位置"+str(Position_Array[str(Condition.box_1)])+ \
          "移动到位置"+str(Position_Array[str(Condition.banana)]))
    Condition.monkey=Condition.banana
    Condition.box_1=Condition.banana
    return Condition
#猴子移动2号箱子到香蕉函数
def Monkey_Movebox_2_banana(Condition,Moment):
    print("第"+str(Moment)+"步,猴子将2号箱子从位置"+str(Position_Array[str(Condition.box_2)])+ \
          "移动到位置"+str(Position_Array[str(Condition.banana)]))
    Condition.monkey=Condition.banana
    Condition.box_2=Condition.banana
    return Condition
#猴子移动1号箱子1到毒药函数
def Monkey_Movebox_1_posion(Condition,Moment):
    print("第"+str(Moment)+"步,猴子将1号箱子从位置"+str(Position_Array[str(Condition.box_1)])+ \
          "移动到位置"+str(Position_Array[str(Condition.poison)]))
    Condition.monkey=Condition.poison
    Condition.box_1=Condition.poison
    return Condition
#猴子移动2号箱子到毒药函数
def Monkey_Movebox_2_posion(Condition,Moment):
    print("第"+str(Moment)+"步,猴子将2号箱子从位置"+str(Position_Array[str(Condition.box_2)])+ \
          "移动到位置"+str(Position_Array[str(Condition.poison)]))
    Condition.monkey=Condition.poison
    Condition.box_2=Condition.poison
    return Condition
#猴子从1号箱子上下来函数
def Monkey_Downbox_1(Condition,Moment):
    Condition.monkey_onbox_1=0
    print("第"+str(Moment)+"步,猴子从1号箱子上下来")
    return Condition
#猴子爬上1号箱子函数
def Monkey_Upbox_1(Condition,Moment):
    Condition.monkey_onbox_1=1
    print("第"+str(Moment)+"步,猴子爬上1号箱子")
    return Condition
#猴子从2号箱子上下来函数
def Monkey_Downbox_2(Condition,Moment):
    Condition.monkey_onbox_2=0
    print("第"+str(Moment)+"步,猴子从2号箱子上下来")
    return Condition
#猴子爬上2号箱子函数
def Monkey_Upbox_2(Condition,Moment):
    Condition.monkey_onbox_2=1
    print("第"+str(Moment)+"步,猴子爬上2号箱子")
    return Condition
#打碎毒药行动函数
def Destory_Posion(Condition,Moment):
    if Condition.monkey==Condition.poison \
    and (Condition.box_1==Condition.poison and Condition.monkey_onbox_1==1) \
    or (Condition.box_2==Condition.poison and Condition.monkey_onbox_2==1):
        global End
        End=Moment
        print("第"+str(Moment)+"步,猴子破坏毒药")
    else:
        if (Condition.monkey_onbox_1==1) or (Condition.monkey_onbox_2==1):
            if Condition.monkey_onbox_1==1:
                if Condition.monkey!=Condition.poison:
                    Condition=Monkey_Upbox_1(Monkey_Movebox_1_posion(Monkey_Downbox_1(Condition,Moment),Moment+1),Moment+2)
                    Moment=Moment+3
            else:
                if Condition.monkey!=Condition.poison:
                    Condition=Monkey_Upbox_2(Monkey_Movebox_2_posion(Monkey_Downbox_2(Condition,Moment),Moment+1),Moment+2)
                    Moment=Moment+3
        else:
            if (Condition.monkey==Condition.box_1) or (Condition.monkey==Condition.box_2):
                if Condition.monkey==Condition.box_1:
                    if Condition.box_1==Condition.poison:
                        Condition=Monkey_Upbox_1(Condition,Moment)
                        Moment=Moment+1
                    else:
                        Condition=Monkey_Upbox_1(Monkey_Movebox_1_posion(Condition,Moment),Moment+1)                       
                        Moment=Moment+2
                else:
                    if Condition.box_2==Condition.poison:
                        Condition=Monkey_Upbox_2(Condition,Moment)
                        Moment=Moment+1
                    else:
                        Condition=Monkey_Upbox_2(Monkey_Movebox_2_posion(Condition,Moment),Moment+1)                       
                        Moment=Moment+2
            else:
                if (Condition.box_1==Condition.poison) or (Condition.box_2==Condition.poison):
                    if Condition.box_1==Condition.poison:
                        Condition=Monkey_Upbox_1(Monkey_Move_1(Condition,Moment),Moment+1)
                        Moment=Moment+2
                    else:
                        Condition=Monkey_Upbox_2(Monkey_Move_2(Condition,Moment),Moment+1)
                        Moment=Moment+2
                else:
                    if(abs(Condition.monkey-Condition.box_1)+abs(Condition.monkey-Condition.box_1)< \
                        abs(Condition.monkey-Condition.box_2)+abs(Condition.monkey-Condition.box_2)):
                        Condition=Monkey_Upbox_1(Monkey_Movebox_1_posion(Monkey_Move_1(Condition,Moment),Moment+1),Moment+2)
                        Moment=Moment+3
                    if(abs(Condition.monkey-Condition.box_1)+abs(Condition.monkey-Condition.box_1)> \
                         abs(Condition.monkey-Condition.box_2)+abs(Condition.monkey-Condition.box_2)):
                        Condition=Monkey_Upbox_2(Monkey_Movebox_2_posion(Monkey_Move_2(Condition,Moment),Moment+1),Moment+2)
                        Moment=Moment+3
                    else:
                        if(abs(Condition.box_1-Condition.poison)<abs(Condition.box_1-Condition.poison)):
                            Condition=Monkey_Upbox_1(Monkey_Movebox_1_posion(Monkey_Move_1(Condition,Moment),Moment+1),Moment+2)
                            Moment=Moment+3
                        if(abs(Condition.box_1-Condition.poison)>abs(Condition.box_1-Condition.poison)):
                            Condition=Monkey_Upbox_2(Monkey_Movebox_2_posion(Monkey_Move_2(Condition,Moment),Moment+1),Moment+2)
                            Moment=Moment+3
    End=Moment
    print("第"+str(Moment)+"步,猴子破坏毒药")
#摘香蕉行动函数
def Operation_Banana_Picking(Condition,Moment):
    if Condition.monkey==Condition.banana \
    and (Condition.box_1==Condition.banana and Condition.monkey_onbox_1==1) \
    or (Condition.box_2==Condition.banana and Condition.monkey_onbox_2==1):
        global End
        End=Moment
        print("第"+str(Moment)+"步,猴子摘到香蕉")
    else:
        if (Condition.monkey_onbox_1==1) or (Condition.monkey_onbox_2==1):
            if Condition.monkey_onbox_1==1:
                if Condition.monkey!=Condition.banana:
                    Condition=Monkey_Upbox_1(Monkey_Movebox_1_banana(Monkey_Downbox_1(Condition,Moment),Moment+1),Moment+2)
                    Moment=Moment+3
            else:
                if Condition.monkey!=Condition.banana:
                    Condition=Monkey_Upbox_2(Monkey_Movebox_2_banana(Monkey_Downbox_2(Condition,Moment),Moment+1),Moment+2)
                    Moment=Moment+3
        else:
            if (Condition.monkey==Condition.box_1) or (Condition.monkey==Condition.box_2):
                if Condition.monkey==Condition.box_1:
                    if Condition.box_1==Condition.banana:
                        Condition=Monkey_Upbox_1(Condition,Moment)
                        Moment=Moment+1
                    else:
                        Condition=Monkey_Upbox_1(Monkey_Movebox_1_banana(Condition,Moment),Moment+1)                       
                        Moment=Moment+2
                else:
                    if Condition.box_2==Condition.banana:
                        Condition=Monkey_Upbox_2(Condition,Moment)
                        Moment=Moment+1
                    else:
                        Condition=Monkey_Upbox_2(Monkey_Movebox_2_banana(Condition,Moment),Moment+1)                       
                        Moment=Moment+2
            else:
                if (Condition.box_1==Condition.banana) or (Condition.box_2==Condition.banana):
                    if Condition.box_1==Condition.banana:
                        Condition=Monkey_Upbox_1(Monkey_Move_1(Condition,Moment),Moment+1)
                        Moment=Moment+2
                    else:
                        Condition=Monkey_Upbox_2(Monkey_Move_2(Condition,Moment),Moment+1)
                        Moment=Moment+2
                else:
                    if(abs(Condition.monkey-Condition.box_1)+abs(Condition.monkey-Condition.box_1)< \
                        abs(Condition.monkey-Condition.box_2)+abs(Condition.monkey-Condition.box_2)):
                        Condition=Monkey_Upbox_1(Monkey_Movebox_1_banana(Monkey_Move_1(Condition,Moment),Moment+1),Moment+2)
                        Moment=Moment+3
                    if(abs(Condition.monkey-Condition.box_1)+abs(Condition.monkey-Condition.box_1)> \
                         abs(Condition.monkey-Condition.box_2)+abs(Condition.monkey-Condition.box_2)):
                        Condition=Monkey_Upbox_2(Monkey_Movebox_2_banana(Monkey_Move_2(Condition,Moment),Moment+1),Moment+2)
                        Moment=Moment+3
                    else:
                        if(abs(Condition.box_1-Condition.banana)<abs(Condition.box_1-Condition.banana)):
                            Condition=Monkey_Upbox_1(Monkey_Movebox_1_banana(Monkey_Move_1(Condition,Moment),Moment+1),Moment+2)
                            Moment=Moment+3
                        if(abs(Condition.box_1-Condition.banana)>abs(Condition.box_1-Condition.banana)):
                            Condition=Monkey_Upbox_2(Monkey_Movebox_2_banana(Monkey_Move_2(Condition,Moment),Moment+1),Moment+2)
                            Moment=Moment+3
        End=Moment+1
        print("第"+str(Moment)+"步,猴子摘到香蕉")
#主函数接收输入的状态变量，对其进行合法检验，最终开始摘香蕉行动
if __name__=="__main__":
    Reminder=input("请输入各个元素的位置信息:\n")
    Condition_Input=Reminder.split(" ")
    Condition=Condition(int(Condition_Input[0]),int(Condition_Input[1]),int(Condition_Input[2]), \
                        int(Condition_Input[3]),int(Condition_Input[4]),int(Condition_Input[5]), \
                        int(Condition_Input[6]))
    Condition=Legal_Judgment(Condition)
    number=input("请输入方案:1.只摘香蕉;2.只破坏毒药;3.先摘香蕉后破坏毒药;4.先破坏毒药后摘香蕉 ")
    if number=='1':
        Operation_Banana_Picking(Condition,1)
    if number=='2':
        Destory_Posion(Condition,1)
    if number=='3':
        Operation_Banana_Picking(Condition,1)
        Destory_Posion  (Condition,End+1)
    if number=='4':
        Destory_Posion(Condition,1)
        Operation_Banana_Picking(Condition,End+1)