# Word2Number i18n (Python Implementation)

## Main files to execute persian mode

```bash
python
├── development.txt
├── MANIFEST.in
├── README.md
├── requirements.txt
├── setup.py
├── unit_testing_fa.py
└── word2numberi18n
    ├── data
    │   ├── config_fa.properties
    │   └── __init__.py
    ├── __init__.py
    ├── utils.py
    └── w2n.py
```

## Usage

First, you should import the module and make an instance of persian (`fa`) language. then you can use this instance.
```python
from word2numberi18n import w2n
instance = w2n.W2N(lang_param='fa')
```
There are two main methods in this instance

### word_to_number
this function takes an alphabetical version of number and remove every token that there is not in the number dictionary. you can use it like below:
```python
instance.word_to_number('یک میلیون و هزار و سیصد و هشت')
>>> 1001308
```

### text_to_number
this function, takes an string and find first substring of numbers and convert it to numerical form and replace alphabetical format of number with its numerical format. you can use it like below:
```python
instance.text_to_number('شماره تلفن همراه من، صفر نهصد و دوازده سیصد و شصت و چهار پنجاه و دو پنجاه می‌باشد.', ignore_zero=False)
>>> 'شماره تلفن همراه من، 09123645250 می‌باشد.'
```

## Features
### Current Features
#### convert big numbers that read separately to number (e.g. phone numbers, national ID, ...)
```python
instance.text_to_num('شماره همراه من صفر نهصد و سی و دو پانصد و چهل و هشت هفتاد هشتاد و پنج است', ignore_zero=False)
>>> 'شماره همراه من 09325487085 است'
```

#### convert more than one number in a sentence to number
```python
instance.text_to_num('فصل یک از بخش دو کتاب کمدی الهی', ignore_zero=False)
>>> 'فصل 1 از بخش 2 کتاب کمدی الهی'
```
#### up to 999_999_999_999_999
```python
instance.text_to_num('نهصد و نود و نه تریلیون و نهصد و نود و نه میلیارد و نهصد و نود و نه میلیون و نهصد و نود و نه هزار و نهصد و نود و نه', ignore_zero=False)
>>> '999999999999999'
```
### Future Features (Not Supported yet)
#### Date
```python
instance.text_to_num('امروز بیست و سه چهار هزار و سیصد و هفتاد و هفت می‌باشد.', ignore_zero=False)
>>> 'امروز 1377/4/23 می‌باشد.'
```

#### different form of number reading ('پانزده' == 'پونزده')
this problem, partially resolved but it needs to improve.