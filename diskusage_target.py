#!/usr/bin/env python3
# Author(C), Arun Singh, arunsingh.in@gmail.com for Target systems programming.



import os
import json
import sys
import argparse

def disk_usage(mount_dir):
    
    file_list = []

    for dirpath, dirs, files in os.walk(mount_dir):
        for file in files:
            mapping = {}
            file_path = os.path.join(dirpath, file)
        ## calculate disk usage of file
            file_du = os.stat(file_path).st_blocks * 512
        ## add the file path and its disk usage to list of
            mapping[file_path] = file_du
            file_list.append(mapping)
    
    return json.dumps(file_list, indent=4, separators=(',',','))


if __name__ == "__main__":
    #### diskusage.py as CLI
    #### $ python3 -m diskusage.py --help
    #### $ python3 -m diskusage.py --mountpoint <abs-path-of-mount-dir>
    #### $ python3 -m diskusage.py -m <abs-path-of-mount-dir>
    #### $ python3 -m diskusage.py
    parser = argparse.ArgumentParser(description="determine disk usage of all files on mount point")
    parser.add_argument("-m", "--mountpoint", type=str, default=".", help="absolute path of mount directory")

    args = parser.parse_args()
    
    mount_directory = args.mountpoint
    
    if mount_directory == ".":
        mount_directory = os.getcwd()
    # Check if mount directory exists
    elif not (os.path.exists(mount_directory) and os.path.isdir(mount_directory)):
        sys.exit("I'm afraid the path {} does not exist".format(mount_directory))
    # check if user has access to mount directory
    elif not os.access(mount_directory, os.F_OK):
        sys.exit("I'm afraid you cannot access the path {}".format(mount_directory))
    
    # debug the old way :) print("the mount directory is {}".format(args.mountpoint))
    print(disk_usage(mount_directory))
