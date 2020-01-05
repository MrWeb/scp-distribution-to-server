#!/usr/bin/env python
import subprocess

# Configurations -----------
build_folder='js' # name of the local build folder
ssh='fl' # ssh config alias or full user@ip of the server
server_path='~/www/demos' # Server destintation folder (where the app goes)
# End Configurations -----------

rsync_cmd = 'tar czfvv - '+ paths.build_folder +' | ssh ' + paths.ssh + ' "(cd ' + paths.server_path + ' && rm -rf ' + paths.build_folder + ' ; cat > build.tar.gz && tar -xzf build.tar.gz && rm build.tar.gz)"'

subprocess.run(rsync_cmd, shell=True)