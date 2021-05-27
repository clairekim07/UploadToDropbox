import dropbox
import os
import shutil
class TransferData:
    def __init__(self,access_code):
        self.access_code = access_code

    def initializeDropbox(self,source,destination):
        dbx = dropbox.Dropbox(self.access_code)
        f=open(source,'rb')
        dbx.files_upload(f.read(),destination,mode=WriteMode('overwrite'))
def main():
    access_code = 'cvhAs55FGhQAAAAAAAAAAShJJSVdHF3XwiyOmJlZAMrcbBiBcgEhCVokxfDJDJcI'
    source = input("Enter the file you want to transfer: ")
    destination = input("Enter the full path including the name you want to your file to be: ")
    transferData = TransferData(access_code)
    transferData.initializeDropbox(source,destination)

if __name__ == '__main__':
    main()

