# Greg Smyth
# Dijkstra's algorithm
# dijkstra.py
# Greg Smyth / Institute of Cancer Research 2013
# 
# Written 13-16th October, 12th November 2013
# Original source: Dijkstra (1959) 
# Based on pseudocode in Algorithms (3rd ed) Cormen et al 2009 



def print_path(G,s,v,pi):
    if v==s:
        print s
    elif len(pi) == 0:
        print "no path from", s ,"to", v ,"exists"
    else:
        print_path(G,s,pi[v],pi)
        print v
    return (G,s,v)


def initialise_single_source(G_V):
    d=[]
    pi=[]
    for v in G_V:
        d.append(float("inf"))
        pi.append(0)
    d[s] = 0
    print "d",d
    return (d, pi)


def relax(d,v,u,weights,pi):
    if u in weights and v in weights[u]:
        currentWeight = weights[u][v]
    else:
        currentWeight = float("inf")
    if d[v] > (d[u] + currentWeight):
        d[v] = d[u] + currentWeight
        pi[v]= u
    return (d,pi)


def extract_min(Q, d):
    Qmin = float("inf")
    for v in Q:
        if d[v] < Qmin:
            Qmin = d[v]
    return Qmin    


def dijkstra(G_V,Adj, weights, s):
    ## Initialisation
    (d, pi)=initialise_single_source(G_V)
    S = []
    Q = G_V
    u=0
    ## Process all vertices
    while len(Q) != 0:
        Qmin = extract_min(Q, d)
        u = d.index(Qmin)
        S.append(u)
        Q.remove(u)
        ## Find a new vertex and relax
        for v in Adj[u]:
            relax(d,v,u,weights,pi)
        print "d", d
    return (S,pi)

##
##Runs Dijkstra and prints least cost path between s and v
##
def dijkstraPaths(G_V,Adj, weights, s, v):
    (S, pi) = dijkstra(G_V, Adj, weights, s)
    print_path(G_V,s,v,pi)
    return()
    
################
## Input data ##
################

#
# Numbered list of nodes
#
G_V = [0,1,2,3,4]

#
# Adjacency list as dictionary
#
Adj={}
for v in G_V:
    Adj[v]=dict()

Adj[0]=[1,2,3]
Adj[1]=[0,4]
Adj[2]=[0,4]
Adj[3]=[0,4]
Adj[4]=[1,2,3]

#
# Edge weights as dictionary
#
weights={}
for v in G_V:
    weights[v]=dict()

weights[0][1]=8
weights[0][2]=5
weights[0][3]=7

weights[1][4]=6
weights[2][4]=9
weights[3][4]=4

weights[4][1]=6
weights[4][2]=9
weights[4][3]=4

#
# Define start and end nodes
#
startNode = 0
endNode = 4

#
# Function call
#
dijkstraPaths(G_V,Adj, weights, startNode, endNode)
