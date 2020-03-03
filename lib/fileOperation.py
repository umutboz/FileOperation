#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
## FileOperation
############################################################
## Author: Umut Boz
## Copyright (c) 2020, OneframeMobile, KoçSistem
## Email: oneframemobile@gmail.com
############################################################
## Version: 0.1.0
############################################################

# Built-in/Generic Imports
import os
import sys

# Own modules
from abstract import Base
from enums import CODING
from enums import MESSAGETYPE

class FileOperation(Base):
    _path = ""
    def __init__(self, path=None):
        Base.__init__(self)
        self._path = path

    def getPath(self):
        #path has not chars and is none
        if self._path == None or not str(self._path).strip():
            return os.getcwd()
        else:
            return self._path

    def createFile(self,fileName, content):
        filePath = self.getPath() + CODING.SLASH + fileName
        try:
            filePath = open(filePath, "w")
            filePath.write(content)
            filePath.close()
            Base.log(self,message = "FileOperation " + "createFile : " + str(filePath) + " \ncontent : \n" + content,
             messageType=MESSAGETYPE.INFO)
        except OSError as e:
            Base.log(self,message = "FileOperation " + "createFile : " 
            + " \error : \n" + str(e), messageType=MESSAGETYPE.ERROR)

    def createFileWithPath(self,path,fileName, content):
        filePath = self.getPath() + CODING.SLASH + path + CODING.SLASH + fileName
        try:
            filePath = open(filePath, "w")
            filePath.write(content)
            filePath.close()
            Base.log(self,message = "FileOperation " + "createFileWithPath : " + 
            str(filePath) + " \ncontent : \n" + content, messageType=MESSAGETYPE.INFO)
        except OSError as e:
            Base.log(self,message = "FileOperation " + "createFileWithPath : " 
            + " \error : \n" + str(e), messageType=MESSAGETYPE.ERROR)

    def createFolder(self, folderName):
        folderPath = self.getPath() + CODING.SLASH + folderName
        try:
            if not os.path.isdir(folderPath):
                os.makedirs(folderPath)
                Base.log(self,message = "FileOperation " + "createFolder : " + 
                folderPath + "\n", messageType=MESSAGETYPE.INFO)
            else :
                Base.log(self,message = "FileOperation " + "createFolder : " + 
                folderPath + "\n already path", messageType=MESSAGETYPE.INFO)
        except OSError as e:
            Base.log(self,message = "FileOperation " + "createFileWithPath : " + " \error : \n" + 
            str(e), messageType=MESSAGETYPE.ERROR)

    def appendFile(self, fileName, content,isTruncate=False):
        filePath = self.getPath() + CODING.SLASH + fileName
        try:
            with open(filePath, "a+") as f:
            # f.seek(0)
                if isTruncate:
                    f.truncate()
                f.write(content)
                f.close()
                Base.log(self,message = "FileOperation " + "appendFile : " + 
                    filePath + "\n", messageType=MESSAGETYPE.INFO)
        except OSError as e:
            Base.log(self,message = "FileOperation " + "appendFile : " + " \error : \n" + 
            str(e), messageType=MESSAGETYPE.ERROR)
    
    #has path valid and exist return true
    def isExist(self,path):
        if os.path.exists(path):
            return True
        else:
            return False

    #for file of content is get
    def getFileContentWithPathx(self,filePath):
        print(filePath)
        if self.isExist(filePath):
            fileContent = ""
            data = open(filePath, "r").read(20000)
            fileContent = data.strip()
            return fileContent
        else:
            Base.log(self,message = "FileOperation " + "getFileContent : " + filePath +
                     "\n has not found file", messageType=MESSAGETYPE.INFO)

    #for content of file is get with path 
    def getFileContent(self,fileName):
        filePath = self.getPath() + CODING.SLASH + fileName
        return self.getFileContentWithPath(filePath)
    
    #for content of file is get
    def getFileContentWithPath(self,filePath):
        print(filePath)
        global content
        if self.isExist(filePath):
            print("urn")
            with open(filePath, "r") as data:
                content = data.read()
            return content
        else:
            Base.log(self,message = "FileOperation " + "getFileContent : " + filePath +
                     "\n has not found file", messageType=MESSAGETYPE.INFO)
            return ""