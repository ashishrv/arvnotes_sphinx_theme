# arvnotes_sphinx_theme

Sphinx theme for maintaining notes

## Installation

```bash
pip install git+https://github.com:ashishrv/arvnotes_sphinx_theme.git
pipenv install "git+https://github.com/ashishrv/arvnotes_sphinx_theme.git#egg=arvnotes-sphinx-theme"
```

or
```bash
git clone https://github.com:ashishrv/arvnotes_sphinx_theme.git
cd arvnotes_sphinx_theme
python setup.py install develop
```


## Setup

in conf.py::

    import arvnotes_sphinx_theme


### Styling

Choose a pygment_style

```text
>>> from pygments.styles import STYLE_MAP
>>> STYLE_MAP.keys()
dict_keys(['default', 'emacs', 'friendly', 'colorful', 'autumn', 'murphy', 'manni', 'monokai', 'perldoc', 'pastie', 'borland', 'trac', 'native', 'fruity', 'bw', 'vim', 'vs', 'tango', 'rrt', 'xcode', 'igor', 'paraiso-light', 'paraiso-dark', 'lovelace', 'algol', 'algol_nu', 'arduino', 'rainbow_dash', 'abap', 'solarized-dark', 'solarized-light', 'sas', 'stata', 'stata-light', 'stata-dark', 'inkpot'])
```
