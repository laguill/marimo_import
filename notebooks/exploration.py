

import marimo

__generated_with = "0.13.2"
app = marimo.App(app_title="")


@app.cell
def _():
    import marimo as mo
    return


@app.cell
def _():
    import scripts.analysis_tools as tools
    return


@app.cell
def _():
    import sys
    print(sys.path)
    return


if __name__ == "__main__":
    app.run()
