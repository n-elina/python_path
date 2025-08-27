import os.path
import shutil

CURRENT_FILE = os.path.abspath(__file__)
print(CURRENT_FILE)

CURRENT_DIR = os.path.dirname(CURRENT_FILE)
print(CURRENT_DIR)

FILES_DIR = os.path.join(CURRENT_DIR, 'files_to_zip')
print(FILES_DIR)

NAME = os.path.basename(FILES_DIR)
print(NAME)


# if not os.path.exists('../qa_guru/tmp'):
#     os.mkdir('../qa_guru/tmp')
#     print('Created tmp folder')

# shutil.rmtree(os.path.join(CURRENT_DIR, 'tmp2'))