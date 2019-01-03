import arcpy,os
maindir ='D:\\confirn_vs_walk\\'
def list_files(dir):                                                                                                  
    r = []                                                                                                            
    subdirs = [x[0] for x in os.walk(dir)]                                                                            
    for subdir in subdirs:                                                                                            
        files = os.walk(subdir).next()[2]                                                                             
        if (len(files) > 0):                                                                                          
            for file in files:
                file = file.lower()
                if file.startswith("k"):
                    if file.endswith("_plotno.shp"):
                        r.append(subdir + "\\" +file)
                        print (subdir + "\\" +file)
                              
    return r
myfiles =list_files(maindir)

for file in myfiles:
    arcpy.AddField_management(file, "Kwin_No", "TEXT", field_length = 25)

    #Within each attribute table, write the name of the #current file

    with arcpy.da.UpdateCursor(file, "Kwin_No") as cursor:
        for row in cursor:
            value = file[:-4]
            rIndex = value.rfind("\\") + 1
            row[0] =value[rIndex:]
            cursor.updateRow(row)
    print (file + " completed")
print ("task done!")
