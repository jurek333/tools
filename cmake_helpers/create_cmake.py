import sys
import os


def getProject():
    projDir = os.getcwd()
    projName = os.path.basename(projDir)
    return (projName, projDir)

def writeFileHeader(f):
    f.write("cmake_minimum_required(VERSION 3.6)\n")
    f.write("project(%s)\n"%(projName))
    f.write("\n")

def exutables(f):
    f.write("add_executable(%s "%(projName))
    for dirpath, dirname, filename in os.walk(projDir):
        rp = os.path.relpath(dirpath, projDir)
        if "build" in rp:
           continue 
        for name in filename:
            if name.endswith((".cpp",".c",".cc",".c++",".cxx")):
                p = os.path.join(dirpath, name)
                relative = os.path.relpath(p, projDir) 
                print(" [c] %s"%(relative))
                f.write("%s "%(relative))
    f.write(")")
    
def main():
    cmakeFile = projDir + '\CMakeLists.txt'
    with open(cmakeFile, "w") as f:
        writeFileHeader(f)
        exutables(f)

projName, projDir = getProject()
print("+------------")
print("|    Project:\t%s"%(projName))
print("|    Path:\t%s"%(projDir))
print("+------------")
main()
