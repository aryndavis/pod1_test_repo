import pytest
# this makes sure we look also look at the parent directory to import from the playlist.py file
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from playlist_functions import *

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
	assert get_playlist_titles(playlist) == ["Sometimes", "Mothership Connection (Star Child)", "Another Brick in the Wall", 
	"Unfunky UFO", "Mississippi Goddamn", "Four Women", "Killing Me Softly", "Killing Me Softly"]


# Question 2: Write two test functions for search_by_artist
def test_search_parliament(playlist):
	expected = ["Mothership Connection (Star Child)", "Unfunky UFO"]
	actual = search_by_artist(playlist, "Pink Floyd")
	assert actual == expected

def test_search_nina(playlist):
	expected = ["Mississippi Goddamn", "Four Women"]
	actual = search_by_artist(playlist, "Nina Simone")
	assert actual == expected

# Question 3: Write two test functions for search_by_title
def test_search_brick(playlist):
	expected = [
		{'artist': 'Pink Floyd', 'title': 'Another Brick in the Wall'},
	]
	actual = search_by_title(playlist, "Another Brick in the Wall")
	assert actual == expected

def test_search_killingme(playlist):
	expected = [
		{'artist': 'Roberta Flack', 'title': 'Killing Me Softly'},
		{'artist': 'Fugees', 'title': 'Killing Me Softly'}
	]
	actual = search_by_title(playlist, "Killing Me Softly")
	assert actual == expected