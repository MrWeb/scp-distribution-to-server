#!/usr/bin/env python
import subprocess
import paths

rsync_cmd = 'tar czfvv - '+ paths.build_folder +' | ssh ' + paths.ssh + ' "(cd ' + paths.server_path + ' && rm -rf ' + paths.build_folder + ' ; cat > build.tar.gz && tar -xzf build.tar.gz && rm build.tar.gz)"'

subprocess.run(rsync_cmd, shell=True)
