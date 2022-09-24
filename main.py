# import tensorflow as tf
# tensorflow_version = tf.__version__
# gpu_available = tf.test.is_gpu_available()
# print("tensorflow version:", tensorflow_version, "\tGPU available:", gpu_available)
# a = tf.constant([1.0, 2.0], name="a")
# b = tf.constant([1.0, 2.0], name="b")
# result = tf.add(a, b, name="add")
# print(result)


# class Student:
#     name = None
#
#     def sayhi(self):
#         print(f"我是{self.name}")
#
# stu = Student()
# stu.name = "xls"
# stu.sayhi()

# import winsound
# winsound.Beep(2000,3000)

# class Student:
#
#     print("i am sb")
#
#     def __init__(self,nam,ag,te):
#         self.name = nam
#         self.age = ag
#         self.tel = te
#
# stu = Student("xgw",22,"13290907286")
# print(stu.name,stu.age,stu.tel)





# input("请输入第i位学生信息，总共需要录入10位学生信息")


# class Student:
#
#     print("i am sb")
#
#     def __init__(self,nam,ag,te):
#         self.name = nam
#         self.age = ag
#         self.tel = te
#
# stu = Student("xgw",22,"13290907286")
# print(stu.name,stu.age,stu.tel)
#





# class Phone:
#     __current_voltage = 0.5
#
#     def __keep_single_core(self):
#         print("cup单核运行")
#
#     def call_by_5g(self):
#         if self.__current_voltage >= 1:
#             print("5g on")
#         else:
#             self.__keep_single_core()
#             print("无法使用5g")
#
# phone = Phone()
# phone.call_by_5g()


# # # 黑马程序员 p116作业
# #
# class Phone:
#     __is_5g = True
#
#     def __cheak_5g(self):
#         if self.__is_5g is True:
#             print("5g on")
#         else:
#             print("5g off,useing 4g")
#
#     def call_by_5g(self):
#         self.__cheak_5g()
#         print("calling")
#
#
# ph = Phone()
# ph.call_by_5g()



# import numpy as np
# array = np.array([[1,2,3],
#                  [2,3,4]])
# print(array)



##numpy

# import numpy as np
# def 数组相加(n):
#     a = np.arange(1,n+1)**3
#     b = np.arange(1,n+1)**2
#     return a+b
# print(数组相加(3))
#


# import numpy as np
# a = np.arange(1,6)
#
# print(a.dtype)
# print(type(a))


import numpy as np
a = np.arange(10)
a[a>5] = 1
a[a<=5] = 0
# a[a>5] = 1
print(a)