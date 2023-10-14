import arcpy

def get_closest_feature(target_features, join_features, out_feature_class):
    '''
    For each feature in target_features, what is the closest feature in join_features?

    Args:
        target_features (string): directory of the shapefile that contains the features that you want to find a closest counterpart for each
        join_features (string): directory of the shapefile that contains the counterpart features
        out_feature_class (string): directory of the output shapefile

    Returns:
        out_feature_class: a shapefile that combines target_features and join_features, where for each feature in target_features, we associate it with its closest feature in join_features, and the distance in between
    '''

    arcpy.analysis.SpatialJoin(target_features, join_features, out_feature_class, match_option = 'CLOSEST')
