import nose.tools as n
import new_examples as ne

def test_word_frequency():
	actual = ne.get_word_frequencies_Counter('and', 'fav_novel_chaper13.txt')
	expected = 40
	n.assert_equal(expected, actual)

def test_unique_words_from_string():
	actual = ne.get_unique_words_from_string('and And sam John')
	expected = set(['and', 'sam', 'john'])
	n.assert_equal(expected, actual)