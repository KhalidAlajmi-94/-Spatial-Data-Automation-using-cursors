import arcpy

afolderpath = r"C:\Users\KHALID\Desktop\Geog408\Assignment_04"
aGDB= "Assignment_04.gdb"
nGDB= "PCS_Data.gdb"

arcpy.env.workspace = afolderpath + "\\" + aGDB
aFC=arcpy.ListFeatureClasses()

arcpy.CreateFileGDB_management(r"C:\Users\KHALID\Desktop\Geog408\Assignment_04", "PCS_Data.gdb")

for x in aFC:
    if arcpy.Describe(x).SpatialReference.type=='Geographic':
        outfile= afolderpath + "\\" + nGDB + "\\" + x+"_P"
        arcpy.Project_management(x, outfile, 26945)


arcpy.env.workspace= r"C:\Users\KHALID\Desktop\Geog408\Assignment_04\PCS_Data.gdb"
arcpy.AddField_management("SFV_BG_P", "DI", "Double")
aFc="SFV_BG_P"
with arcpy.da.UpdateCursor(aFc, "*",' WHITE > 0OR BLACK >0 OR HISPANIC >0 OR AMERI_ES >0 OR ASIAN >0 OR HAWN_PI >0 OR OTHER >0 OR MULTI_RACE >0') as aCursor:
    for aRow in aCursor:
        aRow[14]= 1-(((aRow[4]/aRow[3])**2)+((aRow[5]/aRow[3])**2)+((aRow[6]/aRow[3])**2)+((aRow[7]/aRow[3])**2)+((aRow[8]/aRow[3])**2)+((aRow[9]/aRow[3])**2)+((aRow[10]/aRow[3])**2)+((aRow[11]/aRow[3])**2))
        aCursor.updateRow(aRow)
del aRow
del aCursor
        



    
print "done"
    