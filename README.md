# Getting Started

If you are using Visual Studio Code, create a folder called .vscode and add a launch.json file like this:

```yaml
{
    "version": "0.2.0",
    "configurations": [
      {
        "name": "Python: FastAPI",
        "type": "debugpy",
        "request": "launch",
        "module": "uvicorn",
        "args": [
          "main:app",
          "--host",
          "0.0.0.0",
          "--port",
          "8000",
          "--reload"
        ],
        "env": {
          "APP_VERSION": "1.0.0"
        },
        "jinja": true
      }
    ]
  }
```

This is the simplest case.  Put all of your environment variables here so that they are available when the application is being debugged.