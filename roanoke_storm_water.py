import pandas as pd
import numpy as np

import arcpy
from arcgis.features import GeoAccessor, GeoSeriesAccessor

# Define workspace
arcpy.env.workspace = "./sedf_example.gdb"

# Load layers
sdf = pd.DataFrame.spatial.from_featureclass("storm_points")
watersheds = pd.DataFrame.spatial.from_featureclass("watersheds")

# Add new IDs
max_id = np.max(sdf['UNIQUEID'])
idx = sdf['UNIQUEID'] == 0
n = np.sum(idx)
new_ids = np.arange(max_id+1,max_id+n+1)
sdf.loc[idx,'UNIQUEID'] = new_ids

# Add missing watersheds
joined_df = sdf.spatial.join(watersheds.loc[:,['Watershed','SHAPE']])
idx = joined_df['WATERSHED'] == ' '
joined_df.loc[idx,'WATERSHED'] = joined_df.loc[idx,'Watershed']
joined_df = joined_df.drop(labels=['index_right','Watershed'],axis=1)

# Optionally, sort
joined_df = joined_df.sort_values(by='UNIQUEID')

# Write out the data
sdf.spatial.to_featureclass('storm_points_updated')