#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
## test
############################################################
## Author: Umut Boz
## Copyright (c) 2020, OneframeMobile, KoçSistem
## Email: oneframemobile@gmail.com
############################################################
## Version: 0.1.0
############################################################


from enums import MessageType

from enums import CodeLine
from log import Log
from fileOperation import FileOperation
from environment import Environment


MESSAGE = MessageType()

CODE = CodeLine()

path = "/Users/umut/Desktop/Architecture/CodeGenerationCore"
fileName = "test.swift"
#eger bir path belirlenmis ise
#op = FileOperation("/Users/umut/Desktop/Architecture/CodeGenerationCore/lib")
#run path kullanılmak isteniyorsa
op = FileOperation()

#get content of file with relative Path
#print(op.getFileContentWithPath(filePath=path + CODE.SLASH + fileName))

#get content of file
#print(op.getFileContent(fileName=fileName))
print(op.getFileContent(fileName="lib/test.py"))

#init de verilen default path üzerine dosya oluşturulur.
#op.createFile(fileName=fileName,content="hello")

#path param ile verilen path üzerine dosya oluşturulur.
#op.createFileWithPath(path="lib",fileName="test.swift",content="hello")


#init de verilen default path üzerine klasör oluşturulur.
#op.createFolder(folderName="hello/1")

#path is valid
#print(op.isExist("/Users/umut/Desktop/Architecture/CodeGenerationCore/lib"))

#append file add content
#op.appendFile(fileName="test.swift",content="\nworld")


#loglar kapali artik
#Environment.Shared().online()



#print(MESSAGE.ERROR)
#print(DEV_ENV.LOCAL)
#print(CODE.SLASH)


#log samples
#Log.i(message=MESSAGE.INFO)
#Log.s(MESSAGE.SUCCESS)
#Log.e(MESSAGE.ERROR)
