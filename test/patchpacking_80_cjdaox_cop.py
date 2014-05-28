# -*- coding: utf-8 -*-
import re
import os
import shutil
import zipfile
def pcjd(projectname="c", patchreadmefilename="cjdaox_test_351_to_364.txt", jarEnable="n"):
    #f = open('D:\\tmp\\changeLog.txt', 'r')
    #patt = re.compile("M /.+")
    patt2 = re.compile("[M|A] /.+")
    #for l1 in f:
    #  print l1,
    #  fd = patt.findall(l1.strip())
    #  if fd != []:
    #   print(fd)
     #  print len(fd)
    counter = 1
    #patchdir = "D:\\tmp\\"
    patchdestdir = "E:\\patches\\"
    appendwords = "_test"
    #print appendwords
    patchsubdir = patchreadmefilename.replace(".txt",appendwords)#This should be parameter##"version1.0.0.7"
    #print patchsubdir
    readmefile = patchdestdir + patchreadmefilename
    readmeforpublish = patchdestdir + "readmeforpublish.txt"
        
    f = open(readmefile, 'r')
    f_forpub = open(readmeforpublish, 'w')
    if jarEnable == "y" or jarEnable == "Y":
        f_forpub.write("请更新以下文件(注意含jar包)："+"\nfis_svr.jar\n")
    else:
        f_forpub.write("请更新以下文件："+"\n")
    
    cntls = f.readlines()
    #print len(cntls)
    src = ""
    if os.path.exists(patchdestdir+ patchsubdir) != True:
      os.mkdir(patchdestdir+ patchsubdir)
      print "\'"+patchdestdir+ patchsubdir+"\'" + " is created!"
    else:
      print '>>>>>>>>"' + patchdestdir+ patchsubdir + '"<<<<<<' + " exists!!!!"
    dest = patchdestdir+ patchsubdir
    print dest

    if projectname == "c" or projectname == "C":
        lead = "F:\\Workspaces\\fis_cjdaox80"#This should be parameter#
    elif projectname == "m" or projectname == "M":
        lead = "F:\\Workspaces\\fis_cjdao_mid7_80"#This should be parameter#
    elif projectname == "mv1" or projectname == "MV1" or projectname == "mV1" or projectname == "Mv1":
        lead = "F:\\Workspaces\\fis_cjdao_mid7_v1_80"#This should be parameter#
    elif projectname == "h" or projectname == "H":
        lead = "F:\\Workspaces\\fis_huix80"#This should be parameter#
    elif projectname == "p" or projectname == "P":
        lead = "F:\\Workspaces\\fis_cjdao_cop_80"#This should be parameter#
    elif projectname == "l" or projectname == "L":
        lead = "F:\\Workspaces\\LCQ_tag_lcq"
#        lead = "F:\\Workspaces\\LCQ_trunk_lcq"#This should be parameter#LCQ_V0.1.5_V0.1.6.txt
    
    myElement = []
    mySet = set(myElement)
    for element in cntls:
           fd2 = patt2.findall(element)
           #print element
    #       print len(fd2)
           if len(fd2) > 0:
             #print fd2
             strold = fd2[0][2:]
             print "strold ===>  "+strold
             strold2 = strold.replace("/","\\")
             strold2 = strold2.replace("src","webroot\\WEB-INF\\classes")
             strold2 = strold2.replace(".java",".class")
             strold2 = strold2.replace("\\trunk\\fis_cjdao_cop","")
             strold2 = strold2.replace("\\trunk\\fis_cjdaox","")
             strold2 = strold2.replace("\\trunk\\fis_huixiangx","")
             strold2 = strold2.replace("\\trunk\\fis_cjdao_mid7_v1","")#The order between this line and the next one MUST NOT BE CHANGED! 此行和下面一行顺序不能颠倒
             strold2 = strold2.replace("\\trunk\\fis_cjdao_mid7","")#The order between this line and the next one MUST NOT BE CHANGED! 此行和下面一行顺序不能颠倒
             strold2 = strold2.replace("\\trunks\\LCQ","")#svn://192.168.1.80/LCQ/trunks/LCQ
             
             #print "strold2 ===>  "+strold2
             strTemp = strold2.replace("\\","/")
             mySet.add(strTemp)
             #f_forpub.write(strold2+"\n")
             #following is the file name
     #        print strold2
             if len(strold2)>0:
               src = lead + strold2
               #print src
               if os.path.isfile(src) == True:
                 open(src,'r')
                 shutil.copy2(src, dest+"\\.")
                 counter = counter + 1
                 #print("SRC=======>>>>> "+src)
    #         os.system("copy " + src +" "+ dest)
    
    strTmp = str(mySet)
    #print "here ::::"
    #print mySet
    myList=[]
    for item in mySet:
        myList.append(item)
    myList.sort()    
    print "Check here: "
#    for element in myList:
 #       print element
    strTmp = str(myList)
    #print "B4 replace"+strTmp
    strTmp = strTmp.replace(",","\r\n")
    strTmp = strTmp.replace("[","")
    strTmp = strTmp.replace("]","")
    strTmp = strTmp.replace("'","")
    strTmp = strTmp.replace(" ","")
    print strTmp
    f_forpub.write(strTmp+"\n")
    f.close()
    f_forpub.close()
    #print "moving the readme file>>"+ readmefile+" to " + dest+"\\."
    #print "moving the readmeforpublish file>>"+ readmeforpublish+" to " + dest+"\\."
    print "There\'s " + str(counter) +" files in the patch."
    print readmeforpublish
    print readmefile
    shutil.copy(readmefile,dest+"\\.")
    shutil.copy(readmeforpublish,dest+"\\readme.txt")

    if jarEnable == "y" or jarEnable == "Y":
        #print "jar file importing..."
        #time.sleep(2)
        #copy jar file to desitination
        shutil.copy(lead + "\\webroot\\WEB-INF\\lib\\fis_svr.jar",dest+"\\.")
        #print "importing jar file done!"        
    
    print dest
    print patchsubdir
    os.chdir(patchdestdir)
    print ("winrar a " + patchdestdir+patchsubdir+".rar " + patchsubdir+"\*.*")
    os.system("winrar a " + patchdestdir+patchsubdir+".rar " + patchsubdir+"\*.*")
    print os.getcwd()


        
if __name__ == "__main__":
  import patchpacking_80_cjdaox_cop
  import os
  pcjd("cjdaox_test_351_to_364.txt")
