# 1
import os


class Directory:

    def __init__(self, dirname: str = 'New_folder'):
        """
        создание папки с именем 'New_folder' по умолчанию
        :param dirname:
        """
        self.dirname = dirname
        #  self.dirpath = path
        os.makedirs(self.dirname, exist_ok=True)

 # 2
    # {'filenames': [файл1, файл2, файл7], 'dirnames': [папка1, папка2]}
    def make_dict(self):
        """
        создает атрибут класса в виде словаря
        :return:
        """
        my_di = {}
        file_list = []
        folder_list = []
        if os.path.isdir(self.dirname):
            elements = os.listdir(self.dirname)
            for element in elements:
                path_to_element = os.path.join(self.dirname, element)
                if os.path.isdir(path_to_element):
                    folder_list.append(path_to_element)
                else:
                    file_list.append(path_to_element)
            my_di.update({'filenames': file_list, 'dirnames': folder_list})
        return my_di

 # 3

    def sort_dict(self, arg: bool):
        """
        сортировка словаря по bool-значению
        """
        new_di = {}
        old_di = self.make_dict()
        sort_list_files = sorted(old_di['filenames'], key=None, reverse=arg)
        sort_list_folders = sorted(old_di['dirnames'], key=None, reverse=arg)
        if sorted(old_di['filenames'], key=None, reverse=False) == sort_list_files:
            new_di['filenames'] = sort_list_files
        else:
            new_di['filenames'] = sort_list_files.sort()
        if sorted(old_di['dirnames'], key=None, reverse=False) == sort_list_folders:
            new_di['dirnames'] = sort_list_folders
        else:
            new_di['dirnames'] = sort_list_folders.sort()
        return new_di

 # 4

    def name_dir(self, name: str):
        """
        создает словарь с полученным именем папки или файла
        :param name:
        :return:
        """
        li1 = self.make_dict()['filenames']
        li2 = self.make_dict()['dirnames']
        new_di = self.make_dict()
        if "." in name:
            li1.append(name)
        else:
            li2.append(name)
        new_di['filenames'] = li1
        new_di['dirnames'] = li2
        return new_di


obj = Directory()
#print(obj.make_dict())
#print(obj.sort_dict(True))
#print(obj.name_dir("tt.txt"))
