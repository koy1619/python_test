# -*- coding: cp936 -*-
import patchpackingpro
import patchpacking_80_mid7
import patchpacking_80_mid7_v1
import patchpacking_80_cjdaox
import patchpacking_80_huixiangx
import patchpacking_80_cjdaox_cop
import os
#import time
        
if __name__ == "__main__":
    import callpap
    import os
    projectname = raw_input("��������Ŀ����\nc \t= cjdaox; \nm \t= cjdao_mid7;\nmv1 \t= cjdao_mid7_v1;\nh \t= cjdao_huixiangx;\np \t= cjdaox_cop; \nl \t= LCQ; \n��ѡ��:\n")
    filename = raw_input("�����벹���б��ļ�����:\n")
    jarEnable = raw_input("�Ƿ���jar��: y/n ?\n")
    print jarEnable

    #if projectname == "c" or projectname == "C":
     #   patchpacking_80_cjdaox.pcjd(filename)
    #elif projectname == "m" or projectname == "M":
     #   patchpacking_80_mid7.pmid7(filename)
    #elif projectname == "mv1" or projectname == "MV1" or projectname == "mV1" or projectname == "Mv1":
     #   patchpacking_80_mid7_v1.pmid7(filename)
    #elif projectname == "h" or projectname == "H":
     #   patchpacking_80_huixiangx.pmid7(filename)
    #elif projectname == "p" or projectname == "P":
    patchpacking_80_cjdaox_cop.pcjd(projectname,filename,jarEnable)        
    print "pause"

    
print "OVER"
