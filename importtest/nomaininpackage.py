
from .models import *
print(COUNT) #ImportError: attempted relative import with no known parent package

#包内不能有__name__==__main__，即不能作为程序的入口，否则导入就会失败。
#包的名字不能以数字开头