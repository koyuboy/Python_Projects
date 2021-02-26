def func1(arg1, arg2):
    var24 = var5(arg1, arg2)
    var28 = func6(var24, arg1)
    var31 = class8()
    for var32 in range(37):
        var33 = var31.func9
        var33(var24, arg1)
    var38 = func10(var24, var28)
    var39 = arg1 ^ -4 ^ arg2 + var38
    var40 = var28 ^ arg1 | 824657253 - var28
    var41 = var39 | var38
    var42 = var39 & arg1
    var43 = var40 | var39 - arg2 & var42
    if var43 < arg1:
        var44 = 1872227018 | arg2
    else:
        var44 = arg1 ^ -753932887
    var45 = 589563704 ^ var42
    var46 = var39 - var39 + var41
    var47 = var38 | var46
    var48 = arg2 - var45
    var49 = (var42 - var38) ^ (var47 | var43)
    var50 = arg1 + var43 ^ var28 ^ var45
    var51 = (var42 ^ var42 + var42) & var50
    if var42 < var51:
        var52 = -897326910 + arg1 | var51
    else:
        var52 = arg1 & var39 ^ var38 | arg1
    var53 = var24 ^ var40 - arg1 + var49
    var54 = var41 ^ -823822330
    var55 = var49 | (var50 - var46 ^ var51)
    result = var51 + var48
    return result
def func10(arg34, arg35):
    var36 = 0
    for var37 in range(50):
        var36 += -1 + arg34 ^ var36
    return var36
class class8(object):
    def func9(self, arg29, arg30):
        return 0
def func4(arg6, arg7):
    def func5(arg8, arg9):
        var10 = (-75355030 & arg7) & (175825203 - 2083407788) + arg8
        result = arg7 - (arg9 - arg8 + var10 | -518350484)
        return result
    var11 = func5(arg6, arg7)
    var12 = var11 - var11
    var13 = arg6 | var11 | var11
    var14 = var12 | arg7 | arg6
    var15 = arg7 | (var11 - var13)
    if var12 < arg6:
        var16 = var11 ^ arg7
    else:
        var16 = ((-880 | -753) + var12) | var11
    var17 = 1997487354 | (var11 + 494) & arg7
    var18 = var13 & var13 + -939 + var11
    var19 = var13 + arg7
    var20 = var17 & var15
    var21 = var20 ^ arg7 - arg6
    var22 = ((var17 + var18) - var19) | var20
    var23 = (var13 + var21) + var21 + var12
    result = -590967974 ^ 466795854
    return result
def func3():
    closure = [-7]
    def func2(arg3, arg4):
        closure[0] += func4(arg3, arg4)
        return closure[0]
    func = func2
    return func
var5 = func3()
def func6(arg25, arg26):
    def func7(acc, rest):
        var27 = -6 | acc - acc
        if acc == 0:
            return var27
        else:
            result = func7(acc - 1, var27)
            return result
    result = func7(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 11'
    print 'arg_number: 56'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,