{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/LuisCarlosRinconG/CursoPython_UniCafam/blob/main/media_mediana_moda.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import math\n",
        "import matplotlib.pyplot as plt\n"
      ],
      "metadata": {
        "id": "xvIoLKEIa752"
      },
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df=pd.read_csv('/content/sample_data/Mock_data.csv')"
      ],
      "metadata": {
        "id": "XYc6N-5bbDPv"
      },
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "id": "w00lNup-bJAK",
        "outputId": "cfe4b942-d876-4e4f-8182-34f003a92582"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "       id  age  service_call_duration  satisfaction_rating        department  \\\n",
              "0       1   50                    277                    2  Recursos Humanos   \n",
              "1       2   41                    203                    1          Finanzas   \n",
              "2       3   44                    224                    4            Ventas   \n",
              "3       4   43                    108                    1            Ventas   \n",
              "4       5   47                    180                    3          Finanzas   \n",
              "..    ...  ...                    ...                  ...               ...   \n",
              "995   996   39                    177                    4               TIC   \n",
              "996   997   49                      5                    3  Recursos Humanos   \n",
              "997   998   46                    217                    1          Finanzas   \n",
              "998   999   32                    294                    1               TIC   \n",
              "999  1000   44                     33                    3  Recursos Humanos   \n",
              "\n",
              "     start_date      gender  \n",
              "0     8/14/2014        Male  \n",
              "1     2/21/2016      Female  \n",
              "2      5/9/2011  Non-binary  \n",
              "3      6/9/2013      Female  \n",
              "4     7/15/2019        Male  \n",
              "..          ...         ...  \n",
              "995  12/25/2018      Female  \n",
              "996   11/9/2020        Male  \n",
              "997   6/24/2021      Female  \n",
              "998   1/12/2015      Female  \n",
              "999    1/7/2021      Female  \n",
              "\n",
              "[1000 rows x 7 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-dabe1d20-1931-4edd-a6a1-9e9712f311ed\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>id</th>\n",
              "      <th>age</th>\n",
              "      <th>service_call_duration</th>\n",
              "      <th>satisfaction_rating</th>\n",
              "      <th>department</th>\n",
              "      <th>start_date</th>\n",
              "      <th>gender</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>50</td>\n",
              "      <td>277</td>\n",
              "      <td>2</td>\n",
              "      <td>Recursos Humanos</td>\n",
              "      <td>8/14/2014</td>\n",
              "      <td>Male</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>41</td>\n",
              "      <td>203</td>\n",
              "      <td>1</td>\n",
              "      <td>Finanzas</td>\n",
              "      <td>2/21/2016</td>\n",
              "      <td>Female</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>44</td>\n",
              "      <td>224</td>\n",
              "      <td>4</td>\n",
              "      <td>Ventas</td>\n",
              "      <td>5/9/2011</td>\n",
              "      <td>Non-binary</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>43</td>\n",
              "      <td>108</td>\n",
              "      <td>1</td>\n",
              "      <td>Ventas</td>\n",
              "      <td>6/9/2013</td>\n",
              "      <td>Female</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>47</td>\n",
              "      <td>180</td>\n",
              "      <td>3</td>\n",
              "      <td>Finanzas</td>\n",
              "      <td>7/15/2019</td>\n",
              "      <td>Male</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>995</th>\n",
              "      <td>996</td>\n",
              "      <td>39</td>\n",
              "      <td>177</td>\n",
              "      <td>4</td>\n",
              "      <td>TIC</td>\n",
              "      <td>12/25/2018</td>\n",
              "      <td>Female</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>996</th>\n",
              "      <td>997</td>\n",
              "      <td>49</td>\n",
              "      <td>5</td>\n",
              "      <td>3</td>\n",
              "      <td>Recursos Humanos</td>\n",
              "      <td>11/9/2020</td>\n",
              "      <td>Male</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>997</th>\n",
              "      <td>998</td>\n",
              "      <td>46</td>\n",
              "      <td>217</td>\n",
              "      <td>1</td>\n",
              "      <td>Finanzas</td>\n",
              "      <td>6/24/2021</td>\n",
              "      <td>Female</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>998</th>\n",
              "      <td>999</td>\n",
              "      <td>32</td>\n",
              "      <td>294</td>\n",
              "      <td>1</td>\n",
              "      <td>TIC</td>\n",
              "      <td>1/12/2015</td>\n",
              "      <td>Female</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>999</th>\n",
              "      <td>1000</td>\n",
              "      <td>44</td>\n",
              "      <td>33</td>\n",
              "      <td>3</td>\n",
              "      <td>Recursos Humanos</td>\n",
              "      <td>1/7/2021</td>\n",
              "      <td>Female</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>1000 rows × 7 columns</p>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-dabe1d20-1931-4edd-a6a1-9e9712f311ed')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-dabe1d20-1931-4edd-a6a1-9e9712f311ed button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-dabe1d20-1931-4edd-a6a1-9e9712f311ed');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-77f4aa01-36b3-4620-90b0-d7da0f450438\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-77f4aa01-36b3-4620-90b0-d7da0f450438')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-77f4aa01-36b3-4620-90b0-d7da0f450438 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "  <div id=\"id_b852ab3e-aad3-4fc9-ae45-3a1bca0c2ec9\">\n",
              "    <style>\n",
              "      .colab-df-generate {\n",
              "        background-color: #E8F0FE;\n",
              "        border: none;\n",
              "        border-radius: 50%;\n",
              "        cursor: pointer;\n",
              "        display: none;\n",
              "        fill: #1967D2;\n",
              "        height: 32px;\n",
              "        padding: 0 0 0 0;\n",
              "        width: 32px;\n",
              "      }\n",
              "\n",
              "      .colab-df-generate:hover {\n",
              "        background-color: #E2EBFA;\n",
              "        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "        fill: #174EA6;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate {\n",
              "        background-color: #3B4455;\n",
              "        fill: #D2E3FC;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate:hover {\n",
              "        background-color: #434B5C;\n",
              "        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "        fill: #FFFFFF;\n",
              "      }\n",
              "    </style>\n",
              "    <button class=\"colab-df-generate\" onclick=\"generateWithVariable('df')\"\n",
              "            title=\"Generate code using this dataframe.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "    <script>\n",
              "      (() => {\n",
              "      const buttonEl =\n",
              "        document.querySelector('#id_b852ab3e-aad3-4fc9-ae45-3a1bca0c2ec9 button.colab-df-generate');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      buttonEl.onclick = () => {\n",
              "        google.colab.notebook.generateWithVariable('df');\n",
              "      }\n",
              "      })();\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "df",
              "summary": "{\n  \"name\": \"df\",\n  \"rows\": 1000,\n  \"fields\": [\n    {\n      \"column\": \"id\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 288,\n        \"min\": 1,\n        \"max\": 1000,\n        \"num_unique_values\": 1000,\n        \"samples\": [\n          522,\n          738,\n          741\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"age\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 7,\n        \"min\": 24,\n        \"max\": 70,\n        \"num_unique_values\": 42,\n        \"samples\": [\n          39,\n          53,\n          40\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"service_call_duration\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 85,\n        \"min\": 1,\n        \"max\": 300,\n        \"num_unique_values\": 290,\n        \"samples\": [\n          158,\n          195,\n          98\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"satisfaction_rating\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1,\n        \"min\": 1,\n        \"max\": 5,\n        \"num_unique_values\": 5,\n        \"samples\": [\n          1,\n          5,\n          4\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"department\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 5,\n        \"samples\": [\n          \"Finanzas\",\n          \"TIC\",\n          \"Ventas\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"start_date\",\n      \"properties\": {\n        \"dtype\": \"object\",\n        \"num_unique_values\": 910,\n        \"samples\": [\n          \"12/27/2011\",\n          \"3/28/2019\",\n          \"12/29/2017\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"gender\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 8,\n        \"samples\": [\n          \"Female\",\n          \"Genderfluid\",\n          \"Male\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(df.head())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pruFtr92bKEq",
        "outputId": "fea7e0a0-f930-4a8a-d349-b6aaf5d33a1c"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   id  age  service_call_duration  satisfaction_rating        department  \\\n",
            "0   1   50                    277                    2  Recursos Humanos   \n",
            "1   2   41                    203                    1          Finanzas   \n",
            "2   3   44                    224                    4            Ventas   \n",
            "3   4   43                    108                    1            Ventas   \n",
            "4   5   47                    180                    3          Finanzas   \n",
            "\n",
            "  start_date      gender  \n",
            "0  8/14/2014        Male  \n",
            "1  2/21/2016      Female  \n",
            "2   5/9/2011  Non-binary  \n",
            "3   6/9/2013      Female  \n",
            "4  7/15/2019        Male  \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(df.head(10))\n",
        "print(df.tail(10))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-bTLGnk2dpt1",
        "outputId": "2956c445-dc71-4dcf-9a5f-20caac00785e"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   id  age  service_call_duration  satisfaction_rating        department  \\\n",
            "0   1   50                    277                    2  Recursos Humanos   \n",
            "1   2   41                    203                    1          Finanzas   \n",
            "2   3   44                    224                    4            Ventas   \n",
            "3   4   43                    108                    1            Ventas   \n",
            "4   5   47                    180                    3          Finanzas   \n",
            "5   6   51                     77                    1          Finanzas   \n",
            "6   7   55                    269                    4            Ventas   \n",
            "7   8   38                    215                    3          Finanzas   \n",
            "8   9   51                     49                    5            Ventas   \n",
            "9  10   40                    222                    1            Ventas   \n",
            "\n",
            "   start_date      gender  \n",
            "0   8/14/2014        Male  \n",
            "1   2/21/2016      Female  \n",
            "2    5/9/2011  Non-binary  \n",
            "3    6/9/2013      Female  \n",
            "4   7/15/2019        Male  \n",
            "5   8/15/2022      Female  \n",
            "6   7/30/2012      Female  \n",
            "7   11/2/2022    Bigender  \n",
            "8  10/19/2022        Male  \n",
            "9  10/27/2019      Female  \n",
            "       id  age  service_call_duration  satisfaction_rating        department  \\\n",
            "990   991   45                    112                    1               TIC   \n",
            "991   992   49                    129                    2          Finanzas   \n",
            "992   993   39                     37                    5         Marketing   \n",
            "993   994   52                    135                    1  Recursos Humanos   \n",
            "994   995   47                    122                    1          Finanzas   \n",
            "995   996   39                    177                    4               TIC   \n",
            "996   997   49                      5                    3  Recursos Humanos   \n",
            "997   998   46                    217                    1          Finanzas   \n",
            "998   999   32                    294                    1               TIC   \n",
            "999  1000   44                     33                    3  Recursos Humanos   \n",
            "\n",
            "     start_date  gender  \n",
            "990   9/25/2016  Female  \n",
            "991    2/5/2022    Male  \n",
            "992  12/14/2011  Female  \n",
            "993   12/8/2010    Male  \n",
            "994   9/20/2015    Male  \n",
            "995  12/25/2018  Female  \n",
            "996   11/9/2020    Male  \n",
            "997   6/24/2021  Female  \n",
            "998   1/12/2015  Female  \n",
            "999    1/7/2021  Female  \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#contar valores faltantes de cada columna\n",
        "print(df.isnull().sum())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ml6Ilm12eyQZ",
        "outputId": "a0887079-9698-44f1-f598-46be216a1205"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "id                       0\n",
            "age                      0\n",
            "service_call_duration    0\n",
            "satisfaction_rating      0\n",
            "department               0\n",
            "start_date               0\n",
            "gender                   0\n",
            "dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# verificar los tipos de datos\n",
        "print(df.dtypes)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zGx3mMyEe3Fg",
        "outputId": "82d47cfa-aa80-446d-c8d2-59f98bd1064d"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "id                        int64\n",
            "age                       int64\n",
            "service_call_duration     int64\n",
            "satisfaction_rating       int64\n",
            "department               object\n",
            "start_date               object\n",
            "gender                   object\n",
            "dtype: object\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#mostrar info\n",
        "print(df.info())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "10R8LPLsfQbz",
        "outputId": "d49f2bbe-4570-4cdb-ebef-a9037232adc0"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 1000 entries, 0 to 999\n",
            "Data columns (total 7 columns):\n",
            " #   Column                 Non-Null Count  Dtype \n",
            "---  ------                 --------------  ----- \n",
            " 0   id                     1000 non-null   int64 \n",
            " 1   age                    1000 non-null   int64 \n",
            " 2   service_call_duration  1000 non-null   int64 \n",
            " 3   satisfaction_rating    1000 non-null   int64 \n",
            " 4   department             1000 non-null   object\n",
            " 5   start_date             1000 non-null   object\n",
            " 6   gender                 1000 non-null   object\n",
            "dtypes: int64(4), object(3)\n",
            "memory usage: 54.8+ KB\n",
            "None\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#mostrar estadisticas descriptivas generales\n",
        "print(df.describe())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bhtinNlFfdwa",
        "outputId": "231e6c20-ab9e-4be0-9d40-6a9a6469352b"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                id          age  service_call_duration  satisfaction_rating\n",
            "count  1000.000000  1000.000000             1000.00000          1000.000000\n",
            "mean    500.500000    45.191000              152.08000             2.977000\n",
            "std     288.819436     7.245344               85.56921             1.416502\n",
            "min       1.000000    24.000000                1.00000             1.000000\n",
            "25%     250.750000    40.000000               78.00000             2.000000\n",
            "50%     500.500000    45.000000              151.00000             3.000000\n",
            "75%     750.250000    50.000000              225.00000             4.000000\n",
            "max    1000.000000    70.000000              300.00000             5.000000\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Medidas de tendencia central"
      ],
      "metadata": {
        "id": "P-FzhqftgJHQ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "media_age = df['service_call_duration'].mean()\n",
        "\n",
        "print(f'la media es: {media_age}')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ic6FTsI2fwVw",
        "outputId": "b417987f-0755-4d4d-d21e-2f718e8a9b45"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "la media es: 152.08\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "mediana_age = df['service_call_duration'].median()\n",
        "\n",
        "print(f'la mediana es: {mediana_age}')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0vMdp5Eog1Bl",
        "outputId": "486e1904-2520-4b6c-a987-bc124d78436b"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "la mediana es: 151.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "mode_age = df['service_call_duration'].mode()\n",
        "\n",
        "print(f'la moda es: {mode_age}')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3R88hFyDg_RI",
        "outputId": "8f46e926-40ec-4bce-f898-0aaf9196dfb0"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "la moda es: 0    209\n",
            "1    261\n",
            "Name: service_call_duration, dtype: int64\n"
          ]
        }
      ]
    }
  ]
}