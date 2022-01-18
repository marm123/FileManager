from tkinter import *
import os
import shutil
from tkinter import ttk, filedialog, messagebox
from datetime import datetime


class FileManager:
    def __init__(self, master):

        self.now = datetime.now()
        self.current_time = self.now.strftime('%H:%M:%S')

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
        ttk.Label(self.frame_buttons, text='Choose your action:').grid(row=1, column=0, pady=(0, 25))
        ttk.Label(self.frame_footer, text='by Bartosz Marmołowski', font=('Arial', 7)).pack()

        self.changelog_field = Text(self.frame_changelog, width=70, height=10, font=('Arial', 7), wrap=WORD)
        self.changelog_field.grid(row=0, column=0, columnspan=2, padx=(5, 0), pady=5)
        self.changelog_scrollbar = ttk.Scrollbar(self.frame_changelog, command=self.changelog_field.yview)
        self.changelog_scrollbar.grid(row=0, column=2, sticky='nse')
        self.changelog_field['yscrollcommand'] = self.changelog_scrollbar.set

        self.copy_file_button = ttk.Button(self.frame_buttons, text='Copy File', command=self.copy_file)
        self.copy_file_button.grid(row=2)
        self.delete_file_button = ttk.Button(self.frame_buttons, text='Delete File')
        self.delete_file_button.grid(row=3)
        self.rename_file_button = ttk.Button(self.frame_buttons, text='Rename File')
        self.rename_file_button.grid(row=4)
        self.move_file_button = ttk.Button(self.frame_buttons, text='Move File')
        self.move_file_button.grid(row=5)
        self.make_folder_button = ttk.Button(self.frame_buttons, text='Make Folder')
        self.make_folder_button.grid(row=6)
        self.copy_folder_button = ttk.Button(self.frame_buttons, text='Copy Folder')
        self.copy_folder_button.grid(row=7)
        self.delete_folder_button = ttk.Button(self.frame_buttons, text='Delete Folder')
        self.delete_folder_button.grid(row=8)
        self.list_files_button = ttk.Button(self.frame_buttons, text='List all Files in Folder')
        self.list_files_button.grid(row=9)

        self.files_list_field = Text(self.frame_files_list, width=25, height=20)
        self.files_list_field.pack(padx=5, pady=5)

    def copy_file(self):
        original_location = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Please select a file:"
        )

        copied_file_name = os.path.split(original_location)[1]
        original_location_name = os.path.split(original_location)[0]
        destination_location = filedialog.askdirectory()
        potential_destination = os.path.join(destination_location, copied_file_name)
        if os.path.exists(potential_destination):
            question = messagebox.askyesno(title='File already exists!',
                                           message='Do you wish to overwrite existing file?')
            if not question:
                return
        shutil.copy(original_location, destination_location)
        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')
        self.changelog_field.insert('0.0',
                                    f'[{current_time}] copied file {copied_file_name} from '
                                    f'{original_location_name} to {destination_location}\n')
        self.changelog_field.insert('0.0', 'COPY FILE operation\n')


def main():
    root = Tk()
    root.title('FileManager')
    file_manager = FileManager(root)
    root.mainloop()


if __name__ == "__main__": main()
