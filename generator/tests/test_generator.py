"""Test suite for the duplicates.py module"""

import pytest
import generator


def test_generate_internal_lists_from_three_items():
    """ Generate an list of lists from three items """
    internal_list = [1, 2, 3]
    internal_list_of_internal_lists = generator.generate(internal_list)
    assert len(internal_list) == 3
    assert len(internal_list_of_internal_lists) == 4
    assert (internal_list in internal_list_of_internal_lists) is True


def test_generate_internal_lists_from_four_items():
    """ Generate an list of lists from four items """
    internal_list = [1, 2, 3, 4]
    internal_list_of_internal_lists = generator.generate(internal_list)
    assert len(internal_list) == 4
    assert len(internal_list_of_internal_lists) == 7
    assert (internal_list in internal_list_of_internal_lists) is True
