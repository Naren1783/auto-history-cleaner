# Browser History Auto Cleaner

A simple Python script that deletes the Google Chrome history file if the browser has been inactive for a specified number of days.

## Features

* Checks browser inactivity using the History file timestamp.
* Deletes history automatically after the inactivity threshold is exceeded.
* Handles missing files and permission errors.
* Easy to customize.

## Usage

```bash
python history_cleaner.py
```

## Configuration

```python
HISTORYFILEPATH = r'~\AppData\Local\Google\Chrome\User Data\Default\History'
DAYSTHRESHOLD = 2
```

Modify the file path or threshold as needed.

## Note

Close Chrome before running the script, otherwise the History file may be locked.

## License

MIT License
