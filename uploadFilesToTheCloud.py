#This script will check internet connection 
#Then asks which service the user wants: 1) only on cloud drive 2) check for both files
#if service 1
#Then asks which cloud storage platform the user is using
#Then asks the file name
#Then checks if the drive exists in the computer, if not inform to install
#Then script search through the directory and print out the directory to the file
#Then print out the metadata for the file
#Then print out the metadata instruction

#if service 2
#Same process as service 1
#Then asks the user to enter another directory (do not have to be a cloud drive)
#Then asks for the file name (script will check if they are the same)
#Then print out the directory and metadata
#Print out metadata instruction for the user to compare results

import os.path
from os import path
import socket
import datetime
REMOTE_SERVER = "www.google.com"


#detect internet connection
def is_connected():
  try:
    #try connect to google.com
    host = socket.gethostbyname(REMOTE_SERVER)
    s = socket.create_connection((host, 80), 2)
    return "\n*** Your computer is connected to the Internet. ***"
  except:
    return "\n*** Please check your Internet connection, you can still use the service but your files are not up to date. ***"

#collect Cloud Drive name and file name
def collect_names(decision):
    #inputs need to be accurate
    print("============================Please Enter============================")
    directory=raw_input("Please enter the name of your Cloud Storage Solution(Box Sync, DropBox, OneDrive, GoogleDrive): ")
    file_name=raw_input("Please enter the name of the file you want to check if exists in the cloud: ")
    print("")
    #if the user only wants to search cloud drive
    if (decision == 1):
        search_cloud_drive(directory, file_name)
    #if the user wants to search through both drive and compare metadata
    if (decision == 2):
        search_cloud_drive(directory, file_name)
        print("\n")
        collect_another(file_name)

#check if the cloud drive exists in the computer
def search_cloud_drive(driveName, file):
    if (driveName == "Box Sync" or driveName == "DropBox" or driveName == "OneDrive" or driveName == "GoogleDrive"):
        if (driveName == "Box Sync"):
            driveName = "./Box Sync"

        if (driveName == "DropBox"):
            driveName = "./Dropbox"

        if (driveName == "OneDrive"):
            driveName = "./OneDrive"

        if (driveName == "GoogleDrive"):
            driveName = "./Google Drive"
    #invalid input will exit the script
    else:
        print("Invalid drive input!")
        print("")
        exit()
    #check if the drive exists
    if (path.exists(driveName)):
        print("============================Successed============================")
        print("Your cloud drive exists and ready to be searched!")
        print("")
    #there is no such drive, inform the user to install first
    else:
        print("============================Failed============================")
        print("Cloud Drive does not exist, please install first!")
        print("")
    #pass info to search the files
    result = (search_directory(driveName, file))
    #get the metadata based on the file
    get_metadata(result)


#collect another file's information
def collect_another(checkName):
    print("============================Please Enter============================")
    directory=raw_input("Please enter the folder name for your file: ")
    directory=("./"+directory)
    file_name=raw_input("Please enter the name of the file: ")
    print("")
    #check if both names are the same for comparing purpose
    if (checkName == file_name):
        print("============================Successed============================")
        print(" *** File names matched *** ")
        print("")
        search_drive(directory, file_name)
    else:
        print("============================Failed============================")
        print("File name entered does not match the other file!")
        print("")
        exit()

#search through another drive
def search_drive(driveName, file):
    if (path.exists(driveName)):
        print("============================Successed============================")
        print("Your drive exists and ready to be searched!")
        print("")
    else:
        print("============================Failed============================")
        print("Drive does not exist, please install first!")
        print("")
    result = (search_directory(driveName, file))
    get_metadata(result)

#search through the drive to see if file exists
def search_directory(directory, file_name):
    result = []
    for root, dirs, files in os.walk(directory):
        if file_name in files:
            print("============================File Path & Metadata============================")
            print("Your file exists in the drive, below is the directory to your file: ")
            result.append(os.path.join(root, file_name))
    return result

#collect metadata for the file
def get_metadata(result):
    for f in result:
        print("\n %s, \n\nMetadata: %s" %(f,os.stat(f)))
        print("")
        mod_timestamp = datetime.datetime.fromtimestamp(path.getmtime(f))
        print("============================Recent modification============================")
        print("*** This file's most recent content modification time is: ***")
        print(mod_timestamp)
        print("")

#metadata instruction
def metadata_instruction():
    print("============================Metadata instructions============================")
    print("*** Below are the instructions on how to read the metadata. *** ")
    print("st_mode - protection bits,")
    print("st_ino - inode number,")
    print("st_dev - device,")
    print("st_nlink - number of hard links,")
    print("st_uid - user id of owner,")
    print("st_gid - group id of owner,")
    print("st_size - size of file, in bytes,")
    print("st_atime - time of most recent access,")
    print("st_mtime - time of most recent content modification,")
    print("st_ctime - platform dependent; time of most recent metadata change on Unix, or the time of creation on Windows)")
    print("\n\n")

#Main
def Main():
    print("*******************************************************")
    print("*******************************************************")
    print("*********************** Welcome ***********************")
    print("************* You can use this script to **************")
    print("******* identify if your file is successfully *********")
    print("******* uploaded to the cloud storage solution ********")
    print("********** and also compare the metadata of ***********")
    print("********** any previous version of the file ***********")
    print("*** to make sure having the right one on the cloud ****")
    print("*******************************************************")
    print("*******************************************************")
    print(is_connected())
    print("\n\nPlease select a service: (1) or (2)")
    decision = input("1. Search if a file exists in cloud drive. \n2. Compare two files with same name to see the differences.\n")
    if (decision == 1):
        collect_names(decision)
        metadata_instruction()
    if (decision == 2):
        collect_names(decision)
        metadata_instruction()


if __name__ == '__main__':
    Main()