import tkinter as tk
from tkinter import messagebox

def tinh_tien():
    try:
        # Lấy dữ liệu từ người dùng
        chieu_dai = float(entry_dai.get())
        chieu_rong = float(entry_rong.get())
        so_luong = int(so_luong_var.get())  # Lấy số lượng từ biến số lượng

        # Tính diện tích (cm2 -> m2 nếu cần)
        if unit_var.get() == "cm":
            dien_tich = (chieu_dai * chieu_rong) / 10000  # cm2 -> m2
        else:
            dien_tich = chieu_dai * chieu_rong  # m2 -> m2

        # Định nghĩa giá cơ bản
        gia_co_ban = dien_tich

        # Danh sách các yếu tố phụ và mức giá của chúng
        phu_phi = {
            "decal": 5000,
            "can_mang": 2000,
            "soi_day": 3000,
            "soi_trung_quoc": 1000
        }

        # Cộng thêm các phí phụ nếu chọn
        if phu_phi_var.get() == "decal":
            gia_co_ban += dien_tich * phu_phi["decal"]
        elif phu_phi_var.get() == "can_mang":
            gia_co_ban += dien_tich * phu_phi["can_mang"]
        elif phu_phi_var.get() == "soi_day":
            gia_co_ban += dien_tich * phu_phi["soi_day"]
        elif phu_phi_var.get() == "soi_trung_quoc":
            gia_co_ban += dien_tich * phu_phi["soi_trung_quoc"]

        # Áp dụng số lượng
        gia_co_ban *= so_luong

        # Hiển thị kết quả
        gia_co_ban = round(gia_co_ban, -3)  # Làm tròn đến bội số gần nhất của 10.000
        ket_qua_label.config(text=f"Tổng tiền: {gia_co_ban:,} VNĐ")

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng số liệu.")
    except Exception as e:
        messagebox.showerror("Lỗi", "Đã có lỗi xảy ra.")

def convert_units():
    try:
        # Lấy giá trị chiều dài và chiều rộng
        chieu_dai = float(entry_dai.get())
        chieu_rong = float(entry_rong.get())

        # Chuyển đổi giữa cm và m
        if unit_var.get() == "cm":
            # Chuyển đổi từ cm sang m
            entry_dai.delete(0, tk.END)
            entry_rong.delete(0, tk.END)
            entry_dai.insert(0, chieu_dai / 100)  # cm -> m
            entry_rong.insert(0, chieu_rong / 100)  # cm -> m
            unit_var.set("m")  # Đổi trạng thái đơn vị
            unit_label.config(text="Đơn vị: m")
            label_dai.config(text="Chiều dài (m):")  # Cập nhật nhãn chiều dài
            label_rong.config(text="Chiều rộng (m):")  # Cập nhật nhãn chiều rộng
        else:
            # Chuyển đổi từ m sang cm
            entry_dai.delete(0, tk.END)
            entry_rong.delete(0, tk.END)
            entry_dai.insert(0, chieu_dai * 100)  # m -> cm
            entry_rong.insert(0, chieu_rong * 100)  # m -> cm
            unit_var.set("cm")  # Đổi trạng thái đơn vị
            unit_label.config(text="Đơn vị: cm")
            label_dai.config(text="Chiều dài (cm):")  # Cập nhật nhãn chiều dài
            label_rong.config(text="Chiều rộng (cm):")  # Cập nhật nhãn chiều rộng

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng số liệu để chuyển đổi.")

def tang_so_luong():
    so_luong_var.set(int(so_luong_var.get()) + 1)
    so_luong_label.config(text=f"{so_luong_var.get()}")  # Cập nhật số lượng hiển thị

def giam_so_luong():
    if int(so_luong_var.get()) > 1:
        so_luong_var.set(int(so_luong_var.get()) - 1)
        so_luong_label.config(text=f"{so_luong_var.get()}")  # Cập nhật số lượng hiển thị

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Tính Tiền")

# Các nhãn và ô nhập liệu
label_dai = tk.Label(window, text="Chiều dài (cm):")
label_dai.grid(row=0, column=0, padx=5, pady=5)
entry_dai = tk.Entry(window)
entry_dai.grid(row=0, column=1, padx=5, pady=5)

label_rong = tk.Label(window, text="Chiều rộng (cm):")
label_rong.grid(row=1, column=0, padx=5, pady=5)
entry_rong = tk.Entry(window)
entry_rong.grid(row=1, column=1, padx=5, pady=5)

# Biến lưu số lượng và các nút tăng/giảm
so_luong_var = tk.IntVar(value=1)

label_so_luong = tk.Label(window, text="Số lượng:")
label_so_luong.grid(row=2, column=0, padx=5, pady=5)

tang_button = tk.Button(window, text="+", command=tang_so_luong)
tang_button.grid(row=2, column=1, padx=5, pady=5, sticky="w")

giam_button = tk.Button(window, text="-", command=giam_so_luong)
giam_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")

# Hiển thị số lượng
so_luong_label = tk.Label(window, text=f"{so_luong_var.get()}")
so_luong_label.grid(row=2, column=1, padx=5, pady=5)

# Nút chuyển đổi đơn vị
unit_var = tk.StringVar(value="cm")
convert_button = tk.Button(window, text="Chuyển đổi đơn vị", command=convert_units)
convert_button.grid(row=3, column=0, columnspan=1, padx=5, pady=5)

# Nhãn hiển thị đơn vị
unit_label = tk.Label(window, text="Đơn vị: cm")
unit_label.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

# Các radio button để chọn chỉ 1 tùy chọn
phu_phi_var = tk.StringVar(value="none")

decal_radio = tk.Radiobutton(window, text="Decal", variable=phu_phi_var, value="decal")
decal_radio.grid(row=3+1, column=0, padx=5, pady=5, sticky="w")

can_mang_radio = tk.Radiobutton(window, text="Decal + Cán màng", variable=phu_phi_var, value="can_mang")
can_mang_radio.grid(row=4+1, column=0, padx=5, pady=5, sticky="w")

soi_day_radio = tk.Radiobutton(window, text="Sợi dày", variable=phu_phi_var, value="soi_day")
soi_day_radio.grid(row=5+1, column=0, padx=5, pady=5, sticky="w")

soi_trung_quoc_radio = tk.Radiobutton(window, text="Sợi trung quốc", variable=phu_phi_var, value="soi_trung_quoc")
soi_trung_quoc_radio.grid(row=6+1, column=0, padx=5, pady=5, sticky="w")

# Nút tính tiền
tinh_tien_button = tk.Button(window, text="Tính tiền", command=tinh_tien)
tinh_tien_button.grid(row=7+1, column=0, columnspan=2, padx=5, pady=10)



# Nhãn hiển thị kết quả
ket_qua_label = tk.Label(window, text="Tổng tiền:")
ket_qua_label.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()
