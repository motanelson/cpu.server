
print("\033c\033[43;30m\ngive me a cube size? ")
filesvar="""0,0,0,1,0,0
1,0,0,1,1,0
1,1,0,0,1,0
0,1,0,0,0,0
0,0,1,1,0,1
1,0,1,1,1,1
1,1,1,0,1,1
0,1,1,0,0,1
0,0,0,0,0,1
1,0,0,1,0,1
1,1,0,1,1,1
0,1,0,0,1,1"""

i=input()
print("\033[43;30m\ngive me a output file name? ")
filename=input()
filesvar=filesvar.replace("1",i)
f1=open(filename,"w") 
f1.write(filesvar)
f1.close()