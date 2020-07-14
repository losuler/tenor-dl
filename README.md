<div align="center">
<p align="center">
  <a href="https://gitlab.com/losuler/tenor-dl">
  </a>

  <p align="center">
    <h3 align="center">Tenor Downloader</h3>
    <p align="center">
      Download .gif files from Tenor.
    </p>
  </p>
</p>
</div>

<hr />

Allows a way to download .gif files from [Tenor](https://tenor.com/), which is presumably intentionally difficult or impossible to do via a web browser.

## Dependancies

```
requests
clint
```

## Configuration

A [developer API key](https://tenor.com/gifapi/documentation#quickstart-setup) is **required**. This is to be provided in `config.ini` (see `config.ini.example`) or as an optional argument.

## Usage

```
tenor-dl.py [-h] [-a APIKEY] [-d] id
```

### Positional arguments

```
id	the ID of the gif
```

The id for the gif can be found at the end of the URL on the landing page or view page for the gif. For example the id for this gif is `6198981`:

`https://tenor.com/view/kitty-highkitten-mdmacat-cat-happykitty-gif-6198981`

`https://media1.tenor.com/images/f6fe8d1d0463f4e51b6367bbecf56a3e/tenor.gif?itemid=6198981`

### Optional arguments

```
-h, --help                 	show this help message and exit
-a APIKEY, --apikey APIKEY 	the Tenor api key
-d, --download             	download the gif
```
