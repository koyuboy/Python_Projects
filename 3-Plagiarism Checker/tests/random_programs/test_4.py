def func1(arg1, arg2):
    var7 = func2(arg2, arg1)
    var12 = func3(arg2, var7)
    var15 = class4()
    for var16 in xrange(36):
        var17 = var15.func5
        var17(var7, var16)
    var22 = func6(arg1, var12)
    var26 = func7(var7, var12)
    var27 = arg1 ^ arg2
    var28 = 872968337 + var27
    var29 = arg1 - var27 ^ var12
    var30 = 561239968 | var29
    var31 = var22 - (var22 + (arg2 | var22))
    var32 = var28 + var27 + var31
    var33 = 2106063540 - var28 | var31 ^ -297
    var34 = (var7 & var26) & (var33 - arg1)
    var35 = var33 + (var22 & var33) + var33
    var36 = var12 ^ arg2 - (var31 - -96)
    var37 = (arg2 - var26) ^ (arg2 & var22)
    var38 = var36 & var26 | var28 ^ var12
    var39 = var26 ^ var26 | var33 ^ var36
    if var28 < var37:
        var40 = ((var32 & var7) | -1076341429) - var36
    else:
        var40 = var29 | var36 | var33 ^ arg1
    var41 = 427 - (var26 | var28)
    var42 = arg2 | var30 ^ (var26 + var22)
    var43 = (var32 - var31) - 237 | var29
    if var32 < var38:
        var44 = (788 + (arg2 ^ var31)) & var28
    else:
        var44 = ((var27 + var32) - var26) ^ 565
    var45 = (arg1 - var35 + var35) - var22
    var46 = (-1484127246 | var36) | arg2 + var29
    result = (var34 & (var31 & var46 | var42)) ^ var41 & (var7 | var33) & var33
    return result
def func6(arg18, arg19):
    var20 = 0
    for var21 in xrange(15):
        var20 += arg18 - arg18 | 8
    return var20
class class4(object):
    def func5(self, arg13, arg14):
        result = 0 + (253207951 | -1934635583) | -98478248 | 0
        return result
def func3(arg8, arg9):
    var10 = 0
    for var11 in xrange(49):
        var10 += arg8 | var11 - var11
    return var10
def func2(arg3, arg4):
    var5 = (((651 | arg4 - -792 - arg3 | ((((33 | (-1180190499 | arg3)) ^ (arg4 & (arg4 | 156437025 ^ -974 + arg4) + arg3) + 466 ^ 870478705) + arg3) | arg3) & 2017505953) + arg3) ^ 1730590361) | -477378431 ^ 1236890212
    var6 = var5 | arg3
    result = var5 ^ var6
    return result
def func7(arg23, arg24):
    closure = [0]
    def func8(acc, rest):
        var25 = ((-9 - -8 + closure[0]) & -9 & closure[0] | acc) & -8
        closure[0] += var25
        if acc == 0:
            return var25
        else:
            result = func8(acc - 1, var25)
            return result
    result = func8(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 9'
    print 'arg_number: 47'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,