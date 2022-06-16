# Python os Module

## 1. access(path,mode)

This method uses the real uid/gid to test for access to a path. If access is allowed, it returns True.

Else, it returns False. The first argument is the path; the second is the mode.

The mode can take one of four values:

os.F_OK  — Found
os.R_OK  — Readable
os.W_OK  — Writable
os.X_OK  — Executable

```python
>>> os.chdir(path)
>>> os.access('Today.txt',os.R_OK)
 ```
 > return True if readable


 
##  2. chmod(path,mode)
This Python os Module alters the mode of the path to the passed numeric mode.

The mode may be on of the following values(or a bitwise OR combination of them):

stat.S_ISUID − Set user ID on execution
stat.S_ISGID − Set group ID on execution
stat.S_ENFMT – Enforced record locking
stat.S_ISVTX – After execution, save text image
stat.S_IREAD − Read by owner
stat.S_IWRITE − Write by owner
stat.S_IEXEC − Execute by owner
stat.S_IRWXU − Read, write, and execute by owner
stat.S_IRUSR − Read by owner
stat.S_IWUSR − Write by owner
stat.S_IXUSR − Execute by owner
stat.S_IRWXG − Read, write, and execute by group
stat.S_IRGRP − Read by group
stat.S_IWGRP − Write by group
stat.S_IXGRP − Execute by group
stat.S_IRWXO − Read, write, and execute by others
stat.S_IROTH − Read by others
stat.S_IWOTH − Write by others
stat.S_IXOTH − Execute by others

```python
>>> import stat
>>> os.chmod('Today.txt',stat.S_ISVTX)
 ```

 ##  3. fchown(fd,uid,gid)
 fchown() alters the owner and the group id of the file specified by fd to the numeric uid and gid.

Setting an id to -1 leaves it unchanged.

Sample usage:

```python
>>> fd = os.open( "/tmp", os.O_RDONLY )
>>> os.fchown( fd, 100, -1)
>>> os.fchown( fd, -1, 50)
>>> print "Changed ownership successfully!!"
>>> os.close( fd )
 ```
 
 ##  4. link(src,dst)
 link() will create a hard link that points to an src named dst.

You can do this when you want to create a copy of an existing file.

Sample usage:

```python
>>> path = "/var/www/html/Today.txt"
>>> fd = os.open( path, os.O_RDWR )
>>> os.close( fd )
>>> dst = "/tmp/Today.txt"
>>> os.link( path, dst)
 ```
 
 ## 5. listdir(path)
```python
>>> path = "/var/www/html/"
>>> dirs = os.listdir( path )
>>> for file in dirs:
print(file)
 ```
 
 ## 6. lstat(path)
 Like fstat(), lstat() returns information about a file, but does not follow symbolic links.

lstat is an alias for fstat() on those platforms that do not support symbolic links, for instance, Windows.

It returns the following structure:

st_dev − ID of device containing file
st_ino − inode number
st_mode – protection
st_nlink − number of hard links
st_uid − user ID of owner
st_gid − group ID of owner
st_rdev − device ID (if special file)
st_size − total size, in bytes
st_blksize − blocksize for filesystem I/O
st_blocks − number of blocks allocated
st_atime − time of last access
st_mtime − time of last modification
st_ctime − time of last status change
Sample usage:

```python
>>> path = "/var/www/html/Today.txt"
>>> fd = os.open( path, os.O_RDWR)
>>> os.close( fd )
>>> info = os.lstat(path)
>>> print(f"File Info: {info}")
>>> print(f"UID of the file: {info.st_uid}")
>>> print(f"GID of the file: {info.st_gid}")
 ```
 
  ## 7. mkdir(path[, mode])
mkdir() Python os Module creates a directory ‘path’ with the numeric mode ‘mode’. Some systems ignore mode.

But where used, it masks out the current umask value first.
Default mode=0777 (octal).

Sample usage:

```python
>>> path = "/tmp/home/monthly/daily/hourly"
>>> os.mkdir( path, 0755 )
 ```

 ## 8. makedirs(path[, mode])
 makedirs() creates a directory recursively. This way, it is like mkdir().

However, it mandates that all intermediate-level directories contain the leaf directory.

Sample usage:
```python
>>> path = "/tmp/home/monthly/daily"
>>> os.makedirs( path, 0755 )
 ```
 
 ## 9. remove(path)

remove() removes the specified file path. If that path is a directory, it raises an OSError.

Sample usage:
```python
>>> print(f"The dir is: {os.listdir(os.getcwd())}")
>>> os.remove("aa.txt")
>>> print(f"The dir after removal of path: {os.listdir(os.getcwd())}")
 ```

  ## 10. removedirs(path)
This Python os Module will remove directories recursively.

And if we successfully remove the leaf directory, it attempts to successively remove every parent directory displayed in that path.

Sample usage:
```python
>>> print(f"The dir is: {os.listdir(os.getcwd())}")
>>> os.removedirs("/tutorialsdir")
>>> print(f"The dir after removal is: {os.listdir(os.getcwd())}")
 ```

  ## 11. rename(src,dst)
  rename() renames a file or directory. If the destination is a file or a directory that already exists, it raises an OSError.

```python
>>> print(f"The dir is: {os.listdir(os.getcwd())}”)
>>> os.rename("tutorialsdir","tutorialsdirectory")
>>> print(“Successfully renamed”)
>>> print(f"The dir is: {os.listdir(os.getcwd())}")
 ```

  ##  12. renames(old,new)
renames() Python os Module renames directories and files recursively.

It is like os.rename(), but it also moves a file to a directory, or a whole tree of directories, that do not already exist.

Sample usage:

```python
>>> print("Current directory is: { os.getcwd()}")
>>> print("The dir is: { os.listdir(os.getcwd())}")
>>> os.renames("aa1.txt","newdir/aanew.txt")
>>> print("Successfully renamed”)
>>> print(f"The dir is: {os.listdir(os.getcwd())}")
 ```

  ## 13. rmdir(path)
Python os Module rmdir() removes the directory path specified. If the directory isn’t empty, however, it raises an OSError.

Sample usage:
```python
>>> print(f"the dir is: { os.listdir(os.getcwd())}")
>>> os.rmdir("mydir")
>>> print(f"the dir is: { os.listdir(os.getcwd())}"
 ```