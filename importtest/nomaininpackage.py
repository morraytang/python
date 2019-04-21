
from .models import *
print(COUNT) #ImportError: attempted relative import with no known parent package

#包内不能有__name__==__main__，即不能作为程序的入口，否则from .models 导入就会失败,应为解释器会把其当做为顶级包。
#有一种替代方案就是，不要用相对导入，用绝对导入  from importtest.modules import * 这样还是可以的
#包的名字不能以数字开头