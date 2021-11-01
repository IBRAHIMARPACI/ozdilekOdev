Specification Heading
=====================

This is an executable specification file. This file follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

To execute this specification, run
	gauge specs


Ozdilekim
-------------------------------------------------------------

*"2" saniye bekle
* "com.ozdilek.ozdilekteyim:id/nav_categories" Id'li elemente tıkla
*"2" saniye bekle
* "//*[@text='Kadın']" xpath'li elemente tıkla
*"2" saniye bekle
* "//*[@text='Pantolon']" xpath'li elemente tıkla
*"2" saniye bekle
* "com.ozdilek.ozdilekteyim:id/imgFav" Id'li elemente tıkla
* "2" saniye bekle
* "com.ozdilek.ozdilekteyim:id/etEposta" Id'li elemente "iibrahimarpacii" değerini yaz
* "1" saniye bekle
* "com.ozdilek.ozdilekteyim:id/etPassword" Id'li elemente "İbrahim12345" değerini yaz
* "1" saniye bekle
* "com.ozdilek.ozdilekteyim:id/ivBack" Id'li elemente tıkla
*"2" saniye bekle
* "com.ozdilek.ozdilekteyim:id/ivBack" Id'li elemente tıkla
*"2" saniye bekle
* "//*[@text='İkoll Kadın Pantolon 25680']" xpath'li elemente tıkla
*"2" saniye bekle
* "com.ozdilek.ozdilekteyim:id/relLayAddCartBtn" Id'li elemente tıkla
