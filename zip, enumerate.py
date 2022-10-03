{
  "metadata": {
    "kernelspec": {
      "name": "python",
      "display_name": "Python (Pyodide)",
      "language": "python"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    }
  },
  "nbformat_minor": 5,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "code",
      "source": "from math import sqrt\nfrom random import sample\n\n# Rename the built-in zip (http://docs.python.org/3/library/functions.html#zip)\n_zip = zip\n\n#This function takes in a sequence s, a one-argument function mapper, and a one-argument function filterer. \n#It returns a new list containing the result of calling mapper on each element of s for which filterer returns a true value. \n#Make sure your solution is only one line and uses a list comprehension\n\ndef map_and_filter(s, mapper, filterer):\n    \"\"\"Return a new list containing the result of calling mapper on each\n    element of sequence s for which filterer returns a true value.\n\n    >>> square = lambda x: x * x\n    >>> is_odd = lambda x: x % 2 == 1\n    >>> map_and_filter([1, 2, 3, 4, 5], square, is_odd)\n    [1, 9, 25]\n    \"\"\"\n    # BEGIN Question 0\n    return [mapper(item) for item in s if filterer(item)==True]",
      "metadata": {
        "trusted": true
      },
      "execution_count": 21,
      "outputs": [],
      "id": "44dd0bf4-66b0-474c-b035-16e4a03bff50"
    },
    {
      "cell_type": "code",
      "source": "#testing return CORRECT, as per doctest\ns= [1, 2, 3, 4, 5]\nsquare = lambda x: x * x\nis_odd = lambda x: x % 2 == 1\nmap_and_filter([1, 2, 3, 4, 5], square, is_odd)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 22,
      "outputs": [
        {
          "execution_count": 22,
          "output_type": "execute_result",
          "data": {
            "text/plain": "[1, 9, 25]"
          },
          "metadata": {}
        }
      ],
      "id": "69f5f155-4ba6-4e19-bfe7-5034532e7f83"
    },
    {
      "cell_type": "code",
      "source": "#The built-in min function takes a sequence (such as a list or a dictionary) and returns the sequence's smallest element. \n#The min function can also take a keyword argument called *key*, which must be a **one-argument function**. \n#The key function is called with **each element of the list**, and the return values are used for comparison. \n\n### implement key_of_min_value\n#which takes in a dictionary d and returns the key that corresponds to the minimum value in d. \n#This behavior differs from just calling min on a dictionary, which would return the smallest key. \n#Make sure your solution is only one line and uses the min function.\n#\n\ndef key_of_min_value(d):\n    \"\"\"Returns the key in dict d that corresponds to the minimum value of d.\n\n    >>> letters = {'a': 6, 'b': 5, 'c': 4, 'd': 5}\n    >>> min(letters)\n    'a'\n    >>> key_of_min_value(letters)\n    'c'\n    \"\"\"\n    # BEGIN Question 0\n    return [key for key in d if d[key] == min([d[key] for key in d])][0]\n    # END Question 0",
      "metadata": {
        "trusted": true
      },
      "execution_count": 44,
      "outputs": [],
      "id": "bd869034-d008-415b-8515-58ba4e585bbc"
    },
    {
      "cell_type": "code",
      "source": "letters = {'a': 6, 'b': 5, 'c': 4, 'd': 5}\n[key for key in letters if letters[key] == min([letters[key] for key in letters])][0]",
      "metadata": {
        "trusted": true
      },
      "execution_count": 45,
      "outputs": [
        {
          "execution_count": 45,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'c'"
          },
          "metadata": {}
        }
      ],
      "id": "7b3a5cbc-f8d4-4b2e-b34e-948d1fcbe4a0"
    },
    {
      "cell_type": "code",
      "source": "#testing return CORRECT, as per doctest\nletters = {'a': 6, 'b': 5, 'c': 4, 'd': 5}\nmin(letters)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 46,
      "outputs": [
        {
          "execution_count": 46,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'a'"
          },
          "metadata": {}
        }
      ],
      "id": "75795651-f8bf-4ca3-8c6f-368dd3f5608f"
    },
    {
      "cell_type": "code",
      "source": "key_of_min_value(letters)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 47,
      "outputs": [
        {
          "execution_count": 47,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'c'"
          },
          "metadata": {}
        }
      ],
      "id": "fbf9ee04-afb7-4085-a800-74a33db30140"
    },
    {
      "cell_type": "code",
      "source": "def zip(*sequences):\n    \"\"\"Returns a list of lists, where the i-th list contains the i-th\n    element from each of the argument sequences.\n\n    >>> zip(range(0, 3), range(3, 6))\n    [[0, 3], [1, 4], [2, 5]]\n    >>> for a, b in zip([1, 2, 3], [4, 5, 6]):\n    ...     print(a, b)\n    1 4\n    2 5\n    3 6\n    >>> for triple in zip(['a', 'b', 'c'], [1, 2, 3], ['do', 're', 'mi']):\n    ...     print(triple)\n    ['a', 1, 'do']\n    ['b', 2, 're']\n    ['c', 3, 'mi']\n    \"\"\"\n    return list(map(list, _zip(*sequences)))",
      "metadata": {
        "trusted": true
      },
      "execution_count": 54,
      "outputs": [],
      "id": "6314010a-ffd0-437b-ac0d-bc979118c4ba"
    },
    {
      "cell_type": "code",
      "source": "#Use the zip function to implement enumerate, which takes a sequence s and a starting index start. \n#It returns a list of pairs, in which the i-th element is i+start paired with the i-th element of s. \n#Make sure your solution is only one line and uses the zip function and a range.\n\ndef enumerate(s, start=0):\n    \"\"\"Returns a list of lists, where the i-th list contains i+start and the\n    i-th element of s.\n\n    >>> enumerate([6, 1, 'a'])\n    [[0, 6], [1, 1], [2, 'a']]\n    >>> enumerate('five', 5)\n    [[5, 'f'], [6, 'i'], [7, 'v'], [8, 'e']]\n    \"\"\"\n    # BEGIN Question 0\n    return zip([i for i in range(start,start + len(s))],s)\n    # END Question 0",
      "metadata": {
        "trusted": true
      },
      "execution_count": 82,
      "outputs": [],
      "id": "68065ea6-a73b-4183-ac7d-f82a3faadbdb"
    },
    {
      "cell_type": "code",
      "source": "#wrong code, debug\nzip([i for i in range(len(s))],[s])",
      "metadata": {
        "trusted": true
      },
      "execution_count": 83,
      "outputs": [
        {
          "execution_count": 83,
          "output_type": "execute_result",
          "data": {
            "text/plain": "[[0, [6, 1, 'a']]]"
          },
          "metadata": {}
        }
      ],
      "id": "63e88bb1-15e2-4947-9ab4-76e8e2fa00ac"
    },
    {
      "cell_type": "code",
      "source": "#step debug\ns = [6, 1, 'a']\n[i for i in range(len(s))]",
      "metadata": {
        "trusted": true
      },
      "execution_count": 84,
      "outputs": [
        {
          "execution_count": 84,
          "output_type": "execute_result",
          "data": {
            "text/plain": "[0, 1, 2]"
          },
          "metadata": {}
        }
      ],
      "id": "7c5d2e9e-442d-468b-aebb-791b50618086"
    },
    {
      "cell_type": "code",
      "source": "#step debug successful, rewritten part\nzip([i for i in range(len(s))],s)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 85,
      "outputs": [
        {
          "execution_count": 85,
          "output_type": "execute_result",
          "data": {
            "text/plain": "[[0, 6], [1, 1], [2, 'a']]"
          },
          "metadata": {}
        }
      ],
      "id": "f48b00ef-e17f-4f90-8f15-1331fe763536"
    },
    {
      "cell_type": "code",
      "source": "#rewrite function above and get the doctest correct\nenumerate([6, 1, 'a'])",
      "metadata": {
        "trusted": true
      },
      "execution_count": 86,
      "outputs": [
        {
          "execution_count": 86,
          "output_type": "execute_result",
          "data": {
            "text/plain": "[[0, 6], [1, 1], [2, 'a']]"
          },
          "metadata": {}
        }
      ],
      "id": "c29946e4-b86b-4fec-99a1-c163b5ea39e5"
    },
    {
      "cell_type": "code",
      "source": "# the doctest correct\nenumerate('five', 5)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 87,
      "outputs": [
        {
          "execution_count": 87,
          "output_type": "execute_result",
          "data": {
            "text/plain": "[[5, 'f'], [6, 'i'], [7, 'v'], [8, 'e']]"
          },
          "metadata": {}
        }
      ],
      "id": "378b76a8-29a4-492c-b121-dd34ccfb0af6"
    },
    {
      "cell_type": "code",
      "source": "def distance(pos1, pos2):\n    \"\"\"Return the Euclidean distance between pos1 and pos2, which are pairs.\n\n    >>> distance([1, 2], [4, 6])\n    5.0\n    \"\"\"\n    return sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)\n\ndef mean(s):\n    \"\"\"Return the arithmetic mean of a sequence of numbers s.\n\n    >>> mean([-1, 3])\n    1.0\n    >>> mean([0, -3, 2, -1])\n    -0.5\n    \"\"\"\n    assert len(s) > 0, 'cannot find mean of empty sequence'\n    return sum(s) / len(s)",
      "metadata": {},
      "execution_count": null,
      "outputs": [],
      "id": "b1701907-2035-4468-aca4-35a1032cbe69"
    }
  ]
}
