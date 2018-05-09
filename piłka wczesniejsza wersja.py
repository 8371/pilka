import pygame
from pprint import pprint
lenx = [191, 450, 360]
leny = [282, 400, 280]
#
color=(0,0,255)
ruchy=[]
clock = pygame.time.Clock()
pygame.init()
#global lenx,leny
draw=3
o=46
srodek=49
graph = {}
xk,yk=191,283
graph = {}
ekran = pygame.display.set_mode((382,565))
boisko = pygame.image.load('boisko.png')
ekran.blit(boisko,(0,0))
y=1
gracz='Gracz 2'
def przycisk(x,y):
    font = pygame.font.SysFont("comicsansms",25)
    text = font.render("X: "+str(x), True,(0,0,0))
    ekran.blit(text, (0,0))
    textt = font.render("X: "+str(y), True,(0,0,0))
    ekran.blit(textt, (5,520))
def add_node(graph, node):
    if node not in graph:
        graph[node] = []
def listnodes(graph):
    return graph.keys()
def add_edge_undirected(graph, edge):
    source, target = edge
    add_node(graph, source)
    add_node(graph, target)
    if target not in graph[source]:
        graph[source].append(target)
    if source not in graph[target]:
        graph[target].append(source)
for i in range(105):
    add_node(graph,i)
def switch():
    global y, gracz,color
    if y==1:
        gracz='Gracz 2'
        color=(0,0,0)
        y=2
    else:
        gracz='Gracz 1'
        color=(255,0,0)
        y=1
def zmiana(x):
    global ruchy,srodek,color,y
    if x==6:
        if srodek not in graph[srodek+11]:
            if len(graph[srodek+11]) ==0:
                switch()
            print(color)
            pygame.draw.line(ekran,color,(lenx[0],leny[0]),(lenx[0]+o,leny[0]),draw)
            add_edge_undirected(graph,(srodek,srodek+11))
            lenx[0] += o
            ruchy += [2]
            srodek += 11
    if x==2:
        if srodek not in graph[srodek+1]:
            if len(graph[srodek+1]) ==0:
                switch()            
            pygame.draw.line(ekran,color,(lenx[0],leny[0]),(lenx[0],leny[0]+o),draw)
            add_edge_undirected(graph,(srodek,srodek+1))
            leny[0] += o
            ruchy += [4]
            srodek += 1
    if x==8:
        if srodek not in graph[srodek-1]:
            if len(graph[srodek-1]) ==0:
                switch()            
            pygame.draw.line(ekran,color,(lenx[0],leny[0]),(lenx[0],leny[0]-o),draw)
            add_edge_undirected(graph,(srodek,srodek-1))
            leny[0] += -o
            ruchy += [0]
            srodek += -1                                        
    if x==4:
        if srodek not in graph[srodek-11]:
            if len(graph[srodek-11]) ==0:
                switch()
            pygame.draw.line(ekran,color,(lenx[0]-o,leny[0]),(lenx[0],leny[0]),draw)
            add_edge_undirected(graph,(srodek,srodek-11))
            lenx[0] += -o
            ruchy += [6]
            srodek += -11               
    if x==9:
        if srodek not in graph[srodek+10]:
            if len(graph[srodek+10]) ==0:
                switch()
            pygame.draw.line(ekran,color,(lenx[0],leny[0]),(lenx[0]+o,leny[0]-o),draw)
            add_edge_undirected(graph,(srodek,srodek+10))
            lenx[0] += o
            leny[0] += -o
            ruchy += [1]
            srodek += +10              
    if x==7:
        if srodek not in graph[srodek-12]:
            if len(graph[srodek-12]) ==0:
                switch()
            pygame.draw.line(ekran,color,(lenx[0],leny[0]),(lenx[0]-o,leny[0]-o),draw)
            add_edge_undirected(graph,(srodek,srodek-12))
            lenx[0] += -o
            leny[0] += -o
            ruchy += [7]
            srodek += -12
    if x==1:
        if srodek not in graph[srodek-10]:
            if len(graph[srodek-10]) ==0:
                switch()
            pygame.draw.line(ekran,color,(lenx[0],leny[0]),(lenx[0]-o,leny[0]+o),draw)
            add_edge_undirected(graph,(srodek,srodek-10))
            lenx[0] += -o
            leny[0] += +o
            ruchy += [5]
            srodek += -10 
    if x==3:
        if srodek not in graph[srodek+12]:
            if len(graph[srodek+12]) ==0:
                switch()
            pygame.draw.line(ekran,color,(lenx[0],leny[0]),(lenx[0]+o,leny[0]+o),draw)
            add_edge_undirected(graph,(srodek,srodek+12))
            lenx[0] += +o
            leny[0] += +o
            ruchy += [3]
            srodek += 12
    #if srodek=102 or srodek = 103 or srodek=104:
      #  print('Gracz #2 Win')
   # if srodek=99 or srodek = 100 or srodek=101:
     #   print('Gracz #1 Win')
def serce():
    while True:    
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP6:                    
                    zmiana(6)
                if event.key == pygame.K_KP2:                    
                    zmiana(2)
                if event.key == pygame.K_KP8:
                    zmiana(8)                                        
                if event.key == pygame.K_KP4:                    
                    zmiana(4)
                if event.key == pygame.K_KP9:                   
                    zmiana(9)
                if event.key == pygame.K_KP7:                    
                    zmiana(7)
                if event.key == pygame.K_KP1:                    
                    zmiana(1)
                if event.key == pygame.K_KP3:                    
                    zmiana(3)
               # if event.key == p
                if event.key == pygame.K_k:
                    mysz = pygame.mouse.get_pos()
                    print(mysz)
                    #switch()
                    print(srodek)                    
                    global gracz,color
                    print(color)
                    print(gracz)
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.draw.rect(ekran, (255,255,255),(0,0,80,30))
        pygame.draw.rect(ekran, (255,255,255),(0,520,140,30))   
        przycisk(srodek,gracz)
        pygame.display.update() 
pygame.draw.circle(ekran,(255,0,0),((xk,yk)),(5),0)
serce()
    
