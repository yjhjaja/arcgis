import arcpy

def get_centroid_of_polygon(in_features, field_name_lat = 'lat', field_name_lon = 'lon', coordinate_system = arcpy.SpatialReference('WGS 1984')):
	'''
	Generate the centroid of each polygon in a polygon shapefile
 	
  	Args:
   		in_features (string): directory of the shapefile
     		field_name_lat (string): name of the latitude  field of the centroid
       		field_name_lon (string): name of the longitude field of the centroid
	 	coordinate_system (SpatialReference): spatial reference of the coordinates of the centroid
   	
    	Returns:
     		nothing; simply edits in_features
	'''

	arcpy.management.AddField(in_features, field_name_lat, 'DOUBLE')
	arcpy.management.AddField(in_features, field_name_lon, 'DOUBLE')

	arcpy.management.CalculateGeometryAttributes(in_features, [[field_name_lat, 'CENTROID_Y'], [field_name_lon, 'CENTROID_X']], coordinate_system = coordinate_system)
