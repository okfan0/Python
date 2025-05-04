USER_MENU = """Nhập:
a - Thêm bộ phim mới
b - Hiển thị danh sách phim
c - Tìm bộ phim theo tên
d - Xóa bộ phim
e - Cập nhật bộ phim
f - Thoát
Lựa chọn bộ phim: """

# Danh sách phim (list chứa các dict)
movies = []

# Tập hợp để kiểm tra tên phim duy nhất
prves = set()

# ======================== CÁC HÀM ========================

# Thêm bộ phim mới
def add_movie():
    name = input("Nhập tên phim: ")
    
    while name in prves:
        print("Bộ phim đã có sẵn, vui lòng nhập lại!")
        name = input("Nhập tên phim: ")

    daodien = input("Nhập tên đạo diễn phim: ")
    release_year = input("Nhập năm phát hành phim: ")

    movie = {
        'name': name,
        'daodien': daodien,
        'release_year': release_year
    }

    movies.append(movie)
    prves.add(name)
    print("✅ Thêm phim thành công!")

# Hiển thị thông tin 1 bộ phim
def show_movie(movie):
    print(f"Tên: {movie['name']}")
    print(f"Đạo diễn: {movie['daodien']}")
    print(f"Năm phát hành: {movie['release_year']}")

# Hiển thị tất cả phim
def show_movies():
    if movies:
        for idx, movie in enumerate(movies, start=1):
            print(f"\n🎬 THÔNG TIN BỘ PHIM {idx}")
            show_movie(movie)
    else:
        print("❌ Danh sách phim trống.")

# Tìm bộ phim theo tên
def search_movie():
    if movies:
        movie_name = input("Nhập tên bộ phim: ")

        for idx, movie in enumerate(movies, start=1):
            if movie_name == movie['name']:
                print(f"\n🔍 THÔNG TIN BỘ PHIM {idx}")
                show_movie(movie)
                break
        else:
            print(f"❌ Không tìm thấy bộ phim '{movie_name}'.")
    else:
        print("❌ Danh sách phim trống!")

# Xóa bộ phim theo tên
def remove_movie():
    if movies:
        movie_name = input("Nhập tên bộ phim cần xóa: ")

        for idx, movie in enumerate(movies):
            if movie['name'] == movie_name:
                del movies[idx]
                prves.remove(movie_name)
                print("🗑️ Đã xóa bộ phim thành công.")
                break
        else:
            print(f"❌ Không tìm thấy bộ phim '{movie_name}'.")
    else:
        print("❌ Danh sách phim trống!")

# Cập nhật thông tin bộ phim
def update_movie():
    if movies:
        movie_name = input("Nhập tên bộ phim cần cập nhật: ")

        for idx, movie in enumerate(movies):
            if movie['name'] == movie_name:
                movie['daodien'] = input("Nhập tên đạo diễn mới: ")
                movie['release_year'] = input("Nhập năm phát hành mới: ")
                print("✅ Cập nhật bộ phim thành công.")
                break
        else:
            print(f"❌ Không tìm thấy bộ phim '{movie_name}'.")
    else:
        print("❌ Danh sách phim trống!")

# ======================== CHƯƠNG TRÌNH CHÍNH ========================

# Dict chứa các lựa chọn và hàm tương ứng
operations = {
    'a': add_movie,
    'b': show_movies,
    'c': search_movie,
    'd': remove_movie,
    'e': update_movie
}

# Vòng lặp chính cho đến khi người dùng chọn 'f' để thoát
user_choice = input(USER_MENU)

while user_choice != 'f':
    if user_choice in operations:
        operations[user_choice]()
    else:
        print("❗ Lựa chọn không hợp lệ. Vui lòng thử lại.")

    print()  # Dòng trắng cho dễ nhìn
    user_choice = input(USER_MENU)

print("👋 Chương trình kết thúc. Cảm ơn bạn đã sử dụng!")
