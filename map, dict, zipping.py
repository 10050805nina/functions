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
      "source": "def mul_by_num(num):\n    \"\"\"\n    Returns a function that takes one argument and returns num\n    times that argument.\n    >>> x = mul_by_num(5)\n    >>> y = mul_by_num(2)\n    >>> x(3)\n    15\n    >>> y(-4)\n    -8\n    \"\"\"\n    return lambda x : x * num",
      "metadata": {
        "trusted": true
      },
      "execution_count": 1,
      "outputs": [],
      "id": "832526f0-c286-48f5-b99e-f7a8de4e79df"
    },
    {
      "cell_type": "code",
      "source": "x = mul_by_num(5)\nx(3)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 2,
      "outputs": [
        {
          "execution_count": 2,
          "output_type": "execute_result",
          "data": {
            "text/plain": "15"
          },
          "metadata": {}
        }
      ],
      "id": "d52cf742-b9a0-4104-9a7c-8a0d2249fd38"
    },
    {
      "cell_type": "code",
      "source": "y = mul_by_num(2)\ny(-4)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 3,
      "outputs": [
        {
          "execution_count": 3,
          "output_type": "execute_result",
          "data": {
            "text/plain": "-8"
          },
          "metadata": {}
        }
      ],
      "id": "6355579a-844f-4392-b8c7-38074409a0c5"
    },
    {
      "cell_type": "code",
      "source": "def compose(f, g):\n    \"\"\"Write a function that takes in 2 single-argument functions, f and g, and returns another lambda function \n    that takes in a single argument x. The returned function should return the output of applying f(g(x)). \n    Hint: The staff solution is only 1 line!\n\n    Return the composition function which given x, computes f(g(x)). \n\n    >>> add_two = lambda x: x + 2  \t\t# adds 2 to x\n    >>> square = lambda x: x ** 2 \t\t# squares x\n    >>> a = compose(square, add_two) \t# (x + 2 ) ^ 2\n    >>> a(5) \n    49\n    >>> mul_ten = lambda x: x * 10 \t\t# multiplies 10 with x\n    >>> b = compose(mul_ten, a) \t\t# ((x + 2 ) ^ 2) * 10\n    >>> b(5)\n    490\n    >>> b(2)\n    160\n    \"\"\"\n    return lambda x : f(g(x)) ",
      "metadata": {
        "trusted": true
      },
      "execution_count": 4,
      "outputs": [],
      "id": "b1f13fcf-3094-4bbc-9c08-e354856ef56f"
    },
    {
      "cell_type": "code",
      "source": "add_two = lambda x: x + 2\nsquare = lambda x: x ** 2\na = compose(square, add_two)\na(5)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 5,
      "outputs": [
        {
          "execution_count": 5,
          "output_type": "execute_result",
          "data": {
            "text/plain": "49"
          },
          "metadata": {}
        }
      ],
      "id": "e8143b71-c193-4a90-b718-3c01ae375c66"
    },
    {
      "cell_type": "code",
      "source": "mul_ten = lambda x: x * 10\nb = compose(mul_ten, a)\nb(5)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 6,
      "outputs": [
        {
          "execution_count": 6,
          "output_type": "execute_result",
          "data": {
            "text/plain": "490"
          },
          "metadata": {}
        }
      ],
      "id": "eb925686-c4b6-44db-a65a-4daf6b3362e7"
    },
    {
      "cell_type": "code",
      "source": "b(2)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 7,
      "outputs": [
        {
          "execution_count": 7,
          "output_type": "execute_result",
          "data": {
            "text/plain": "160"
          },
          "metadata": {}
        }
      ],
      "id": "0dfa1d55-de14-4a30-9070-32c6e6480355"
    },
    {
      "cell_type": "code",
      "source": "def counter(message):\n    \"\"\" Returns a dictionary of each word in message mapped\n    to the number of times it appears in the input string.\n\n    >>> x = counter('to be or not to be')\n    >>> x['to']\n    2\n    >>> x['be']\n    2\n    >>> x['not']\n    1\n    >>> y = counter('run forrest run')\n    >>> y['run']\n    2\n    >>> y['forrest']\n    1\n    \"\"\"\n    word_list = message.split()\n    d = {word : word_list.count(word) for word in word_list}\n    return d",
      "metadata": {
        "trusted": true
      },
      "execution_count": 8,
      "outputs": [],
      "id": "06cd01bc-f3dc-4c56-bca9-109252cd6c4b"
    },
    {
      "cell_type": "code",
      "source": "x = counter('to be or not to be')\nx['to']",
      "metadata": {
        "trusted": true
      },
      "execution_count": 9,
      "outputs": [
        {
          "execution_count": 9,
          "output_type": "execute_result",
          "data": {
            "text/plain": "2"
          },
          "metadata": {}
        }
      ],
      "id": "75219583-9513-48e0-8515-c521491569f6"
    },
    {
      "cell_type": "code",
      "source": "x['be']",
      "metadata": {
        "trusted": true
      },
      "execution_count": 10,
      "outputs": [
        {
          "execution_count": 10,
          "output_type": "execute_result",
          "data": {
            "text/plain": "2"
          },
          "metadata": {}
        }
      ],
      "id": "065cdb4b-e392-4832-9a7c-0a01375488df"
    },
    {
      "cell_type": "code",
      "source": "x['not']",
      "metadata": {
        "trusted": true
      },
      "execution_count": 11,
      "outputs": [
        {
          "execution_count": 11,
          "output_type": "execute_result",
          "data": {
            "text/plain": "1"
          },
          "metadata": {}
        }
      ],
      "id": "23aac4a9-f548-4929-8083-dba65a6307ac"
    },
    {
      "cell_type": "code",
      "source": "y = counter('run forrest run')\ny['run']",
      "metadata": {
        "trusted": true
      },
      "execution_count": 12,
      "outputs": [
        {
          "execution_count": 12,
          "output_type": "execute_result",
          "data": {
            "text/plain": "2"
          },
          "metadata": {}
        }
      ],
      "id": "33be1397-b01f-4722-8090-4e27c1cf26ea"
    },
    {
      "cell_type": "code",
      "source": " y['forrest']",
      "metadata": {
        "trusted": true
      },
      "execution_count": 13,
      "outputs": [
        {
          "execution_count": 13,
          "output_type": "execute_result",
          "data": {
            "text/plain": "1"
          },
          "metadata": {}
        }
      ],
      "id": "7510ca02-d54e-4ce6-bcaa-df4e959419d2"
    },
    {
      "cell_type": "code",
      "source": "def common_players(roster):\n    \"\"\"Returns a dictionary containing values along with a corresponding\n    list of keys that had that value from the original dictionary.\n    >>> full_roster = {\"bob\": \"Team A\", \"barnum\": \"Team B\", \"beatrice\": \"Team C\", \"bernice\": \"Team B\", \"ben\": \"Team D\", \"belle\": \"Team A\", \"bill\": \"Team B\", \"bernie\": \"Team B\", \"baxter\": \"Team A\"}\n    >>> player_dict = common_players(full_roster)\n    >>> dict(sorted(player_dict.items()))\n    {'Team A': ['bob', 'belle', 'baxter'], 'Team B': ['barnum', 'bernice', 'bill', 'bernie'], 'Team C': ['beatrice'], 'Team D': ['ben']}\n    \"\"\"\n    res = {}\n    for i, v in roster.items():\n        res[v] = [i] if v not in res.keys() else res[v] + [i]\n    return res",
      "metadata": {
        "trusted": true
      },
      "execution_count": 24,
      "outputs": [],
      "id": "5b07bb7f-eaba-489f-8335-f5b04c915027"
    },
    {
      "cell_type": "code",
      "source": "full_roster = {\"bob\": \"Team A\", \"barnum\": \"Team B\", \"beatrice\": \"Team C\", \"bernice\": \"Team B\", \"ben\": \"Team D\", \"belle\": \"Team A\", \"bill\": \"Team B\", \"bernie\": \"Team B\", \"baxter\": \"Team A\"}",
      "metadata": {
        "trusted": true
      },
      "execution_count": 25,
      "outputs": [],
      "id": "87ff6347-db70-4721-a918-e94690eb2834"
    },
    {
      "cell_type": "code",
      "source": "player_dict = common_players(full_roster)\ndict(sorted(player_dict.items()))",
      "metadata": {
        "trusted": true
      },
      "execution_count": 26,
      "outputs": [
        {
          "execution_count": 26,
          "output_type": "execute_result",
          "data": {
            "text/plain": "{'Team A': ['bob', 'belle', 'baxter'],\n 'Team B': ['barnum', 'bernice', 'bill', 'bernie'],\n 'Team C': ['beatrice'],\n 'Team D': ['ben']}"
          },
          "metadata": {}
        }
      ],
      "id": "7bd7d3bc-2ccf-4d34-b937-939f457fd105"
    },
    {
      "cell_type": "code",
      "source": "",
      "metadata": {},
      "execution_count": null,
      "outputs": [],
      "id": "76770d0b-5034-4794-8cfe-c146527977f9"
    }
  ]
}