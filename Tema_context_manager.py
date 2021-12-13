import contextlib

#KeyError with Class
# class just_some_exceptions:
#     def __init__(self):
#         self.dictionary = {
#                             'brand': 'Dell',
#                             'model': 'Latitude 3510',
#                             'ram': '16 GB',
#                             'price': 3000
#                             }
#     def __enter__(self):
#         return self.dictionary
#
#     def __exit__(self, exc_type, exc_value, exc_tb):
#         try:
#             dict_brand = dict['brand']
#             print(dict_brand)
#             dict_model = dict['model']
#             print(dict_model)
#             dict_procesor = dict['procesor']
#             print(dict_procesor)
#         except KeyError as key:
#             print(f"Cheia {key} nu este in dictionar")
#         finally:
#             return
#
# with just_some_exceptions() as dict:
#     print('-' * 100)
#     print(dict)

#IndexError with Class
# class just_some_exceptions:
#     def __init__(self):
#         self.list = [1, 2, 3]
#
#     def __enter__(self):
#         return self.list
#
#     def __exit__(self, exc_type, exc_value, exc_tb):
#         try:
#             n = input("Please enter an index to check: ")
#             print(f"Number is {list[int(n)]}")
#         except IndexError as error:
#             print(error)
#         finally:
#             return
#
# with just_some_exceptions() as list:
#     print('-' * 100)
#     print(list)

#KeyError with Generator
# @contextlib.contextmanager
# def just_some_exceptions():
#     dict = {'brand': 'Dell',
#               'model': 'Latitude 3510',
#               'ram': '16 GB',
#               'price': 3000}
#     yield
#     try:
#         dict_brand = dict['brand']
#         print(dict_brand)
#         dict_model = dict['model']
#         print(dict_model)
#         dict_procesor = dict['procesor']
#         print(dict_procesor)
#     except KeyError as key:
#         print(f"Cheia {key} nu este in dictionar")
#     finally:
#         return
#
# with just_some_exceptions() as dict:
#     print('-' * 100)
#     print(dict)

#IndexError with Generator
# @contextlib.contextmanager
# def just_some_exceptions():
#     list = [1, 2, 3]
#     print(list)
#     yield
#     try:
#         n = input("Please enter an index to check: ")
#         print(f"Number is {list[int(n)]}")
#     except IndexError as error:
#         print(error)
#     finally:
#         return
#
# with just_some_exceptions() as list:
#     print('-' * 100)
