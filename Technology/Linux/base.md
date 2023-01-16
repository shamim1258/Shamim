# Linux

### Commands

**Help :**
- `man`
   - Used to display the user manual of any command.
   - Example `man ls`

**Path :**
- To get present working directory path :  
```pwd```  

**Directory and Files :**
-  `ls`
   -  To get the list of files and directory in plain text format without showing much information. We can use this command with below optional arguments also.
   -  `ls -r` - to print files in reverse order i.e. descending.
   -  `ls -l` - list the permissions of the files and directories as well as other attributes such as folder names, file and directory sizes, and modified date and time.
   -  `ls -t` - sorts the file by modification time, showing the last edited file first.
   -  `ls -a` - to list all files including hidden files which start with dot.
   -  `ls -R` - to display the directory tree of files and folders.
-  `grep`
   -  The grep filter searches a file for a particular pattern of characters, and displays all lines that contain that pattern. The pattern that is searched in the file is referred to as the regular expression (grep stands for global search for regular expression and print out).
   -  Example `grep "Order" *` to search files in all files and folder

**Search :**
- To find file with file name as testfile.txt in current and its sub-directories.
```find . -name thisfile.txt```

**Process :**
-  `ps`
   -  To get all running process in static format
-  `top`
   -  To get all running process in dynamic format

**Customize :**
-  `alias`
   -  To create alias of a command example `alias="ls -l"`
-  `unalias`
   -  To remove the alias example `unalias ls`
