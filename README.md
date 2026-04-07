# Tangent

Tangent is a hover-activated Windows sidebar combining an AI chatbot, autonomous agents, on-screen visual search, and a temporary file dock. It acts as an unobtrusive copilot to accelerate your workflow without cluttering your screen. The project aims to provide a lightweight, always-available workspace companion that can stay pinned to the edge of the screen and expand into a richer utility surface when needed.

## Overview

The long-term vision for Tangent is an unobtrusive productivity layer for Windows that can support:

- AI-assisted conversations
- autonomous task agents
- visual or on-screen search workflows
- quick-access temporary file handling

At the moment, the repository contains the early desktop UI foundation for that experience: a frameless, always-on-top PyQt application with separate inactive and active screen states.

## Current Status

This project is currently in the prototype stage.

Implemented today:

- a transparent `QMainWindow` shell
- a `QStackedWidget`-based screen manager
- an inactive sidebar strip loaded from a Qt `.ui` file
- click-based transition from the inactive state to the active state
- a placeholder active screen for future expansion

Not yet implemented:

- AI chat integration
- agent orchestration
- file dock workflows
- visual search features
- packaging, installer, and production configuration

## Tech Stack

- Python
- PyQt5
- Qt Designer `.ui` files

## Project Structure

```text
Tangent/
|-- README.md
|-- dev/
|   |-- main.py
|   `-- screen/
|       |-- activeScreen/
|       |   `-- __init__.py
|       `-- inactiveScreen/
|           |-- __init__.py
|           `-- inactiveScreen.ui
`-- .gitignore
```

## How It Works

The application starts in a compact inactive state positioned near the top-left edge of the screen. When the inactive widget is clicked, the main window switches to the active screen using a stacked-widget pattern. This architecture is intended to make future screen additions and state transitions straightforward.

## Getting Started

### 1. Clone the repository

```bash
git clone "https://github.com/sarabayushman/Tangent.git"
cd Tangent
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install PyQt5
```

### 4. Run the application

```bash
python dev/main.py
```

## Development Notes

- The current code is optimized for quick iteration rather than production readiness.
- Screen modules are separated into `activeScreen` and `inactiveScreen` to keep the UI flow modular.
- The inactive UI is currently defined in `dev/screen/inactiveScreen/inactiveScreen.ui`.


## Contributing

Contributions, suggestions, and design ideas are welcome. If you plan to extend the project, it is best to keep the screen architecture modular and document any new interaction patterns clearly.

## License

No license has been added. I am making this an opensourced project
