import datetime
# import sys
# import struct
import shutil
import os

Import("env")

def copy_generated(source, target, env):
	bootloader_name = "./Generated/WisBlock_SENS_V%s.%s.%s_bootloader.bin" % (version_tag_1,version_tag_2,version_tag_3)
	partition_name = "./Generated/WisBlock_SENS_V%s.%s.%s_partitions.bin" % (version_tag_1,version_tag_2,version_tag_3)

	if os.path.isfile(bootloader_name):
		try:
			os.remove(bootloader_name)
		except:
			print('Cannot delete '+bootloader_name)
	if os.path.isfile(partition_name):
		try:
			os.remove(partition_name)
		except:
			print('Cannot delete '+partition_name)

	shutil.copy2("./.pio/build/rak3112/bootloader.bin", bootloader_name)
	shutil.copy2("./.pio/build/rak3112/partitions.bin", partition_name)

	print("===================================")
	print("Flash files are in folder Generated")
	print("===================================")

my_flags = env.ParseFlags(env['BUILD_FLAGS'])
defines = {k: v for (k, v) in my_flags.get("CPPDEFINES")}

build_tag = "RAK_"

version_tag_1 = defines.get("SW_VERSION_1")
version_tag_2 = defines.get("SW_VERSION_2")
version_tag_3 = defines.get("SW_VERSION_3")
build_date = datetime.datetime.now().strftime('%Y.%m.%d.%H.%M.%S')

# env.Replace(PROGNAME="../../../Generated/WisBlock_SENS_V%s.%s.%s_%s" % (version_tag_1,version_tag_2,version_tag_3,build_date))
env.Replace(PROGNAME="../../../Generated/WisBlock_SENS_V%s.%s.%s" % (version_tag_1,version_tag_2,version_tag_3))
# Add callback after .bin file was created
env.AddPostAction("$PROGPATH", copy_generated)


