ó
ÿÿc           @   sp   e  Z e r# d  d  Z   Z n  d d l Z d d l Z d d l Z d d l Z d   Z d   Z e   d S(   i    iÿÿÿÿNc          C   sM   t  j d  Ht d  }  |  d k r5 t d  }  n  t j |   } | GHd  S(   Nt   clears   ENTER DOMAIN NAME : t    (   t   ost   systemt	   raw_inputt   sockett   gethostbyname(   t   usert   get_ip(    (    s	   web-ip.pyt   main   s    c           C   s   t  d  GHd  S(   Ns
   google.com(   t   get_ip_address(    (    (    s	   web-ip.pyt   main1   s    (	   t   Falset   foot   barR   t   syst   timeR   R	   R   (    (    (    s	   web-ip.pyt   <module>   s   
	
	