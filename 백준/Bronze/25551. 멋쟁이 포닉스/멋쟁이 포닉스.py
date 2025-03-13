Mw, Mb = map(int, input().split())
Tw, Tb = map(int, input().split())
Pw, Pb = map(int, input().split())

Tb_Set = min(Mw, Pw, Tb)
Tw_Set = min(Mb, Pb, Tw)

print(min((Tb_Set + Tw_Set), (min(Tb_Set, Tw_Set) * 2 + 1)))