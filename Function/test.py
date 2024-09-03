

# def user_info(user_salary, user_name, user_dept, user_city):
#     print(f"user name is : {user_name}")
#     print(f"user salary is : {user_salary}")
#     print(f"user dept is : {user_dept}")
#     print(f"user city is : {user_city}")


# def user_info(*args):
#     print(args)
#     print(f"user name is : {args[0]}")
#     print(f"user salary is : {args[1]}")
#     print(f"user dept is : {args[2]}")
#     print(f"user city is : {args[3]}")
#
#
#
# user_info(200, "PQR", "IT", "PUNE")

# user_info(200, "PQR")

# user_info(user_city="PUNE", user_name="PQR", user_salary=100, user_dept="Software")

# user_info(200, "PQR", user_dept="IT", user_city="Pune")

# user_info(user_dept="IT", user_city="Pune", 200, "PQR" )










# def add(*args):
#     print("args :: ", args)
#     print("args :: ", type(args))
#     # result = a + b + c
#     # print("result :: ", result)
#     result = 0
#     for i in args:
#         result = result + i
#     print("result ::", result)



# add(a=10, b=20)
# add(10, 20, 30)





def user_info(**kwargs):
    print("kwargs :: ", kwargs)
    print("kwargs :: ", type(kwargs))
    print(f"user name is : {kwargs.get('user_name')}")
    print(f"user salary is : {kwargs.get('user_salary')}")
    print(f"user dept is : {kwargs.get('user_dept')}")
    print(f"user city is : {kwargs.get('user_city')}")
    print(f"user age is : {kwargs.get('user_age')}")
    print(f"user blood  group : {kwargs.get('blood_group')}")
    # print(f"user name is : {user_name}")
    # print(f"user salary is : {user_salary}")
    # print(f"user dept is : {user_dept}")
    # print(f"user city is : {user_city}")
    # print(f"user age is : {user_age}")






user_info(user_name="PQR", user_dept="IT", user_city="PUNE", user_salary=200, user_age=30)

print("\n\n")
user_info(user_name="PQR", user_dept="IT", user_city="PUNE", user_salary=200, user_age=30, blood_group="O+")














