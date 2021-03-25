class Booklist():
	def __init__(self):
		self.books = []
		pass

	def add(self, title, author):
		book = {}
		book["author"] = author
		book["title"] = title
		self.books.append(book)
		pass

	def count_books(self):
		return len(self.books)
		pass

	def remove_title(self, title):
		for book in self.books:
			if book["title"] == title:
				self.books.remove(book)

		pass

	def display_titles(self):
		title = []
		for book in self.books:
				title.append(book["title"])
		title.sort()

		return title
				



		pass

