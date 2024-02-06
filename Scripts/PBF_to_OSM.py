import osmium

class OsmHandler(osmium.SimpleHandler):
    def __init__(self, writer):
        super(OsmHandler, self).__init__()
        self.writer = writer
        self.nodes_processed = 0
        self.ways_processed = 0
        self.relations_processed = 0
        self.progress_interval = 10000  # Adjust the interval based on your preferences

    def node(self, n):
        self.writer.add_node(n)
        self.nodes_processed += 1
        self.print_progress()

    def way(self, w):
        self.writer.add_way(w)
        self.ways_processed += 1
        self.print_progress()

    def relation(self, r):
        self.writer.add_relation(r)
        self.relations_processed += 1
        self.print_progress()

    def print_progress(self):
        if (self.nodes_processed + self.ways_processed + self.relations_processed) % self.progress_interval == 0:
            print(
                f"Processed: Nodes={self.nodes_processed}, Ways={self.ways_processed}, Relations={self.relations_processed}")


if __name__ == "__main__":
    input_pbf_file = "your_input.osm.pbf"
    output_osm_file = "your_output.osm"

    writer = osmium.SimpleWriter(output_osm_file)
    handler = OsmHandler(writer)
    handler.apply_file(input_pbf_file, locations=True)
    handler.print_progress()

    writer.close()

