USER_MENU="""Nhập
a - Thêm bộ phim mới
b - Hiển thị danh sach phim
c - Tìm bộ phim theo tên
d - Xóa bộ phim
e - Cập nhật bộ phim
f - Thoát"""

#list[dist]
movies = []

#kiểm tra duy nhất
prves=set()

#Định nghĩa hàm
#Thêm bộ phim mới
def add_move():
    #Nhập
    name = input("Nhập tên phim: ")

    #kiểm tra trùng lặp
    while name in prves:
        print("Bộ phim đã có sẵn, Vui lòng nhập lại!")
        name = input("Nhập tên phim: ")
    daodien = input("Nhập tên đạo diễn phim: ")
    release_year = input("Nhập năm phát hành phim: ")

    #tạo bộ phim
    movie ={
        'name'  :name,
        'daodien'   :daodien,
        'release_year'  :release_year
    }

    #Thêm vào danh sách
    movies.append(movie)
    prves.add(name)

def show_movies():
    movie_name=movies['name']
    movie_daodien=movies['daodien']
    movie_release_year=movies['release_year']

    #hiển thị
    print("Tên: {movie_name}")
    print("Đạo diễn: {movie_daodien}")
    print("Năm phát hành: {movie_release_year}")
