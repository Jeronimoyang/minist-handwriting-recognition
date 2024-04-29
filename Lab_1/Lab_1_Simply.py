import os
#建立一个位置数组A、B、C分别为1、2、3
Position_Array={'1':'A','2':'B','3':'C'}
#定义Condition类，存入各个元素的位置信息
class Condition:
    def __init__(Condition,monkey=1,banana=2,box=3,monkey_onbox=0):
        Condition.monkey=monkey
        Condition.banana=banana
        Condition.box=box
        Condition.monkey_onbox=monkey_onbox
#判断输入的元素位置信息是否合法       
def Legal_Judgment(Condition):
    if (Condition.monkey<1 or Condition.monkey>3)\
    or(Condition.banana<1 or Condition.banana>3)\
    or(Condition.box<1 or Condition.box>3)\
    or(Condition.monkey_onbox<0 or Condition.monkey_onbox>1)\
    or(Condition.monkey!=Condition.box and Condition.monkey_onbox==1):
        print("输入元素位置信息不合法")
        os._exit(0)
    else:
        return Condition
#猴子运动函数
def Monkey_Move(Condition,Moment):
    print("第"+str(Moment)+"步,猴子从位置"+str(Position_Array[str(Condition.monkey)])+ \
          "运动到位置"+ str(Position_Array[str(Condition.box)]))
    Condition.monkey=Condition.box
    return Condition
#猴子移动箱子函数
def Monkey_Movebox(Condition,Moment):
    print("第"+str(Moment)+"步,猴子将箱子从位置"+str(Position_Array[str(Condition.box)])+ \
          "移动到位置"+str(Position_Array[str(Condition.banana)]))
    Condition.monkey=Condition.banana
    Condition.box=Condition.banana
    return Condition
#猴子从箱子上下来函数
def Monkey_Downbox(Condition,Moment):
    Condition.monkey_onbox=0
    print("第"+str(Moment)+"步,猴子从箱子上下来")
    return Condition
#猴子爬上箱子函数
def Monkey_Upbox(Condition,Moment):
    Condition.monkey_onbox=1
    print("第"+str(Moment)+"步,猴子爬上箱子")
    return Condition
#摘香蕉行动函数
def Operation_Banana_Picking(Condition):
    Moment=1
    if Condition.monkey==Condition.banana \
    and Condition.box==Condition.banana \
    and Condition.monkey_onbox==1:
        print("第%d步,猴子摘到香蕉"%(Moment))
        return
    else:
        if Condition.monkey_onbox==1:
            if Condition.monkey!=Condition.banana:
                Condition=Monkey_Upbox(Monkey_Movebox(Monkey_Downbox(Condition,Moment),Moment+1),Moment+2)
                Moment=Moment+3
        else:
            if Condition.monkey==Condition.box:
                if Condition.box==Condition.banana:
                    Condition=Monkey_Upbox(Condition,Moment)
                    Moment=Moment+1
                else:
                    Condition=Monkey_Upbox(Monkey_Movebox(Condition,Moment),Moment+1)                       
                    Moment=Moment+2
            else:
                if Condition.box==Condition.banana:
                    Condition=Monkey_Upbox(Monkey_Move(Condition,Moment),Moment+1)
                    Moment=Moment+2
                else:
                    Condition=Monkey_Upbox(Monkey_Movebox(Monkey_Move(Condition,Moment),Moment+1),Moment+2)
                    Moment=Moment+3
        print("第%d步,猴子摘到香蕉"%(Moment))
#主函数接收输入的状态变量，对其进行合法检验，最终开始摘香蕉行动
if __name__=="__main__":
    Reminder=input("请输入各个元素的位置信息:\n")
    Condition_Input=Reminder.split(" ")
    Condition=Condition(int(Condition_Input[0]),int(Condition_Input[1]),int(Condition_Input[2]),int(Condition_Input[3]))
    Condition=Legal_Judgment(Condition)
    Operation_Banana_Picking(Condition)