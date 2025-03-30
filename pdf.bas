
dim t as integer=1
dim a as string=""
dim aa as string=""
dim ccc1 as integer
dim ccc as integer
color 0,6
cls 

print "creat..."
input "file to open .pdf file ? ",a
t=1
ccc=1
aa=""
if instr(a,".txt")>0 then
    shell "notepad /p "+ a
else
    shell "start "+ a+ " /p "
end if