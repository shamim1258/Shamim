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
      -  Output `-rwxrw-r-- 1 owner group size modification_date file_or_folder_name` where first character is `-` for file and `d` for directory.
   -  `ls -t` - sorts the file by modification time, showing the last edited file first.
   -  `ls -a` - to list all files including hidden files which start with dot.
   -  `ls -R` - to display the directory tree of files and folders.
-  `grep`
   -  The grep filter searches a file for a particular pattern of characters, and displays all lines that contain that pattern. The pattern that is searched in the file is referred to as the regular expression (grep stands for global search for regular expression and print out).
   -  Example `grep "Order" *` to search files in all files and folder
-  `chmod`
   -  To change the file permission - read(r), write(w) and execcute(x) for user or owner(u), group(g) and other(o) by using operator +,- and =.
   -  Example `chmod u+rwx filename`.
   -  To change permission for all its sub-directories and files use `-R` example `chomod -R +rwx .`
   -  Permission calculation
^
    Numeric	Symbolic	Permission
    0	---	none
    1	--x	execute only
    2	-w-	write only
    3	-wx	write and execute
    4	r--	read only
    5	r-x	read and execute
    6	rw-	read and write
    7	rwx	read, write, and execute
^
**Search :**
- To find file with file name as testfile.txt in current and its sub-directories.
```find . -name thisfile.txt```

**Process :**
-  `ps`
   -  To get all running process in static format
-  `top`
   -  To get all running process in dynamic format

**Service :**
-  `systemctl`
   -  To manage services and reboot or shutdown system.

**Customize :**
-  `alias`
   -  To create alias of a command example `alias="ls -l"`
-  `unalias`
   -  To remove the alias example `unalias ls`
