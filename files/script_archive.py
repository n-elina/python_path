from zipfile import ZipFile


with ZipFile('../qa_guru/tmp/40348747.zip') as zip_file:
    print(zip_file.namelist())
    text = zip_file.read('40348747.pdf')
    # print(text)
    zip_file.extract('40348747.pdf', path='../qa_guru/tmp')
