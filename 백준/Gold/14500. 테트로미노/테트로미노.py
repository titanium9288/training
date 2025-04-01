N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]


# 회전시킨 블록 list 생성
def generate_rotations(base_shape):
    rotated_shapes = [base_shape]

    for _ in range(3):
        rotated = []
        for r, c in rotated_shapes[-1]:
            rotated.append((-c, r))
        rotated_shapes.append(rotated)

    return rotated_shapes


# 입력 받은 블록을 대칭시켜서 원본과 return
def generate_reflection(base_shape):
    reflected = []
    for r, c in base_shape:
        reflected.append((-r, c))
    return reflected


# 대칭과 회전을 이용해서 모든 변형 생성
def generate_all_variants(base_shape):
    variants = set()

    for rotation in generate_rotations(base_shape):
        reflected = generate_reflection(rotation)
        variants.add(normalize_shape(rotation))
        variants.add(normalize_shape(reflected))

    return variants


# 좌표를 0, 0 기준으로 변환
def normalize_shape(shape):
    min_r = min(r for r, c in shape)
    min_c = min(c for r, c in shape)

    normalized = tuple(sorted([(r - min_r, c - min_c) for r, c in shape]))
    return normalized


# 기본 테트리미노 만들기
# 모든 미노는 0, 0부터 시작한다.
I_mino = [(0, 0), (1, 0), (2, 0), (3, 0)]
O_mino = [(0, 0), (1, 0), (0, 1), (1, 1)]
L_mino = [(0, 0), (1, 0), (2, 0), (2, 1)]
S_mino = [(0, 0), (1, 0), (1, 1), (2, 1)]
T_mino = [(0, 0), (0, 1), (1, 1), (0, 2)]

base_shapes = [I_mino, O_mino, L_mino, S_mino, T_mino]
all_unique_variants = set()

# 모든 기본 미노에 대해 19개의 (1 + 2 + 4 + 4 + 8) 변형 생성, 중복 제거
for base_shape in base_shapes:
    for variant in generate_all_variants(base_shape):
        all_unique_variants.add(variant)


# 브루트포스
answer = 0

for r in range(N):
    for c in range(M):
        for shape in all_unique_variants:
            shape_total = 0
            for dr, dc in shape:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < N) and (0 <= nc < M):
                    shape_total += paper[nr][nc]
                else:
                    shape_total = 0
                    break
            answer = max(answer, shape_total)

print(answer)
