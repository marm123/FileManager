from distutils.dir_util import copy_tree
from tkinter import *
import os
import shutil
from tkinter import ttk, filedialog, messagebox, simpledialog
from datetime import datetime


class FileManager:
    def __init__(self, master):

        self.frame_header = ttk.Frame(master)
        self.frame_header.grid(row=0, columnspan=2)

        self.frame_changelog = ttk.Frame(master)
        self.frame_changelog.grid(row=1, columnspan=2)

        self.frame_buttons = ttk.Frame(master)
        self.frame_buttons.grid(row=2, column=0)

        self.frame_files_name_type = ttk.Frame(master)
        self.frame_files_name_type.grid(row=2, column=1)

        self.frame_footer = ttk.Frame(master)
        self.frame_footer.grid(row=3, column=1, columnspan=2)

        ttk.Label(self.frame_header, text='This script will help you manage files on your computer.').grid(row=0,
                                                                                                           column=1)
        ttk.Label(self.frame_buttons, text='Choose your action:').grid(row=1, column=0, pady=(0, 15))
        ttk.Label(self.frame_footer, text='\t\tby Bartosz Marmołowski', font=('Arial', 7)).grid(row=0, column=1)

        self.changelog_field = Text(self.frame_changelog, width=70, height=10, font=('Arial', 7), wrap=WORD)
        self.changelog_field.grid(row=0, column=0, columnspan=2, padx=(5, 0), pady=5)
        self.changelog_scrollbar = ttk.Scrollbar(self.frame_changelog, command=self.changelog_field.yview)
        self.changelog_scrollbar.grid(row=0, column=2, sticky='nse')
        self.changelog_field['yscrollcommand'] = self.changelog_scrollbar.set
        self.changelog_field.config(state=DISABLED)

        self.copy_file_button = ttk.Button(self.frame_buttons, text='Copy File', command=self.copy_file)
        self.copy_file_button.grid(row=2, sticky='ew', padx=10)
        self.delete_file_button = ttk.Button(self.frame_buttons, text='Delete File', command=self.delete_file)
        self.delete_file_button.grid(row=3, sticky='ew', padx=10)
        self.rename_file_button = ttk.Button(self.frame_buttons, text='Rename File', command=self.rename_file)
        self.rename_file_button.grid(row=4, sticky='ew', padx=10)
        self.move_file_button = ttk.Button(self.frame_buttons, text='Move File', command=self.move_file)
        self.move_file_button.grid(row=5, sticky='ew', padx=10)
        self.make_folder_button = ttk.Button(self.frame_buttons, text='Create Folder', command=self.create_folder)
        self.make_folder_button.grid(row=6, sticky='ew', padx=10)
        self.copy_folder_button = ttk.Button(self.frame_buttons, text='Copy Folder', command=self.copy_folder)
        self.copy_folder_button.grid(row=7, sticky='ew', padx=10)
        self.delete_folder_button = ttk.Button(self.frame_buttons, text='Delete Folder')
        self.delete_folder_button.grid(row=8, sticky='ew', padx=10)
        self.list_files_button = ttk.Button(self.frame_buttons, text='List all Files in Folder',
                                            command=self.list_files_in_dir)
        self.list_files_button.grid(row=9, sticky='ew', ipadx=10, padx=10)
        self.list_files_button = ttk.Button(self.frame_buttons, text='Export Actions Log')
        self.list_files_button.grid(row=10, sticky='ew', ipadx=10, padx=10)

        self.frame_file_list = Frame(self.frame_files_name_type)
        self.frame_file_list.grid(row=1, column=0)
        self.file_name_list_field = Text(self.frame_file_list, width=25, height=25, wrap=NONE, font=('Arial', 7))
        self.file_name_list_field.grid(row=1, column=0)
        self.file_name_list_field.config(state=DISABLED)

        self.file_type_field = Text(self.frame_file_list, width=12, height=25, wrap=NONE, font=('Arial', 7))
        self.file_type_field.grid(row=1, column=1)
        self.file_type_field.config(state=DISABLED)

        self.file_list_scrollbar = Scrollbar(self.frame_file_list)
        self.file_list_scrollbar.grid(row=1, column=2, sticky='nsew')
        self.file_list_scrollbar['command'] = self.scrollbar_func
        self.file_name_list_field['yscrollcommand'] = self.text_scroll_func
        self.file_type_field['yscrollcommand'] = self.text_scroll_func

        self.file_name_scrollbar = Scrollbar(self.frame_file_list, orient='horizontal',
                                             command=self.file_name_list_field.xview)
        self.file_name_scrollbar.grid(row=2, column=0, sticky='we')
        self.file_name_list_field['xscrollcommand'] = self.file_name_scrollbar.set
        self.file_type_scrollbar = Scrollbar(self.frame_file_list, orient='horizontal',
                                             command=self.file_type_field.xview)
        self.file_type_scrollbar.grid(row=2, column=1, sticky='we')
        self.file_type_field['xscrollcommand'] = self.file_type_scrollbar.set

    def scrollbar_func(self, *args):
        self.file_name_list_field.yview(*args)
        self.file_type_field.yview(*args)

    def text_scroll_func(self, *args):
        self.file_list_scrollbar.set(*args)
        self.scrollbar_func('moveto', args[0])

    def copy_file(self):
        original_location = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Select a file to copy"
        )
        if not original_location:
            return
        copied_file_name = os.path.split(original_location)[1]
        original_location_name = os.path.split(original_location)[0]

        destination_location = filedialog.askdirectory(
            title='Choose destination'
        )
        if not destination_location:
            return
        potential_destination = os.path.join(destination_location, copied_file_name)
        if original_location_name == destination_location:
            messagebox.showerror(title='Same location!',
                                 message='Chosen destination is the same as original file location!')
            return
        if os.path.exists(potential_destination):
            question = messagebox.askyesno(title='File already exists!',
                                           message='Do you wish to overwrite existing file with the same name?')
            if not question:
                return
        shutil.copy(original_location, destination_location)
        messagebox.showinfo(title='File copied.', message='File copied successfully!')
        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')
        self.changelog_field.config(state=NORMAL)
        self.changelog_field.insert('0.0',
                                    f'[{current_time}] Copied file {copied_file_name} from '
                                    f'{original_location_name} to {destination_location}.\n\n')
        self.changelog_field.insert('0.0', 'COPY FILE operation:\n')
        self.changelog_field.config(state=DISABLED)

    def delete_file(self):
        file_location = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Select a file to delete"
        )
        if not file_location:
            return
        question = messagebox.askyesno(title='Confirmation required.',
                                       message='Are you sure you want to delete this file?')
        if not question:
            return
        os.remove(file_location)
        messagebox.showinfo(title='File deleted.', message='File deleted successfully!')
        deleted_file_name = os.path.split(file_location)[1]
        deleted_file_location = os.path.split(file_location)[0]
        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')
        self.changelog_field.config(state=NORMAL)
        self.changelog_field.insert('0.0',
                                    f'[{current_time}] Deleted file {deleted_file_name} from '
                                    f'{deleted_file_location}.\n\n')
        self.changelog_field.insert('0.0', 'DELETE FILE operation:\n')
        self.changelog_field.config(state=DISABLED)

    def rename_file(self):
        file_location = filedialog.askopenfilename()
        if not file_location:
            return
        file_location_dir = os.path.dirname(file_location)
        extension = os.path.splitext(file_location)[1]
        original_file = os.path.split(file_location)[1]
        original_file_name = os.path.splitext(original_file)[0]
        new_filename = simpledialog.askstring(title='New file name.', prompt='Enter new file name:')
        if new_filename is None:
            return
        elif new_filename == '':
            messagebox.showerror(title='File name error!', message='No new name was provided!')
            return
        elif original_file_name == new_filename:
            messagebox.showerror(title='File name error!', message='New file name is the same as the original one!')
            return
        else:
            question = messagebox.askyesno(title='Confirmation required.',
                                           message=f'Are you sure you want to rename your file to \'{new_filename}\'?')
            if not question:
                return
        renamed_file_location = os.path.join(file_location_dir, new_filename + extension)
        os.rename(file_location, renamed_file_location)
        messagebox.showinfo(title='File renamed.', message='File renamed successfully!')
        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')
        self.changelog_field.config(state=NORMAL)
        self.changelog_field.insert('0.0',
                                    f'[{current_time}] Renamed file {original_file} to '
                                    f'{new_filename + extension} inside {file_location_dir}.\n\n')
        self.changelog_field.insert('0.0', 'RENAME FILE operation:\n')
        self.changelog_field.config(state=DISABLED)

    def move_file(self):
        original_location = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Select a file to move"
        )
        if not original_location:
            return
        moved_file_name = os.path.split(original_location)[1]
        original_location_name = os.path.split(original_location)[0]

        destination_location = filedialog.askdirectory(
            title='Choose destination'
        )
        if not destination_location:
            return
        potential_destination = os.path.join(destination_location, moved_file_name)
        if original_location_name == destination_location:
            messagebox.showerror(title='Same location!',
                                 message='Chosen destination is the same as original file location!')
            return
        if os.path.exists(potential_destination):
            question = messagebox.askyesno(title='File already exists!',
                                           message='Do you wish to overwrite existing file with the same name?')
            if not question:
                return
        shutil.move(original_location, destination_location)
        messagebox.showinfo(title='File moved.', message='File moved successfully!')
        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')
        self.changelog_field.config(state=NORMAL)
        self.changelog_field.insert('0.0',
                                    f'[{current_time}] Moved file {moved_file_name} from '
                                    f'{original_location_name} to {destination_location}.\n\n')
        self.changelog_field.insert('0.0', 'MOVE FILE operation:\n')
        self.changelog_field.config(state=DISABLED)

    def create_folder(self):
        new_folder_location = filedialog.askdirectory()
        if not new_folder_location:
            return
        new_folder_name = simpledialog.askstring(title='Folder name.',
                                                 prompt='Enter folder name that you would like to create:')
        new_folder = os.path.join(new_folder_location, new_folder_name)
        if os.path.exists(new_folder):
            messagebox.showerror(title='Folder exists!',
                                 message=f'Folder with that name already exists in {new_folder_location}')
        else:
            os.mkdir(new_folder)
            messagebox.showinfo(title='Folder created.', message='Folder created successfully!')
        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')
        self.changelog_field.config(state=NORMAL)
        self.changelog_field.insert('0.0',
                                    f'[{current_time}] Created folder {new_folder_name} in '
                                    f'{new_folder_location}.\n\n')
        self.changelog_field.insert('0.0', 'CREATE FOLDER operation:\n')
        self.changelog_field.config(state=DISABLED)

    def copy_folder(self):
        folder_to_copy = filedialog.askdirectory()
        if not folder_to_copy:
            return
        folder_destination = filedialog.askdirectory()
        if not folder_destination:
            return
        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')
        try:
            folder_destination_name = os.path.join(folder_destination, os.path.basename(folder_to_copy))
            os.mkdir(folder_destination_name)
            copy_tree(folder_to_copy, folder_destination_name)
        except FileExistsError:
            folder_destination_name = os.path.join(folder_destination, os.path.basename(folder_to_copy + ' - copy'))
            os.mkdir(folder_destination_name)
            copy_tree(folder_to_copy, folder_destination_name)
        self.changelog_field.config(state=NORMAL)
        self.changelog_field.insert('0.0',
                                    f'[{current_time}] Copied folder {folder_to_copy} into '
                                    f'{folder_destination}.\n\n')
        self.changelog_field.insert('0.0', 'COPY FOLDER operation:\n')
        self.changelog_field.config(state=DISABLED)

    def list_files_in_dir(self):
        folderList = filedialog.askdirectory()
        if not folderList:
            return
        self.file_name_list_field.config(state=NORMAL)
        self.file_type_field.config(state=NORMAL)
        self.file_name_list_field.delete(1.0, END)
        self.file_type_field.delete(1.0, END)
        for file in os.listdir(folderList):
            file_name = os.path.splitext(file)[0]
            file_type = os.path.splitext(file)[1]
            self.file_name_list_field.insert(END, file_name + '\n')
            if file_type == '':
                self.file_type_field.insert(END, 'folder' + '\n')
            else:
                self.file_type_field.insert(END, file_type + '\n')
        self.file_name_list_field.config(state=DISABLED)
        self.file_type_field.config(state=DISABLED)


def main():
    root = Tk()
    root.title('FileManager')
    file_manager = FileManager(root)
    root.mainloop()


if __name__ == "__main__": main()
