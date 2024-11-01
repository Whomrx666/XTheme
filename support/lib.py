# -*- coding: utf-8 -*-
# XTheme/support/lib.py
# Credit By Mr.X
import os, sys, time, requests, getpass
from .echo import xtheme, note
from .echo import merah, putih, pxh, hijau, oren, netral, kuning, abu


now = "v0.1.0"
_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(b'dFkmyMw/n7r/+z/fkHx79+3x+71V5/Bv/RO4//W78/Xyf//fvd//fdd98/7x87T8/ft313/r++733jvv3rcY3+/fn//fu+d5+/v93fb+//25//l+//T2VE3e8//b8/v+XUy027/eTVExbjpJWlWdAvDDNKC4FNK+tGUQjOCHzsbXOG7gvi06Zy182sal6EFK6280MP21kW4B4HYRgc23wIuQ4s4yHQXT0QRZEIASUNwnVABK6NPQkaxwc0xjsQgRlCdQDAySssB2BldZK1t1zZoK9tpP/tpRYgwMAKOPXOuWdsuKb6piVuqXYUWMYkpnsttSq3g6vfqWssVSDSX5yPL/W1TTqQ607LBSrkeJEznzombaRoK6p6Lat2PNyuK7+4zs8OzsqixVPDKiOtVlxXNshPPRhyqhA+qdYA7IXK/TmNItsOUd10bQsk7rQFX2+PzTvqaBuLjN7MANpvkmUFqC0i1L8En864yzybDEex7EaaufQnQSXkc7BW/hRWINxyurGbo1Rk/hYbYqqmXApr8otwv82nGf2yi2uBHZeDs9+VWH66BoZ75Xy640+QQlFoBnOJ3AwwU78GTauV2lKJQiEtwBPOUHBNK90rE8C6njK6NzgD0T0EG3X8gAXL+W+h4VN/KiKrAxM2EqEn/xGQSCwbIMK46473CesMd07I0duGmIFmyWB9v1cDPbu+PprOORGNiNtZWPPS+y5nvooi3V7k6cFw405ggxrak9J0hjPYd2T5zq3ngkSfmvrNddPwNY4M7B8K/AnJaXwscZLOD6vsmSzyFU7vO9iGxHmZeyY5To5rcYV63GD8mCfzEjrYehuumfgBtFRCytdHIZZ31BY3qHfxZOjZagX12eO3WCNj/gT40wCaFPyKrX3xvfLJDgcF3XvBjjovZTw+qXTSRkh5zNV90XUdegsSrJGAS45m0xI5/NtnqkucVHpFt9L4FKm5rpGrDjR9vhNSc298J13v6IkNnBFyrZo8L2n+pwmsm9Dn00Ue5gyVTQonpNWiw2qEicL8dsid7V0F9RytV1t3kvML3LZTwvz46M32bDbBm2jdAyxsPXfSwcte7tZJMgFzsgUHFX94KYRQ1DaTtcqTfivgC8YD22O0VJnFYipDbmuqrFwiQivEMoJ3XY8FTeNuqc0J39ixV3C3TY19TQ7b9DA7NH04bXGB70Cz8/5EKp1aW0MxZ4ccgZNIoc5A6QDuISPcMUebfSQfIAz+olBrcgGZUAyl4ixuA3hZ4gApN4Z8mwgSgNodSNOUCettl4aC7xCTkNeu3KHpeh475aBoWibHTTgUTogZxXd/IZmGkHI6UjHUw507jeUxaZsP6YWvs9qPgP44PlzWuW+94eQgAcPRZ6/CHqB+ScGcevaP3K9eoFBNYG3ifOv/85pUO+Xj8rHz5nHssdV4gHM3lk0q6XDanYZDe2p02MPyxQZbyYtzMkooV1cBW+bqlFsfxMBWHEN8O7wX5wOFE41cK4hzrWTU6CO0fxu2JZpTkz0YuaLrZ/qc3oJT+onpfwbl4xjrocom5hppMdoWf9mkVEpKqTYK7nR6ZpUNPmRF/SGiPSicUPMNzwp6dtm6eAbExFRTCP+TSLuT5wJ0QhIgKv3O9M/NSEYp6dFIpQcvo4CI0lKG1T28HU5aAEogacYDs2231pBUa10aA7gYjWKLK4cUTDwb+5Y59nQb2it4YeoEdu7MKUq4e4BPl6scFazrusFV4gTPHQRIcP6lWuPohOoLTS3Lsye75p25KTMqoP0hI7nchG6omr8aBxGVbDpHFycHMM1HRfBFUidsMg9DCSs9MzthlCWwxX3FN3WDZSaMyzDvZMAV7IGBAI5R06uncYmCne506N7FcozH/nakMuTSzLBPGa5ef17XWCHAaqKQ9iO32Wuho+NvKwMlqJx2vr9mTqlR0/ADy1+oTJBbXT3dwtXtfkZHwBpMQa2kzlN250IVF04TEsOxKGfnA6OOCT5SPppCocNpfo6L5r6YWjrAAKYIFsSbPx82bxHds+ywmbjbqLQGxJkqIWd3m/QJUnp/rhQq0EXkRzDHM7L+MWbxKlS+p7oxNFssZFQ3DHSfWMy/gaVAAXL82s7kQP/2bV/BjIRvx042EJA+va08u6VOaZwBqxS0aY80+e0uLhKheCXzMShL7kUiu3MDKqwPlY7QIBIvZBfEwHnvfXu2xTDau+xLZ/lgQEMntmwWsgm6mMYNEwD1egHaBKHIM9O6WvazxGHivuSgDkc+kD+BgjDqiJ+b9RijjaNFdF/GW/fRqq9Ypxncpv4Wsfc7zhStqo1Ry9eGyDcO9+Xj4jdGqe8m5XABNK7MnQo9x5zMXVpRUWuu5nDhmvHJObS1OJ/4Xu+zTNUV5Bb8aIMnZgHc2EwdtPLKZLU1IwoorZ8b5JbegJPgQL3A+1n9MlthbVaOEa2+8+3J+mfK9eEsq35d6AChjCvOdwYYJec7p9TueITdHkGllmeC1ZioW6JpEX69WuBlo3VYffY8g4T91myJ7H1yrRpErESUvADYVjroeTnFjMXTnpWIfJqxcDhTyzqmNiFu9mAkDuiGgK4SKILgdzUzNZ0xt6uF2/6Mtu6nRhq71ZSU5MxGDDHDo1pXgw4FcruHcn3g+wTsNaN/VxepekkGg9AN5oLqU35xqqtAFfiFEa7pC5P7bW/DS5hsx7x/Gw0Ip7Um6KGnwwGr1WnTLeyIBfFMsCy6ftYly/acXF6TdmQiOHn7GOlT2dLy/d0YF3FipSwLtRu3BAst6c9+xt7qCtEQXl7Hpll0o5wZlg0o1Eeveu07KxqHnXn38Sen7y6TDsqtR6AanhpXQaVyegh6jcxoHjgvHcFKj4lRRahQAcj+XEdd0RQrIYnCei1AXO0pqlglIEOSrBvB8yRd225IgCzLXKYRjDVoJ8aNRI1fyXE0DTEpigTbPce7EjhybBP/KmbZUYjM4oZffdIoh7TUOOYeT+ta21fMWuI2XiH4iwUeEyIEyvYEvAHQNiEMY+VW1j2qkX1RahmMcb9NDxlPbg6FvJET9c4Pks030sWeQA1uQfOtsxcOn79bkDF6EWqnCfiR6YjF6EKIfNIVRMvhnwGM0+JvXt7xCNT/1TJCsf+Xr8a0OmyJginE+1F6bqy9cXkJ808CH/kkD3hWhQAlPeV/7+P7TJKZeujyz97qK4KAIeKWtD+DQNJcXQSPYjwBJA3hJltjVXbkfeE9SylqCnjkDN9bOlrRxxVRTNMD5l0S3pjz++mHGezMdzkS9coWiOwShWsbVQBiOb0TPub1lmD5UGrV8J+V/BmLB0rcAFDXNg1il1zvx9RdBbiOk/ZCBx2MdU8vb8bR1OM5OHrlZqncUb1kYVDfpG9Vak++OUeGuqPO5FmgbND8Tmg3P0Cxyfcl6vnOnWm4To+hxpufQteMCCYNY96BaEZ59jMZB5QQLPvc+AOlpz6O6RioviOrSkWRbbwiTDG7adBleZJFz9WU5tgxvYhVEy1SQO1wJ9pJULh16qIqbusGt3v02OYArhHlPIv2sxq7lcXSIJ/Rz+7M9VGY+DtqgcWfWlf93WosKOa8LaolKToyPxQV0DHFj45yfkNeihuQUPcx78RVvOc8wfIqwrm5722ZaByGUt8hMCFGGx38t69ec0crkw/eupvQ3d5i3R9ZZnWM3pAjukoefTFIoWQuIwrarkjtds+4L4pFJeSVJJPe2GMHiif3DNKVQiCLp6i62dnyOKGyBlBZc2NJOytX9T853+JKWVrtCVn2dhzB0ht8/gvp9MBvgpW0yozpj0q6hfEr0VWj6APIVfCMOZyMRGr3SX6+tcmHs7eref8/cEgkVq/moxTkdiKi3wS7o9eOY7Mq+OQNrhBT63Z7WmVif2kP4oND9tViSMIfCKcNbWK3ZplVhdgCGjsGHZFTu6nmUZCqD/C3LubLfUgtQCK7gvRzKYbE1cUPOEeJgWiM4iXf7hudIClMArm/dxc+vzeIdTzDKSCEJa3CQFeDBRlWYDeVKsGmztJXAetnGfYV2HodEUEREhIJIIVNh2QM9A7qCL+qnsFkay063MPJkBrXGQAqDIVwo5sI56oVWVAlXatz8+bHerbwcLc9V2dUzou1vYQAF7NQ/XMd+7szQOLq6FfSrPeHJ63SMmPeq0rA+nn8NQVgBkm6/iF8qvmOssV2/BzNSdNiCZvkhdtnnCB64JWPkyBj0c3rEVE3cSnLvhB/aEzlck1TFnh6MGmODgaUYbqzxiU12MaDnoDK+jevV4XLbl/ciTAcjoPvb0azKBr7KkfCow7T8m4Ffux5D5ngg9xghGU4kHWEj3ZYyKPN71UFI/XDPpKR4fi7PCy/Q9Ap/2sVI0t3X9I8j71rek9/xNdeNyHcvDkgiyTDTggZgcrRqlaCCEkR+f4sBNH7BV3FuOiROtWZc2SAKIcPOYmio16ZTbnCs+c/mgbmci6l0hNt5KCjr2QSzqQsgJr8ZgpVylqDycoqO/CJtP+UxXhdWNBCZycppGuuyYFj9h0B6r9KDtCDft9cCoR6GfLIgwU0YtIlKAPyhB80Rx6p7IFdYJlSoq+dmnHzfELmZLpHebuKz3S4GRFoOeqy89LeE/rkuKW33nObY/N3TxucZCuo1dKFqjhSRSAxILESwo+yKu7FaO4Bx8rpNzEQ7wzW9QpyfWwJfPCCblOsCmn/tEdXFWUGofhn0PcOO5PgeQARmZHvnWK1G1iToFdVRaRzgzi15OJ34CDGdP0PG7kapWLuEjXQ/xV9mPcl7shX8s2tEWj6BcL9TkVBv8Lo+HhzDd7TGQ8yblP9xLV5A0DIwDkp7+N/FBN6eV7TYdjLXH/QBrRqrou/nUrjd7vzQZ5Ytxe49US+GRxAxXEmA8IZKnzbsZtOUMcBkVo8izQ8xhBUkgbgMdnxx6zgiURuzTiquGuJc7rnhd4slcnIqKq4tSBIiOQOISqUxBvygE7p7c9hYWnlVsPvV37LtsHUAw++2l216VtwwzYcJYrqRE6PvWHIAIQp0U7C/Vd5z0nRfOWcAUo0KFW008sh7IJCvjtJ1LMM4iagH51g/RJatnsCvpHauVcv1GOlmDHxzzo5T0qgQiye8pNjf7pCb+n3wIsTGM+d80qXx0s9cQTPtkY1dhmeQDODja96fXAB4ynsWbSkcqQJ9BkjHMYItFyrhixgFOZsFRmvWPYKp9RiMg+oQDFZT+YpNbG331Xh+y+G3GUqFAlCMOar5dbpGPLHKMQaqmcINMnE7SvPddPwoM562kK8Jj7N1uSY6ykrpGjKAAtKm8wAHiQ5XIuCpQldlWa67wFoW2NqBa9nSmalaDq583qavdbN6e+OVvOsOvX0BzAwflBffN7++rZpTlx+DbYWuUbZumAJlEC7uvYpd+gD945v4bS4TPFfHAlJZyPLGhGmzGKo8/fiCxjT9WUab8m5zO9y1fMEo+ygMqIcGcCMwQ6YU1Mzd92Me0+k5RX+cbawqAlnH9oSlKukScaEq13bELBkgm8811F3FmH8643N123Aa5/Sxnh0rv1rosWgmdZeBxO4y4pSpzxC7YtdNKsmM9FN1g/t2diIMLzAMIouhckiD2Lw7el1s0zNdxMh304On7rVlLb6S5L+IerTFsmEAZQ8B15TdMVW7UvpsEmQ8Zh6+lXrnLmmSMW/YuRlwYFS8lyiSRuhBx22Q404H6yeGr5/100D9yW1IyEJoAh0u4GbY5HtwUbyAQhSX1M1sGtww+b+KoiaqjKQfY2SBug9UCDdzWh+lbgde8kJTbxZYXkohJhZUiFxlrOV8JT6rt6O6hESMN6EVkzzaBSTkh9lttzFfOuhXHZ2mKaKNCVIzvAzMbOaKvf3HPUO9+SfriSmVo/CChfOK8QmaMBz6tcFDjyDaKPFjRCp7n4K1UVj/DqOhychw5L9z+CEYnDdwXv2MJ3sK7c2DjKJbRWHJPA+AIAu0HMZIR35+kXiK61LR9jTcwZZfDe5gNnFq7eHfDqJjYSj9yi/2i5tJ28rU+Hd+GnSh/1VgK3UxAjSPmlVeWUCBvBoyQoOgMOfpoqTeSpUl1WxrRL5VmFu6VEP6AivDKQtN3saYIvXtXj5d438La51Z4cdOBaVWBlK3homwlMG1RcLW3mzCRWbyev+hqcJvNjnY17rvw7FjIqGFb08zvzdpXqiQp931wqfOtHdsmIvoOraHLrCodqKpWOvYzvSj3FFi38FLDInoVBRuMdkWdjHZCefBHNnqyZTyIe4B40+nNHIo+egUCTXBs0NIZw870cRoeL6LtSee+yQV4ui7JgiSWb8K8gh13siEHbbln+m5ODoGp1t9yuxAy34kkPqpbKKvpA4swQOBI7IoeeYKg3sLJUwHeqOSexzt0FtYg8lX6cbRxwlScv4IxYR7lWx+aJgKt9LIAvY8c7b5Q3kTmn7gJap2wTaiN1wLw3ctaeZAEJk+Z2bBFzuQJm7wLDaDS9chzNxl+3l4rpjOqpYf9R9nc2dGfNuMl1XXXAL6KMk324VND19M/KHnGTGjgMocs0w/ZN20FUmWYReXTojTnoeHZdaaDYH7QRnLZPIOhmWQ/tKRDd/813ttR30ObtrSmPz9mLccluQeopC4E1hFR5d2IovuwjLNpQ3lUPpn5eiyGNXwXclj2AVj8LUeHw4Asb+RSae4beCctf9Gess44vITX6VNTehcTkVlTW2EAa/0p+0YJCL9D1BU1pQJZ60F1UpNni05ITW/U/IPbWTBFBQ1JwSJxNpzDh4hd7sJnwsEBc+DLh0gVSX2KFKKhDOVU9DcezJcW8raZFc+svc9H2Kr28OjmTOer8vJEzvuRnI/Woh4r7wWDDae9dmEBqsa9X3Z4LwMfDqKMXkVvumWibNbz1Jw8wTWSJjHmSshOismJHdILqoV1aSUdk4F/oOWiS8qw/M5QxzNlhCV8AleOUyA5ydF/MDyvN48gnb8ykpjCS7pLeU1NIzHWumeXzslsWVpp/4cVFG9uy+tT3QgXJwx/NqQT4R8c/d68JJNHXccCHou8kM9l1Lujsa+S0bE1HUBe9jLODVeMjtUUIT++vdnesNvfeRaH22oKvg/6nRnCJy5T5uwATjpwPmVjpZhkcbshQQ+b2lYdq49PS2eenLCqLnb2Wo1ogfnzH+6XcRSTF6uVXo6kNXXKl0HimddYbic29yb9Tkw4jka5i1yighnaSCh5dKsOcALiXvRm+ONWzmb8CgiAHSi5mQh56tZfrJ/W2PlYH/DNl+z4TzLThmExhCQx57jChMPYgEVchNdgVdwsxx2zY8KWFok+aAsDBVKtPJp5UT5F54vHQs1K+YljGMfBE43MgGQDbyLUPrn9Y3yJM0QDwHcWX2bV5DPETakFsQ3osiOvmw5rgk1qQDzdkqqxPWaFD/pAtDwsvijLFOIub7ZLSP3mJpPUxvtsqI55aHJcj0i3w/3sIOv1nUlR38kIjLQKFBW7U/5QvvZswuz4DVsKlXTQrKu8lmzydal1+GttxO/4wVHJnoDX37csu4IHarJWJ7/YYiRJT0J5skWMtptphV70wBqfNiHbsc/Dx3VYvhsGH/hJID/Orn2BY4eo6wGDzl/a5oFVGx0ya9dbfM+HYh3/1WiDxzahdIWmKSO7l0pSy+WeQP5OziGImDAVlXWLevpMkEyiWEIIifd1bt/5jk7jh3uvOoJiuTMnjWk0OM762/Nd4fG638Io0ZMr/u7c4SM6CTwMxVYt5zu/dTkfDMK46cG8Bs3Kf+TnzlANblZPWjfo0ncOAGASlO6Ww8qVeElpyB4ELNsD4j1mEKaIOOzBBIofFKfAgPO8QDq4i2w3k7J2VyKm9ASFda9jD9GQiAQ/IlBYYHp9RAQGcbvIzDDUyoKepZcVDaUFDRP936qDTObvRk5oiAGXNVBcNwXKue9IJ+0RNR3vQ+2z0yv2wnrUu+svzla1yZoxBD7ZovqJ0Dd0PlLSyHX5a3MZz3MBan35amsBamQLaaxgsmYfCnWf/8OmW68+KkcnV8X5Njhw8wD3N15YoM9S0YrduWyNpr2q88w3IOOlf90jnFluzlA9XSHRFEmdu55WvVe+mQFyfrAWoeTrWY/rgDsI08fWduIcvxZi80js7qoXxThZ61Eq84MyOmq6cyRzNTLZLvk31g10bwFm3Kc28zgy51TXoQwP4qh9BTtpDSx7MWn+IS7tRMd6Bqs/uWIwK1Ww/C1pX+e+bO5HugcyDpBlg3YLOnzBWn3O6zEG/SnLSWEb8uOY+qWBQ9lTJ1IUNZo/cCKQshh/aQi7xzleM5Z/RHmzVS/kUR04wMyWC+9+OATLjKwPM0UtQywA/ahkgeLNLdcKzdMLFo8sViUg82nvCkFU2O8RADhUzYtknd+q8wG7rj80K7XMa3rPTHTtlNIDVWsoDu0zpUcs6mWjMCtwHkuuXCF31Vgfnwn75IPTZy1N7XX9yiUbJ37pZkD+h3HGVPglA4Vty5WUEWn5n95+565mwZDXZd+5QCvGDMP1eNwlrROcQ5mfHvCMKqw7FMBub4KwyYcISBtDEAQAVt1ukaha/Xk3aRLG5jhA5M7diiVUEKrQ5jMPkXGRU+079mdCuVyvvRALBxblrjcOFACGGiLdxLYIMBRMcHJ5Qlh6bDjpUr4thrkZe+NuL55rAaaEQ8GtoJd9MqSTLxs30sDP8BYsAfr2rOJM7Fi42S/XSDChsBm2rm8LempQt5VaDUKifm9br3rQOExeZjPJReRTjIdYaf9gszTS1MGkng9/wzgLPaz3OtYzcU5TBC/YHk3ApI2t75ASy7KuQoIPEtPoMSRROsciDtWQzFYivm4eECiupgRLdON+2R+XmbA7WOXlb9oLwbzPTkvvuS3a3TXXbfh2HGI0M7hm5O5NYw5RNeZNCPsY2QMaMU9K5tDt2GoxBYpNtsQ+4JAvUXdS0DInXL8zt9JGdGG2vKliBJQ4R02oVF6Q/NXyyI/8iuvUdP33NCCnAji86VHRZ1JYg76vR+bVpXQlTEo5q/n4Y+MFU4GzQJXKV5f+RRhKt4VyqKzh5NShl4dgd/UcZ9dMvUj+lIQFz/tiaetVtoWB138nFq9qGrpCLs5G5q3SXA7Ziud1wAbiWn/BZz1/8rqfCzfa99+QyOiJNs5aA59eeFPzjQVHoRPvJCuRz5/xtQ4ZrbAFX80BPkwEhARQk7CaM2eUcQYDSRiOt5ehlfu5wnuDcPbFTgXuiz4GkqFo+CKwHNLNdmfGlzqWYDqVovTGmmP+mBFibtrg1maLF5lcAdGaGu2EOqZkq0eD3QdOoAQfDXwY4ZAE0ZR/Kxf4tc55oc4/vbwWdDKoHbss7JRM3uXv2uSXcbgqo53DmSDNZ91pvG6HdvmeSY9uxkBbuhJbNDeQMm0wUSXO8zZwLwJlAJNQsBsxDBeBa2AOxHtqwof4lVCgu9iNINHi7K46y1U43wMDQE45Lhb9kuxGw91p9k/3U6lHD+OkYWruRzBsCptbO9HTRb3+rXAAIL2AaKUhiQ56PceUmOyRnWb1Ry2HdTLQxjaLrvCQ8KFrsXSHT+vOxB3E3DAPMyAtMk4VxjE9vmIgmiIM8lm9/UECDajY0LtoCj1qNN1OIgfhlj+V/8znTfvZsN1aHjULyL+V3JqVg9xqaS63ib2N8DdQPaJJgUiyoirJGkGv0GNq0nba6ZFJwZbbWEY99ZsKwmwKa7X3lgBwCoz/GC7rSB+LywgAsa+Wfv22T1/wudhe61RQJ5/ohk5q+I7zrMCDo4TZ7ADOjrf8vN8ky6y8FNVGQqAWnidgshqr+Ewoq9SODV13lwHhGKPKyX9QHW49jHWRf+9Hb/ADquPHAslb1jxCoAimMaVUTDPsJFVCMGU7rGFfJk/XLPrYPh9+Ahhz9uJESztPhZFbUi9MUAmrkbwRrGltGfAWZlL1BcGmgC7zNH2wspSovJdTGrEhp1O+6jRdeP6oiIvhEx7G+iRX6nTUHKlBi4l74mQ3JDp7noxP7tbu9Kw8mpaCdNWjoob4EbtGfZTK83/gjoCg+wWypC7PlYiJ24lHf/5YEfThy8fcMHdcPbBJFapyDOzmevoVFsWisKaeEAHiOfYnAx9gPUJqVBal6pRHJejDrrMG6Ytb2IRj1ORLSioq0jXcWdd75ktEDXdioxU/ExiK4LmLSlBOoSp48DWrMB9LZr8lQwp9BAXlIQ0H2OZ+ajiYt8703XsNuHx+GxjoTTk27TGPDQDSKgOczQ9gtBo3qy8n95frRpRXAhAXRhlW6m+97yxQPh8skD2jhX+UzdH5LSeLZMs6BQGjzNTGfAqRzDZA0SP/KZeBa16EI9aRRxc9Mz9rwt4qhdjIWN7KrqHpQ0RG909gPBkodhQ0GV9AUd5Go+ckNMdpHHn3T5biFv4IhaycFRQsGhswU/jchv6+UXZkgUZnQ2gWWyl8EJ26ROKPtyb+/Vkc4aZOD9qTXAiWwUV9Frkfv+UXLt2n0BbbJLRNzafh2ZulROTSSRP6Hl79bJAkIkPhVSVN8gHrYUrSXBYnPQ0JunvufF75y1pH2aqwqIEMb0sfRD2gqSRAcxuhzXTY1dps8ePA3Iqjoz58eMlh1SeUvQ8tg/0HKrZpmJiNMxLNuLp7wr/Imqk5JdANZkJIRW6dbhodcZ6Wx7GLMUGVK0ftj3V6NVq9Zzz7DrZ5+q95Hspr15lEYO+vjq1qnZK+WSl31YDYPu8m3SoGAQVs2EpUIOot+nmFJ9aIl57+0CnxKUkNKeve6gi0es5ydtSUA1iQnHUEjCpCXv+lUnPONRxBaAmSFWB1nW8EV7lgWoKJxcJNNXwa5f1ONJUbqhtCupyXq6R+LKPBBIItgEheAiUXyx0a7lCd7kVoZZ/Guq54CKYjEzXyRzwkzE42zF7aPV9UyjiF5EA6JXWK2x/7nbO//BA1FPO9ME4t+ZA88J5Dl77DN1oNlWAHQ625XQCBYlVnMg3/Lei612tkDAVx32zTx+fyiUCKu6oAlNdOkJF6X4x5LXKqBRpEtiTcgGwSMEyD+LumohoTJ75748PtRAjYkaHn/MZ/q76CyZLAvftshvWrI8nkW9uN2DMmF6KujJwlqz+UPz3OmDlin6iuTks8Zl9vqdt5YRlMeQaY7kyh3Uf37i1DePkzLZK146nFJWgfEaay6w2BUG85ZalMrQQE6QKJM6PDQMOh/nPss/Adv3XW6H12s3K4TBvDQUMnDyhEGulSWcTAGJTu2ficXPUsdn5W53tNhU9ihPd0+odK4drEsYoy9BENqeTS6fWhTrhrJHrxIaX2xBsrcGfKVcD8/9tXf4j3DOMsfqIo7FZsHIRy51Q9bmdfPFtkTJ7xYqibehpNovRsk3FD6nR82GZ+tAm4242buGbK0FqgN4RAI9Rvs5dX3CwF22MUDY4SB3N2NiAMVUxAx3whMPXsIC6IsxYBtjHw6kfRiqAsSvkohAzaEqN1IPUJ4Cj75JXSp57Ai5qlbrD1sqdcH2byIOkW5Xob2c4pDF544hBPRN6qIFjMM1oEFeUCmgLxIQEuKNz++GPfByVKYjwaFPJLy5R5iPjQWPfxjOgKL/XuMTwvXDzwXuXVkg6o8UFzbP1OSmbKpxG/FYZzc5vsZ46wN9Oz51+LIz7MJ0JxFrM6Gfy5A/SFgkqK1QEVFC2jMzRgKhZG4M55ygBmns23jLaIOXClROUoyJRqQx1T6l4qkUBK0HUpIV3OINMxsqLbIdoPZvm9oxB+5tafnkIpVVIoysMs0HSZnEj90U2DB1m77Y/yDe6LvNHeqW1TXbEmq5pp5+1pl0oZpSEmx4EsPUFZwP7NdUQs+eD03MmgdqqL0SMn4UwQSjt59qbfWXzXQW/eIsiSl+RLX6rYTkFSm1/u9ETw2TkzYCJhfhdscOTsnQud6B3Uu+jtI4WpwHfPebwwnAnVHcvbOHgPPiFd0tdEee/RLLEcTL3k7jfzX05Wp05lglfo0MNOU123ESurOjxrNDhxLnpteyNuVpGtx77XMm3atBFtfbOKykIceJrCF8SBp+b5FYaycFgo/8JmUyhH/qKenO3Kb9f+D3KjX/0mfPpzcjcyY28AEkoLUrc3JV6nqxA8FJu/kq8OOel9/bEfhGWOEHjbXDKq1CU03xCaR7eM0+JE5LBDS9N5RMEXgOvZ8FG7No8M4EvNJlH0B0BEHPFyAIDQYB5u1oZcVSusiwT/z712qj5Cic9KGV/OoJx7xoMWEyXFApN8Ew6PbgyBE1t6B//pgPOD1M9OnVHtpd0ZZqd/5ChoQ3PbZhvON9N2AAUODgI4pc/UuBJ3hmr0RmVfe3J3bEuUkcozIJrrIj7f7P+QikH4x55jbwX7HdF7AYVycYd8KTB7+CENdvNZ80um1zztkgTOy49Rm/XaRzPQnXmUsHtqWSXTnB/AvzxwdnScgy0ef1V8Xkf8QdgJaFgdB2dvZXFz2fqLa23RGD/QRvgOTaMFx58EaF4XKjeL0zmYBlyNwBujzbV9lxoZf8DoQznnWv3NYv24Fvf9vhTwQ4kqPHhfKSxVWjTSsmVRa3DJT26zPki0pueBKYtY40OqQ0rsHm5X896tzNe8rh0n+GPgIOiH+F4NN+BKReiFBjs8q33gsgbuKYqcnM9dV2hUREB5h7sZsw4j99DaLlXSdvxYmI96tmySis05XpdqFLLJVD4djgfPS2/VXpatrDLnNHKpmfPQb2ViZZE3PBVRYTJKTrDOni2Gu5vCWOzR4K2iFDOmukGk98Yiu8gFyWdvLiqPbLBo0MQGzgqyfqghGUmCUjSXwJpQf7Tjuq9MC01e6Fb2w/jfP/JlvKGLOBerZ4NjX4F4972qqEjj6wuvbdlcBLXh9mrKxKRnibq6ghXFmsxGCXio5H5ZPoONzAPrQXekF7rMqxRZaRfTmmeLI8SaGH0cnikkzrkxmLxRshz0mqUeFzd9JFT3jcdL0lpaOVlUyGP7vlRKJjEDQ3oq3Mm2iI9ZYnpQOpa40RuufeR0DeNXbnM7J6pPFA9e1vkbF8ouSVT7jt8U0aVWHdA+AmxRsWPFW1p9gGB3R+pGwWGLFR59zYUOWMR5vWLwOiTXvgVERCTSfChsk3vdGvlu0X74QJeXqZNfbkYaUTI9DNhJC5gdGAfyIMBYI8k47/fnosEx1naLZEd0mpiMSClj5uSBafO66gLdPmE+Gw2s6IFmdxcHl+4g66Hq8t7XkJgPjDy3XbRtbrajprQU962aN6KelHWhOmLxDSQOBoBKE7F29K12fuy1eQaAEkaYFe0bZg5ErC2j4JfIpyt/rcfcMSIwr/aj2jbNFhd2KbQZ4TvaOa+6TwKG1ell3rYwkMz6RUOV7tGeNjt4YWJXTAtd6PvI+uPnA/19Wc4K66F5BWhl8HSoxaN5OFmv/M9S2uztGo/UlPWMI1vjovY+pF3rqBsWknrCeJBsB7nfzLjSQAX6fiPmwldg5NjGC4Lakuc3YuhL68VR6n48U1dInHNVopvfzlfjW/XvGewRyn0zhepSSNoskY2FR+EJ+hkgSOTfjORgEyD0ZtZZ34OQe0ouL7i5pEPDfyOkhNMm1xO76SOgN35Oo6H1tMcGSY7NQ9zEekA1iDJQDj86C6j5oO/hGuW9YEtmnfzjAKTcdWDZjWLLaz5M09vM9DTUQBOIat2wypliLyKsguSW4awRljz9vqyRpPLwIf1E4K7Nf/DAM2T03evb7i8sitLPxr8itragCIo/j8DbFJ9PeT4jbN8l0cLAcB//n6WRYblG163vSoFVOM/n7ljDgynLU7a3SkFBo2PZuo6HM6pi58RqZnPwyUeJmN7cComCPiRjMBFlnNgArIKOoyIRwqKqjx+yMpOVygA822I8m8P7U0lRA/Bx57spBvwCOklW9gA7KMme/ZjzNhyYaoUQ1WrHNlYRb+CCjxaHnRo52LVfzAOM1E5kveZHjbvS8RFvrwWtlBwzbDh8TE+NqQkrBr/0PCLyG78xUEnpKV7I2LU4KIrUjj61nkZn8x2sJXLntMFp+oTlqibiibjHyOPTEmWpB6YagZwLOs8wHJpowYdRA7++hZMxKsVag/3whEfbIgetX41289bE29NhYbMPAbkUH/Cknh/DRXTorgKHN6T88f5eiftb7U/DWEBipIYYxshuVnBJ6lm12BzshpziJcjNkKg0JJ3mfazVqnPYqAEWJZ05y2u8c135iFntkIkIggy603eKrHsz79zADBG2P50Xg42NxcIBcbMgpVoDBRshdAsdXt/WfDRfEfAQTmtKIYzM3Tmf/pmulZmcwKBQC54A1uSCYQ7CDrigBr+zVK3li3Q/o5LfQJSSLMBn9YTJLZO+sEzSEYUTjNCQH7jyy7jRGDOZWCtudrPxeABn7YpzUIXqoMCtTv16FMR0EZ0rujPSIaT69Ra+2uOhoyk+5hrhC3cOGZbKi4oyuJScxXa7Z/scYlizXqLZGBwiTQ6zcLGF+XBqCZC/BlCby6i1srzI79k3VC7n2iHQm03wyyMmNvWq/v/Bvi2VLu0PC+CjyrzJtLUQqiWRTVkBYubhEDxNZC/gAG/E4eOLU4PozV1L0S0ivSyD6/zzXh5U4FiBst2NUav4GNZYFd8cC5qQttl4d4swSqVjQYO1nW3TrKnQBLAZA+bYNUz8RFz6z77VtBYa0BFueohPOh/nf/GpvVKxSeobLDgVrQnSg8v36s57mooY1Evk45AvPsDUSAT2IWv2v2JicucoddIlC4oTlnriBXo+fMw26GLuUlRHEF9OW0CKQ8DtytR026kCH7VQGWNRL7bxFSJ7Z4U1t7bsxjwPvNxSGuErfZ92tQD+1XKnBTXeaem1fyX/0NxykH2NSm4/x7MrRSgUxnMv6aIR6OpJhhUy5/wqJEH631NUIP6uhKJh/Zjo5517qbWzaOlZAVveNIirntLjRc7pkagnc5nvCT7djdXrMs/7jgZhPPNFrMhoQDcgEFvOhE/GfGxJ8Dl0ylYeVT8UWws5gAmMNmfoQELIacT4YUICbFjE5ZmU2GUiHJUXxvnHQy6wHK0KKbh/MHMDJXlA5AHUpqT6OzdQswi94jxpbrj1VHCRB3STMcG4LujM18/8zmKRrdUGk7kFI7ZCaiEzY66CdLGXGViByYIE2jB/N2XEnIsPs6O74uZNtpC62WYYnwCJtXlqapnyAKM07CX7C3BOuR5Cr7v6yxH3p/4XXMnk56VMqdcdL7/qRIXhh2XgMbGstWbBSNzRjR33WdB8sjHW7sp6AQsB/XurZUZv+4XeC50IWsL2XKSA9PRXzJxLT/fW3eVsNOf0y9DJVMJ2RdC44W9YWpVps3S/eezCP+eex5dUazBMbMrfUj6f93wssc9Dyl3cNerMDvJ/DamWo/cKFl+Fj5K0NfHUTF4HdSlOuf6lRtqDyR/FnxHrc6zZJ4cVmTDKbjxiXVTKmbfrnkZfB8AZN8GnmKLlCe49wXgrSOZqNyweMr/vilaDk3dPCey5XSvvf9QJN37sUynOgIkYEKQwMCU4vKlJO/MXo5DzQpfy6ymGVimzZAD/cZwcckIDz2kC2CpUXJuQE9MrqSnws1qh9zHN5BOsA1sAyErfY38yIT5nQ/ppWspdAZriOBaBqgX+M7t+t7Vk/GyynEgxUT9ekCDrHiBr/IfAum0tu3ES44Y8rr7N4w+Z/M8mvIC8Dd4Xs+uPZv3W48pkIh2+6Kp1sTMVyobqAwkNHLzh4nVNQUvaXb41bmMuY9B1KPS12Wjd9IkZrr/Y2lyeGuqhpfQrm9aP5VN8p8nTSpk3f5zUEOP7yvB3cAv8YB2RZnK+bZtQHuvazdFPZ/Q3W9BUPgM8l7CCXADKrGPfkTa7t86tWajCHzkG3laaTJI0HDA2kMrFxrDog8OiUNzo0CNfQth9d4JzMG3b8oB4BwbGu/7m9HqwfnS76fZyWbFWaIZUD/15/3DHlZk8N13dq8h0NN44OXZl1jOWnZOLydWagpRMH+PZXSTY2HTZZKCFV9D6ljqfSJxVjuhRkuJx/WBq8p/MDdqz9R86xyRr8CxaXB9BGLwA3g2bf4tXcDDla/b1n5iGuPxXA9visL//MaLuICXS7f43RwlNLGbFVjqzSPVCnSRwuf3h92/JUNc77dK8DvvdGuzk7X7QADgTBhk+YcX6FJTBNhhN4Rbg9B/67V5h2+Y/yGyUhcXAiyRCheK4XYBWWI6KSyl1NChnm4aWWE0SWw0G3nqe209xKcvBipvVaWXOZdXtMMV7uyfxVZ/IX1kzEnkQ/485Ff6lrDZX4Y6vxTfTuXWCl0N/3iSzODCeG7/+3ZWNWInoiFRIEytvNIk7+q5MKjaffpaEyMvG9CPhlTIf1I+lfvRZoLKK/4XmApdvXLvcsSz3odOp8E/PLtUGHy4bVOa6/RZJtM5nBn/QyB8X/5PHupdqynJADTu9rcEz7gxGCO6KhAlvbbyW06kdpcwbLqPBp6pM48G7YIKcnMC1Qrvdav99FQDWyDWFuO3tC1xfj+CKgC1GkBfniXQEKpIlXTM/Lfd1YINz9UbDqBIQnf8klJ8+qHJShP3O/PpVUzix+MsBsjzY89ApgE1xaRMDoPP9Wb527xgNx1J7+jXEN+EDuLKXqfR5BWVXl/3Q1bGbYFdAyPYpxQ8XYYc7DvyyIsCV4wNubsgyapKLkxsi//U8z/mrwYjWvUbrxShzPXlh7FfrXC2Ad7hAwighHyMshNz9l59DsgonT7TI07p+2LPAYG8gx7QGfkk3ZFRWl97tHPKTRQkAkgigKfk1CPXqCWZXZRrIgpMrxnTaiaaNSQOeJnCpG2qJzhJAgQxOvKnVEY4vpEp1VMfG7O/AzcPeBTDuzxseHO8SRaFMVFGtTNHDI7WsiY8knms1xX9txUBjv5GXxlZWwyCqOS0HX5P3g3QmSxxbIbzSgqVMMvvshlGyv/JMQ4Y/oGo0R2z2f8Pfs+MLXK9GL7LYyaB2ROaZDUmRCLiAyWa0W9teUTdmK/R9dU3VbmFGczjPQxC64wo9PeJDXxul1DkTAZHJyyzbka01OJSBBwtIdN1eaAMBmcoRqLYiZgvvdTCdQtbyRTd7djgNNRyxcnfF5rexfYFJJh01eL5/f5dFack0xs0A8Ihm0RNXZFj+N/pBuYqsyqv5UeDkfbMfZl4XmETtbGMoXaOJAuJ1ktMNr9q22hDO6jcbkzuIMQ1EpuFDGfDK6FdIkCFWAyc0NnP4QxlQfLKueo5SWjvpvYGxGeZ01olSVcN60uMMllKuDup/KZQ7awktnvKJzjTNzV9s0QAR0ZWja5/Ob+bNn9evVWvVjrlO9uYjivz53f2U3fgAbHSpEhFw1l0VAOc23v7zfBv3EiZC6q8pFBO/wpFYEF6Zi9Pgs1g+WzajkPnvqxSV6oI6C3TSSnYONSiaF15z/fvSQGf9eITTQsRSOe3RfSwCyVNBPf2WAtorZa2BaKkYs1pyuy8k8fwVFCOPwsva1HEh+39Em42vITi+Jq6TaO81I2uikLQv0bqqwgyHmvwSIrYGV2uAmj4rQHeYkszSToZmTWIFaxYB/opJFVJQRk7uvReTJRjfc/585sOd9XW3w2vpn/GXW455dvSDq9bA0nueMwwLPAiVXTF+j1HKihCxdGBfwfMNzUVjp94hHKTSt5sCxfmLL9fN8x6BOFpuuDkKs2o2DRaNkAI4KDhyo63gT9OLoqzIsVegf43KRwUUzRKx/GudGVAUEP+cMze+WT2KFNz4y6xyL8kOo2HtMEbc7J/+y7YhEhIDU/q1ENxW80Y4eK2dXVTv7RC1hjUnOUcGDZfrlV5BKaBD1a+o2JD7cgZmSq9KIfaa94v52ivyhfzv1ZEqFIbSG26StuvIK10ica5sMsEuZPWW58e3jUrFV7QR0T1sl+lMybWHbyiER+4ws0EUgj9uXlHA6d9C14KhN5YWHrxip76Yu/08Hy1Kn3vZfSmEteqTpCa6/aqTkgiRcHVA4od2MedxKTbL/NFKtCzupi/yTa1UekubxoSDHJKH03D3UQe9XfaTL7YoBlbbB+IB6rRu7d09nox1N9HTj6hxwes/u3pyhb0RKVi0t23/iyilOTeClReut0gcFxgMd4lD4PYjIEZWnhS+ptZxpOH7fk4x9CYu23nNr5beYpqc2BFkNJ2VQHanb8/RZMtmL7HSDn7E9mfwufO97iuYtPX8mmwSk7UIHh8T3+Bn8+6FWGlk9nyS2fRiPEh++kX4zUwzaIVo+R4nfhd+rBjRYvrB/2j1TTtE4TTN1bdp3Vk4ORNt8OG25tghceJCCZM8iziGw8iuhVAuZ99PiicUxEEifU8aLre7mdJAEHQywTEUeXf0vV5IXlteFV2zBOWJPOTD9pBTWctfos3HLEVPulEzJAl9GQ9A61lDfnxaapYlo4oSJgHJ0jT/0VbzFls59WrfWlm6GVMwufSKfx2LMdD6rU51XrHG+1mQvBCyRyqpZrLcmNBQ20z72lfugrohre0nOv8R16f3oXtxy4XHi64RGFQrw4SxN18J3jxLOH6/IuSCw7u/Iv6Eo71HkJqGB8He81UBuO4inHrEkqH2hPbtBGCupYHvx8wL5F+UzSv0YcEpP4UTiqP25LqYsF6EYIcT8btD8/y4XRwILDI72WJn4Q82xTgNPcdR09+rVeqpeIM09doc6IADHAP3x+FZ1Ov6SLXd3bBvLxTXN9SkiKHjaDokavCxJ34vAlJSRSda50+Hhurj4J5Jb8XlBYpzoIL3DowAcL4suYFcFNvjfwKqm4lhso4cwD5fCLuFtXMYnwfzS22zuYLXOGF3Q+5VdJEygUxlG1hqKO9MAYaTvaztsoBnWPQAEhdrB+Gip/DgDkZeIcvXBEFn4V8fE4WBetLA7/pEFfK1XGyOu6DN4JY4b313k+P8U0ojEqRt0JKxEIbpk8ddYZDCkbAq/UeRuDlDcR+WG0EyRAQHPudIuSf/XR5c02GIUlWltf5KrG7mYyLjx1zjhuu3eEwqCRxLDW0T92bA+PZNImXxT4ikz1AMNAC9oBYvdPQMQpAi5mK9GgCnNWrqpCkPFQvP+IFeJH4A5atrQryL9ex1CzQ/LYVhz/YRgbY4mDYTktKFmjJyW9ImFhM5huBpxzmlwgnghvD9INeBs0sBP2zz68+H9DEnXaIFKWHXfv7+wJZMacNx+KFFuyFsuHBFAZMIhhxGbrVCZGcXb4aTAXgr58OehDW8t+44nL+O8mEaIrl8bDHC5UP6r9dLb0IZi5hpna+qlBl+THH7zw0FY3OnSa4ATEwY3MHe4FFMjY1bSDrhjq0zKKBs+1cohcr3RC6FTW9DMIkWztlO54fV1j+lzTnMtjtZtxkErOY4JIzcuz1znMsL+3+OM1ThyCNs1PIKDvh30O14jPIHnhre8fXu043R9zAh32SSWlWUH7R5L622fXuuBQZ4w0ssXT/Xn90S89ykHCDeKqro/XemaN2p5MWfv2W4aDP576iHWxzqzw4XWmK9ckrtwuISkrk5hC1AjSqO4sepMW6Zii+jZs8BlvBrz8LlyqWme1Snu+mm4GWcjwq2S9srnLUTeX2B5wSgjVt1eJ8ZUf2aVGrxZ041uvmfSMgeOhP/57Er/Pt74TdLZR0UvecD1Bc/pGEVTZMxagIsWdtKV+F3CUxGdtaeScwfct+cNzFXgzK1OId5Lo8h/7pDdXdr8pC31MNeeVp6FB6YMmsU5u7MbGMJZwQ9tIo7ZiSPqwU9pexBv/VCV514+zTbDWbe9mwhXGvkqQdIcm9Of0XaR6b88ojn+XJYZob3DA8LqEOGxgyRWDvEsxErfhrUAQe99Ya7NucC5Za0fAtc3AxhPWuiQ9P/cICDXh5/5DOMgd15G2N+8kBb11mc82uEygB5O9hPRHDWAwWPq966GoPfv0TmnbXL7M40lOy+rw6F


def version(now):
    try:
        response = requests.get(url)
        response.raise_for_status()
        dat_up = response.json()
        new_ver = dat_up[0]["name"]
        if new_ver > now:
            print(f"{putih}[{oren}âˆ†{putih}] new version is available, please update now {oren}!!")
            print(f"{putih}[{oren}âˆ†{putih}] current version {now}, latest version {new_ver} \n")
            ask = input(f"{abu}do you want to read update help? (y/n) > ").lower()
            if ask == "y":
                os.system("nano update.txt")
            else:
                sys.exit()
        else:
            return
    except requests.exceptions.RequestException:
        print(f"{putih}[{merah}âˆ†{putih}] cannot connect to the internet {merah}!!")
        print(f"{putih}[{oren}âˆ†{putih}] make sure you are connected to the internet")
        sys.exit()


def runntxt(x):
    for i in x + "\n":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1 / 100)


def entry():
    while True:
        time.sleep(1)
        os.system("clear")
        runntxt(xtheme)
        print(f"\n{pxh}for tokens, you can contact Mr.X {netral}")
        code = getpass.getpass(f"{putih}enter token {hijau}>{putih} ").lower()
        if code == "hackedbymrx":
            time.sleep(1)
            print(f"\n{putih}login successfully [{hijau}âœ“{putih}]")
            time.sleep(1)
            break
        else:
            time.sleep(1)
            print(f"\n{putih}login failed [{merah}X{putih}]")
            time.sleep(1)
            ask = input(f"\n{putih}want to try again? {kuning}(y/n) > ").lower()
            if ask == "n":
                message("exit")



def load(duration=7, interval=0.1):
    animation_chars = "[â˜…*******]","[*â˜…******]","[**â˜…*****]","[***â˜…****]","[****â˜…***]","[*****â˜…**]","[******â˜…*]","[*******â˜…]"
    num_frames = int(duration / interval)
    for i in range(num_frames):
        sys.stdout.write(f"\r{putih}[{hijau}âˆ†{putih}] please wait{hijau} {animation_chars[i % len(animation_chars)]}")
        sys.stdout.flush()
        time.sleep(interval)


def message(x):
    if x == "font":
        os.system("clear")
        os.system("termux-reload-settings")
        print(xtheme)
        time.sleep(0.5)
        print(f"\n\n{putih}[{hijau}âœ“{putih}] successfully changed Termux font")
        time.sleep(1)
        print(f"{abu}[{hijau}~{abu}] open a new session to see changes")
        time.sleep(0.5)
        print(f"\n\n{abu}[{kuning}*{abu}] if You want to exit press CTRL + Z")
        time.sleep(1)
        input(f"\n{abu} press enter to return ..")
        return
    elif x == "background":
        os.system("clear")
        os.system("termux-reload-settings")
        print(xtheme)
        time.sleep(0.5)
        print(f"\n\n{putih}[{hijau}âœ“{putih}] successfully changed Termux background")
        time.sleep(1)
        print(f"{abu}[{hijau}~{abu}] open a new session to see changes")
        time.sleep(0.5)
        print(f"\n\n{abu}[{kuning}*{abu}] if You want to exit press CTRL + Z")
        time.sleep(1)
        input(f"\n{abu} press enter to continue ..")
        return
    elif x == "theme":
        os.system("clear")
        os.system("termux-reload-settings")
        print(xtheme)
        time.sleep(0.5)
        print(f"\n\n{putih}[{hijau}âœ“{putih}] successfully changed Termux theme")
        time.sleep(1)
        print(f"{abu}[{hijau}~{abu}] open a new session to see changes")
        time.sleep(0.5)
        print(f"\n\n{abu}[{kuning}*{abu}] if You want to exit press CTRL + Z")
        time.sleep(1)
        input(f"\n{abu} press enter to return ..")
        return
    elif x == "wrong":
        print(f"\n{putih}please input the correct choice [{merah}!{putih}]")
        time.sleep(1.5)
        return
    elif x == "exit":
        time.sleep(1)
        print(f"\n{putih}thank you for using XTheme")
        time.sleep(1)
        print(f"\n{putih}bye bye {netral}ðŸ‘‹\n")
        time.sleep(1)
        sys.exit()
    elif x == "about":
        os.system("clear")
        print(note)
        input(f"\n{abu} press enter to return ..")
        return
    if x == "coming":
        os.system("clear")
        print(xtheme)
        time.sleep(0.5)
        print(f"\n\n{putih}[{hijau}âœ“{putih}] sorry, this funnction has not been added")
        time.sleep(1)
        print(f"{abu}[{hijau}~{abu}] this function will be added in the next update")
        time.sleep(1)
        input(f"\n{abu} press enter to return ..")
        return
    else:
        return
