# FileOperation
File Operations Libraries for Python

## import package example


```python
from fileOperation import FileOperation
```

## using example
```python
op = FileOperation()

#get content of file with relative Path
print(op.getFileContentWithPath(filePath=path + CODE.SLASH + fileName))

#get content of file
print(op.getFileContent(fileName=fileName))
print(op.getFileContent(fileName="lib/test.py"))

#init de verilen default path üzerine dosya oluşturulur.
op.createFile(fileName=fileName,content="hello")

#path param ile verilen path üzerine dosya oluşturulur.
op.createFileWithPath(path="lib",fileName="test.swift",content="hello")


#init de verilen default path üzerine klasör oluşturulur.
op.createFolder(folderName="hello/1")

#path is valid
print(op.isExist("/Users/umut/Desktop/Architecture/CodeGenerationCore/lib"))

#append file add content
op.appendFile(fileName="test.swift",content="\nworld")
