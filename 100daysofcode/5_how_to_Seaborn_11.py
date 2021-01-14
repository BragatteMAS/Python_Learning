{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Seaborn0.11",
      "provenance": [],
      "authorship_tag": "ABX9TyPcbGQY81LUOz0JMxr8YqsN",
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
        "<a href=\"https://colab.research.google.com/github/BragatteMAS/Python_Learning/blob/master/100daysofcode/5_how_to_Seaborn_11.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Ki_pDgnajK_-"
      },
      "source": [
        "'''\n",
        "100daysofcode\n",
        "\n",
        "\"How to display change Statistical_test\"\n",
        "\n",
        "Refactor by  @bragatte ^202101132240\n",
        "\n",
        "Day 5\n",
        "\n",
        "[Seaborn 0.11 Updates](https://towardsdatascience.com/seaborn-0-11-just-released-with-great-new-features-c5b45efad7e2)\n",
        "'''"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-w5KQ-0luZtd"
      },
      "source": [
        "!pip install seaborn==0.11.0"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "jREamTn516am"
      },
      "source": [
        "sns.displot(data=diabetes, x='Glucose', kind='hist', height=6, aspect=1.2)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "U7QOosQc16kV"
      },
      "source": [
        "sns.displot(data=diabetes, x='Glucose', y='BloodPressure',\n",
        "kind='hist', height=6, aspect=1.2)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xGb_iRZb16pG"
      },
      "source": [
        "sns.histplot(data=diabetes, x='Glucose', y='BloodPressure')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Hm-WwBOj2W1o"
      },
      "source": [
        "\n",
        "[Churn](https://www.kaggle.com/sonalidasgupta95/churn-prediction-of-bank-customers)"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8_m38Q3F16qi"
      },
      "source": [
        "sns.displot(data=churn, x='CreditScore', kind='hist',\n",
        "col='Geography', hue='Exited')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xAuw6iNz16qI"
      },
      "source": [
        "sns.displot(data=churn, x='Age', kind='ecdf', col='Geography', hue='Exited')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rzJD0uKx16oq"
      },
      "source": [
        "sns.jointplot(data=diabetes, x='Insulin', y='BMI', hue='Outcome',\n",
        "height=7)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3JxT3TTl16oN"
      },
      "source": [
        "sns.jointplot(data=diabetes, x='Insulin', y='BMI', hue='Outcome',\n",
        "kind='hist', height=7)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "f7mMUTTX2J8s"
      },
      "source": [
        "Set function has been renamed as set_theme. It adjusts several properties of the theme used in visualizations.\n",
        "\n",
        "The axlabel function is no longer available. It is recommended to use ax.set(xlabel=, ylabel=) instead."
      ]
    }
  ]
}