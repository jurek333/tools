import os
import errno
import subprocess

def getProject():
    projDir = os.getcwd()
    projName = os.path.basename(projDir)
    return (projName, projDir)

projName, projDir = getProject()

def createDir(name):
    buildDir = os.path.join(projDir, name)
    if os.path.exists(buildDir):
        return buildDir
    
    try:
        os.makedirs(buildDir)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
            
    return buildDir

def main():
    print("+-------------------------------------------")
    bdir = createDir("build")
    print("+- moving to %s"%(bdir))
    os.chdir(bdir)
    print("+- run cmake ..")
    operation = subprocess.run(["cmake", ".."], stdout=subprocess.PIPE)
    print(operation.stdout.decode("cp852"))
    print("+- run cmake --build ")
    cmd = ["cmake", "--build", ".", "--config", "Release"]
    operation = subprocess.run(cmd, stdout=subprocess.PIPE)
    print(operation.stdout.decode("cp852"))

main()
