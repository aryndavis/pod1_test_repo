class Booklist():
	def __init__(self):
		self.book_list = []
		

	def add(self, title, author):
		book_dict = {}
		nyt_bestellers = {}
		book_dict['title'] = title
		book_dict['author'] = author
		self.book_list.append(book_dict)

		

	def count_books(self):
		print(len(self.book_list))

		

	def remove_title(self, title):
		for book_dict in self.book_list:
			if title == book_dict['title']:
				self.book_list.pop(self.book_list.index(book_dict))
				return
		else:
			print("This title is not in your library")

		
# Don't know why my code won't work. Checked the solutions and it still wont work
	def display_titles(self):
		titles = []
		for book_dict in self.book_list:
			titles.append(book_dict(['title'])
		titles.sort()
		print(titles)
