# scp-distribution-to-server
Downloads files on the server once the git repo gets updated

1. Add `paths.py` and `dist.py` on the root of your project
2. In `paths.py` set:
   - the absolute server `path` where the directory needs to go (ie: path='~/public_html/live')
   - the server ssh connection string in full (`user@you.ip.add.res`) or the .ssh/config alias
   - the build folder name (i.e. `build`, or `dist`)
3. To push a build go to the root of your project and from the terminal run: `python3 -B dist.py`
