# this script's main role is to make custom websites work on sharepoint.
# 1. find all .html files
# 2. edit the text. replace ".html" with ".aspx"
# 3. save the text as .aspx file

import os, shutil


def main(in_folder, out_folder):

	# copy files from in_folder to out_folder only if in_folder is not the same as out_folder
	# if in_folder == out_folder, then the tool will basically convert the in_folder
	if in_folder != out_folder:
		try:
			shutil.rmtree(out_folder)
		except:
			pass
		shutil.copytree(in_folder, out_folder)

	# get a list of full path of all the html files
	html_files = []
	for root, dirs, files in os.walk(out_folder):
		for filename in files:
			if filename.lower().endswith('.html'):
				html_files.append(os.path.join(root,filename))

	# work on each .html file. rename the file to .aspx, and replace all .html texts to .aspx
	for file in html_files:
		# create a new aspx file
		aspx_filename = file.lower().replace('.html','.aspx')

		original = open(file, "r")
		final = open(aspx_filename, "w")
		for line in original:
			final.write(line.replace('.html','.aspx'))

		original.close()
		final.close()




if __name__ == '__main__':
	in_folder = r'D:\ACTIVE\HomeOffice\RAP_Outputs\new_browser_2021\html'
	out_folder = r'D:\ACTIVE\HomeOffice\RAP_Outputs\new_browser_2021\aspx'
	main(in_folder, out_folder)
