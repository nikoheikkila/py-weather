# Python Weather

This is a small Python executable that checks current weather in given location using the excellent [wttr.in](http://wttr.in) weather API.

## Usage

There is only one argument and that is the desired location of weather report.

```bash
>>> weather San Francisco
```

## Building

Install packages with `pipenv install --dev`, then run `make build && make install && make clean`. The binary is copied to `/usr/local/bin` so make sure it's in your `$PATH`.

## TODO

- [ ] If location is omitted, use IP address location.
