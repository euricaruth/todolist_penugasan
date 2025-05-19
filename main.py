from todo import TodoList
from ui import (
    display_menu,
    get_user_choice,
    get_task_input,
    display_tasks,
    display_message,
    get_task_index,
    get_edit_input,
    confirm_delete,
    wait_for_enter
)

def main():
    todo_list = TodoList()
    todo_list.load_tasks()

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == '1':  # Tambah Tugas & Deadline
            description, deadline = get_task_input()
            todo_list.add_task(description, deadline)
            display_message("Tugas berhasil ditambahkan.")
            wait_for_enter()
        elif choice == '2':  # Tandai Tugas Selesai
            display_tasks(todo_list.get_all_tasks())
            index = get_task_index()
            if todo_list.mark_task_completed(index):
                display_message("Tugas berhasil ditandai selesai.")
            else:
                display_message("Nomor tugas tidak valid.")
            wait_for_enter()
        elif choice == '3':  # Edit atau Hapus Tugas
            display_tasks(todo_list.get_all_tasks())
            index = get_task_index()
            action = input("Ketik 'e' untuk edit, 'h' untuk hapus: ").lower()
            if action == 'e':
                new_description, new_deadline = get_edit_input()
                if todo_list.edit_task(index, new_description, new_deadline):
                    display_message("Tugas berhasil diedit.")
                else:
                    display_message("Nomor tugas tidak valid.")
            elif action == 'h':
                if confirm_delete():
                    if todo_list.delete_task(index):
                        display_message("Tugas berhasil dihapus.")
                    else:
                        display_message("Nomor tugas tidak valid.")
                else:
                    display_message("Penghapusan tugas dibatalkan.")
            else:
                display_message("Aksi tidak dikenal.")
            wait_for_enter()
        elif choice == '4':  # Tampilkan Daftar Tugas
            display_tasks(todo_list.get_all_tasks())
            wait_for_enter()
        elif choice == '5':  # Keluar
            todo_list.save_tasks()
            display_message("Terima kasih telah menggunakan sistem.")
            break
        else:
            display_message("Pilihan tidak valid. Silakan coba lagi.")
            wait_for_enter()

if __name__ == "__main__":
    main()
