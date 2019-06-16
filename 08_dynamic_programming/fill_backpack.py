# 물건의 가격과 파운드
objects = {}
objects["guitar"] = {"price": 1500, "size": 1}
objects["stereo"] = {"price": 3000, "size": 4}
objects["laptop"] = {"price": 2000, "size": 3}

# 격자의 행 정보 : 물건
grid_row = ["guitar", "stereo", "laptop"]

# 격자의 열 정보 : 파운드
grid_col = [1, 2, 3, 4]

# 격자
grid = [
    [],
    [], 
    []
]

for i in range(len(grid_row)):
    for j in range(len(grid_col)):
        name = grid_row[i] # 현재 행의 물건
        size = grid_col[j] # 현재 열의 파운드
        obj_price = objects[name]["price"] # 해당 물건의 가격
        obj_size = objects[name]["size"] # 해당 물건의 파운드
        price = obj_price if i == 0 and size >= obj_size else 0
        if i > 0:
            if size < obj_size:
                price = grid[i-1][j]
            else:
                if grid[i-1][j] < obj_price:
                    price = obj_price
                else:
                    price = obj_price + grid[i-1][grid_col.index(size - obj_size)]
        grid[i].append(price)

print(grid)