#!/usr/bin/python3
# -*- coding: latin-1 -*-
blob = """       c�d�z�x�~矑�M�}N��1�
{Y*����ڨ��!£#�>59�i�>�T;sKk	�M��S	e�*3���*yG�'���'�Ff�Zn9��ik���؊q7�e�\�!�Ңx�Z�w�Hd"""
from hashlib import sha256
if(sha256(blob.encode('latin-1')).hexdigest())=="e4893cfbc3b2c3d57bd52a41bf327bf6bc6ad88bc1daafab82ed767024c3ffc5":
	print('print("Hashing is not encryption!")')
	print(sha256(blob.encode('latin-1')).hexdigest())
elif(sha256(blob.encode('latin-1')).hexdigest())=="0b6a9e57a7035d6ea532b00050dd447753472d6f7a170a9742842c1656cc6f24":
	print('print("Security through obscurity!")')
	print(sha256(blob.encode('latin-1')).hexdigest())