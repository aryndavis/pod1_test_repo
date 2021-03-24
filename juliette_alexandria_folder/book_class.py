class Booklist():
	def __init__(self):
		self.books = []

	def add(self, title, author):
		book = {}
		book['title'] = title
		book['author'] = author
		self.books.append(book)

	def count_books(self):
		return (len(self.books))

	def remove_title(self, title):
		for book in self.books:
			if book['title'] == title:
				self.books.remove(book)
				
	def display_titles(self):
		titles = []
		for i in self.books: #for every item in books
			titles.append(i['title']) #take the title key/value and append it to the new titles list
		titles.sort() #Sorts the new titles list alphabetically
		print(titles)