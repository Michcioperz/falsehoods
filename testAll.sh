#!/bin/sh
for binary in bin/false-*
do
  ./test.py $binary
done
