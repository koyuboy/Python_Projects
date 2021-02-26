def func1(arg1, arg2):
    var7 = func2(arg2, arg1)
    var27 = var10(arg2, arg1)
    var28 = func13()
    var29 = var7 ^ (-325 + var27)
    var30 = var7 | (arg1 - 1698819157)
    var31 = var29 | 1964618555 + var29 & -511868226
    var32 = (var30 ^ arg2) | var30 & var30
    var33 = var7 + var29 | var27
    var34 = var30 + (var29 ^ -499 - var29)
    var35 = arg1 - 1233143591
    var36 = (var28 + (var31 ^ var34)) + var33
    var37 = var30 + var31
    var38 = var30 + var27 + 253 - -1445645149
    var39 = var30 - (-1662114178 ^ 521) | var32
    result = var37 ^ var30
    return result
def func13():
    func11()
    result = len(range(11))
    func12()
    return result
def func12():
    global len
    del len
def func11():
    global len
    len = lambda x : 9
def func5(arg11, arg12):
    var17 = func6(arg12, arg11)
    if var17 < var17:
        var22 = class7()
    else:
        var22 = class9()
    for var23 in range(39):
        var24 = var22.func8
        var24(arg11, arg11)
    var25 = 301780265 & 823692732 ^ 689
    var26 = 10 - var17
    result = var26 | (((1669576828 & arg12) + 548) & arg11 | -980) | (((415 + (1637323550 + var17) + var17) + 2017167303) & arg12)
    return result
class class9(object):
    def func8(self, arg20, arg21):
        result = arg20 ^ 2067725594 ^ -937204459
        return result
class class7(object):
    def func8(self, arg18, arg19):
        result = (370970206 ^ 1 & 1 - arg19) & -1
        return result
def func6(arg13, arg14):
    var15 = 0
    for var16 in range(9):
        var15 += (arg13 | -7) & var16
    return var15
def func4():
    closure = [-2]
    def func3(arg8, arg9):
        closure[0] += func5(arg8, arg9)
        return closure[0]
    func = func3
    return func
var10 = func4()
def func2(arg3, arg4):
    var5 = 0
    for var6 in xrange(12):
        var5 += var6 ^ var5 | arg3
    return var5
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 14'
    print 'arg_number: 40'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,