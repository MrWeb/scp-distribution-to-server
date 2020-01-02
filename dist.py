#!/usr/bin/env python
import subprocess
import paths

rsync_cmd = "scp -pr dist/. " + paths.ssh + ":" + paths.path

subprocess.run(rsync_cmd, shell=True)