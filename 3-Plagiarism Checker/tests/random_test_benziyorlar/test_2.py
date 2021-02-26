def func2(arg3, arg4):
    var12 = func3(arg3, arg4)
    var40 = func4(arg4, arg3)
    var47 = func5(arg3, arg4)
    var71 = func6(arg4, arg3)
    var74 = class9()
    for var75 in xrange(25):
        var74.func10(var71, var40)
    var76 = (483 ^ arg4 | var71) & -686376255 - var71
    result = (arg4 ^ arg3) + var76
    return result
class class9(object):
    def func10(self, arg72, arg73):
        result = arg72 - -1 - arg73 & (arg72 ^ arg73)
        return result
def func8(arg50, arg51):
    var52 = (arg50 + arg50) ^ -1791454041
    var53 = (arg51 + arg51) - arg50 & 695
    var54 = var53 | 384
    var55 = (var53 | var53) | arg50
    var56 = var53 - var52 ^ var54 + arg50
    var57 = (var56 + var56) & var54
    var58 = var56 | var53 ^ arg50 - arg51
    if var55 < var52:
        var59 = -1977887126 | var53
    else:
        var59 = -1298260890 - (arg50 - arg51) + 877
    var60 = -272072832 + (var54 | var53) - arg51
    var61 = var57 + (var54 + var56)
    var62 = 812312890 & var52 - var53
    var63 = (1232627430 & -331363204) ^ var52 - var55
    var64 = var61 + var61 | var61 | arg50
    var65 = var61 - (var54 ^ var52) - var62
    var66 = var52 & var58
    var67 = -951233771 & (var56 - arg51 ^ arg50)
    var68 = var63 ^ arg51
    var69 = arg50 | var63 | var68 | var61
    result = (var62 ^ var61) - var60
    return result
def func5(arg41, arg42):
    var43 = 559 | -1752738988 | arg42 | ((-378356345 - (arg42 - (-709 ^ (-1957757516 - (arg42 & arg42 & 1725908074 ^ arg41 | (1549201802 + arg41) - arg41 | 1853741612 - arg42 + 958 & (arg42 - arg41)))))) + arg41) - 81 - arg42
    var44 = arg42 ^ -823 - -87
    if var43 < var44:
        var45 = var43 - var43 ^ 373066544
    else:
        var45 = (var43 | (arg42 ^ arg41) - (arg41 - (1520621433 & var43) & var44 | arg42 ^ (arg42 | var44) | (((-387 ^ ((-11631211 + 541 + (var44 & arg42) & arg42) | arg41 + -312534379)) & -1099880196) | arg41) + var43)) - var43
    var46 = var44 | (1239942335 ^ -456)
    result = -922 & (var46 & arg42) - arg42 ^ var46 & var44
    return result
def func4(arg13, arg14):
    var15 = arg13 & -932 - arg14 - -1525072571
    var16 = arg13 - arg14
    var17 = var15 - (var15 + arg14) | -224891319
    var18 = (var15 - var15) - (var17 & var16)
    var19 = var15 & var18
    var20 = (var19 + var15) - var19 | 38848108
    if var20 < var19:
        var21 = var20 | var19 + arg14
    else:
        var21 = var16 - 265
    var22 = (var15 + var16 + var15) | var18
    var23 = arg14 ^ var19 & var18 | arg13
    var24 = arg14 - var18 | 1140523566 + 379
    var25 = (-143770138 - var15) | arg13
    var26 = arg13 - (var25 & -1334166434) & var19
    var27 = -1116542993 | var26 + -1138329795 & var26
    var28 = var19 & arg14 | var20 & var23
    var29 = var19 & var26
    var30 = var25 | (var17 | (arg14 | var23))
    var31 = var28 - var24
    var32 = var17 ^ (var20 - var16 | var26)
    var33 = var32 | var25
    var34 = var33 & var18
    var35 = var23 - (var32 - var32 & arg13)
    var36 = arg13 - 1669166003
    var37 = (var29 + var17) - var33
    var38 = var17 ^ var27 - (var33 & var18)
    var39 = -424792714 - var22 | var34 ^ var34
    result = var36 | (var23 + var32 - (var33 & (arg13 & ((var37 - (var20 - var35 | var29)) & var33)) - var15) - var26)
    return result
def func3(arg5, arg6):
    var7 = 310657746 ^ arg6 + -1554186877 + -1338391562 ^ ((((arg6 & (-132 ^ arg5)) - arg5) | 476) | -822 - -1356976178)
    var8 = (arg6 - -817 - ((var7 + -234 | (((var7 - ((589 ^ arg6) + (var7 & -953932493 & arg6 ^ arg5) ^ -130 & arg6)) | arg5) + var7 + -899 ^ -357 - 1766544402)) ^ arg5) & -792 + var7) & arg5
    var9 = var8 ^ arg6
    var10 = var8 & -986
    var11 = var10 ^ (921 | var8)
    result = var8 ^ var8
    return result
def func1(arg1, arg2):
    result = arg1 & (arg2 | (-200 & -1197006156)) + (arg1 - arg1 ^ -46 - -474) + arg2
    return result
def func6(arg48, arg49):
    def func7(acc, rest):
        var70 = func8(-9, -7)
        if acc == 0:
            return var70
        else:
            result = func7(acc - 1, var70)
            return result
    result = func7(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 0'
    print 'func_number: 2'
    print 'arg_number: 3'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
    print 'prog_size: 5'
    print 'func_number: 11'
    print 'arg_number: 77'
    for i in xrange(25000):
        x = 5
        x = func2(x, i)
        print x,