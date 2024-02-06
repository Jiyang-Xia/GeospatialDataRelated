import osm2gmns as og

def osm_filter(osm_file, filter_folder):
    net = og.getNetFromFile(osm_file, network_types=('walk', 'bike', 'auto'), POI=True)
    og.consolidateComplexIntersections(net, auto_identify=True)
    og.outputNetToCSV(net, output_folder=filter_folder)
    # og.osmnet.visualization.show(net, save=False, figsize=None)

if __name__ == "__main__":
    osm_file = "your_input.osm"
    filter_folder = "yourfilterfolder"

    osm_filter(osm_file, filter_folder)
    print(f"OSM filter is completed. output files saved to {filter_folder}")
