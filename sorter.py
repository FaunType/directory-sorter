from os import *
from time import *
from tkinter import *
from tkinter import messagebox, filedialog
from gui import CreateGui

class Sorter(CreateGui):

    def __init__(self):
        super().__init__()

        self.dictionary = {
            "HTML": [".html5", ".html", ".htm", ".xhtml"],
            "IMAGES": [".png", ".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".bpg", ".svg",
               ".heif", ".psd", ".jfif"],
            "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"],
            "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  ".pptx"],
            "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
            "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
                    ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
            "PLAINTEXT": [".txt", ".in", ".out"],
            "PDF": [".pdf"],
            "PYTHON": [".py"],
            "XML": [".xml"],
            "EXE": [".exe"],
            "SHELL": [".sh"]
        }

        self.file_types = {
            self.file_type: entry
            for entry, self.file_types in self.dictionary.items()
            for self.file_type in self.file_types
        }

        self.directory = filedialog.askdirectory()
        self.createWidgets()

    def createWidgets(self):
        self.label = Label(self.top_frame, text = f'Garrett\'s Auto Sorter, v1\n\nWould you like to sort \'{self.directory}\'?')
        self.sort_button = Button(self.bottom_frame, text = 'Sort!', command = self.sort)
        self.quit_button = Button(self.bottom_frame, text = 'Quit', command = self.window.destroy)
        self.label.pack(side = 'top')
        self.sort_button.pack(side = 'left')
        self.quit_button.pack(side = 'right')
        self.top_frame.pack()        
        self.bottom_frame.pack()
        mainloop()
    
    def sort(self):
        debug = False
        i = 0
        start_time = time()
        files = listdir(self.directory)

        for file in files:
            _file_name, file_ext = path.splitext(file)

            if file_ext == '':
                continue

            if file_ext in self.file_types:
                directory_path = self.directory+'/'+self.file_types[file_ext]
            else:
                directory_path = self.directory+'/MISC'

            if not path.exists(directory_path):
                mkdir(directory_path)

            replace(self.directory+'/'+file, directory_path+'/'+file)

            i += 1

            if debug == True:
                print(f'{_file_name}\n{file_ext}\n{directory_path}\n{self.file_types[file_ext]}\n{i}\n\n')
        
        end_time = time()
        return messagebox.showinfo('Finished!', f'Sorted {i} files in {str(end_time - start_time)} seconds.')


def main():
    Sorter()

if __name__ == '__main__':
    main()
