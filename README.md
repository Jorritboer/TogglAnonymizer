You need to log your hours for your job, but don't want your boss to know you're doing all your work at 3am? Than this tool is for you! Toggl Anonymizer takes the entries from one workspace, for example your personal workspace, and copies them to another workspace, for example your work workspace, except that the start time is the same fixed time for all entries. That way your boss can see how many hours you worked, and on what, but not when exactly.

## Usage

Add a `secret.py` with your API Token:

```python
API_TOKEN = "<API_TOKEN>"
```

Add a `settings.json` with the following:

```json
{
  "from": {
    "workspace_id": <workspace_id_from>,
    "project_id": <project_id_from>
  },
  "to": {
    "workspace_id": <workspace_id_to>,
    "project_id": <workspace_id_to>,
    "time": "<time>"
  }
}
```

Where `<workspace_id_from>` and `<project_id_from>` are the workspace and project ids to take the entries from, and `<workspace_id_to>` and `<project_id_to>` are the ids where to put copy the entries to. These entries shall all start at `<time>`, in `hh:mm` format.

Finally, run `python3 main.py` to port the entries from today, or provide a date like `python3 main.py -d 2023-02-01` to port the entries from February 1 2023.
