
import pytest
# this makes sure we look also look at the parent directory to import from the playlist.py file
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from playlist_functions_2 import *

@pytest.fixture
def playlist():
	return [
		{'artist': 'Bilal', 'title': 'Sometimes'},
		{'artist': 'Parliament', 'title': 'Mothership Connection (Star Child)'},
		{'artist': 'Pink Floyd', 'title': 'Another Brick in the Wall'},
		{'artist': 'Parliament', 'title': 'Unfunky UFO'},
		{'artist': 'Nina Simone', 'title': 'Mississippi Goddamn'},
		{'artist': 'Nina Simone', 'title': 'Four Women'},
		{'artist': 'Roberta Flack', 'title': 'Killing Me Softly'},
		{'artist': 'Fugees', 'title': 'Killing Me Softly'}
	]

# Question 1: Complete the test for get_playlist_titles function
def test_get_titles(playlist):
	assert get_playlist_titles(playlist) == ['Sometimes', 'Mothership Connection (Star Child)', 'Another Brick in the Wall', 'Unfunky UFO', 'Mississippi Goddamn', 'Four Women', 'Killing Me Softly', 'Killing Me Softly']

	
def test_search_through_artist(playlist):
	assert search_by_artist(playlist, 'Bilal') == ['Sometimes']
	assert search_by_artist(playlist, 'Nina Simone') == ['Mississippi Goddamn', 'Four Women']

	
# Question 3: Write two test functions for search_by_title

def test_search_by_title(playlist):
	assert search_by_title(playlist, 'Unfunky UFO') == [{'artist': 'Parliament', 'title': 'Unfunky UFO'}]
	assert search_by_title(playlist, 'Killing Me Softly') == [{'artist': 'Roberta Flack', 'title': 'Killing Me Softly'}, {'artist': 'Fugees', 'title': 'Killing Me Softly'}]
	
# I learned that to run a pytest, the function must have "test" in the beginning of it's name
