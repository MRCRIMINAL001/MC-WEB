ó
˙˙c           @   sl   e  Z e r# d  d  Z   Z n  d d l Z d d l Z d Z e j d  e GHd GHd   Z e   d S(   i    i˙˙˙˙Nsˇ   [1;94m
    _   __    _       ____________
   / | / /   | |     / / ____/ __ )
  /  |/ /____| | /| / / __/ / __  |
 / /|  /_____/ |/ |/ / /___/ /_/ /
/_/ |_/      |__/|__/_____/_____/

Created By : [1;96mNabil-Rahman |[1;0m [V 1.2.2]

[1;32m------------------------------------------
[93m AUTHOR  : Team DarkWeb T-D
[93m GITHUB  : github.com/Nabil-Official
[93m FB      : nabil.404
[1;32m------------------------------------------
t   cleart    c          C   sř   t  d  }  |  d k r" t   nŇ d GHd |  GHd GHd GH|  d } t j d |  d  t j d | d  t d	  } | j   } t d
  } | j   } | | k r˛ d GHn d GHt j d  Hd GHHt  d  } H| d k rô t j d  n  d  S(   Ns&   >> Enter Website Url With Paramater : R   s&       [1;31m>>> [1;32mTARGET : [1;33ms4       [1;31m>>> [1;32mSCANNING :  [1;33mStarting...s   %27s   curl -s s    | wc -l > line1.txts   | wc -l > line2.txts	   line1.txts	   line2.txts3   [1;31m[+] [1;32mStatus : [1;32mVernavility Founds7   [1;31m[+] [1;32mStatus : [1;32mVernability Not Founds$   rm -rf line1.txt && rm -rf line2.txts/     [1;31m<<< [1;33mThanks For Using [1;31m>>>s8   [1;31m[+] [1;34mPRESS ENTER TO GO BACK MENU [1;31m[+]s   cd .. && python2 n-web.py(   t	   raw_inputt   exitt   ost   systemt   opent   read(   t   webt   web2t   file1t   f1_rt   file2t   f2_rt   user(    (    s   sqli.pyt   main   s2    
	
(   t   Falset   foot   barR   t   syst   logoR   R   (    (    (    s   sqli.pyt   <module>   s   
	