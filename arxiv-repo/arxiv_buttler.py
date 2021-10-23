'''
	this script renames the papers downloaded from arxiv.org
	using the naming format defined by the 'name_format' function
	see the complete documentation at https://github.com/sukiboo/sbn_arxiv_rename
'''

import os
import arxiv
import shutil
import requests



folder_in = r"G:\My Drive\4. Reading List"
folder_out = r"G:\My Drive\4. Reading List"

def name_format(author, title, year):
	title = title.replace(':', '').replace(',', '')
	pdf_name = f"[{author} {year}] {title}.pdf"
	return pdf_name


def should_be_formatted(filename):
    # if > 80% are numbers
    n_numbers = sum(c.isdigit() for c in filename)
    bool_value = n_numbers / len(filename) > 0.8
    return bool_value


def query_paper(paper_id):
	search = arxiv.Search(id_list=[paper_id])
	paper = next(search.results())
	return {"title": paper.title,
			"author": paper.authors[0].name,
			"year": paper.updated.year}


# get the list of pdf files in the current directory
files = [f for f in os.listdir(folder_in) if f.endswith('.pdf')]

for f in files:
	file_name = f.split(".pdf")[0]
	if should_be_formatted(file_name):
		data = query_paper(file_name)
		os.rename(f'{os.path.join(folder_in, file_name)}.pdf',f'{os.path.join(folder_out, name_format(data["author"], data["title"], data["year"]))}') 