from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter
import shutil


class Subject:
    def __init__(self, subject_code: int, name: str, start: int, end: int, sep=None):
        self.subject_code = subject_code
        self.name = name
        self.has_practicals = bool(sep)
        self.start = start
        self.end = end
        self.sep = sep if sep else end

    def __repr__(self):
        return f"{self.subject_code}- {self.name}"


sem_index_page = 3
sem_start = 28
sem_end = 51
subjects = [
    Subject(401, "Theory of Computation", 29, 31, sep=31),
    Subject(402, "Computer Networks", 32, 34, sep=34),
    Subject(403, "Software Engineering", 35, 37, sep=37),
    Subject(404, "IoT Technologies", 38, 40, sep=40),
    Subject(405, "Android Application Development", 41, 43, sep=43),
    Subject(406, "Advanced Application Development", 44, 46, sep=46),
    Subject(4071, "Research Methodology", 47, 48),
]


root = Path("College")
root.mkdir(parents=True, exist_ok=True)

syllabus = Path("syllabus.pdf")
reader = PdfReader(syllabus)
sem_writer = PdfWriter()

sem_writer.add_page(reader.pages[sem_index_page])
for i in range(sem_start, sem_end):
    sem_writer.add_page(reader.pages[i])
sem_writer.write(root / "syllabus.pdf")

for subject in subjects:
    reader = PdfReader(syllabus)

    theory_writer = PdfWriter()
    for i in range(subject.start - 1, subject.sep - 1):
        theory_writer.add_page(reader.pages[i])

    subject_dir = root / str(subject)
    theory_dir = subject_dir / "Theory"
    theory_dir.mkdir(parents=True, exist_ok=True)
    theory_writer.write(theory_dir / "syllabus.pdf")

    if subject.has_practicals:
        practical_writer = PdfWriter()
        for i in range(subject.sep - 1, subject.end):
            practical_writer.add_page(reader.pages[i])

        practical_dir = subject_dir / "Practical"
        practical_dir.mkdir(parents=True, exist_ok=True)
        practical_writer.write(practical_dir / "syllabus.pdf")


shutil.make_archive("College", "zip", root)
shutil.rmtree(root)
