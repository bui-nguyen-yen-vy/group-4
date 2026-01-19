def quyuoc(the):
    hang = ['spades','hearts','diamonds','clubs']

    mahoaso = { 'ace':0, 'king':1, 'queen':2, 'jack':3 }
    chuhoa = { 'ace':'A', 'king':'K', 'queen':'Q', 'jack':'J' }

    bien = {
        'spades':[],
        'hearts':[],
        'diamonds':[],
        'clubs':[]
    }

    for rank, thuhang in the:
        bien[thuhang].append(rank)

    def giatri(rank):
        if rank in mahoaso:
            return mahoaso[rank]
        else:
            return 4

    for thuhang in hang:
        ds = bien[thuhang]
        n = len(ds)
        for i in range(n):
            for j in range(0, n-i-1):
                if giatri(ds[j]) > giatri(ds[j+1]):
                    ds[j], ds[j+1] = ds[j+1], ds[j]

    luu = ""
    for thuhang in hang:
        if len(bien[thuhang]) == 0:
            luu += "-"
        else:
            for rank in bien[thuhang]:
                if rank in chuhoa:
                    luu += chuhoa[rank]
                else:
                    luu += "x"

    return luu
the = [('four', 'spades'), ('nine', 'spades'), ('three', 'hearts'),
 ('five', 'hearts'), ('jack', 'clubs'), ('ten', 'diamonds'),
 ('ace', 'hearts'), ('eight', 'clubs'), ('three', 'spades'),
 ('two', 'hearts'), ('king', 'spades'), ('jack', 'diamonds'),
 ('five', 'hearts')]
output = quyuoc(the)
print(f" Ketqua:{output}")
