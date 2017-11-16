# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class TTaskInfo(list):
    def __init__(self):
        list.__init__(self)

    def asDict(self):
        # DEBUG_MSG("TTaskInfo:asDict")
        # DEBUG_MSG(self)
        datas = {
            "taskNpcName":self[0],
            "taskIndex":self[1],
            "isTaskFinish":self[2],
            "isTaskCommit":self[3]
        }
        return datas

    def createFromDict(self, dicData):
        # DEBUG_MSG("TTaskInfo:createFromDict")
        # DEBUG_MSG(self)
        # DEBUG_MSG(dicData)
        self.extend([dicData["taskNpcName"], dicData["taskIndex"], dicData["isTaskFinish"], dicData["isTaskCommit"]])
        return self

class TASK_INFO_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dic):
        return TTaskInfo().createFromDict(dic)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, TTaskInfo)

task_info_inst = TASK_INFO_PICKLER()

class TTaskInfoList(dict):
    def __init__(self):
        dict.__init__(self)

    def asDict(self):
        """
        转换为固定字典格式存到数据库
        :return:
        """
        # DEBUG_MSG("TTaskInfoList:asDict")
        # DEBUG_MSG(self)

        datas = []
        for key, val in self.items():
            datas.append(val)
        dic = {"values": datas}       #还原为固定字典

        # DEBUG_MSG(dic)
        return dic

    def createFromDict(self, dictData):
        """
        从数据库取出固定字典并转换格式
        taskInfoList=
        {
            npc名字+任务索引:
                {
                    0: npc名字,
                    1: 任务索引,
                    2: 是否完成
                    3: 是否提交
                },
            npc名字+任务索引:
                {
                    0: npc名字,
                    1: 任务索引,
                    2: 是否完成
                    3: 是否提交
                },
        }
        :param dictData:
        :return:
        """
        # DEBUG_MSG("TTaskInfoList:createFromDict")
        # DEBUG_MSG(self)
        # DEBUG_MSG(dictData)
        for data in dictData["values"]:
            self[data[0] + str(data[1])] = data
        return self

class TASK_INFO_LIST_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dic):
        """
        // 此接口被C++底层调用
        // 引擎将数据交给脚本层管理，脚本层可以将这个字典重定义为任意类型
        // dct中的数据为 {"k1" : 0, "k2" : 0}, 它就是一个字典，包含了2个固定的key
        // 且值一定是符合alias.xml中定义的类型
        // XXX_TYPE().createFromDict接口调用后，返回的是一个list([0, 0])
        // createObjFromDict被调用后，返回的数据将直接赋值到脚本中的变量
        """
        return TTaskInfoList().createFromDict(dic)

    def getDictFromObj(self, obj):
        """
        // 此接口被C++底层调用
        // 底层需要从脚本层中获取数据，脚本层此时应该将数据结构还原为固定字典
        // list([0, 0]) => {"k1" : 0, "k2" : 0}
        """
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, TTaskInfoList)

task_info_list_inst = TASK_INFO_LIST_PICKLER()