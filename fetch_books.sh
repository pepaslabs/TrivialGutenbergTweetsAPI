#!/usr/bin/env bash

set -e

mkdir -p books
cd books

if [ ! -e pride_and_prejudice.txt ]
then
    wget -O pride_and_prejudice.txt https://www.gutenberg.org/ebooks/1342.txt.utf-8
fi

if [ ! -e alices_adventures_in_wonderland.txt ]
then
    wget -O alices_adventures_in_wonderland.txt https://www.gutenberg.org/ebooks/11.txt.utf-8
fi

if [ ! -e frankenstein.txt ]
then
    wget -O frankenstein.txt https://www.gutenberg.org/ebooks/84.txt.utf-8
fi

if [ ! -e adventures_of_huckleberry_finn.txt ]
then
    wget -O adventures_of_huckleberry_finn.txt https://www.gutenberg.org/ebooks/76.txt.utf-8
fi

if [ ! -e adventures_of_sherlock_holmes.txt ]
then
    wget -O adventures_of_sherlock_holmes.txt https://www.gutenberg.org/ebooks/1661.txt.utf-8
fi

if [ ! -e moby_dick.txt ]
then
    wget -O moby_dick.txt https://www.gutenberg.org/ebooks/2701.txt.utf-8
fi

if [ ! -e a_modest_proposal.txt ]
then
    wget -O a_modest_proposal.txt https://www.gutenberg.org/ebooks/1080.txt.utf-8
fi

if [ ! -e the_picture_of_dorian_gray.txt ]
then
    wget -O the_picture_of_dorian_gray.txt https://www.gutenberg.org/ebooks/174.txt.utf-8
fi

if [ ! -e metamorphosis.txt ]
then
    wget -O metamorphosis.txt https://www.gutenberg.org/ebooks/5200.txt.utf-8
fi

if [ ! -e a_tale_of_two_cities.txt ]
then
    wget -O a_tale_of_two_cities.txt https://www.gutenberg.org/ebooks/98.txt.utf-8
fi

