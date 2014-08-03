from pyechonest import config
from pyechonest import artist

from pygraphviz import *

from time import sleep

config.ECHO_NEST_API_KEY = "Y3C5I9DKM9SQFZOLF"

filename = "holyother"
seed_artist_name = "Holy Other"

g = AGraph(strict=True, directed=True)

def add_artist(a):
    g.add_node(a.id, label=a.name, hotttnesss=a.hotttnesss)
    
def maybe_add_edge(a, b):
    if g.has_node(a.id) and g.has_node(b.id):
        g.add_edge(a.id, b.id)

def recursively_add_nodes(a, depth):
    sleep(10) # for some reason pyechonest's throttling doesn't quite work for me idk
    for similar in a.similar:
        add_artist(similar)
        if depth > 0:
            recursively_add_nodes(similar, depth=depth-1)

def recursively_add_edges(a, depth):
    for similar in a.similar:
        maybe_add_edge(a, similar)
        if depth > 0:
            recursively_add_edges(similar, depth=depth-1)

def map_artist(a, depth=2):
    add_artist(a)
    recursively_add_nodes(a, depth=depth)
    recursively_add_edges(a, depth=depth)
    
a = artist.Artist(seed_artist_name)
map_artist(a, depth=1)

g.write("%s.dot" % filename)