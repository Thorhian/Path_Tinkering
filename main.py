#!/usr/bin/env python3

import sys
import os
from stl import mesh

from job import Job
import Helper_Functions as hf

# Units should be in Metric.
target_res_per_pixel = 0.2 #Width/Height of each pixel

for arg in sys.argv:
    if arg == '--help' or arg == '-h':
        hf.print_help()
        sys.exit()

if len(sys.argv) <= 3:
    print("Please specify an STL file, depth of cut, and tool diameter (in mm).\n")
    sys.exit()

#Load STL File Target Model
stlTargetModel = os.path.abspath(sys.argv[1])
model_mesh = mesh.Mesh.from_file(stlTargetModel, speedups=False)

#Load STL File Stock Model
stlStockModel = os.path.abspath(sys.argv[2])
stock_mesh = mesh.Mesh.from_file(stlStockModel, speedups=False)

depth_of_cut = float(sys.argv[3])
tool_diameter = float(sys.argv[4])

# stock_dims = (-50, 50, -80, 80, 0, 31.75)
# stock_model = geometry_gens.generate_box(stock_dims)

newJob = Job(model_mesh, stock_mesh, [],
             tool_diameter, target_res=target_res_per_pixel)
print(newJob.bounds)
newJob.render_layers(depth_of_cut)
newJob.save_images()
