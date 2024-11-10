# ******************************************* hybrid and heirarchical inheritance **********************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/tree/main/81-Day-81-Hybrid-and-Hierarchical-Inheritance/.tutorial

# when we combine 2 or more than 2 forms of inheritance we get hybrid inheritance.

'''
class baseClass:1
    pass
class derived1(baseClass):2
    pass
class derived2(baseClass):3
    pass
class derived3(derived1, derived2)4
    pass

1, 2 -> Simple Inheritance
2, 3, 4 -> mulitple Inheritance

'''

'''
class B:
    pass
class C1(B):
    pass
class C2(B):
    pass
class C3(C1):
    pass
class C4(C1):
    pass
class C5(C2):
    pass
class C6(C2):
    pass
'''