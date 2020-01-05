#!/usr/bin/env python
import subprocess

# Configurations -----------
build_folder='dist' # name of the local build folder
ssh='fl' # ssh config alias or full user@ip of the server
server_path='~/public_html/live' # Server destintation folder (where the app goes)
# End Configurations -----------

rsync_cmd = 'cd ' + build_folder + ' && tar czfvv - . | ssh ' + ssh + ' "(cd ' + server_path + ' && rm -rf * ; cat > build.tar.gz && tar -xzf build.tar.gz && rm build.tar.gz)"'

subprocess.run(rsync_cmd, shell=True)