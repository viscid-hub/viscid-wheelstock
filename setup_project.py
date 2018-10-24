#!/usr/bin/env python

from __future__ import print_function
import hashlib
import os
import shutil
import sys
import zipfile

try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen


CIBW_SKIP = "*-win32 *-manylinux1_i686 cp33-* cp34-*"

test_pypi = False

# NOTE: the TWINE_PASSWORD environment variable should be set using a
#       a secure variable in your CI service (travis, appveyor, etc.)
twine_username = 'viscid-hub'
if test_pypi:
    twine_repo_url = 'https://test.pypi.org/legacy/'
else:
    twine_repo_url = 'https://upload.pypi.org/legacy/'

gh_owner = "viscid-hub"
gh_repo_name = "Viscid"
tag = "1.0.0.dev8"
sha256 = "2b10b4afa4486c884062f42de2061827df42fb7e99cd0990ea61601432b50f17"

dl_ext = "zip"

gh_repo_url = "https://github.com/{owner}/{name}".format(owner=gh_owner,
                                                         name=gh_repo_name)
gh_dl_url = "{repo_url}/archive/{tag}.{ext}".format(repo_url=gh_repo_url,
                                                    tag=tag, ext=dl_ext)

zip_filename = "{name}-{tag}.{ext}".format(name=gh_repo_name, tag=tag, ext=dl_ext)
pkgdir = "{name}-{tag}".format(name=gh_repo_name, tag=tag)

print("Downloading:", gh_dl_url)
print("         to:", zip_filename)

with open(zip_filename, 'wb') as fout:
    request = urlopen(gh_dl_url)
    zip_data = request.read()
    zip_sha256_digest = hashlib.sha256(zip_data).hexdigest()
    # zip_sha384_digest = hashlib.sha384(zip_data).hexdigest()
    fout.write(zip_data)
    zip_data = None

print()
print("Checking hashes...")
print()

hash_mismatch = ''

print("sha256:", zip_sha256_digest)
if sha256 and zip_sha256_digest != sha256:
    print("Hash mismatch (sha256):\n"
          "    template:{0}\n".format(sha256), file=sys.stderr)
    hash_mismatch += 'sha256'

# print("sha384:", zip_sha384_digest)
# if sha384 and zip_sha384_digest != sha384:
#     print("Hash mismatch (sha384):\n"
#           "    template:{0}\n".format(sha384), file=sys.stderr)
#     hash_mismatch += 'sha384'

if hash_mismatch:
    raise RuntimeError("hash mismatch ({0})".format(hash_mismatch))

with zipfile.ZipFile(zip_filename, 'r') as fin:
    fin.extractall()

if not os.path.isdir(pkgdir):
    raise RuntimeError("Dest dir: {0} not created.".format(pkgdir))

os.remove(zip_filename)

shutil.copy('numpy_version.py', pkgdir)
shutil.copy('pre_build_linux.sh', pkgdir)
shutil.copy('pre_build_osx.sh', pkgdir)
shutil.copy('pre_build_win.bat', pkgdir)

with open('meta_pkgdir.txt', 'w') as fout:
    fout.write(pkgdir)
with open('meta_pkgname.txt', 'w') as fout:
    fout.write(gh_repo_name)
with open('meta_tag.txt', 'w') as fout:
    fout.write(tag)
with open('meta_owner.txt', 'w') as fout:
    fout.write(gh_owner)

with open('meta_CIBW_SKIP.txt', 'w') as fout:
    fout.write(CIBW_SKIP)

with open('meta_twine_user.txt', 'w') as fout:
    fout.write(twine_username)
with open('meta_twine_repo_url.txt', 'w') as fout:
    fout.write(twine_repo_url)

##
## EOF
##
