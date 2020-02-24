# FileOperation
File Operations Libraries for Python

## import package example


```python
from fileOperation import FileOperation
```

## using example
```python
op = FileOperation()

op.createFile(fileName="test.swift",content="hello")

op.createFileWithPath(path="lib/test",fileName="test.swift",content="hello")

op.createFolder(folderName="hello/1")

#all information disable, default env is debug

#should be import Environment package
from environment import Environment

Environment.Shared().online()

