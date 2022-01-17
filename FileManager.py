from tkinter import *
import os
import shutil
from tkinter import ttk


class FileManager:
    def __init__(self, master):
        self.frame_header = ttk.Frame(master)
        self.frame_header.grid(row=0, columnspan=2)

        self.frame_changelog = ttk.Frame(master)
        self.frame_changelog.grid(row=1, columnspan=2)

        self.frame_buttons = ttk.Frame(master)
        self.frame_buttons.grid(row=2, column=0)

        self.frame_files_list = ttk.Frame(master)
        self.frame_files_list.grid(row=2, column=1)

        self.frame_footer = ttk.Frame(master)
        self.frame_footer.grid(row=3, column=1)

        ttk.Label(self.frame_header, text='This script will help you manage files on your computer.').pack(pady=20)
        ttk.Label(self.frame_footer, text='by Bartosz Marmołowski', font=('Arial', 7)).pack()

        self.changelog_field = Text(self.frame_changelog, width=50, height=10)
        self.changelog_field.pack(padx=5, pady=5)

        self.copy_file_button = ttk.Button(self.frame_buttons, text='Copy File')
        self.copy_file_button.pack()
        self.delete_file_button = ttk.Button(self.frame_buttons, text='Delete File')
        self.delete_file_button.pack()
        self.rename_file_button = ttk.Button(self.frame_buttons, text='Rename File')
        self.rename_file_button.pack()
        self.move_file_button = ttk.Button(self.frame_buttons, text='Move File')
        self.move_file_button.pack()
        self.make_folder_button = ttk.Button(self.frame_buttons, text='Make Folder')
        self.make_folder_button.pack()
        self.copy_folder_button = ttk.Button(self.frame_buttons, text='Copy Folder')
        self.copy_folder_button.pack()
        self.delete_folder_button = ttk.Button(self.frame_buttons, text='Delete Folder')
        self.delete_folder_button.pack()
        self.list_files_button = ttk.Button(self.frame_buttons, text='List all Files in Folder')
        self.list_files_button.pack()

        self.files_list_field = Text(self.frame_files_list, width=25, height=20)
        self.files_list_field.pack(padx=5, pady=5)


def main():
    root = Tk()
    root.title('FileManager')
    file_manager = FileManager(root)
    root.mainloop()


if __name__ == "__main__": main()
