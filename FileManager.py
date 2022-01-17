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

        ttk.Label(self.frame_header, text='This script will help you manage files on your computer.').pack()
        ttk.Label(self.frame_footer, text='by Bartosz Marmołowski').pack(side='bottom')

        copy_file_button = ttk.Button(self.frame_content, text='Copy File')
        copy_file_button.pack()

        delete_file_button = ttk.Button(self.frame_content, text='Delete File')
        delete_file_button.pack()

        rename_file_button = ttk.Button(self.frame_content, text='Rename File')
        rename_file_button.pack()

        move_file_button = ttk.Button(self.frame_content, text='Move File')
        move_file_button.pack()

        make_folder_button = ttk.Button(self.frame_content, text='Make Folder')
        make_folder_button.pack()

        copy_folder_button = ttk.Button(self.frame_content, text='Copy Folder')
        copy_folder_button.pack()

        delete_folder_button = ttk.Button(self.frame_content, text='Delete Folder')
        delete_folder_button.pack()

        list_files_button = ttk.Button(self.frame_content, text='List all Files in Folder')
        list_files_button.pack()




def main():
    root = Tk()
    root.title('FileManager')
    file_manager = FileManager(root)
    root.mainloop()


if __name__ == "__main__": main()
