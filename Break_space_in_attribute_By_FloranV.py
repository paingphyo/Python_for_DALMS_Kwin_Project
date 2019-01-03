fc = "New_Shapefile"
fieldname = "name"
value_list=["       ","      ","     ","    ","   ","  "]
replace_with = " "

for i in value_list:
    with arcpy.da.UpdateCursor(fc, fieldname) as cursor:
        for row in cursor:
            value = row[0]
            value = value.replace(i, replace_with)
            row[0] = value
            cursor.updateRow(row)
    del cursor


with arcpy.da.UpdateCursor(fc, fieldname) as cursor:
    for row in cursor:
        value = row[0]
        if value[:1] == " ":
            value = value[1:]
            row[0] = value
        elif value[-1:] == " ":
            value = value[:-1]
            row[0] = value
        cursor.updateRow(row)
del cursor


