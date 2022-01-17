from tkinter import *
import os
import shutil
from tkinter import ttk


class FileManager:
    def __init__(self, master):
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        self.frame_footer = ttk.Frame(master)
        self.frame_footer.pack()

        ttk.Label(self.frame_header, text='This script will help you manage files on your computer.')
        ttk.Label(self.frame_footer, text='aaaaby Bartosz Marmołowski')

        self.copy_file_button = ttk.Button(self.frame_content, text='Copy File')
        self.copy_file_button.pack()

        self.delete_file_button = ttk.Button(self.frame_content, text='Delete File')
        self.delete_file_button.pack()

        self.rename_file_button = ttk.Button(self.frame_content, text='Rename File')
        self.rename_file_button.pack()

        self.move_file_button = ttk.Button(self.frame_content, text='Move File')
        self.move_file_button.pack()

        self.make_folder_button = ttk.Button(self.frame_content, text='Make Folder')
        self.make_folder_button.pack()

        self.copy_folder_button = ttk.Button(self.frame_content, text='Copy Folder')
        self.copy_folder_button.pack()

        self.delete_folder_button = ttk.Button(self.frame_content, text='Delete Folder')
        self.delete_folder_button.pack()

        self.list_files_button = ttk.Button(self.frame_content, text='List all Files in Folder')
        self.list_files_button.pack()


def main():
    root = Tk()
    root.title('FileManager')
    file_manager = FileManager(root)
    root.mainloop()


if __name__ == "__main__": main()
