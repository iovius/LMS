#funkcija za shranjevanje matrik
def save_float_mtx(filename, M):
    h, w = M.shape
    f = open(filename,'w')
    
    for v in range(h):
        for u in range(w):
            f.write(str(M[v, u])+' ')
        f.write('\n')
        
    f.close()
