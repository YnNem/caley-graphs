""" ------------------Permutation groups--------------------------------
Author: Yonatan Nemtsov

In this program I make methods for analyzing and generating permutation groups.

A permutation is represented as a list, for example [0,2,1] coresponds to the
0->0, 1->2, 2->1 permutation.


"""
from math import factorial
import networkx as nx
import matplotlib.pyplot as plt

def permutation_prod(p,q):                    # Returns p o q.
    prod = []
    for i in q:
        prod.append(p[i])
    return prod

def S(n):                                     # Return Sn group as a list. Works for n<10 only!!
    if n == 1:
        return [[0]]
    Sn = []
    Sn_min_1 = S(n-1)

    for p in Sn_min_1:
        for i in range(n):
            pi = list(p)
            pi.insert(n-1-i,n-1)
            Sn.append(pi)
            
    return sorted(Sn)

def subgroup_gen_by(p):                     # Returns the subgroup generated by a permutation p.
    n = len(p)
    G = [p]
    q = p
    while q != [i for i in range(n)]:
        q = permutation_prod(q,p)
        G.append(q)
    return sorted(G)

def subgroup_gen_by_generators(generators):

    n = len(generators[0])
    I = [i for i in range(n)]
    S = [I]
    T = {1:I}
    
    while len(S)!=factorial(n):
        new_elements = []
        for i in T:
            s = T[i]
            for g in generators:
                k = permutation_prod(g,s)
                if not S.__contains__(k):
                    S.append(k)
                    new_elements.append([len(S),k])
        if new_elements == []:
            break
        T = {}
        for i in new_elements:
             T[i[0]] = i[1]
    return sorted(S)

def cycle_decomposition(permutation):
    pass

def find_subgroups_naive(group):
    G = sorted(group)
    subgroups = []
    H = G
    generators = []
    
    while H!= []:
        g = H[-1]
        generators.append(g)
        C = subgroup_gen_by(g)
        subgroups.append(C)
        for x in C:
            if H.__contains__(x):
                H.remove(x)

    T = True
    while T == True:
       pass    
        
        
    return subgroups


def cayley_graph(generators):
    n = len(generators[0])
    cayley_graph = nx.DiGraph()
    I = list(range(n))
    _S = [I]
    S = {1:I}
    T = {1:I}
    while len(S)!=factorial(n):
        new_elements = []
        for i in T:
            s = T[i]
            for g in generators:
                k = permutation_prod(g,s)
                if not _S.__contains__(k):
                    _S.append(k)
                    new_elements.append([len(_S),k])
        if new_elements == []:
            break
        T = {}
        for i in new_elements:
             S[i[0]] = i[1]
             T[i[0]] = i[1]
        print(T)
             
        
    for i in S:
        s = S[i]
        
        for g in generators:
            k = permutation_prod(s,g)
            cayley_graph.add_edge(i,_S.index(k)+1)
            
    return cayley_graph

def order(permutation):
    return len(subgroup_gen_by(permutation))






#Examples

#example 1
edge_color = 100*['blue','red']
G = cayley_graph([[1,0,2,3],[3,2,0,1]])
node_color = ['black']+(G.order()-1)*['blue']
nx.draw(G,nx.kamada_kawai_layout(G),edge_color = edge_color, node_color = node_color)
plt.show()






#example 2

for i in S(4):
    for j in S(4):

        if subgroup_gen_by(i)== subgroup_gen_by(j):
            break
        
        G = cayley_graph([i,j])
        

        node_color = ['black']+(G.order()-1)*['blue']

        edge_color = 1000*['red','blue']
        pos1 = nx.spectral_layout(G)
        pos2 = nx.kamada_kawai_layout(G)
        pos3 = nx.shell_layout(G, center=[1,2])
        #pos4 = nx.planar_layout(G)
        nx.draw(G,pos2,node_color = node_color ,edge_color = edge_color)
        plt.show()







