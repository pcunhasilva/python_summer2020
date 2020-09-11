"""Data Structures Working with Graphs/Networks"""

## Function to link 2 nodes (not in the sense of last script)
def makeLink(G, node1, node2):
  if node1 not in G:
    G[node1] = {}
  (G[node1])[node2] = True
  if node2 not in G:
    G[node2] = {}
  (G[node2])[node1] = True
  return G 

## empty graph 
ring = {} 

## number of nodes 
n = 5 

## Add in edges with makeLink function
for i in range(n):
  ring = makeLink(ring, i, (i+1)%n)
  print (ring)

print (ring)

## How many nodes?
print (len(ring))

## How many edges?
print (sum([len(ring[node]) for node in ring.keys()])/2 )


## Grid Network
## TODO: create a square graph with 256 nodes using the makeLink function
## TODO: define a function countEdges

import math
n = 9
g = {}
for i in range(1,n):
  n_width = int(math.sqrt(n))
  ## if we are not on a boundary
  ## i.e., if node is not multiple of our set node width
  ## then link to next node
  if i%n_width != 0:
    makeLink(g, i, i+1)
  ## if not on last row
  ## link to node directly below
  if i <= n-n_width:
    makeLink(g, i, i+n_width)


def count_edges(graph):
  ## apply len function to each element of graph (how many connections)
  ## sum up all connections
  ## divide by 2 since each counted twice in graph (1->2 and 2<-1)
  return sum(map(len, graph.values()))/2

count_edges(g)


##  Social Network
class Actor(object):
  def __init__(self, name):
    self.name = name 

  def __repr__(self):
    return self.name 

ss = Actor("Susan Sarandon")
jr = Actor("Julia Roberts")
kb = Actor("Kevin Bacon")
ah = Actor("Anne Hathaway")
rd = Actor("Robert DeNiro")
ms = Actor("Meryl Streep")
dh = Actor("Dustin Hoffman")

movies = {}

movies = makeLink(movies, dh, rd) # Wag the Dog
movies = makeLink(movies, rd, ms) # Marvin's Room
movies = makeLink(movies, dh, ss) # Midnight Mile
movies = makeLink(movies, dh, jr) # Hook
movies = makeLink(movies, dh, kb) # Sleepers
movies = makeLink(movies, ss, jr) # Stepmom
movies = makeLink(movies, kb, jr) # Flatliners
movies = makeLink(movies, kb, ms) # The River Wild
movies = makeLink(movies, ah, ms) # Devil Wears Prada
movies = makeLink(movies, ah, jr) # Valentine's Day





def findPath(graph, start, end, path=[]):
    ## create list
    path = path + [start]
    ## base case, reached end
    if start == end:
        return path
    if start not in graph:
        return None
    ## for each connection to starting node
    for node in graph[start]:
        ## check if it is already in path
        if node not in path:
            break
    ## if not, call recursively, thus adding node to path
    ## carry around path object with you
    return findPath(graph, node, end, path)


print (findPath(movies, jr, ms))

## start with julia roberts 
## who is she directly connected to?
movies[jr].keys()
## who are they connected to?
movies[ss].keys() 
movies[ah].keys() ## found meryl streep!
movies[dh].keys()
movies[kb].keys() ## found meryl streep!
## so shortest path is either
## jr -- ah -- ms
## jr -- kb -- ms




## TODO: implement findAllPaths() to find all paths between two nodes
## allPaths = findAllPaths(movies, jr, ms)
## for path in allPaths:
##   print path

def findAllPaths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return None
        allpaths = []
        for node in graph[start]:
            if node not in path:
                allpaths.extend(findAllPaths(graph, node, end, path))
        allpaths = filter(None, allpaths)
        return allpaths

allpaths = findAllPaths(graph = movies, start = ms, end = ss)

for path in allpaths:
  print (path)


## TODO: implement findShortestPath() to print shorest path between actors
## print findShortestPath(movies, ms, ss)

def findShortestPath(graph, start, end):
    allpaths = findAllPaths(graph, start, end)
    return min(allpaths, key = len)

findShortestPath(movies, ms, ss)



# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.