import os.path

from pypdf import PdfReader


reader = PdfReader('../qa_guru/tmp/testing.pdf')

print(reader.pages)
print(len(reader.pages))

print(reader.pages[0].extract_text())

assert 'В  разных  источниках  фазы  немного  отличаются,  но  глобально  суть  везде  \nодинакова.' in reader.pages[0].extract_text()

print(os.path.getsize('../qa_guru/tmp/testing.pdf'))
assert os.path.getsize('../qa_guru/tmp/testing.pdf') == 8129321
