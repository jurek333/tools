#!Actually works only on Windows ;)
# A simple environment switcher by Gynvael Coldwind (assume MIT license)
# Before first usage:
#   - Make sure to change/fix all the paths.
#   - Probably the code won't work anyway. Happy debugging!
# ---------------------------------------------------------------------------
# My modification added :)
#
import sys
#from winapicon import *
from glob import glob

COMPILERS = []

def usage():
	print "-=- Available compilers/interpreters -=-"
	print "ID               Description"

	global COMPILERS
	COMPILERS = sorted(COMPILERS, key=lambda x: x[0])

	for cid, cname, _ in COMPILERS:
		print "%-16s" % cid,
		print "%-s" % cname

	print "usage: switch <id>"

def write_bat_script(s=""):
	with open("C:\\Users\\Maciej\\tools\\switch-worker-output.bat", "w") as f:
		f.write("@echo off\r\n")
		f.write(s)

def populate_python():
	for path in glob("D:\\Python*"):
		tmp = path.replace("Python", "")
		ver = tmp.split("\\")[1]
		ver = "%c.%c"%(ver[0], ver[1])
		bits = "64"
		cid = "py%s-%s" % (ver, bits)
		cname = "Python %s (%s bits)" % (ver, bits)

		COMPILERS.append((cid, cname, "set PATH=%s;%s\\Scripts;%%PATH%%" % (path, path)))    

def populate_clang():
	path = "C:\\Program Files\\LLVM" 
	ver = "6.0.0"
	bits = "64"
	cid = "clang%s-%s" % (ver, bits)
	cname = "LLVM clang %s (%s bits)" % (ver, bits)

	call_cmd = '"C:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\Community\\VC\\Auxiliary\\Build\\vcvarsx86_amd64.bat"',

	COMPILERS.append((cid, cname, """
	call %s
	set PATH=%s\\bin;%%PATH%%
	set CPATH=C:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\Community\\VC\\Auxiliary\\VS\\include;C:\\Program Files (x86)\\Windows Kits\\10\\Include\\10.0.16299.0\\ucrt;C:\\Program Files (x86)\\Windows Kits\\10\\Include\\10.0.16299.0\\um;C:\\Program Files (x86)\\Windows Kits\\10\\Include\\10.0.16299.0\\shared;C:\\Program Files (x86)\\Windows Kits\\10\\Include\\10.0.16299.0\\winrt;C:\\Program Files (x86)\\Windows Kits\\NETFXSDK\\4.6.1\\Include\\um;C:\\Program Files\\LLVM\\include;
	""" % (call_cmd, path)))

def populate_gcc():
	for path in glob("d:\\bin\\gcc\\*"):
		tmp = path.split("\\")[-1]
		arch, ver, threads, excp, runtime, rev = tmp.split("-")

		bits = {
			"i686": "32",
			"x86_64": "64",
		}[arch]

		cid = "gcc%s-%s" % (ver, bits)
		cname = "GCC %s (%s bits, %s threads, %s excp)" % (
				ver, bits, threads, excp
		)

		COMPILERS.append((cid, cname, """
		set PATH=%s\\mingw%s\\bin;%%PATH%%
		""" % (path, bits)))

def populate_msvc():
	COMPILERS.extend([
		("msvc17-32", "Microsoft C++ 2017 (32 bits)",
		'call "C:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\Community\\VC\\Auxiliary\\Build\\vcvars32.bat"'),
		("msvc17-64", "Microsoft C++ 2017 (64 bits)",
		'call "C:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\Community\\VC\\Auxiliary\\Build\\vcvars64.bat"'),
	])

def populate_compilers():
	populate_python()
	populate_clang()
	#populate_gcc()
	populate_msvc()

def main():
	populate_compilers()

	if len(sys.argv) == 1:
		usage()
		write_bat_script()
		return 1

	selected_cid = sys.argv[1].strip()
	for cid, cname, cscript in COMPILERS:
		if cid != selected_cid:
			continue

		print "Switching to:",
		print cname
		write_bat_script(cscript)
		return 0

	print "Error: %s not found" % selected_cid
	write_bat_script()
	return 1

if __name__ == "__main__":
	sys.exit(main())

