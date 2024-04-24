{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMkon8duQAM3UGw7D1P+9UT",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/danfernie96/Codigos-python-learning/blob/main/Actividades_de_desempe%C3%B1o_Taller_1.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Actividades de desempeño / Taller 1"
      ],
      "metadata": {
        "id": "ColXWZZCf5rw"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RrWiMIRSf29p",
        "outputId": "b65008b9-d5a3-4a34-f2d6-9a120b796238"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ingresa una palabra:murcielag\n",
            "esta palabra tiene 4 vocales:\n",
            "5\n"
          ]
        }
      ],
      "source": [
        "\"\"\" 1. Pide al usuario que ingrese una palabra o frase y usa un ciclo for para contar cuántas vocales\n",
        "(a, e, i, o, u) contiene. Luego, muestra el conteo de cada vocal por separado\"\"\"\n",
        "\n",
        "contador=0\n",
        "palabra= str(input(\"Ingresa una palabra:\"))\n",
        "lista_vocales=['a','e','i','o','u']\n",
        "for i in palabra:\n",
        "  if i in lista_vocales:\n",
        "    contador+=1\n",
        "print(f\"esta palabra tiene {contador} vocales:\")\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\"\"\" 2. Escribe un programa que lea una lista de nombres e imprima la lista en orden alfabético.\"\"\"\n",
        "\n",
        "lista_nombres=['daniel','juan','pedro','amanda']\n",
        "lista_ordenada=[]\n",
        "for i in lista_nombres:\n",
        "  lista_ordenada.append(i)\n",
        "  lista_ordenada.sort()\n",
        "print(lista_ordenada)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qRCsHG2kh7m8",
        "outputId": "e608d0bc-9039-47b9-b424-7a36ca5ea135"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['amanda', 'daniel', 'juan', 'pedro']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\"\"\" 3. Escribe un programa que lea una lista de palabras e imprima la\n",
        "lista de palabras que comiencen con una determinada letra.\"\"\"\n",
        "\n",
        "Lista_palabras = [\"Amor\", \"Paz\", \"Vida\", \"Solidaridad\", \"Temor\", \"Sabiduría\", \"Felicidad\", \"Esperanza\", \"Alegría\", \"Amistad\"]\n",
        "for palabra in Lista_palabras:\n",
        "    if palabra[0] == \"A\":\n",
        "      print(palabra)"
      ],
      "metadata": {
        "id": "FgKpwZ2th-L9",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d5baca24-0682-4d2c-e499-1b96af8de928"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Amor\n",
            "Alegría\n",
            "Amistad\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "palabra = []\n",
        "Lista_palabras = [\"burro\", \"vaca\", \"carro\", \"casa\", \"perro\", \"gato\", \"mesa\", \"silla\", \"libro\", \"agua\",\n",
        "                  \"ventana\", \"computadora\", \"televisor\", \"teléfono\", \"camión\",\n",
        "                  \"elefante\", \"jirafa\", \"dinosaurio\", \"helado\", \"playa\"]\n",
        "lista = [Lista_palabras]\n",
        "lista.append(palabra)\n",
        "x = input(\"ingresar letra:\")\n",
        "for palabra in Lista_palabras:\n",
        "    if palabra[0] == x :\n",
        "       print(palabra)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XwwE9K1riCcc",
        "outputId": "e3bce72b-8149-4607-d923-dd1c77b9ae82"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "ingresar letra:c\n",
            "carro\n",
            "casa\n",
            "computadora\n",
            "camión\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\"\"\" 4.Escribe un programa lea una lista de números e imprima la suma de los números pares\"\"\"\n",
        "\n",
        "lista_numeros=[1,2,3,4,5,6,7,8,9,10]\n",
        "pares=[]\n",
        "impares=[]\n",
        "for i in lista_numeros:\n",
        "  if i%2==0:\n",
        "    pares.append(i)\n",
        "  else:\n",
        "    impares.append(i)\n",
        "print(f\"los numeros impares son: {impares}\")\n",
        "print(f\"los numeros pares son {pares} y su suma es: {sum(pares)}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dBuqJPhLiFec",
        "outputId": "5ab15f93-e245-4c14-bdc1-224a179d3265"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "los numeros impares son: [1, 3, 5, 7, 9]\n",
            "los numeros pares son [2, 4, 6, 8, 10] y su suma es: 30\n"
          ]
        }
      ]
    }
  ]
}
