from datetime import datetime

def display_menu():
    print("\n=== SISTEM TO-DO LIST PENUGASAN SEDERHANA ===")
    print("1. Tambah Tugas & Deadline")
    print("2. Tandai Tugas Selesai")
    print("3. Edit atau Hapus Tugas")
    print("4. Tampilkan Daftar Tugas")
    print("5. Keluar")

def get_user_choice():
    return input("Pilih menu (1-5): ")

def get_task_input():
    description = input("Masukkan deskripsi tugas: ")
    while True:
        deadline = input("Masukkan deadline tugas (format: YYYY-MM-DD HH:MM, opsional): ")
        if not deadline:
            break
        try:
            datetime.strptime(deadline, "%Y-%m-%d %H:%M")
            break
        except ValueError:
            print("Format deadline salah. Coba lagi.")
    return description, deadline

def display_tasks(tasks):
    if not tasks:
        print("Tidak ada tugas untuk ditampilkan.")
    else:
        print("\nDaftar Tugas:")
        for i, task in enumerate(tasks, start=1):
            status = "✓" if task.get("completed", False) else "✗"
            deadline = task.get("deadline", "-")
            print(f"{i}. [{status}] {task['description']} (Deadline: {deadline})")

def display_message(message):
    print(f"\n{message}\n")

def get_task_index():
    try:
        index = int(input("Masukkan nomor tugas: ")) - 1
        return index
    except ValueError:
        return -1

def get_edit_input():
    new_description = input("Masukkan deskripsi tugas baru: ")
    while True:
        new_deadline = input("Masukkan deadline tugas baru (format: YYYY-MM-DD HH:MM, opsional): ")
        if not new_deadline:
            break
        try:
            datetime.strptime(new_deadline, "%Y-%m-%d %H:%M")
            break
        except ValueError:
            print("Format deadline salah. Coba lagi.")
    return new_description, new_deadline

def confirm_delete():
    return input("Apakah yakin ingin menghapus tugas ini? (y/n): ").lower() == 'y'

def wait_for_enter():
    input("\nTekan ENTER untuk kembali ke menu utama...")
