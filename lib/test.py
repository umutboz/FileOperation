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

#eger bir path belirlenmis ise
#op = FileOperation("/Users/umut/Desktop/Architecture/CodeGenerationCore/lib")
#run path kullanılmak isteniyorsa
op = FileOperation()

#init de verilen default path üzerine dosya oluşturulur.
#op.createFile(fileName="test.swift",content="hello")

#path param ile verilen path üzerine dosya oluşturulur.
#op.createFileWithPath(path="lib/test",fileName="test.swift",content="hello")


#init de verilen default path üzerine klasör oluşturulur.
#op.createFolder(folderName="hello/1")

#loglar kapali artik
Environment.Shared().online()



#print(MESSAGE.ERROR)
#print(DEV_ENV.LOCAL)
#print(CODE.SLASH)


#log samples
#Log.i(message=MESSAGE.INFO)
#Log.s(MESSAGE.SUCCESS)
#Log.e(MESSAGE.ERROR)
