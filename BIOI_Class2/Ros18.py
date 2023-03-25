{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "AABAAABBBBABBBABAAAABAAABBAAABABBAABBAABAAABAABBBB\n",
      "\n",
      "['0.621', '0.379', '0.67', '0.621', '0.621', '0.379', '0.33', '0.33', '0.33', '0.67', '0.379', '0.33', '0.33', '0.67', '0.379', '0.67', '0.621', '0.621', '0.621', '0.379', '0.67', '0.621', '0.621', '0.379', '0.33', '0.67', '0.621', '0.621', '0.379', '0.67', '0.379', '0.33', '0.67', '0.621', '0.379', '0.33', '0.67', '0.621', '0.379', '0.67', '0.621', '0.621', '0.379', '0.67', '0.621', '0.379', '0.33', '0.33', '0.33']\n",
      "2.135456332061625e-16\n"
     ]
    }
   ],
   "source": [
    "#Ros18.py\n",
    "#quinn thomas\n",
    "#Rosalind 18\n",
    "import os\n",
    "import math\n",
    "import numpy\n",
    "\n",
    "\n",
    "#identify the directory you are working in\n",
    "mydir = \"/Users/QuinnThomas/Desktop/BIOI_500/\"\n",
    "#save input file to variable and read by lines\n",
    "infile = open(mydir + \"rosalind_ba10a.txt\", 'r').readlines()\n",
    "#create output file\n",
    "outfile = open(mydir + 'Ros18.txt', 'w')\n",
    "\n",
    "pi = infile[0]\n",
    "states = infile[2].strip().split()\n",
    "matrix = []\n",
    "for line in infile[5:]:\n",
    "\tline = line.strip().split()\n",
    "\t#print(line)\n",
    "\tmatrix.append(line[1:])\n",
    "\n",
    "\n",
    "\n",
    "matrix = matrix[0]+matrix[1]\n",
    "#print(matrix)\n",
    "\n",
    "matrix_dict= {}\n",
    "matrix_dict[states[0]+states[0]] = matrix[0]\n",
    "matrix_dict[states[0]+states[1]] = matrix[1]\n",
    "matrix_dict[states[1]+states[0]] = matrix[2]\n",
    "matrix_dict[states[1]+states[1]] = matrix[3]\n",
    "\n",
    "#print(matrix_dict)\n",
    "print(pi)\n",
    "#print(states)\n",
    "\n",
    "probability_list = []\n",
    "for i in range(len(pi)-2):\n",
    "    transition = pi[i]+pi[i+1]\n",
    "    #print(transition)\n",
    "    probability = matrix_dict[transition]\n",
    "    probability_list.append(probability)\n",
    "print(probability_list)\n",
    "\n",
    "product = 0.5\n",
    "for x in probability_list:\n",
    "    x = float(x)\n",
    "    product *= x\n",
    "    \n",
    "print(product)\n",
    "\n",
    "outfile.write(str(product))\n",
    "outfile.close()\n",
    "              \n",
    "#product = round(product, 11)\n",
    "#print(product)\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
