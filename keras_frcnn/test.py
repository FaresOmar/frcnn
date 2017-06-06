file = 'output.txt'
with open(file, 'r+') as f:
		data = f.read()
		data = int(data) + 1
		f.seek(0)
		f.write(str(data))
		f.truncate()
		f.close()