class Grafos():
    def __init__(self,vertices:list,adj:list):
        self.vertices = vertices
        self.adj = adj
    def vizinho(self,v1,v2):
        cj = 0
        for j in self.vertices:
            if j == v1:
                for i in self.adj[cj]:
                    if i == v2:
                        return True
            cj += 1
        return False
    def vizinhos(self,v):
        cj = 0
        for j in self.vertices:
            if j == v:
                return self.adj[cj]
            cj += 1
        return('Vazio!')


    def __str__(self):
        mt = ['Vertices : Lista de Adjacência']
        for i,j in zip(self.vertices,self.adj):
            mt.append(f'\n{i}:{j}')
        mt = ' '.join(mt)
        return mt
g = Grafos([1,2,3,4,5],[[2,5],[1,5],[2,4],[2,5,3],[4,1,2]])
print(g.__str__())
if g.vizinho(3,3):
    print('Vizinho')
else:
    print('Não')
print(f'Vizinhos:{g.vizinhos(3)}')