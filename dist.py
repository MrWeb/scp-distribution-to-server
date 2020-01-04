#!/usr/bin/env python
import subprocess
import paths

rsync_cmd = "scp -pr " + paths.build_folder + "/. " + paths.ssh + ":" + paths.path

subprocess.run(rsync_cmd, shell=True)
