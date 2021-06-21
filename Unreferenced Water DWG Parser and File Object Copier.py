import shutil, os

referencedDWGsFolder = r'R:\Projects\Active\CW2020_Water\Working\Record_Drawings\Pontiac_PS\Referenced' # folder housing the referenced DWGs
destinationFolder = r'R:\Projects\Active\CW2020_Water\Working\Record_Drawings\Pontiac_PS\Unreferenced' # folder to store the unreferenced DWGs
sourceFolder = r'F:\Scans' # folder housing all the scans to pull dwgs from

referencedListAllFiles = [] # create an empty array to store ALL the files in the referenced folder
unreferencedListNoExtension = [] # create an empty array to store the names of dwgs WITHOUT an extension
extensionEndings = ['.pdf','.tif', '.png','.jpeg','.jpg'] # various extensions for testing valid file objects

referencedListAllFiles = os.listdir(referencedDWGsFolder) # save the file names in the referenced DWGs folder to the variable

for each in referencedListAllFiles: # loop through each file ending in .tif and parse it to make it useable

    if each.endswith(".tif"):

        if "1_r.tif" in each: # various endings need to be parsed
            dwgName = each[:-7] # stare the parsed file name ending in .tif
            unreferencedListNoExtension.append(dwgName) # save it to a variable without the extension
            print(each[:-7] + ' added to the list.')

        elif "1.tif" in each:
            dwgName = each[:-5]
            unreferencedListNoExtension.append(dwgName)
            print(each[:-5] + ' added to the list.')

        elif "R.tif" in each:
            dwgName = each[:-5]
            unreferencedListNoExtension.append(dwgName)
            print(each[:-5] + ' added to the list.')

        elif "R1.tif" in each:
            dwgName = each[:-6]
            unreferencedListNoExtension.append(dwgName)
            print(each[:-5] + ' added to the list.')

        elif "1_u.tif" in each:
            dwgName = each[:-7]
            unreferencedListNoExtension.append(dwgName)
            print(each[:-7] + ' added to the list.')

        else:
            dwgName = each
            unreferencedListNoExtension.append(dwgName)
            print(each + ' added to the list.')

for each in unreferencedListNoExtension: # loop through each file name without an extension

    for fileEnding in extensionEndings: # loop through each file name extension
        fileObjectWithEnding = each + fileEnding # create a file object for each extension to test if it exists

        sourceFolderDWGObject = os.path.join(sourceFolder, fileObjectWithEnding)
        destinationFolderDWGObject = os.path.join(destinationFolder, fileObjectWithEnding)

        if os.path.exists(sourceFolderDWGObject) and not os.path.isdir(sourceFolderDWGObject): # test to see if the ending is correct
            shutil.copyfile(sourceFolderDWGObject, destinationFolderDWGObject) # if it is not a directory and exists, copy it!

