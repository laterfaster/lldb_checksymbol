# lldb_checksymbol
## Customize the debugging command for LLDB

## Introduction

### Dependencies:

lldb, python-lldb

### Preparations:
  
Extract the project file to your `~/`  

### checksymbol command usage: 

(lldb) `checksymbol address n`

**Just accepts two parameters**: memory **address** and the number of bytes **n**, and then prints the following **n** bytes of memory **address**, contents and descriptions of them on the terminal.

## 使用说明：

### 依赖

lldb, python-lldb

### 准备工作：

将项目文件解压至 `~/`

### checksymbol命令的用法:

(lldb) `checksymbol address n`

**只接受两个参数**：内存地址 **address** 和字节数 **n** ，然后在终端上输出内存地址 **address** 接下来 **n** 字节的内存地址，内存内容及其描述。

## Reference:

https://blog.mengy.org/extend-gdb-with-python/#more
