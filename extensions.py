ans = input("File name: ")

if ans.endswith(".gif"):
	print("image/gif")
elif ans.endswith(".jpg"):
	print("image/jpeg")
elif ans.endswith(".jpeg"):
	print("image/jpeg")
elif ans.endswith(".png"):
	print("image/png")
elif ans.endswith(".pdf"):
	print("application/pdf")
elif ans.endswith(".txt"):
	print("text/plain")
elif ans.endswith(".zip"):
	print("application/zip")
else:
	print("application/octet-stream")