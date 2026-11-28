from enum import Enum

class Biome(Enum):
    T = "Trees"
    G = "Garden"
    O = "Orchard"
    D = "Dirt"
    S = "Swamp" 
    F = "Fountain"
    C = "Center"
    W = "Wall"




if __name__ == "__main__":
    t = Biome.T
    print(t) # should be T
    print(t.value) # Trees
    print(t.name) # T