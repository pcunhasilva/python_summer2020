import math

"""Data Structures Working with Graphs/Networks"""

def makeLink(G, node1, node2):
  if node1 not in G:
    G[node1] = {}
  (G[node1])[node2] = 1
  if node2 not in G:
    G[node2] = {}
  (G[node2])[node1] = 1
  return G

# Ring Network
ring = {} # empty graph

n = 5 # number of nodes

# Add in edges
for i in range(n):
  ring = makeLink(ring, i, (i+1)%n)

# How many nodes?
print (len(ring))

# How many edges?
print (sum([len(ring[node]) for node in ring.keys()])/2)

# Grid Network
# TODO: create a square graph with 256 nodes and count the edges

# It creates the square graph with the 256 nodes and diagonals.
def createsquare(n):
    square = {}
    sq = math.sqrt(n)
    for i in range(1, n):
        if i < sq:
            makeLink(square, i, int(i + 1))
            makeLink(square, i, int(i + sq))
            makeLink(square, i, int(i + sq + 1))
            if i > 1:
                makeLink(square, i, int(i + sq - 1))
        elif i == sq:
            makeLink(square, i, int(i - 1))
            makeLink(square, i, int(i + sq - 1))
            makeLink(square, i, int(i + sq))
        elif i == n - sq:
            makeLink(square, i, int(i + sq - 1))
            makeLink(square, i, int(i + sq))
        elif i == n:
            break
        elif i > n - sq:
            makeLink(square, i, int(i + 1))    
        elif i % sq == 0:
            makeLink(square, i, int(i + sq - 1))
            makeLink(square, i, int(i + sq))
            if n % 2 != 0:
                makeLink(square, i, int(i + sq + 1))
        else:
            makeLink(square, i, int(i + 1))
            makeLink(square, i, int(i + sq))
            makeLink(square, i, int(i + sq + 1))
            r = [int(1 + sq)]
            for k in range(int(sq)):
                r.append(int(r[len(r)-1] + sq))        
            if i not in r:
                makeLink(square, i, int(i + sq - 1))         
            if math.ceil(n / 2) == i:
                makeLink(square, i, int(i + sq - 1))
    return square


# TODO: define a function countEdges
def countEdges(graph):
    f = graph
    k = []
    for i in f.keys():
        for j in f[i].keys():
            k.append([i, j])
    for i in range(0, len(k)): k[i].sort()
    unique = set(map(tuple, k))
    return len(unique)



mysquare = createsquare(n = 9)
countEdges(mysquare)

# Social Network
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

makeLink(movies, dh, rd) # Wag the Dog
makeLink(movies, rd, ms) # Marvin's Room
makeLink(movies, dh, ss) # Midnight Mile
makeLink(movies, dh, jr) # Hook
makeLink(movies, dh, kb) # Sleepers
makeLink(movies, ss, jr) # Stepmom
makeLink(movies, kb, jr) # Flatliners
makeLink(movies, kb, ms) # The River Wild
makeLink(movies, ah, ms) # Devil Wears Prada
makeLink(movies, ah, jr) # Valentine's Day


def tour(graph, nodes):
  for i in range(len(nodes)):
    node = nodes[i]
    if node in graph.keys():
      print (node)
    else:
      print( "Node not found!")
      break
    if i+1 < len(nodes):
      next_node = nodes[i+1]
      if next_node in graph.keys():
        if next_node in graph[node].keys():
          pass
        else:
          print ("Can't get there from here!")
          break

# TODO: find an Eulerian tour of the movie network and check it
tour(movies, [ah,ms])
tour(movies, [rd,ms,kb,jr,ah,ms])
movie_tour = []
tour(movies, movie_tour)


def findPath(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in graph:
            return None
        for node in graph[start]:
            if node not in path:
                newpath = findPath(graph, node, end, path)
                if newpath: return newpath
        return None

print(findPath(movies, jr, ms))


# TODO: implement findAllPaths() to find all paths between two nodes
def findAllPaths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return None
    paths = []
    for node in graph[start]:
        if node not in path:
            p = findAllPaths(graph, node, end, path)
            for i in p:
                paths.append(i)
    return paths

findAllPaths(graph = movies, start = ms, end = ss)

# TODO: implement findShortestPath()

def findShortestPath(graph, start, end, path = []):
    x = findAllPaths(graph, start, end, path)
    lengs = [len(i) for i in x]
    return x[lengs.index(min(lengs))]

print (findShortestPath(graph = movies, start = ms, end = ss))


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
